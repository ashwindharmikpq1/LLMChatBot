import requests


def set_token():
    url = "https://securetoken.googleapis.com/v1/token?key=AIzaSyAwuXaQy86JJJSf95NfcL5PK9d_NbA_9hc"

    payload = ('grant_type=refresh_token&'
               'refresh_token=AMf-vBzXgFLf-_qqjlk3fha13clkq5rwotKi0GAluIFNVlBPYoy3mXWzOcmvcPOLqeL0B_'
               'Y2dTNFnkHTTooxnAhS1HAb89PyBIf2s2ugXhWsikVlmphQML9KL737AYXYtqgbrGaIEg2NCjG6mgxoYkaFykT8GEmkS5C_'
               'jgJLPeRbkUARRfcv3zWuOrbCdblnDQbhpAsiavF5jmWi_CRohEF4OwotiPYHpL6wXlEdVSCkM1osaDbxc_A')
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = response.json()

    # Get the access token
    access_token = response_json.get("access_token")
    # print("Access Token:", access_token)

    if access_token:
        # Read the current content of the .env file
        with open('.env', 'r') as env_file:
            lines = env_file.readlines()

        # Write the updated content back, replacing the TOKEN line if it exists
        with open('.env', 'w') as env_file:
            token_found = False
            for line in lines:
                if line.startswith('TOKEN='):
                    env_file.write(f'TOKEN={access_token}\n')
                    token_found = True
                else:
                    env_file.write(line)

            # If TOKEN was not found, add it at the end
            if not token_found:
                env_file.write(f'TOKEN={access_token}\n')


# set_token()
