from flask import Flask, render_template, request
import openai

openai.api_key = "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"


app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def website():
    return render_template('index.html')

@app.route("/", methods = ["GET", "POST"])
def get_details():
    if request.method == "POST":
        poem_language = request.form.get("original-text")
        translation_language = request.form.get("translated-text")
        theme = request.form.get("theme-search")
        # type = request.form.get("")

        prompt = f"{poem_language} based on {theme} with a translation in {translation_language}"

        return prompt
    
    return render_template("form.html")

@app.route("/")
def generator(prompt):
    response = openai.Completion.create(engine="text-davinci-001",
                                        prompt=prompt,
                                        temperature=0.6,
                                        max_tokens=200)
    

if __name__ == '__main__':
    app.run(debug=True)