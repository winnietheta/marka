<?php

use Random\RandomException;

/**
 * A universal class that generates UUID
 */
class UUIDGenerator
{
    /**
     * Generates UUID v4
     * @param null $data
     * @return string
     */
    public function guidv4($data = null): string
    {
        try {
            $data = $data ?? random_bytes(16);
        } catch (RandomException $e) {
            return false;
        }

        assert(strlen($data) == 16);

        $data[6] = chr(ord($data[6]) & 0x0f | 0x40);
        $data[8] = chr(ord($data[8]) & 0x3f | 0x80);

        return vsprintf('%s%s-%s-%s-%s-%s%s%s', str_split(bin2hex($data), 4));
    }
}
