# Projeto E-commerce CheckApp
feito com Django 2.2.4 e Python 3.7.3.

### Conteúdo educacional

### Este projeto NÃO inclui

- Combinações de variações de produto (tem apenas uma variação)
- Cupons de desconto no carrinho de compras
- Cálculo de frete
- Métodos de pagamento (MercadoPago, PayPal, PagSeguro, enfim...)

### TODOs
Abaixo uma lista do que adicionei ou ainda pretendo adicionar.

- [x] Model produtos
- [x] Model variações
- [x] Listagem e detalhes de produtos e variações
- [x] Carrinho de compras baseado em session
- [x] Remover produtos do carrinho
- [x] Model perfil (criar e atualizar)
- [x] Login e Logout do cliente
- [x] Registrar pedido do cliente
- [x] Página de pagamento

### Tutorial 

1 - Criar a pasta do projeto
2 - Instalatr o django = pip install django
3 - fazer o upgrade do pip = python.exe -m pip install --upgrade pip43 - instalar o pillow para imagens = pip install pillow
4 - instalar o django summernote para editar textossimilar ao word = pip install django-summernote
5 - instalar o MySQL Cliente = pip install mysqlClient
6 - startar o projeto = django-admin startproject nome_do_projeto
7 - startar os aplicativos 


Abaixo uma lista de comandos para clonar e configurar este projeto na sua 
máquina local:

- Instalar git (Windows, Linux e Mac) e depois:

```
link github =
```

- Para **Windows**:

```
pip install django-summernote
pip install requests 
pip install django-admin-interface
pip install django-admin-interface --upgrade

cd django-simple-ecommerce
pip install -U Pillow
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel --user
python -m pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

- Para **Linux**:

```
cd django-simple-ecommerce
python3.7 -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

- Para **Mac**

```
cd django-simple-ecommerce
python -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
```

Pronto!

Admin = admin senha 12345

username senha 123
