import requests
import json

"""
As informações redirect_uri, client_id e client_secret são obtidas ao criar uma aplicação na plataforma do 
Linkedin em https://www.linkedin.com/secure/developer?newapp=
A variável code é obtida configurando a autenticação oauth2. https://developer.linkedin.com/docs/oauth2
"""

class AuthenticationApi(object):

	def __init__(self):
        print("init")
        pass

	def oauth2(self):

		url = "https://www.linkedin.com/oauth/v2/accessToken"

		code = "..."

		Headers = {	    
		    "Content-Type":"application/x-www-form-urlencoded"
		}

		payload = {
			"grant_type":"authorization_code",
			"code":code,
			"redirect_uri":"...",
			"client_id":"...",
			"client_secret": "..."
		} 

		r = requests.post(url, data=json.dumps(payload), headers=Headers)
		json_data = json.loads(r.text)
		
		accessToken = json_data["access_token"]

		return accessToken
