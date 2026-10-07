from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/calcolo", methods=['POST'])
def miaFunzione():
    a = 10
    b = 30
    return str(a + b)

@app.route("/calcolo", methods=['GET'])
def miaFunzione2():
    a = 40
    b = 30
    return str(a + b)

@app.route("/calcolo", methods=['PATCH'])
def miaFunzione3():
    a = 0
    b = 30
    return str(a + b)

@app.route("/calcolo", methods=['DELETE'])
def miaFunzione4():
    a = 40
    b = 90
    return str(a + b)

@app.route("/calcolo", methods=['PUT'])
def miaFunzione5():
    a = 100
    b = 90
    return str(a + b)