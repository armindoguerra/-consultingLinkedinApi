#!/usr/bin/env python

import pandas as pd
import json
import os
from flask import Flask
from flask import request, jsonify
import requests


# Flask app should start in global layout
app = Flask(__name__)


@app.route('/login/callback', methods=['POST'])
def auth_my_app():

	# Informações obtidas ao criar aplicação no plataforma do linkedin https://www.linkedin.com/secure/developer?newapp=
	client_id = "..."
	client_secret = "..."
	redirect_uri = "https://..." 
    
	# Código obtido por meio da autenticação oauth2, descrita em https://developer.linkedin.com/docs/oauth2
	code = "..." # 
	
	# Obtendo access_token para realizar as requisições
	url = 'https://www.linkedin.com/oauth/v2/accessToken'

	Headers = {	    
	    "Content-Type":"application/x-www-form-urlencoded",
	    "Accept": "application/json"
	}

	payload = {
		"grant_type":"authorization_code"
		"code":code
		"redirect_uri":redirect_uri
		"client_id":client_id
		"client_secret": client_secret
	} 

	r = requests.post(url, data=json.dumps(payload), headers=Headers)
	json_data = json.loads(r.text)
	access_token = json_data["access_token"]

	return access_token

def linkedin_companies_parser(url):

	# Montando a requisição para a API do Linkedin

	r = request.get_json(url, headers={'Authorization': auth_my_app()})

	entityStatus = r["entityStatus"]
	vanityName = r["vanityName"]	
	id1 = r["id"]
	industries = r["industries"]
	foundedOn = ra["foundedOn"]
	website = r["website"]
	specialties = r["specialties"]
	staffCountRange = r["staffCountRange"]


	data = {
	    "entityStatus":entityStatus,
	    "vanityName":vanityName,
	    "id":id1,
	    "industries":industries,
	    "foundedOn":foundedOn,
	    "website":website,
	    "specialties":specialties,
	    "staffCountRange":staffCountRange

	}

	return data

 
def consult_api():
    
	# Recebendo os dados das empresas que estão no arquivo csv

    df = pd.read_csv('listaEmpresas.csv')

    company_list = [tuple(x) for x in df.values]
    
    extracted_data = []
    for i in company_list:
    	url = 'https://api.linkedin.com/v2/organizations?q=vanityName&vanityName='+i
    	extracted_data.append(linkedin_companies_parser(url))
    	f = open('data.json', 'w')
    	json.dump(extracted_data, f, indent=4)


if __name__ == '__main__':
    
	# Rodando API na porta 8000
    port = int(os.getenv('PORT', 8000))
    app.run(debug=True, port=port)

