<?php

require_once __DIR__ . '/../RequiredChecker.class.php';
require_once __DIR__ . '/../ApiAnswer.class.php';
require_once __DIR__ . '/../MarkRepository.class.php';

$rc = (new RequiredChecker('uuid', $_GET))->check();

$mr = new MarkRepository();
$mr->delete_mark($_GET['uuid']);

echo (new ApiAnswer(true, 'MARK_DELETED', array()))->make_json();
