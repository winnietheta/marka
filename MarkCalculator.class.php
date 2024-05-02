<?php

class MarkCalculator
{
    public function count(float|int $targetAverageMark, float|int $currentAverageMark, int $marksNumber, int $actionMark)
    {
        if ($targetAverageMark >= $actionMark) {
            return 'IMPOSSIBLE_TARGET';
        }

        $markSum = $marksNumber * $currentAverageMark;

        $i = 0;
        while ($markSum / ($marksNumber + $i) < $targetAverageMark) {
            $i = $i + 1;
            $markSum = $markSum + $actionMark;
        }

        return $i;
    }
}
