import requests
import json

"""
As informações redirect_uri, client_id e client_secret são obtidas ao criar uma aplicação na plataforma do 
Linkedin em https://www.linkedin.com/secure/developer?newapp=

A variável code é obtida configurando a autenticação oauth2. https://developer.linkedin.com/docs/oauth2
"""

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
print(json_data)