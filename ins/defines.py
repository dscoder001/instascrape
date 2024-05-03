import requests
import json

def getCreds() :
	""" Get creds required for use in the applications
	
	Returns:
		dictonary: credentials needed globally

	"""

	creds = dict() # dictionary to hold everything
	creds['access_token'] = 'EAAPuZBW1w6YMBOwrJHLgnv0eEL6ONiyxTebfod7yoWP2IN9j0zcMzVZBowhUVaQQ0Tjge06MBlAPCwLO2xZAEj4y11oQhMu9JKIiAZA3qJrV0ZAJLJ8ZBKsAYkQUxTknUO5fSwZCBz0OMy0O8bNhho8XTNZAvcqJ3gVZADZA7nYfcoUWFHkfk6jMWI2nAg' # access token for use with all api calls
	creds['client_id'] = '1107179980515715' # client id from facebook app IG Graph API Test
	creds['client_secret'] = '04d408e8ede3f08ce0d5b9a1c1df3cdc' # client secret from facebook app
	creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
	creds['graph_version'] = 'v19.0' # version of the api we are hitting
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
	creds['debug'] = 'no' # debug mode for api call
	creds['page_id'] = '288635377667802' # users page id
	creds['instagram_account_id'] = '17841466372695032'
	creds['ig_username'] = 'cosmetics_world64'
	return creds

def makeApiCall( url, endpointParams, debug = 'no' ) :
	""" Request data from endpoint with params
	
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters


	Returns:
		object: data from the endpoint

	"""

	data = requests.get( url, endpointParams ) # make get request

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

	if ( 'yes' == debug ) : # display out response info
		displayApiCallData( response ) # display response

	return response # get and return content

def displayApiCallData( response ) :
	""" Print out to cli response from api call """

	print("\nURL: ") # title
	print(response['url']) # display url hit
	print("\nEndpoint Params: " )# title
	print(response['endpoint_params_pretty']) # display params passed to the endpoint
	print("\nResponse: ") # title
	print(response['json_data_pretty']) # make look pretty for cli