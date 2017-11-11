import subprocess, json, datetime, sys

# load API KEY
from myenv import KEY

# template of youtube play url
URL_TEMPLATE = 'https://www.youtube.com/embed/'

# template of youtube search command
SEARCH_CMD_TEMPLATE = 'curl "https://www.googleapis.com/youtube/v3/search?part=id&order=date&key=' + KEY

# get today's date for video search
today = datetime.datetime.today()
today_str = today.strftime("%Y-%m-%dT00:00:00Z")
AfterTodayFilter = '&publishedAfter=' + today_str

# search command today's video of A.I.Channel
aichannel_search_cmd = SEARCH_CMD_TEMPLATE + '&channelId=UC4YaOt1yT-ZeyB0OmxHgolA'
aichannel_search_cmd = aichannel_search_cmd + AfterTodayFilter + '"'

# search command today's video of A.I.Games
aigames_search_cmd = SEARCH_CMD_TEMPLATE + '&channelId=UCbFwe3COkDrbNsbMyGNCsDg'
aigames_search_cmd =  aigames_search_cmd + AfterTodayFilter + '"'

# search A.I.Channel
proc_c = subprocess.Popen(aichannel_search_cmd,stdout=subprocess.PIPE, shell=True)
out = proc_c.communicate()[0]
items_c = json.loads(out)['items']

# search A.I.Games
proc_g = subprocess.Popen(aigames_search_cmd,stdout=subprocess.PIPE, shell=True)
out = proc_g.communicate()[0]
items_g = json.loads(out)['items']

# if today's video is empty, then keep last search result and exit
if len(items_c) == 0 and len(items_g) == 0:
  sys.exit()

# make playlist url for playing
is_first_video = True
url = URL_TEMPLATE
for video_c in items_c:
  vid = video_c['id']['videoId']
  if is_first_video:
    is_first_video = False
    url += vid + '?autoplay=1&cc_load_policy=0&playlist='
  else:
    url += vid + ','
for video_g in items_g:
  vid = video_g['id']['videoId']
  if is_first_video:
    is_first_video = False
    url += vid + '?autoplay=1&cc_load_policy=0&playlist='
  else:
    url += vid + ','

f = open('playlisturl.txt','w')
f.write(url)
f.close()
