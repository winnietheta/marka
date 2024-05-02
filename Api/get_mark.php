<?php

require_once __DIR__ . '/../RequiredChecker.class.php';
require_once __DIR__ . '/../ApiAnswer.class.php';
require_once __DIR__ . '/../MarkRepository.class.php';

$rc = (new RequiredChecker('uuid', $_GET))->check();

$mr = new MarkRepository();

echo (new ApiAnswer(true, 'MARK_GOT', $mr->get_mark($_GET['uuid'])))->make_json();
