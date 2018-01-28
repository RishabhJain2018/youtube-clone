from django.shortcuts import render

from .utils import youtube_search


def get_video_by_keyword(request):
	keyword = request.GET.get('q') # get_keyword
	if not keyword:
		print "No keyword is provided"
		pass
	data = youtube_search(keyword, 5) # pass keyword with max videos value
	print data
	# return data

	