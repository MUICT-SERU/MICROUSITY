#! /bin/sh
# (
#     cd ../zeek
#     zeek -i lo0 track.zeek &
#     cd -
#     echo $pwd
#     source start.sh &
#     sleep 120
#     (
#         cd ../..
#         dotnet bin/restler/Restler.dll fuzz-lean \
#         --grammar_file Compile/grammar.py \
#         --dictionary_file Compile/dict.json \
#         --settings Compile/engine_settings.json \
#         --no_ssl
#     )
#     trap 'kill $(jobs -p)' EXIT
# )
