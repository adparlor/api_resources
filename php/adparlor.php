<?php

# $url='https://app.adparlor.com/api/facebook/report-raw';  # USE THIS URL IF YOU'RE FETCHING FACEBOOK STATS
# $url='https://app.adparlor.com/api/twitter/v1/stats/normandy/query';  # USE THIS URL IF YOU'RE FETCHING TWITTER STATS
$query = ''; # PUT YOUR QUERY PROVIDED HERE
$access_token = ""; # PUT YOUR PROVIDED ACCESS TOKEN HERE

$curl = curl_init();
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_HTTPHEADER, array(
    'X-Wsse: '.$access_token,
    'Accept: application/json',
    'Content-type: application/x-www-form-urlencoded'
    ));
curl_setopt($curl, CURLOPT_POSTFIELDS, $query);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$result = curl_exec($curl);
$parsed_result = json_decode($result, true);

$mapped_results = [];
foreach($parsed_result["data"]["metrics"] as $metric){
  $temp_row = array_merge($metric["dimensions"], $metric["stats"]);
  $mapped_results[] = $temp_row;
}

# You can now use mapped_results as flat objects
print_r($mapped_results);