# libraries
import requests
import json

def api_response(url, head = HEAD):
  response = requests.get(url, headers=head) # What is the difference between `x = 4` and something like `headers=head`
  apiResponse = json.loads(response.text) # Why didn't we write `apiResponse = json.loads(requests.get(url, headers=head).text)`? Readability?
  #apiResponseDictKeys = list(apiResponse.keys()) # Does `apiResponse.keys()` scan the json file for "keys" and in this case put them into a list? 
  #print(apiResponseDictKeys)
  return apiResponse#, apiResponseDictKeys