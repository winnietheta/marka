<?php

require_once __DIR__ . '/../RequiredChecker.class.php';
require_once __DIR__ . '/../ApiAnswer.class.php';
require_once __DIR__ . '/../MarkRepository.class.php';

$rc = (new RequiredChecker('telegram_id|subject|mark|date', $_GET))->check();

$mr = new MarkRepository();
$mr->add_mark($_GET['telegram_id'], $_GET['subject'], $_GET['mark'], $_GET['date']);

echo (new ApiAnswer(true, 'MARK_ADDED', array()))->make_json();
