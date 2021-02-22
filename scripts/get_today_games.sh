#!/bin/bash
URL=$1
curl -s -k -X GET \
    –header 'Content-Type: application/json' –header 'Accept: application/json' \
    "${URL}/get_today_games"