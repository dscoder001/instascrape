from defines import getCreds, makeApiCall
import sys
import csv
import json


def getHashtagInfo( params ) :
	""" Get info on a hashtag
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/ig_hashtag_search?user_id={user-id}&q={hashtag-name}&fields={fields}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['user_id'] = params['instagram_account_id'] # user id making request
	endpointParams['q'] = params['hashtag_name'] # hashtag name
	endpointParams['fields'] = 'id,name' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + 'ig_hashtag_search' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call


def getHashtagMedia( params ) :
	""" Get posts for a hashtag
	
	API Endpoints:
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/top_media?user_id={user-id}&fields={fields}
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['user_id'] = params['instagram_account_id'] # user id making request
	endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type'] # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call


try : # try and get param from command line
	hashtag = sys.argv[1] # hashtag to get info on
except : # default to coding hashtag
	hashtag = 'NorthIndianwedding' # hashtag to get info on
	
params = getCreds() # params for api call
params['hashtag_name'] = hashtag # add on the hashtag we want to search for
hashtagInfoResponse = getHashtagInfo( params ) # hit the api for some data!
params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']; # store hashtag id

print("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> HASHTAG INFO <<<<<<<<<<<<<<<<<<<<\n") # section heading
print("\nHashtag: " + hashtag) # display hashtag
print("Hashtag ID: " + params['hashtag_id']) # display hashtag id

print("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> HASHTAG TOP MEDIA <<<<<<<<<<<<<<<<<<<<\n") # section heading
params['type'] = 'top_media' # set call to get top media for hashtag
hashtagTopMediaResponse = getHashtagMedia( params ) # hit the api for some data!

for post in hashtagTopMediaResponse['json_data']['data'] : # loop over posts
	print("\n\n---------- POST ----------\n") # post heading
	print("Link to post:") # label
	print(post['permalink']) # link to post
	print("\nPost caption:") # label
	print(post['caption']) # post caption
	print("\nMedia type:") # label
	print(post['media_type']) # type of media




with open('hashtag_top_media.json', 'w') as outfile:
  json.dump(hashtagTopMediaResponse['json_data'], outfile)

with open('hashtag_top_media.csv', 'a', newline='') as csvfile:
  writer = csv.writer(csvfile)

for post in hashtagTopMediaResponse['json_data']['data']:
	writer.writerow([post['permalink'], post['caption'], post['media_type']])




print("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> HASHTAG DONE <<<<<<<<<<<<<<<<<<<<\n") # section heading