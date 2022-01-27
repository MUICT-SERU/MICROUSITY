#! /bin/sh
(
    trap 'kill 0' SIGINT # kill all process in one go
    (
        cd ../zeek
        zeek -i lo0 track.zeek
    ) &
    ZEEKPID=$!
    source start.sh &
    P1=$!
    sleep 60
    (
        cd ../..
        dotnet bin/restler/Restler.dll compile \
        --api_spec sample-spring-microservices-new-master/Swagger/swagger-Department.json
        dotnet bin/restler/Restler.dll fuzz-lean \
        --grammar_file Compile/grammar.py \
        --dictionary_file Compile/dict.json \
        --settings Compile/engine_settings.json \
        --no_ssl
    )
    trap "exit" INT TERM
    trap "kill 0" EXIT
)
