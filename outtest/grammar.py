""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_businesses_get_businesses_0_id = dependencies.DynamicVariable("_businesses_get_businesses_0_id")

_menu_items_put_id = dependencies.DynamicVariable("_menu_items_put_id")

_menu_items_put_seq = dependencies.DynamicVariable("_menu_items_put_seq")

def parse_businessesget(data):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None
    # Parse the response into json
    try:
        data = json.loads(data)
    except Exception as error:
        raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))

    # Try to extract each dynamic object


    try:
        temp_7262 = str(data["businesses"][0]["id"])
    except Exception as error:
        # This is not an error, since some properties are not always returned
        pass


    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_businesses_get_businesses_0_id", temp_7262)


def parse_menuitemsput(data):
    """ Automatically generated response parser """
    # Declare response variables
    temp_8173 = None
    temp_7680 = None
    # Parse the response into json
    try:
        data = json.loads(data)
    except Exception as error:
        raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))

    # Try to extract each dynamic object


    try:
        temp_8173 = str(data["id"])
    except Exception as error:
        # This is not an error, since some properties are not always returned
        pass


    try:
        temp_7680 = str(data["seq"])
    except Exception as error:
        # This is not an error, since some properties are not always returned
        pass


    # If no dynamic objects were extracted, throw.
    if not (temp_8173 or temp_7680):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_8173:
        dependencies.set_variable("_menu_items_put_id", temp_8173)
    if temp_7680:
        dependencies.set_variable("_menu_items_put_seq", temp_7680)

req_collection = requests.RequestCollection([])
# Endpoint: /businesses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("businesses"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {
        'post_send':
        {
            'parser': parse_businessesget,
            'dependencies':
            [
                _businesses_get_businesses_0_id.writer()
            ]
        }
    },

],
requestId="/businesses"
)
req_collection.add_request(request)

# # Endpoint: /businesses/categories, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("businesses"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("categories"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/businesses/categories"
)
req_collection.add_request(request)

# Endpoint: /businesses/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("businesses"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    # primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/businesses/{id}"
)
req_collection.add_request(request)

# # Endpoint: /businesses/{id}, method: Put
# request = requests.Request([
#     primitives.restler_static_string("PUT "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("businesses"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "tags":
#     [
#         """),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#     ],
#     "averageWaitTimeInSecond":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string(""",
#     "bookable":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "branch":
#         {
#             "english":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "primary":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "thai":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ,
#     "businessNo":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "categories":
#         {
#             "all":
#             [
#                 """),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string("""
#             ],
#             "main":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string("""
#         }
#     ,
#     "checker":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "contact":
#         {
#             "address":
#                 {
#                     "coordinate":
#                         {
#                             "latitude":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string(""",
#                             "longitude":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string("""
#                         }
#                     ,
#                     "hint":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#                     "region":
#                         {
#                             "id":"""),
#     primitives.restler_static_string('"'),
#     # primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""",
#                             "name":
#                                 {
#                                     "english":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#                                     "primary":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#                                     "thai":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#                                 }
#                             ,
#                             "type":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#                         }
#                     ,
#                     "streetAddress":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#                     "zipCode":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#                 }
#             ,
#             "email":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "facebookHomepage":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "homepage":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "instagram":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "line":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "phoneNumbers":
#             [
#                 {
#                     "number":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#                 }
#             ]
#         }
#     ,
#     "creditCardAccepted":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "deliveryHours":
#     [
#         {
#             "day":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "from":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "to":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ],
#     "gallery":
#         {
#             "defaultPhoto":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#             "logo":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#             "manualDefault":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string("""
#         }
#     ,
#     "goodForGroups":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "goodForKids":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "highlightPicture":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#     "hotelRestaurant":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "id":"""),
#     primitives.restler_static_string('"'),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string("""",
#     "inOpeningHour":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "information":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "musicVenues":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "name":
#         {
#             "english":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "primary":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "thai":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ,
#     "numberOfSeats":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "owner":
#         {
#             "email":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "id":"""),
#     primitives.restler_static_string('"'),
#     # primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""",
#             "name":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ,
#     "ownerMessage":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "parking":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "petFriendly":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "priceRange":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "readyForRmsDelivery":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "rms":
#         {
#             "packageLevel":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ,
#     "rmsManaged":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "rmsSettings":
#         {
#             "acceptLinePay":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#             "rmsForceClosed":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#             "rmsForceOpened":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string("""
#         }
#     ,
#     "servedAlcohols":
#     [
#         """),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#     ],
#     "serviceCharge":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string(""",
#     "temporaryCloseEndDate":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#     "temporaryCloseStartDate":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#     "temporaryClosed":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "vat":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string(""",
#     "wifi":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "wongnaiUrl":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "workingHours":
#     [
#         {
#             "day":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "from":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "to":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ]}"""),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/businesses/{id}"
# )
# req_collection.add_request(request)

