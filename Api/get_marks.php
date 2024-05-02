<?php

require_once __DIR__ . '/../RequiredChecker.class.php';
require_once __DIR__ . '/../ApiAnswer.class.php';
require_once __DIR__ . '/../MarkRepository.class.php';

$rc = (new RequiredChecker('telegram_id', $_GET))->check();

$mr = new MarkRepository();

echo (new ApiAnswer(true, 'MARKS_GOT', $mr->get_marks($_GET['telegram_id'])))->make_json();
