#!/bin/bash


while IFS="," read -r r1 r2 r3 r4 r5
do
  if [ $r4 -ne 0 ]
  then
    echo "failed load test"
    docker stop locust_container nginx_container gunicorn_container
    docker rm locust_container nginx_container gunicorn_container
  fi
done < <(tail -1 stats/_stats.csv)

