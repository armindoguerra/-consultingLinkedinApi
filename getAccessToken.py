import requests
import json

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