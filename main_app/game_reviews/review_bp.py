from flask import Blueprint, render_template
from config import utils


review_bp = Blueprint('review_bp', __name__)
utils.CORS(review_bp)

db = utils.get_db('raw_review')
collection_list = db.list_collection_names()


@review_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html', collection_list=collection_list)

@review_bp.route('/<collection_name>/review_info/', methods=['GET'])
def read_info(collection_name):
    collection_info = utils.get_collection(db, collection_name).find({},{'_id': False})
    doc_count = utils.get_collection(db, collection_name).count_documents({})
    return render_template('game_reviews/reviews.html', collection_info=collection_info, collection_name=collection_name,collection_list=collection_list, doc_count=doc_count)
   