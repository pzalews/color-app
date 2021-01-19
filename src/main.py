from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    color1 = os.getenv("COLOR1")
    color2 = os.getenv("COLOR2")
    
    return f"""
<html><body bgcolor="{color2}">
<h1 style="color:{color1};">Hello world!</h1>
</body></html>
    """


if __name__ == "__main__":
   app.run(host='0.0.0.0')
