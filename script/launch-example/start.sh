#! /bin/sh
cd ../../sample-spring-microservices-new-master
trap 'kill $(jobs -p)' EXIT INT KILL TERM
cd config-service
java -jar $(find . -name "*.jar") 1
sleep 20
cd -
cd discovery-service
java -jar $(find . -name "*.jar") 1
sleep 5
cd -
cd employee-service
java -jar $(find . -name "*.jar") 1
sleep 1
cd -
cd department-service
java -jar $(find . -name "*.jar") 1
sleep 1
cd -
cd organization-service
java -jar $(find . -name "*.jar") 1
sleep 1
cd -
cd gateway-service
java -jar $(find . -name "*.jar") 1
cd -
wait