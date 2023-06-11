from flask import Blueprint, render_template, jsonify, request
from config import utils


game_bp = Blueprint('game_selection', __name__,)
utils.CORS(game_bp)

db = utils.get_db('raw_review')

@game_bp.route("/select/game", methods=["GET"])
def get_game():
        queried_collection= request.args.get('cname')
        game = request.args.get('game')
        print(queried_collection, game)
        game_info = utils.get_collection(db, queried_collection).find({'game': game},{'_id': False})
        doc_count = utils.get_collection(db, queried_collection).count_documents({'game': game})
        return jsonify({ "new_data" : render_template("game/game_filter.html",
           game_info=game_info, doc_count=doc_count) })