from flask import Flask, render_template, request, session, make_response

from src.common.database import Database
from src.models.blog import Blog
from src.models.posts import Post
from src.models.user import User

app = Flask(__name__)
app.secret_key = '12sasad'


@app.route('/')
def home_template():
    session['email'] = None
    return render_template('homepage.html')


@app.route('/jotter')
def user_profile():
    if session['email'] is None:
        return render_template('homepage.html')
    else:
        user = User.get_by_email(session['email'])
        return render_template('profile.html', author=user.author)


@app.route('/login')
def login_template():
    return render_template("login.html")


@app.route('/register')
def register_template():
    return render_template("register.html")


@app.before_first_request
def intialize_database():
    Database.initalisation()


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None
        return render_template('incorrect.html')

    author = User.get_by_name(email)
    # return author
    return render_template('profile.html', author=author)


@app.route('/auth/register', methods=['POST'])
def register_user():
    author = request.form['full_name']
    email = request.form['email']
    password = request.form['password']

    User.register(author, email, password)
    return render_template('profile.html', author=author)


@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def show_blogs(user_id=None):
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session['email'])
    blogs = user.get_blogs()
    return render_template('blogs.html', blogs=blogs, user=user.author)


@app.route('/posts/<string:blog_id>')
def blog_post(blog_id):
    blog = Blog.from_mongo(blog_id)
    posts = blog.get_posts()
    return render_template('posts.html', posts=posts, blog_title=blog.title, blog_id=blog_id)


@app.route('/blogs/new', methods=['POST', 'GET'])
def create_new_blog():
    if request.method == 'GET':
        return render_template('new_blog.html')
    else:
        title = request.form['title']
        description = request.form['description']
        user = User.get_by_email(session['email'])
        new_blog = Blog(author=user.author, title=title, description=description, author_id=user._id)
        new_blog.save_to_mongo()
        return make_response(show_blogs(user._id))


@app.route('/posts/new/<string:blog_id>', methods=['POST', 'GET'])
def create_new_post(blog_id):
    if request.method == 'GET':
        return render_template('new_post.html', blog_id=blog_id)
    else:
        title = request.form['title']
        content = request.form['content']
        user = User.get_by_email(session['email'])
        new_post = Post(blog_id, title, content, user.author)
        new_post.save_to_mongo()
        return make_response(blog_post(blog_id))


@app.route('/logout')
def logout():
    session['email'] = None
    return render_template("homepage.html")


@app.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'GET':
        user = User.get_by_email(session['email'])
        return render_template("edit-profile.html", old_name=user.author, old_email=user.email)
    else:
        user = User.get_by_email(session['email'])
        author = request.form['author']
        email = request.form['email']
        password = request.form['password']
        if request.form['author'] == "":
            user = User.get_by_email(session['email'])
            User.update_name(user.author)
        else:
            User.update_name(author)
        if request.form['email'] == "":
            user = User.get_by_email(session['email'])
            User.update_email(user.email)
        else:
            # user = User.get_by_email(session['email'])
            User.update_email(email)
            session['email'] = email
        if request.form['password'] == "":
            user = User.get_by_email(session['email'])
            User.update_password(user.password)
        else:
            User.update_password(password)
        return render_template('profile.html', author=user.author)


if __name__ == '__main__':
    app.run(debug=True)
