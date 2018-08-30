# Linkedin Organizations App

Essa aplicação recebe de um arquivo csv com uma lista de nomes de empresas e retorna um arquivo json com os seguintes dados: 

    • entityStatus;
    • vanityName;
    • id;
    • industries;
    • foundedOn;
    • website;
    • specialties;
    • staffCountRange;

Foi utilizada a Organization Lookup API do Linkedin v2 (https://developer.linkedin.com/docs/guide/v2/organizations/organization-lookup-api) 

Para executar a aplicação é necessário ter alguns pacotes instalados. 

```
$ pip install -r requirements.txt
```

Após a instalação dos pacotes, basta salvar o arquivo csv no mesmo diretório em qua está o código fonte da aplicação `app.py`.

Para iniciar a aplicação, basta executar:
 ```
 $ python app.py
 ```










