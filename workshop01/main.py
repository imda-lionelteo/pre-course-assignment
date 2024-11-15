import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    repo_location = "https://github.com/imda-lionelteo/pre-course-assignment"
    texts = [
        "Logic will get you from A to B. Imagination will take you everywhere.",
        "There are 10 kinds of people. Those who know binary and those who don't.",
        "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
        "It's not that I'm so smart, it's just that I stay with problems longer.",
        "It is pitch dark. You are likely to be eaten by a grue."
    ]
    selected_text = random.choice(texts)
    return render_template('index.html', dynamic_text=selected_text, repo_location=repo_location)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)