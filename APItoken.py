import os

def apiToken():
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

    with open('api_token.txt', 'w') as file:
        file.write(api_token)
        file.close()

    print(f'''
    ============================================

    Your key has been set to:

    {api_token}

    ============================================
    ''')
    return api_token

if os.path.isfile('api_token.txt') == True:
    with open('api_token.txt', 'r') as file:
        API_TOKEN = file.read().strip()
else:
    with open('api_token.txt', 'w') as file:
        API_TOKEN = apiToken()
        file.write(API_TOKEN)
        print(API_TOKEN)
        file.close()
        if API_TOKEN == '':
            MCA_API_TKN = API_TOKEN
            print('''
instructions to call the method again
            ''')
        else:
            MCA_API_TKN = API_TOKEN

    #print('api_token.txt isfile: False')
    file.close()
