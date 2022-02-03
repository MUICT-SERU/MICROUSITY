#! /bin/sh
(
    cd ../zeek
    zeek -i lo0 track.zeek &
    sleep 5
    cd -
    (
        cd ../..
        dotnet bin/restler/Restler.dll fuzz-lean \
        --grammar_file grammar/grammar.py \
        --dictionary_file grammar/dict.json \
        --settings grammar/restler_user_settings.json \
        --no_ssl
    )
    trap 'kill $(jobs -p)' EXIT
)
