from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
<head>
     <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
</head>
    <body>
        <form action="/" method="post">
            <label for="rotate by">Rotate by</label>
            <input type="text" name="Rot" value=0>
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit Query">

    </body>
</html>
"""
@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rotate_number = int(request.form['Rot']) 
    text_box = request.form['text']

    return form.format(rotate_string(text_box, rotate_number))

    #string_answer = "The encryption is " +  rotate_string(text_box, rotate_number)-->
    #return string_answer-->
    

app.run()