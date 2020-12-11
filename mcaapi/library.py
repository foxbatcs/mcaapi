# libraries
import requests
import json

def api_response(url, head = HEAD):
  response = requests.get(url, headers=head)
  apiResponse = json.loads(response.text)
  #apiResponseDictKeys = list(apiResponse.keys()) 
  #print(apiResponseDictKeys)
  return apiResponse#, apiResponseDictKeys
