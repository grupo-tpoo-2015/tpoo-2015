Instalar pip
```
sudo apt-get install python-pip
```

Instalar virtualenv y virtualenvwrapper
```
sudo pip install virtualenv virtualenvwrapper
```

Agregar esto al final del .bashrc
```
export WORKON_HOME=$HOME/

#Virtualenvwrapper config
export WORKON_HOME=~/envs #donde creamos los entornos
VENV_WRAPPER=/usr/local/bin/virtualenvwrapper.sh #script principal

#Si tenemos el script principal entonces lo cargamos al iniciar
if [ -f $VENV_WRAPPER ]; then
source $VENV_WRAPPER
fi
```


Crear entorno virtual
```
mkvirtualenv TPOO
```

Activar entorno virtual
```
workon TPOO
```

Instalar conectores MySql
```
sudo apt-get install python-mysqldb
sudo apt-get install libmysqlclient-dev
sudo apt-get install python-dev
pip install MySQL-python  # que igual ya está en el requirements.txt
```

Para instalar las dependencias con pip:
```
pip install -r requirements.txt
```

Para crear las bases de datos necesarias, ejecutar en la consola de MySQL:
```
CREATE DATABASE tpoo;
CREATE DATABASE tpoodump;
```

Luego de hacer algun cambio en los esquemas:
```
python manage.py makemigrations
python manage.py migrate
```

Para ver si hay migraciones pendientes:
```
python manage.py migrate  --list
```

Desactivar entorno virtual
```
deactivate
```

Instalar Graphviz (necesario para convertir archivos DOT a PNG)
```
sudo apt-get install graphviz
```

Generar un diagrama de los models y convertirlo a PNG
```
python manage.py graph_models usability_tests tasks > models.dot
dot -Tpng models.dot -o models.png
```

Después de instalar algo nuevo con pip, hacer esto:
```
pip freeze > requirements.txt
```