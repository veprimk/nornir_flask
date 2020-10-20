git clone https://github.com/veprimk/nornir_flask.git

cd nornir_flask

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

set FLASK_APP=netapp.py

set FLAS_ENV=development

flask run

