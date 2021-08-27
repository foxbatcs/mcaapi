import os
#defines absolute path and the api token file name
here = os.path.abspath(os.path.dirname(__file__))
token_path = os.path.join(here, 'api_token.txt')

def apiToken(token_path):
    api_token = input('''
Use of this library requires obtaining an API Key from
The Maricopa County Assessor's Office. This can be done by
visiting https://preview.mcassessor.maricopa.gov/contact/
and filling out the form.

Change the "Subject" Field to "API Token/Question",
provide your name, number, and a brief note. Then click
"Send Message". MCA's web developer will send you an email
shortly after with the API Key. You can hit CTRL-C to exit.

If you already have a key, please enter it here:
    ''')

    with open(token_path, 'w') as file:
        file.write(api_token)
        file.close()

    print(f'''
    ============================================

    Your key has been set to:

    {api_token}

    ============================================
    ''')
    return api_token

#print('APItoken.py CWD: ', os.getcwd())
if os.path.isfile(token_path) == True:
    with open(token_path, 'r') as file:
        API_TOKEN = file.read().strip()
else:
    API_TOKEN = apiToken(token_path)
    #print(API_TOKEN)

#         if API_TOKEN == '':
#             MCA_API_TKN = API_TOKEN
#             print('''
# instructions to call the method again
#             ''')
#         else:
#             MCA_API_TKN = API_TOKEN

    #print('api_token.txt isfile: False')
