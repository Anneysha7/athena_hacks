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

        prompt1 = f"{poem_language} based on {theme} with a translation in {translation_language}"
        prompt2 = f""

        return prompt1
    
    return render_template('index.html', **locals())

@app.route("/generator", methods= ["POST", "GET"])
def generator(prompt):
    response = openai.Completion.create(engine="text-davinci-001",
                                        prompt=prompt,
                                        temperature=0.6,
                                        max_tokens=200)
    
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Wow, you beat the AI this time.'
    else:
        answer = 'Wow, you beat the AI this time.'

    return render_template('index.html', answer)

if __name__ == '__main__':
    app.run(debug=True)