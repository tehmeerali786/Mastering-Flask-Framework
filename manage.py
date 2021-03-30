import os
from webapp import db, migrate, create_app
from webapp.blog.models import User1, Post, Tag

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User1=User1, Post=Post, Tag=Tag, migrate=migrate)
