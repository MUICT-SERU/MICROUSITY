#! /bin/sh
trap 'killall zeek' EXIT
if [ "$#" -lt 2 ]; then
    echo "need interface and port as argument"
    exit 1
fi
(
    cd ../zeek
    if [ "$#" -eq 2 ]; then
    (
        mkdir -p $1
        cd $1
        zeek -C -i $1 ../track.zeek track::bff_port=$2
    ) &
    elif [ "$#" -eq 3 ]; then
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
    fi
    sleep 5
    cd -
    (
        cd ../..
        dotnet bin/restler/Restler.dll fuzz-lean \
        --grammar_file lineman/grammar.py \
        --dictionary_file lineman/dict.json \
        --settings lineman/restler_user_settings.json \
        --token_refresh_command /Users/pumipat/SP2021-TRITECH/lineman/token.py \
        --token_refresh_interval 3600 \
        --no_ssl
    )
)
