require 'json'
require 'httparty'

# url='https://app.adparlor.com/api/facebook/report-raw'  # USE THIS URL IF YOU'RE FETCHING FACEBOOK STATS
# url='https://app.adparlor.com/api/twitter/v1/stats/normandy/query'  # USE THIS URL IF YOU'RE FETCHING TWITTER STATS
query = '' # PUT YOUR QUERY PROVIDED HERE
access_token = "" # PUT YOUR PROVIDED ACCESS TOKEN HERE

headers = {
  "X-Wsse" => access_token,
  "Accept" => "application/json",
  "Content-type" => "application/x-www-form-urlencoded"
}

result = HTTParty.get(url, {body: query, headers: headers})
parsed_data = JSON.parse(result.body)

mapped_results = []
parsed_data["data"]["metrics"].each do |row|
  mapped_results.push(row["dimensions"].merge(row["stats"]))
end

# You can now use mapped_results as flat objects
p mapped_results