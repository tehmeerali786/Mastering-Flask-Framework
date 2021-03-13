from main import app, db, User1, Post, Tag, migrate

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User1=User1, Post=Post, Tag=Tag, migrate=migrate)
