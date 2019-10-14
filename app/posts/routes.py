from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app import db
from app.models import Post
from app.posts.forms import PostForm
from app.users.utils import save_video
posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    return render_template('blob.html', title='Blob')


@posts.route('/post/new/vlog',methods=['GET','POST'])
def new_vlog():
    if current_user.is_authenticated:
        return render_template('vlog.html',title='New Vlog')
        video=recordedBlob()
        post=Vlog(video.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.home'))
    else:
            return redirect(url_for('users.login'))


@posts.route('/post/new/blog',methods=['GET','POST'])
def new_blog():
    if current_user.is_authenticated:
        return render_template('blog.html',title='New Blog')
        form = PostForm()
        if form.validate_on_submit():
           post = Post(title=form.title.data, content=form.content.data, author=current_user, post=post)
           db.session.add(post)
           db.session.commit()
           flash('Your post has been created!', 'success')
           return redirect(url_for('main.home'))
    return render_template('layout.html', title='New Post',
                           form=form,legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))




@posts.route("/vlog/",methods=['GET','POST'])
def vlog():
    return redirect(url_for('posts.new_post'))

@posts.route("/blog/",methods=['GET','POST'])
def blog():
        return redirect(url_for('posts.new_post'))
    

@posts.route("/blob/",methods=['GET','POST'])
def blob():
        return render_template('blob.html', title='Blob')
        