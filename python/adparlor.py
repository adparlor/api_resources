import json
import httplib, ssl, urllib2, socket

# url='https://app.adparlor.com/api/facebook/report-raw'  # USE THIS URL IF YOU'RE FETCHING FACEBOOK STATS
# url='https://app.adparlor.com/api/twitter/v1/stats/normandy/query'  # USE THIS URL IF YOU'RE FETCHING TWITTER STATS
query = "" # PUT YOUR QUERY PROVIDED HERE
access_token = "" # PUT YOUR PROVIDED ACCESS TOKEN HERE

req = urllib2.Request(url, query)
req.add_header('Accept', 'application/json')
req.add_header("Content-type", "application/x-www-form-urlencoded")
req.add_header('X-Wsse', access_token)
res = urllib2.urlopen(req)
result = res.read()
data = json.loads(result)

# ROWS ARE IN data["data"]["metrics"]
# TOTALS ARE IN data["data"]["totals"]

# The following take the stats and dimensions objects of each row and combines them
mapped_results = []

for index in range(len(data["data"]["metrics"])):
   core_obj = data["data"]["metrics"][index]
   stats = core_obj["stats"]
   dimensions = core_obj["dimensions"]
   merged_dict = {key: value for (key, value) in (stats.items() + dimensions.items())}
   mapped_results.append(merged_dict)

# You can now use mapped_results as flat JSON objects
print json.dumps(mapped_results)