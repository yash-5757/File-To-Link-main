from flask import Flask
app = Flask( __ name __ )
@app.route('/')
def hello_world():
return 'GreyMatters'
if __name__ == " __ main_":
app.run( )