# Endpoint: /businesses/{id}/delivery-status, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("businesses"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delivery-status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/businesses/{id}/delivery-status"
)
req_collection.add_request(request)

# Endpoint: /businesses/{id}/delivery-status, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("businesses"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("delivery-status"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: application/json\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "force":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/businesses/{id}/delivery-status"
)
req_collection.add_request(request)

# Endpoint: /businesses/{id}/menu-approved, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("businesses"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("menu-approved"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: application/json\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "menuApproved":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/businesses/{id}/menu-approved"
)
req_collection.add_request(request)

# Endpoint: /businesses/{id}/rlp-credential, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("businesses"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("rlp-credential"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/businesses/{id}/rlp-credential"
)
req_collection.add_request(request)

# Endpoint: /businesses/{id}/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("businesses"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/businesses/{id}/settings"
)
req_collection.add_request(request)

# # Endpoint: /businesses/{id}/settings, method: Put
# request = requests.Request([
#     primitives.restler_static_string("PUT "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("businesses"),
#     primitives.restler_static_string("/"),
#     # primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     # primitives.restler_static_string("2262<script>alert(\"555\")</script>"),
#     primitives.restler_static_string("2262"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("settings"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "autoOpenCloseDelivery":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "paymentAccountInformation":
#         {
#             "accountName":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "accountNumber":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "bankName":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ,
#     "reportRecipients":
#     [
#         {
#             "email":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ],
#     "testingMode":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "voiceNotificationNumber":
#         {
#             "number":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     }"""),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/businesses/{id}/settings"
# )
# req_collection.add_request(request)

# Endpoint: /businesses/{id}/statistic, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("businesses"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statistic"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/businesses/{id}/statistic"
)
req_collection.add_request(request)


# # Endpoint: /businesses/{pid}/crm-settings, method: Get Unauthorise
# request = requests.Request([
#     primitives.restler_static_string("GET "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("businesses"),
#     primitives.restler_static_string("/"),
#     primitives.restler_fuzzable_string("5463489", quoted=False),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("crm-settings"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/businesses/{pid}/crm-settings"
# )
# req_collection.add_request(request)

# # Endpoint: /businesses/{pid}/crm-settings, method: Put un authorise
# request = requests.Request([
#     primitives.restler_static_string("PUT "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("businesses"),
#     primitives.restler_static_string("/"),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=False),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("crm-settings"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "bahtToPointRatio":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string(""",
#     "memberCard":
#         {
#             "cover":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ,
#     "pointLifetime":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#     "welcomeBonus":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string("}"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/businesses/{pid}/crm-settings"
# )
# req_collection.add_request(request)

# Endpoint: /config, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("config"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/config"
)
req_collection.add_request(request)

# # Endpoint: /login, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("login"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "email":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "password":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("}"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/login"
# )
# req_collection.add_request(request)

# # Endpoint: /login-phone, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("login-phone"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "phoneNumber":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("}"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/login-phone"
# )
# req_collection.add_request(request)

# Endpoint: /menu, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("menu"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("businessId="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/menu"
)
req_collection.add_request(request)

# # Endpoint: /menu/associate, method: Put Method not allow
# request = requests.Request([
#     primitives.restler_static_string("PUT "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("menu"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("associate"),
#     primitives.restler_static_string("?"),
#     primitives.restler_static_string("businessId="),
#     #primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#      primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "groups":
#     [
#         """),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string("""
#     ],
#     "menus":
#     [
#         """),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string("""
#     ]}"""),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/menu/associate"
# )
# req_collection.add_request(request)

# # Endpoint: /menu/groups, method: Put
# request = requests.Request([
#     primitives.restler_static_string("PUT "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("menu"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("groups"),
#     primitives.restler_static_string("?"),
#     primitives.restler_static_string("businessId="),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "menuGroups":
#     [
#         {
#             "id":"""),
#     primitives.restler_static_string('"'),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string("""",
#             "name":
#                 {
#                     "english":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#                     "primary":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#                     "thai":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#                 }
#             ,
#             "recommended":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#             "seq":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string("""
#         }
#     ]}"""),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/menu/groups"
# )
# req_collection.add_request(request)

