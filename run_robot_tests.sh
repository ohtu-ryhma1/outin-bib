#!/bin/bash

echo "Running robot tests"

# launch Flask-server
echo "Starting Flask server"
poetry run invoke start
echo "Flask server started"


# wait until server is ready
echo "Waiting for server"
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5001)" != "200" ]];
    do sleep 1;
done
echo "Server ready"


# run robot tests
echo "Starting robot tests"
poetry run robot --variable HEADLESS:true src/robot_tests
status=$?
echo "Robot tests complete"


# stop the server
kill $(lsof -t -i:5001)


# exit
exit $status
