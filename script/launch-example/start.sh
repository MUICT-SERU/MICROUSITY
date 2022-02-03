#! /bin/sh
cd ../../sample-spring-microservices-new-master
trap 'kill $(jobs -p)' EXIT SIGINT SIGKILL SIGTERM
cd config-service
java -jar $(find . -name "*.jar") 1>../../output/java.log &
sleep 20
cd -
cd discovery-service
java -jar $(find . -name "*.jar") 1>../../output/java1.log &
sleep 5
cd -
cd employee-service
java -jar $(find . -name "*.jar") 1>../../output/java2.log &
sleep 1
cd -
cd department-service
java -jar $(find . -name "*.jar") 1>../../output/java3.log &
sleep 1
cd -
cd organization-service
java -jar $(find . -name "*.jar") 1>../../output/java4.log &
sleep 1
cd -
cd gateway-service
java -jar $(find . -name "*.jar") 1>../../output/java5.log &
cd -
wait