# # Endpoint: /menu/items, method: Put
# request = requests.Request([
#     primitives.restler_static_string("PUT "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("menu"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("items"),
#     primitives.restler_static_string("?"),
#     primitives.restler_static_string("businessId="),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "description":
#         {
#             "english":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "primary":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "thai":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ,
#     "id":"""),
#     primitives.restler_static_string('"'),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string("""",
#     "menuGroupIds":
#     [
#         """),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string("""
#     ],
#     "name":
#         {
#             "english":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "primary":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "thai":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ,
#     "photo":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#     "price":
#         {
#             "exact":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string(""",
#             "max":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string(""",
#             "min":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string(""",
#             "text":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#         }
#     ,
#     "properties":
#     [
#         {
#             "max":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#             "min":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#             "name":
#                 {
#                     "english":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#                     "primary":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#                     "thai":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#                 }
#             ,
#             "type":"""),
#     primitives.restler_fuzzable_group("fuzzable_group_tag", ['CHECKBOX','RADIO']  ,quoted=True),
#     primitives.restler_static_string(""",
#             "values":
#             [
#                 {
#                     "additionalPrice":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string(""",
#                     "name":
#                         {
#                             "english":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#                             "primary":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#                             "thai":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#                         }
#                     ,
#                     "outOfStock":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string("""
#                 }
#             ]
#         }
#     ],
#     "recommended":"""),
#     primitives.restler_fuzzable_bool("true"),
#     primitives.restler_static_string(""",
#     "seq":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string("}"),
#     primitives.restler_static_string("\r\n"),
    
#     {
#         'post_send':
#         {
#             'parser': parse_menuitemsput,
#             'dependencies':
#             [
#                 _menu_items_put_id.writer(),
#                 _menu_items_put_seq.writer()
#             ]
#         }
#     },

# ],
# requestId="/menu/items"
# )
# req_collection.add_request(request)

# # Endpoint: /menu/items/{id}/available-status, method: Put
# request = requests.Request([
#     primitives.restler_static_string("PUT "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("menu"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("items"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("available-status"),
#     primitives.restler_static_string("?"),
#     primitives.restler_static_string("businessId="),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "availableStatus":"""),
#     primitives.restler_fuzzable_group("fuzzable_group_tag", ['AVAILABLE','SOLD_OUT_TODAY','SUSPENDED','TERMINATED']  ,quoted=True),
#     primitives.restler_static_string("}"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/menu/items/{id}/available-status"
# )
# req_collection.add_request(request)

# # Endpoint: /menu/property-values/mark-out-of-stock, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("menu"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("property-values"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("mark-out-of-stock"),
#     primitives.restler_static_string("?"),
#     primitives.restler_static_string("businessId="),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "propertyValueNames":
#     [
#         """),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#     ]}"""),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/menu/property-values/mark-out-of-stock"
# )
# req_collection.add_request(request)

# # Endpoint: /menu/sort, method: Put
# request = requests.Request([
#     primitives.restler_static_string("PUT "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("menu"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("sort"),
#     primitives.restler_static_string("?"),
#     primitives.restler_static_string("businessId="),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "groupId":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#     "menuItems":
#     [
#         {
#             "id":"""),
#     primitives.restler_static_string('"'),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string("""",
#             "seq":"""),
#     primitives.restler_static_string('"'),
#     primitives.restler_static_string(_menu_items_put_seq.reader()),
#     primitives.restler_static_string(""""
#         }
#     ]}"""),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/menu/sort"
# )
# req_collection.add_request(request)



# Endpoint: /orders, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orders"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("orderStatus="),
    primitives.restler_fuzzable_group("fuzzable_group_tag", ['CREATED','IN_PROGRESS','DELIVERING','FINISH']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("businessId="),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    #primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orders"
)
req_collection.add_request(request)

# Endpoint: /orders/count, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orders"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("count"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("businessId="),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    #primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orders/count"
)
req_collection.add_request(request)

# Endpoint: /orders/history, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orders"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("history"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("date="),
    #primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_fuzzable_datetime("2021/04/01", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("businessId="),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    #primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orders/history"
)
req_collection.add_request(request)

# Endpoint: /orders/history/list, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orders"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("history"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("list"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("date="),
    #primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_fuzzable_datetime("2021/04/01", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("businessId="),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    #primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("orderStatus="),
    primitives.restler_fuzzable_group("fuzzable_group_tag", ['FINISH','CANCELED']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orders/history/list"
)
req_collection.add_request(request)

# Endpoint: /orders/history/statistics, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("orders"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("history"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("statistics"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("date="),
    #primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_fuzzable_datetime("2021/04/01", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("businessId="),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    #primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/orders/history/statistics"
)
req_collection.add_request(request)

# # Endpoint: /orders/test-order, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("orders"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("test-order"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/orders/test-order"
# )
# req_collection.add_request(request)

# # Endpoint: /orders/{id}, method: Get Dnno order id
# request = requests.Request([
#     primitives.restler_static_string("GET "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("orders"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/orders/{id}"
# )
# req_collection.add_request(request)

