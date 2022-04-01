#! /bin/sh
trap 'killall zeek' EXIT
(
    cd ../zeek
    (
        mkdir -p $1
        cd $1
        zeek -C -i $1 ../track.zeek track::bff_port=$3
    ) &
    (
        mkdir -p $2
        cd $2
        zeek -C -i $2 ../track.zeek
    ) &
    sleep 5
    cd -
    (
        cd ../..
        dotnet bin/restler/Restler.dll fuzz-lean \
        --grammar_file $4 \
        --dictionary_file $5 \
        --settings $6 \
        --token_refresh_command $7 \
        --token_refresh_interval 3600 \
        --no_ssl
    )
)
