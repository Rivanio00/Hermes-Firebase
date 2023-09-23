#API
from flask import Flask
import requests
import json

app = Flask(__name__)

address = "https://hermes-bank-default-rtdb.firebaseio.com"

requisition_get = requests.get(f'{address}/Clients/.json')
data = requisition_get.json() #Recebe os dados do firebase

@app.route('/Clients',methods=['GET'])
def get_clients():
    return json.dumps(data)

@app.route('/Clients/<int:CPF>',methods=['GET'])
def search_client(CPF,data):

@app.route('/Clients/Creat',methods=['POST'])
def post_client(address, data, comment):
    
    requisition_client = requests.post(f'{address}/Clients/.json', data=json.dumps(data))   # Novo cliente

    print(requisition_client)
    print(requisition_client.text)

 

@app.route('/Comment',methods=['POST'])
def post_comment(data, addres, comment):
    
    requisition_msg = requests.post(f'{address}/Comments/.json', data=json.dumps(comment))  # Nova msg

    print(requisition_msg)
    print(requisition_msg.text)

app.run(port=5001, host='localhost', debug=True)
