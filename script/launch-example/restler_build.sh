mkdir restler_bin
git clone https://github.com/microsoft/restler-fuzzer.git
CWD="$(pwd)"
cd restler-fuzzer
python3 ./build-restler.py --dest_dir "$CWD/restler_bin"

cat > defaultDict.json << ENDOFFILE
{
  "restler_fuzzable_string": [
    "fuzzstring"
  ],
  "restler_fuzzable_string_unquoted": [],
  "restler_fuzzable_datetime": [
    "2019-06-26T20:20:39+00:00"
  ],
  "restler_fuzzable_datetime_unquoted": [],
  "restler_fuzzable_uuid4": [
    "566048da-ed19-4cd3-8e0a-b7e0e1ec4d72"
  ],
  "restler_fuzzable_uuid4_unquoted": [],
  "restler_fuzzable_int": [
    "1",
    "0"
  ],
  "restler_fuzzable_number": [
    "1.23"
  ],
  "restler_fuzzable_bool": [
    "true"
  ],
  "restler_fuzzable_object": [
    "{ \"fuzz\": false }"
  ],
  "restler_custom_payload": {},
  "restler_custom_payload_unquoted": {},
  "restler_custom_payload_uuid4_suffix": {}
}
ENDOFFILE
chmod 755 defaultDict.json

cat > config.json << ENDOFFILE
{
  "SwaggerSpecFilePath": [
    "$CWD/spec2.json"
  ],
  "GrammarOutputDirectoryPath": "$CWD/restler_bin/restler/Compile",
  "CustomDictionaryFilePath": "$CWD/restler-fuzzer/defaultDict.json",
  "IncludeOptionalParameters": true,
  "UseHeaderExamples": true,
  "UseQueryExamples": true,
  "UseBodyExamples": true,
  "DiscoverExamples": false,
  "ExamplesDirectory": "",
  "DataFuzzing": true,
  "ReadOnlyFuzz": false,
  "ResolveQueryDependencies": true,
  "ResolveBodyDependencies": true,
  "UseRefreshableToken": true,
  "AllowGetProducers": true,
  "TrackFuzzedParameterNames": false
}
ENDOFFILE


cat > restler_user_settings.json << ENDOFFILE
{
        "checkers": {
        "invaliddynamicobject": {
            "invalid_objects" : [
                "someinvalidobject",
                "valid-object/$*",
                "valid-object=valid-object",
                "valid-object=?valid-object",
                "valid-object?valid-object",
                "valid-object,valid-object"
            ]
        }
    }
}
ENDOFFILE
chmod 755 restler_user_settings.json

cd ..
cd restler_bin
cd restler 
dotnet ./Restler.dll compile $CWD/restler-fuzzer/config.json
