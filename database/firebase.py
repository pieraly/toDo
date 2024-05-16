import firebase_admin
from firebase_admin import credentials
import json
import pyrebase

import os

from dotenv import load_dotenv

load_dotenv()

configs= {
    "FIREBASE_SERVICE_ACCOUNT_KEY" : os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY"),
    "FIREBASE_CONFIG" : os.getenv('FIREBASE_CONFIG')
              
}

firebase_config_json  =  json.loads(configs['FIREBASE_CONFIG'])
service_account_key_json = json.loads(configs["FIREBASE_SERVICE_ACCOUNT_KEY"])


if not firebase_admin._apps: 
    cred = credentials.Certificate(service_account_key_json)
    firebase_admin.initialize_app(cred)

 
firebase = pyrebase.initialize_app(firebase_config_json)
db = firebase.database()
authTodo = firebase.auth()