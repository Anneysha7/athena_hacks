from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def website():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)