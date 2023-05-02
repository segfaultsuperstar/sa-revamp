from flask import Flask
from my_reviews.review_bp import review_bp
from api.api_bp import api_bp

app = Flask(__name__)
app.register_blueprint(review_bp)
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run()

