from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<int:post_id>')
def post(post_id):
    # Placeholder for fetching and displaying a single post
    return render_template('post.html', post_id=post_id)
