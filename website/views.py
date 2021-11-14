from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from . import db



views = Blueprint("views", __name__)

@views.route('/')
@views.route("/home")
@login_required
def home():

    posts= Post.query.all()
    return render_template("home.html", user=current_user, posts= posts)





@views.route("/create-post", methods=['GET', 'POST'])
@login_required
#creating posts
def create_post():
    if request.method =='POST':
        text = request.form.get('text')

        if not text:  #Posting empty text
            flash('Post cannot be empty.',category = "error")
        else:
            post = Post(text=text, author=current_user.id)
            flash('Post created.', category='success')
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('views.home'))

    return render_template("create_post.html",user=current_user)


#delete post method
@views.route("delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash('Post does not exist.', category='error')
    elif current_user.id != post.id:
        flash('You do not have permission to delete the post.', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', category='success')
    return redirect(url_for('views.home'))


