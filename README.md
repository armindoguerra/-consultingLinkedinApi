# Consulta a Lookup API do Linkedin v2

Essa aplicação tem como objetivo consultar informações de empresas na API oferecida pela Linkedin. As seguintes informções serão consultadas:

    • entityStatus;
    • vanityName;
    • id;
    • industries;
    • foundedOn;
    • website;
    • specialties;
    • staffCountRange;

Para maiores informações sobre a API acesse: https://developer.linkedin.com/docs/guide/v2/organizations/organization-lookup-api

Os nomes das empresas a serem consultados podem ser inseridas no arquivo que executa a aplicação (`test.py`). O projeto exige poucas dependências, além do Python 3, são necessários os pacotes `requests` e `json`

Para iniciar a aplicação, basta executar:
 ```
 $ python test.py
 ```
Um arquivo `data.json` será gerado com o resultado no mesmo diretório em que os códigos fontes estão.








