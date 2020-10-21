# learnops-python

Apredendo a codar: Um pequeno sistema em Python

Leia, pode te ajudar: https://python.org.br/introducao/

## Requisitos básicos

- Uma API capaz de responder um catalogo de produtos, com preço em BRL, USD e EUR
  - método para responder o valor do EUR em função do BRL
  - método para responder o valor do USD em função do BRL
  - método para listar os produtos do catalogo com valor apenas em BRL
  - método para listar todos os produtos com preços em todas as moedas listadas
  - Formato da resposta

```json
{
  "time": "HORARIO_DA_CONSULTA",
  "last-refresh": "HORARIO_DA_COTACAO",
  "products": [
    {
      "id": "ID_DO_PRODUTO1",
      "name": "NOME_DO_PRODUTO1",
      "prices": {
        "BRL": 1,
        "USD": 5.5,
        "EUR": 6
      }
    },
    {
      "id": "ID_DO_PRODUTO2",
      "name": "NOME_DO_PRODUTO2",
      "prices": {
        "BRL": 2,
        "USD": 11,
        "EUR": 12
      }
    }
  ]
}
```

- A cotação das outras moedas deve vir da API https://economia.awesomeapi.com.br/all/USD-BRL para USD e https://economia.awesomeapi.com.br/all/EUR-BRL para EUR
    - Caso prefira, você pode tentar pegar todas as moedas e depois internamente usar o identificador para encontrar a cotação com a URL https://economia.awesomeapi.com.br/all (recomendo esse caminho)
- O catalogo a ser usado: catalog.txt (arquivo separado por TAB: \t)
  - deve ser carregado do arquivo no inicio do programa e deixado em uma estrutura de dados para acesso dos demais métodos (https://www.w3schools.com/python/python_file_handling.asp)

## Requisitos extras

- Use um banco de dados para armazenar as informações:
  - postgres: https://www.postgresqltutorial.com/postgresql-python/
  - mysql: https://www.w3schools.com/python/python_mysql_getstarted.asp
- Crie um mecânismo de autênticação
  - Uma integração com firebase usando login de redes sociais seria ótimo
  - Apenas pedidos com autenticação podem ter acesso aos dados da API
- Crie uma interface web para exibir as informações
- Sua a aplicação usando containers
- Faça a automação de todo o processo de publicação e provisionamento da solução
- Publique seu código no git

## Dicas

### Onde começar a procurar?
https://www.w3schools.com/python/default.asp é uma ótima opção, tem muito conteúdo e de uma forma bem didática

### Configurando o ambiente
- use python 3 (https://www.python.org/downloads/)
  - Linux: https://python.org.br/instalacao-linux/
  - Windows: https://python.org.br/instalacao-windows/
- instale o pip como sudo/administrador (https://pip.pypa.io/en/stable/installing/)
- usar virtualenv para criar o ambiente de desenvolvimento (https://virtualenv.pypa.io/en/latest/installation.html)
- user o fastAPI para fazer as APIs (https://fastapi.tiangolo.com/deployment/)
  
### Vai te evitar dor de cabeça no futuro
- crie classes para os dados que vai guardar em memória e para as respostas
- user o modulo de json do próptio python para fazer as respostas

### Como chamar uma API no python

```python
import requests
import json

req = requests.get("example_url")
response = req.json()

print(response)
```

### Como ativar o virtualenv

```shell
source bin/activate
```

### Como executar a aplicação em modo de web server

```shell
./run.sh
```

Não entendeu qualquer coisa q está escrito aqui? pesquise, leia, anote as dúvidas (qualquer uma) e me pergunte.

