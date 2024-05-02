<?php

/**
 * A universal class that form api answer
 */
class ApiAnswer
{
    public bool $status;
    public string $code;
    public array $data;

    /**
     * Make a new ApiAnswer object
     * @param bool $status answer status: true or false, depends on operation state
     * @param string $code answer code, for example: SUCCESSFUL_DELETED
     * @return \ApiAnswer
     */
    public function __construct(bool $status, string $code, array $data)
    {
        $this->status = $status;
        $this->code = $code;
        $this->data = $data;

        return $this;
    }

    /**
     * Returns JSON pretty unescaped unicode format answer string
     * @return string
     */
    public function make_json(): string
    {
        return json_encode(array(
            'status' => $this->status,
            'code' => $this->code,
            'data' => $this->data
        ), JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    }
}
