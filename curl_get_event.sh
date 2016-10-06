#!/bin/bash

clear

echo "Fetching event from C42 REST API:"
echo "event_id=d6e66cb0ced8e46102bcfd93ceac51b0_14752373875438"
EVENT_ID="d6e66cb0ced8e46102bcfd93ceac51b0_14752373875438"

if [ "$1" = "store" ]
then
	curl --request GET \
	--header "Accept: application/json" \
	--header "Content-type: application/json" \
	--header "Authorization: Token 5e1e8530f7a69e7306e83ad673ffa0c23cb04fae" \
	"https://demo.calendar42.com/api/v2/events//$EVENT_ID/" \
	| python -mjson.tool > event_object.json
else
	curl --request GET \
	--header "Accept: application/json" \
	--header "Content-type: application/json" \
	--header "Authorization: Token 5e1e8530f7a69e7306e83ad673ffa0c23cb04fae" \
	"https://demo.calendar42.com/api/v2/events//$EVENT_ID/" \
	| python -mjson.tool | pygmentize -l json
fi