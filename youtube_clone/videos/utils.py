from apiclient.discovery import build

from .config import (DEVELOPER_KEY,
					 YOUTUBE_API_SERVICE_NAME,
					 YOUTUBE_API_VERSION)


def youtube_search(keyword, max_results):

  	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    			 developerKey=DEVELOPER_KEY)

  	# Call the search.list method to retrieve results matching the specified
  	# query term.
 	videos = []
  	search_response = youtube.search().list(q=keyword,
    									 part="id,snippet",
    									 maxResults=max_results).execute()
  	results = search_response.get("items", [])
  	return results
 
	# for search_result in search_response.get("items", []):
	# 	if search_result["id"]["kind"] == "youtube#video":
	# 	  videos.append("%s (%s)" % (search_result["snippet"]["title"],
	# 	                             search_result["id"]["videoId"]))

	# return videos
