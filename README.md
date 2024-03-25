# AgendaPyPg

NOTA: Utilizar ventana de comandos gitbash

--Instalar virtualenv

pip install virtualenv

-- Crear entorno Virtual

virtualenv venv --python=python3

-- Activar el entorno virtual

source ./venv/Scripts/activate

-- Instalar Librerias necesarias

pip install -r requirements.txt

-- Para instalar otras librerías distintas al archivo requirements, ejecutar (Con entorno virtual activado) lo siguiente:

pip install nombre_libreria

-- Para actualizar el archivo requirements.txt

python -m pip freeze > requirements.txt
