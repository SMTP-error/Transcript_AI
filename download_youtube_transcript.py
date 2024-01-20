from youtube_transcript_api import YouTubeTranscriptApi
import sys
import json

if len(sys.argv) == 2:
	print(json.dumps(YouTubeTranscriptApi.get_transcript(sys.argv[1])))
elif len(sys.argv) == 3 and '-t' in sys.argv:
	sys.argv.remove('-t')
	transcript = YouTubeTranscriptApi.get_transcript(sys.argv[1])
	for rec in transcript:
		print(rec['text'])

