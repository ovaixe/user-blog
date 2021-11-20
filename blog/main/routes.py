from flask import Blueprint, render_template, request
from blog.models import Post   


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home', methods=['GET'])
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('home.html', posts=posts, title='Home')


@main.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About')
