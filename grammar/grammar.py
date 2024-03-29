""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
import time
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_organization_get_0_departments_0_employees_0_id = dependencies.DynamicVariable("_organization_get_0_departments_0_employees_0_id")

def parse_organizationget(data):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None
    # Parse the response into json
    try:
        #print(data)
        #data = json.loads(data)
        #time.sleep(5)
        print(type(data))
        print(data)

        if data == None:
            # Do something ...
            data = [
    {
        "id": 1,
        "name": "Microsoft",
        "address": "Redmond, Washington, USA",
        "departments": [],
        "employees": []
    },
    {
        "id": 2,
        "name": "Oracle",
        "address": "Redwood City, California, USA",
        "departments": [],
        "employees": []
    }
]
        else:
            data = json.loads(data) 
        
        
    except Exception as error:
        #data = json.loads(data)
        raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))


    # Try to extract each dynamic object


    try:
        temp_7262 = str(data[0]["id"])
    except Exception as error:
        # This is not an error, since some properties are not always returned
        pass


    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_organization_get_0_departments_0_employees_0_id", temp_7262)

req_collection = requests.RequestCollection([])
# Endpoint: /organization, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8060\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {
        'post_send':
        {
            'parser': parse_organizationget,
            'dependencies':
            [
                _organization_get_0_departments_0_employees_0_id.writer()
            ]
        }
    },

],
requestId="/organization"
)
req_collection.add_request(request)

# Endpoint: /organization/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_organization_get_0_departments_0_employees_0_id.reader()),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8060\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/organization/{id}"
)
req_collection.add_request(request)

# Endpoint: /organization/{id}/with-departments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_organization_get_0_departments_0_employees_0_id.reader()),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("with-departments"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8060\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/organization/{id}/with-departments"
)
req_collection.add_request(request)

# Endpoint: /organization/{id}/with-departments-and-employees, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_organization_get_0_departments_0_employees_0_id.reader()),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("with-departments-and-employees"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8060\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/organization/{id}/with-departments-and-employees"
)
req_collection.add_request(request)

# Endpoint: /organization/{id}/with-employees, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("organization"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_organization_get_0_departments_0_employees_0_id.reader()),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("with-employees"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: localhost:8060\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/organization/{id}/with-employees"
)
req_collection.add_request(request)