# # Endpoint: /orders/{id}, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("orders"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "additionalItems":
#     [
#         {
#             "name":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "price":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string("""
#         }
#     ],
#     "items":
#     [
#         {
#             "memo":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "menuItemId":"""),
#     primitives.restler_static_string('"'),
#     primitives.restler_static_string(_menu_items_put_id.reader()),
#     primitives.restler_static_string("""",
#             "name":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "quantity":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#             "totalPrice":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string(""",
#             "unitPrice":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string("""
#         }
#     ],
#     "structuredOrderItems":
#     [
#         {
#             "memo":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "name":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#             "options":
#             [
#                 {
#                     "key":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#                     "values":
#                     [
#                         {
#                             "key":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("""
#                         }
#                     ]
#                 }
#             ],
#             "quantity":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string("""
#         }
#     ]}"""),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/orders/{id}"
# )
# req_collection.add_request(request)

# # Endpoint: /orders/{id}/read-cancelled, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("orders"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("read-cancelled"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/orders/{id}/read-cancelled"
# )
# req_collection.add_request(request)

# # Endpoint: /orders/{id}/readed, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("orders"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("readed"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/orders/{id}/readed"
# )
# req_collection.add_request(request)

# # Endpoint: /orders/{id}/status, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("orders"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("status"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "averageWaitTimeInSecond":"""),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(""",
#     "rejectDescription":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "rejectReason":"""),
#     primitives.restler_fuzzable_group("fuzzable_group_tag", ['SHOP_CLOSED','OUT_OF_STOCK','NOT_AVAILABLE','OTHER']  ,quoted=True),
#     primitives.restler_static_string(""",
#     "status":"""),
#     primitives.restler_fuzzable_group("fuzzable_group_tag", ['IN_PROGRESS','READY_TO_PICK_UP','CANCEL_OWNER']  ,quoted=True),
#     primitives.restler_static_string("}"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/orders/{id}/status"
# )
# req_collection.add_request(request)

# # Endpoint: /photo, method: Post Type is require
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("photo"),
#     primitives.restler_static_string("?"),
#     primitives.restler_static_string("businessId="),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     #primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/photo"
# )
# req_collection.add_request(request)

# Endpoint: /promote/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("promote"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/promote/{id}"
)
req_collection.add_request(request)

# # Endpoint: /report, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("report"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "endDate":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "startDate":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("}"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/report"
# )
# req_collection.add_request(request)

# # Endpoint: /report/summary/send, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("report"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("summary"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("send"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "endDate":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "restaurantId":"""),
#     primitives.restler_fuzzable_number("1.23"),
#     primitives.restler_static_string(""",
#     "startDate":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("}"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/report/summary/send"
# )
# req_collection.add_request(request)

# # Endpoint: /report/{id}, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("report"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "endDate":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "startDate":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("}"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/report/{id}"
# )
# req_collection.add_request(request)

# Endpoint: /reviews, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("reviews"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("businessId="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.2.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/reviews"
)
req_collection.add_request(request)

# # Endpoint: /reviews/{id}, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("reviews"),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string(_businesses_get_businesses_0_id.reader()),
#     primitives.restler_static_string("?"),
#     primitives.restler_static_string("businessId="),
#     primitives.restler_fuzzable_int("1"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "description":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("}"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/reviews/{id}"
# )
# req_collection.add_request(request)

# Endpoint: /users/settings, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/settings"
)
req_collection.add_request(request)

# Endpoint: /users/settings, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("settings"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_static_string("Content-Type: application/json\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "subscribeMonthlyReport":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "subscribeWeeklyReport":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
    "testingMode":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/settings"
)
req_collection.add_request(request)

# Endpoint: /users/token, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("users"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("token"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("accept-version: <=7.20201123.0\r\n"),
    primitives.restler_static_string("Host: localhost:3000\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/users/token"
)
req_collection.add_request(request)

# # Endpoint: /validate-phone-login, method: Post
# request = requests.Request([
#     primitives.restler_static_string("POST "),
#     primitives.restler_static_string("/"),
#     primitives.restler_static_string("validate-phone-login"),
#     primitives.restler_static_string(" HTTP/1.1\r\n"),
#     primitives.restler_static_string("Accept: application/json\r\n"),
#     primitives.restler_static_string("Host: localhost:3000\r\n"),
#     primitives.restler_static_string("Content-Type: application/json\r\n"),
#     primitives.restler_refreshable_authentication_token("authentication_token_tag"),
#     primitives.restler_static_string("\r\n"),
#     primitives.restler_static_string("{"),
#     primitives.restler_static_string("""
#     "code":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string(""",
#     "phoneNumber":"""),
#     primitives.restler_fuzzable_string("fuzzstring", quoted=True),
#     primitives.restler_static_string("}"),
#     primitives.restler_static_string("\r\n"),

# ],
# requestId="/validate-phone-login"
# )
# req_collection.add_request(request)
