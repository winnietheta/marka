<?php

require_once __DIR__ . '/ApiAnswer.class.php';

/**
 * A class for checking if required fields were sent
 */
class RequiredChecker
{
    private string $fields;
    private array $data;

    /**
     * Creates RequiredChecker object
     * @param string $fields required fields, for example: id|id2|id3
     * @param array $data user POST/GET fields
     * @return \RequiredChecker
     */
    public function __construct(string $fields, array $data)
    {
        $this->fields = $fields;
        $this->data = $data;

        return $this;
    }

    /**
     * Compares POST/GET to required fields
     * @return true|array
     */
    public function check(): bool|array
    {
        $array = explode('|', $this->fields);

        $unset = array();

        foreach ($array as $item) {
            if (!isset($this->data[$item])) {
                $unset[] = $item;
            }
        }

        if (count($unset) == 0) {
            return true;
        }

        $answer = new ApiAnswer(false, 'NOT_ENOUGH_PARAMS', $unset);
        die($answer->make_json());
    }
}
