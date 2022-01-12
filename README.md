# SP2021-TRITECH
A repo for the Tritech team.

All web application component are in the Web directory

## How to run web
1. Clone the repo
2. cd to Web directory
3. type `npm i`
4. type `node app.js`

## How to run sample project
https://github.com/piomin/sample-spring-microservices-new

https://piotrminkowski.com/2018/04/26/quick-guide-to-microservices-with-spring-boot-2-0-eureka-and-spring-cloud/

- req: Jdk 8 with maven
1. Start the config service first (8088)
2. Start discovery service (8061)
3. Start Organization service
4. Start Department service
5. Start Employee service
6. Start gateway service (8060)

Swagger UI: http://localhost:8060/webjars/swagger-ui/index.html?configUrl=%2Fv3%2Fapi-docs%2Fswagger-config&urls.primaryName=department

Discovery: http://localhost:8061
