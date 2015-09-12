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
