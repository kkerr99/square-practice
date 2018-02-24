#!/usr/bin/python
import httplib, json

# All requests to the Square Connect API require an access token in an
# Authorization header. Specify your application's personal access token here.
# Available from the Application Dashboard: https://connect.squareup.com/apps
access_token = 'sq0atp-vxVbGUVmxgnNa1HQeTqAYw'

# In addition to an Authorization header, requests to the Connect API should
# include the indicated Accept and Content-Type headers.
request_headers = {'Authorization': 'Bearer ' + access_token,
                   'Accept':        'application/json',
                   'Content-Type':  'application/json'}

# Send a GET request to the ListLocations endpoint and obtain the response.
request_path = '/v2/locations'
request_body = ''

connection = httplib.HTTPSConnection('connect.squareup.com')
connection.request('GET', request_path, request_body, request_headers)
response = connection.getresponse()

# Convert the returned JSON body into an array of locations you can work with.
locations = json.loads(response.read())

# Pretty-print the locations array.
print json.dumps(locations, indent=2, separators=(',',': '))
