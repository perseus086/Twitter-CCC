#!/bin/bash
#

ip1=$(fab -f test_instantiate.py create_couch)
ip2=$(fab -f test_instantiate.py create_appserver)

echo$ip1
echo$ip2

fab -H ubuntu@$ip1 couch_server
fab -H ubuntu@$ip2 app_server

