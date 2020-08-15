from flask import Flask,jsonify,request

app= Flask(__name__)
app.users = {}
app.id_count =1

@app.route("/sign-up",methods=['POST'])
def sign_up():
    new_user = request.json
    new_user["id"]=app.id_count
    app.users[app.id_count]=new_user
    app.id_count=app.id_count+1
    return jsonify(new_user)


@app.route("/ping",methods=['GET'])
def ping():
    return "pong"

#Linux = FLASK_APP=app.py FLASK_DEBUG=1 flask run
#http://127.0.0.1:5000/ping
if __name__ == '__main__':
	app.run()



