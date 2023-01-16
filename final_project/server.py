from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    etf_results = translator.english_to_french(textToTranslate)
    return etf_results

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    fte_results = translator.french_to_english(textToTranslate)
    return fte_results

@app.route("/")
def renderIndexPage():
    render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
