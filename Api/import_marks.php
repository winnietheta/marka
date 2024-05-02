<?php

require_once __DIR__ . '/../RequiredChecker.class.php';
require_once __DIR__ . '/../ApiAnswer.class.php';
require_once __DIR__ . '/../MarkRepository.class.php';

$rc = (new RequiredChecker('telegram_id|session_id', $_GET))->check();

$mr = new MarkRepository();

if ($mr->import_marks($_GET['telegram_id'], $_GET['session_id'])) {
    echo (new ApiAnswer(true, 'MARKS_IMPORTED', array()))->make_json();
} else {
    echo (new ApiAnswer(false, 'MARKS_NOT_IMPORTED', array()))->make_json();
}
