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

if __name__ == '__main__':
    app.run(debug=True)