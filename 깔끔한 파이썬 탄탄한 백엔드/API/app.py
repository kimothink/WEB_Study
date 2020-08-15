from flask import Flask

app= Flask(__name__)

@app.route("/ping",methods=['GET'])
def ping():
    return "pong"

#Linux = FLASK_APP=app.py FLASK_DEBUG=1 flask run
#http://127.0.0.1:5000/ping
if __name__ == '__main__':
	app.run()



