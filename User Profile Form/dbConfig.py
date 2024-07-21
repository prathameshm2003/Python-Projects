from google.cloud import firestore
import json
#firestore database configuration
credentials_path ='./setup/tkinter-e1092-firebase-adminsdk-ug9gp-15d8f8579b.json'
with open(credentials_path) as json_file:
 credentials_info = json.load(json_file)
db = firestore.Client.from_service_account_info(credentials_info)