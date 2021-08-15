## SNET CRUD

<br />

[![Author](https://img.shields.io/badge/author-lukassousaf-1E90FF?style=flat-square)](https://github.com/lukassousaf)
[![Languages](https://img.shields.io/github/languages/count/lukassousaf/snet-project?color=%231E90FF&style=flat-square)](#)
[![Stars](https://img.shields.io/github/stars/lukassousaf/snet-project?color=1E90FF&style=flat-square)](https://github.com/lukassousaf/login-page/snet-project)
[![Forks](https://img.shields.io/github/forks/lukassousaf/snet-project?color=%231E90FF&style=flat-square)](https://github.com/lukassousaf/snet-project/network/members)
[![Contributors](https://img.shields.io/github/contributors/lukassousaf/snet-project?color=1E90FF&style=flat-square)](https://github.com/lukassousaf/snet-project/graphs/contributors)

## Instalação:

<h3 align="justify">Instalar django</h3>

```bash
$ pip install django
```

<h3 align="justify">Instalar as dependências</h3>

```bash
$ pip install -r requirements.txt
```

<h3 align="justify">Criar um ambiente virtual</h3>

```bash
$ python -m venv venv
```

<h3 align="justify">Ativar o ambiente virtual</h3>

```bash
$ .\venv\Scripts\Activate
```

## Banco de Dados

<h3 align="justify">Criar um banco de dados postgresql e configurar em DATABASES no arquivo

**`settings.py`** </h3>

<h3 align="justify">Alterar o "NAME", "USER" e "PASSWORD" </h3>

```

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "bancodedados",
        "USER": "postgres",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": 5432,
    }
}
```

## Iniciar

```bash
$ python manage.py runserver
```
