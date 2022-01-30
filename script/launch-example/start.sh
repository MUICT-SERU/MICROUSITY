#! /bin/sh
cd ../../sample-spring-microservices-new-master
trap 'kill $(jobs -p)' EXIT SIGINT SIGKILL SIGTERM
cd config-service
java -jar $(find . -name "*.jar") 1>/dev/null &
sleep 20
cd -
cd discovery-service
java -jar $(find . -name "*.jar") 1>/dev/null &
sleep 5
cd -
cd employee-service
java -jar $(find . -name "*.jar") 1>/dev/null &

cd -
cd department-service
java -jar $(find . -name "*.jar") 1>/dev/null &

cd -
cd organization-service
java -jar $(find . -name "*.jar") 1>/dev/null &

cd -
cd gateway-service
java -jar $(find . -name "*.jar") 1>/dev/null &
cd -
wait