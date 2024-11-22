from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>SKAI Solutions</h1><div><p>Multi-Cloud Architecture | AI & Machine Learning | DevOps Consulting</p><ul><li><a href='#'>Home</a></li><li><a href='#'>About</a></li><li><a href='#'>Services</a></li><li><a href='#'>Products</a></li><li><a href='#'>Contact</a></li></ul></div><div><p>&copy; 2024 CloudTech Solutions</p></div></body></html>\n"

