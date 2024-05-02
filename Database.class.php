<?php

/**
 * A class for working with database
 */
class Database
{
    private string $host;
    private string $database;
    private string $user;
    private string $password;
    private string $charset;

    private string $dsn;
    private array $opt;
    private PDO $pdo;

    public function __construct()
    {
        $this->host = "127.0.0.1";
        $this->database = "marka";
        $this->user = "root";
        $this->password = "";
        $this->charset = "utf8";

        $this->dsn = "mysql:host=$this->host;dbname=$this->database;charset=$this->charset";
        $this->opt = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ];

        try {
            $this->pdo = new PDO($this->dsn, $this->user, $this->password, $this->opt);
        } catch (Exception $ex) {
            die('Database connection failed: ' . $ex);
        }
    }

    /**
     * Executes SQL query and return single row
     * @param string $sql SQL query with placeholders
     * @param array $data Array contains placeholders
     * @return false|array
     */
    public function single_query(string $sql, array $data): false|array
    {
        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute($data);
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch (Exception $ex) {
            return false;
        }
    }

    /**
     * Executes SQL query and return multiple rows
     * @param string $sql SQL query with placeholders
     * @param array $data Array contains placeholders
     * @return false|array
     */
    public function plural_query(string $sql, array $data): bool|array
    {
        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute($data);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (Exception $ex) {
            return false;
        }
    }
}
