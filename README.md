# teste-python

## Teste para a empresa Polibras Software

1. O programa foi feito em python 3
2. Foi utilizado o software Postman (https://www.getpostman.com/) para realizar os comandos de GET, POST, PUT e DELETE  no servidor
2. É preciso utilizar um ambiente virtual para executar o projeto. Para isso, abra o terminal na pasta raiz e faça o seguinte:
    
    ## Ativar ambiente virtual
    $ pipenv shell

    ## Instalar as dependencias
    $ pipenv install
    
    * Caso os comandos não funcionem, é preciso instalar o pipenv e suas dependências, assim:
      $ pip3 install pipenv
    - Um arquivo chamado pipfile será criado, e nele estarão as dependências necessárias para a execução do projeto.
    - Agora entre no ambiente virtual com "pipenv shell" e instale as dependências
      $ pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy

    ## Criar Banco
    ```bash
    $ python
    >> from main import db
    >> db.create_all()
    >> exit()
    
    # Excluir Banco (caso seja necesssário)
    
    $ python
    >> from main import db
    >> db.create_all()
    >> exit()
    ```

    ## Iniciar o Servidor (http://localhost:5000)
    python main.py
    
    # Faça as requisições utilizando o Postman
    Execute o software e insira a url do servidor (http://localhost:5000) + enpoint
    
    Escolha qual requisição (POST, GET, PUT, DELETE) e clique em SEND
    
    ### Endpoints Empresa
    * GET /company
    * GET /company/:id
    * POST /company
    * PUT /company/:id
    * DELETE /company/:id
    
    ### Endpoints Versões
    * GET /version
    * GET /version/:id
    * POST /version
    * PUT /version/:id
    * DELETE /version/:id
    
