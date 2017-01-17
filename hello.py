from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hej Lina, vad fin du ser ut."

if __name__=='__main__':
    app.run(debug=True)

