import flask
import requests
import json

app = flask.Flask('__main__')

def site_name():
    return 'https://denaro-node.gaetano.eu.org/'

db = []

@app.route('/', defaults={'path': ''},methods=['GET', 'POST'])
@app.route('/<path:path>',methods=['GET', 'POST'])
def proxy(path):
    if flask.request.method == 'POST':
        
        response = requests.post(site_name()+path,data=flask.request.data,headers={'Content-Type': 'application/json'},timeout=300).content
        print(response,len(db))
        jres = json.loads(response)
        if not jres in db:
            print(flask.request.data)
            db.append(jres)
            print(jres)
        return jres
    else:
        print(site_name()+path,len(db))
        res = requests.get(site_name()+path,headers={'Content-Type': 'application/json'},timeout=300).content
        jres = json.loads(res)
        return jres

app.run(host='0.0.0.0', port=3006,debug=True)