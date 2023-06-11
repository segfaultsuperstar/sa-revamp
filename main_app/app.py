from flask import Flask
from .game_reviews.review_bp import review_bp
from .game.game_bp import game_bp


app = Flask(__name__)
app.register_blueprint(review_bp)
app.register_blueprint(game_bp)

app.static_folder = '../static'
app.template_folder = 'templates'


