from flask import Flask

app = Flask(__name__)

# Setting route
@app.route("/")
@app.route("/home")
def hello():
    return "Hello Welcome to home"

#taking input from URL
@app.route("/input/<string:name>")
def takeInput(name):
    return "Hello "+name 

#taking multiple input from URL
@app.route("/input/<string:name>/id/<int:id>")
def takeMultipleInput(name,id):
    return "Hello your name is "+name +" and Id is "+str(id)

#Allow specific Method 
@app.route("/onlyget/", methods=['GET'])
def onlyGet():
    return "Only get method"

 
@app.route("/onlypost/", methods=['POST'])
def onlyPost():
    return "Only post method"

if __name__ == "__main__":
    app.run(debug=True)