<?php

require_once __DIR__ . '/Database.class.php';
require_once __DIR__ . '/MarkCalculator.class.php';
require_once __DIR__ . '/UUIDGenerator.class.php';

class MarkRepository
{
    private Database $db;
    private MarkCalculator $mc;
    private UUIDGenerator $uuid_generator;

    public function __construct()
    {
        $this->db = new Database();
        $this->mc = new MarkCalculator();
        $this->uuid_generator = new UUIDGenerator();
    }

    public function get_marks(string $telegram_id): array
    {
        $subjects_db = $this->db->plural_query('SELECT * FROM marks WHERE telegram_id = :telegram_id', array('telegram_id' => $telegram_id));

        $subjects = array();
        foreach ($subjects_db as $item) {
            $subjects[] = $item['subject'];
        }
        $subjects = array_values(array_unique($subjects));

        $marks = array();
        foreach ($subjects as $subject) {
            $marks_db = $this->db->plural_query('SELECT * FROM marks WHERE telegram_id = :telegram_id AND subject = :subject ORDER BY date DESC', array('telegram_id' => $telegram_id, 'subject' => $subject));
            $marks_db_count = count($marks_db);

            $marks_sum = 0;
            foreach ($marks_db as $mark) {
                $marks[$subject]['marks'][] = array(
                    'uuid' => $mark['uuid'],
                    'mark' => $mark['mark'],
                    'date' => date("d.m.Y", strtotime($mark['date']))
                );
                $marks_sum += (int)$mark['mark'];
            }

            $marks[$subject]['average'] = number_format(floor($marks_sum / $marks_db_count * 100) / 100, 2);

            if ($marks[$subject]['average'] < 4.50 && $marks[$subject]['average'] >= 3.50) {
                $marks[$subject]['required_five_to_4.50'] = $this->mc->count(4.50, $marks[$subject]['average'], $marks_db_count, 5);
            } else if ($marks[$subject]['average'] < 3.50 && $marks[$subject]['average'] >= 2.50) {
                $marks[$subject]['required_five_to_3.50'] = $this->mc->count(3.50, $marks[$subject]['average'], $marks_db_count, 5);
                $marks[$subject]['required_four_to_3.50'] = $this->mc->count(3.50, $marks[$subject]['average'], $marks_db_count, 4);
            } else if ($marks[$subject]['average'] < 2.50) {
                $marks[$subject]['required_five_to_2.50'] = $this->mc->count(2.50, $marks[$subject]['average'], $marks_db_count, 5);
                $marks[$subject]['required_four_to_2.50'] = $this->mc->count(2.50, $marks[$subject]['average'], $marks_db_count, 4);
                $marks[$subject]['required_three_to_2.50'] = $this->mc->count(2.50, $marks[$subject]['average'], $marks_db_count, 3);
            }
        }

        return $marks;
    }

    public function get_mark(string $uuid): bool|array
    {
        return $this->db->single_query('SELECT * FROM marks WHERE uuid = :uuid', array('uuid' => $uuid));
    }

    public function delete_mark(string $uuid): void
    {
        $this->db->single_query('DELETE FROM marks WHERE uuid = :uuid', array('uuid' => $uuid));
    }

    public function import_marks(string $telegram_id, string $session_id): bool
    {
        try {
            $curlHandler = curl_init();

            curl_setopt_array($curlHandler, [
                CURLOPT_URL => 'https://school.vip.edu35.ru/api/MarkService/GetSummaryMarks?date=' . date('Y-m-d', time()),
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_COOKIE => 'sessionid=' . $session_id
            ]);

            $response = curl_exec($curlHandler);
            curl_close($curlHandler);

            $response = json_decode($response, true);

            if (!isset($response['discipline_marks'])) {
                return false;
            }

            $this->reset_marks($telegram_id);

            foreach ($response['discipline_marks'] as $discipline_mark) {
                foreach ($discipline_mark['marks'] as $mark) {
                    if ($mark['mark'] == '•') {
                        $mark['mark'] = '2';
                    }

                    $this->add_mark($telegram_id, $discipline_mark['discipline'], $mark['mark'], $mark['date']);
                }
            }

            return true;
        } catch (Exception) {
            return false;
        }
    }

    public function reset_marks(string $telegram_id): void
    {
        $this->db->single_query('DELETE FROM marks WHERE telegram_id = :telegram_id', array('telegram_id' => $telegram_id));
    }

    public function add_mark(string $telegram_id, string $subject, string $mark, string $date): void
    {
        $ts = strtotime($date);
        $subject = mb_strimwidth($subject, 0, 20);
        $date = date('Y-m-d', $ts);
        $this->db->single_query('INSERT INTO marks (uuid, telegram_id, subject, mark, date) VALUES (:uuid, :telegram_id, :subject, :mark, :date)', array('uuid' => $this->uuid_generator->guidv4(), 'telegram_id' => $telegram_id, 'subject' => $subject, 'mark' => $mark, 'date' => $date));
    }
}
