#!/bin/bash


while IFS="," read -r r1 r2 r3 r4 r5
do
  if [ $r4 -ne 0 ]
  then
    echo "failed load test"
    docker stop locust nginx gunicorn
    docker rm locust nginx gunicorn
  fi
done < <(tail -1 stats/_stats.csv)

