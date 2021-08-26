# Assessor API request URL
URL = 'https://api.mcassessor.maricopa.gov/'

with open('api_token.txt', 'r') as file:
    API_TOKEN = file.read().strip()
    file.close()
PAYLOAD={}
HEAD = {
  'AUTHORIZATION': API_TOKEN
}
