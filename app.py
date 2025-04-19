from flask import Flask, render_template, jsonify, request
import datetime

app = Flask(__name__)

user_data = {
    "start_time": None,
    "selections": []
}

@app.route('/')
def home():
    """Serves the Welcome Screen."""
    page_data = {
        "title": "Melody Muse",
        "welcome_text": "Welcome to Melody Muse, a fun, interactive platform for users to learn to play piano!",
        "secondary_text": "Whether you're reading your first note or just want to practice without a piano, there is something for everyone!",
        "image_url": "/static/images/keyboard_image.jpg"
    }
    return render_template('welcome.html', data=page_data)

@app.route('/learn')
def learn():
	return render_template('learn.html')

@app.route('/learn/naturals')
def learn_naturals():
	return render_template('naturals/learn_naturals.html')

@app.route('/learn/treble')
def learn_treble():
	return render_template('naturals/learn_treble.html')

@app.route('/learn/bass')
def learn_bass():
	return render_template('naturals/learn_bass.html')

@app.route('/learn/accidentals')
def learn_accidentals():
	return render_template('accidentals/learn_accidentals.html')

@app.route('/learn/challenge')
def learn_challenge():
	return render_template('challenge/learn_challenge.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)