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