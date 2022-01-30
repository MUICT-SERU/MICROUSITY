#! /bin/sh
cd ../../sample-spring-microservices-new-master
(
    trap 'kill 0' SIGINT
    (
        cd config-service
        mvn spring-boot:run
    ) &
    sleep 20
    (
        cd discovery-service
        mvn spring-boot:run
    ) &
    sleep 5
    (
        cd employee-service
        mvn spring-boot:run
    ) &
    (
        cd department-service
        mvn spring-boot:run
    ) &
    (
        cd organization-service
        mvn spring-boot:run
    ) &
    (
        cd gateway-service
        mvn spring-boot:run
    )
)
