#!/usr/bin/env bash
for i in `adb devices|grep 'device$'|awk '{print $1}'`
do
  echo $i
  udid = $i pytest test test_search.py &
done