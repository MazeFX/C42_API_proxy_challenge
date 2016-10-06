#!/bin/bash

clear

echo "Fetching event from API proxy at mazefx.pythonanywhere.com:"
echo "event_id=d6e66cb0ced8e46102bcfd93ceac51b0_14752373875438"
EVENT_ID="d6e66cb0ced8e46102bcfd93ceac51b0_14752373875438"

curl --request GET \
"https://mazefx.pythonanywhere.com/C42/events-with-subscriptions/$EVENT_ID/" \
| python -mjson.tool | pygmentize -l json