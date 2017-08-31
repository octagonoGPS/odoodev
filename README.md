[![Build Status](http://runbot.odoo.com/runbot/badge/flat/1/10.0.svg)](http://runbot.odoo.com/runbot)
[![Tech Doc](http://img.shields.io/badge/10.0-docs-875A7B.svg?style=flat)](http://www.odoo.com/documentation/10.0)
[![Help](http://img.shields.io/badge/10.0-help-875A7B.svg?style=flat)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](http://img.shields.io/badge/10.0-nightly-875A7B.svg?style=flat)](http://nightly.odoo.com/)


# Instalacion y configuracion de la plataforma

Lo primero que hay que hacer es actualizar la distribucion

```
sudo apt-get dist-upgrade
```

Luego reiniciamos

```
sudo reboot
```

Instalamos postgresql

```
sudo apt-get install postgresql
```

Cambiamos al usuario de postgres

```
sudo su - postgres
```

Le damos permiso al usuario para crear bases de datos y salimos

```
createuser --createdb --username postgres --no-createrole --pwprompt odoodev
exit
```

Instalamos las siguientes dependencias

```
sudo apt-get install python-cups python-dateutil python-decorator python-docutils python-feedparser

sudo apt-get install python-gdata python-geoip python-gevent python-imaging python-jinja2 python-ldap python-libxslt1 python-lxml python-mako python-mock python-openid python-passlib python-psutil python-psycopg2 python-pybabel python-pychart python-pydot python-pyparsing python-pypdf python-reportlab python-requests python-simplejson python-tz python-unicodecsv python-unittest2 python-vatnumber python-vobject

sudo apt-get install python-werkzeug python-xlwt python-yaml wkhtmltopdf

sudo apt-get install python-pip python-dev libevent-dev gcc libxml2-dev libxslt-dev node-less geoip-database-contrib
```

Instalamos git

``` 
sudo apt-get install git
```

Agregamos el repositorio

```
git remote add octagono git@bitbucket.org:octagono_dev/odoo-octagono.git
```

Luego creamos un directorio e inicializamos un repositorio vacio

```
git init
```

Por ultimo nos traemos los archivos desde el repositorio (Debe tener [configurado](#configuracion-con-bitbucket) las claves SSH)

```
git pull octagono master
```

# Ejecucion del servidor Odoo

Nos vamos a la carpeta de donde nos bajamos el proyecto y ejecutamos lo siguiente

```
./odoo-bin
```

# Configuracion con Bitbucket
----

Es importante configurar las claves SSH con Bitbucket antes de traernos los archivos desde el repositorio, el siguiente es un tutorial de la misma pagina de Bitbucket para realizar dicha configuracion

[Tutorial SSH con Bitbucket](https://confluence.atlassian.com/bitbucket/set-up-ssh-for-git-728138079.html)

Si no sabe manejar GIT, este es un muy buen curso para aprender lo basico

[Tutorial GIT](https://www.codeschool.com/courses/try-git)
