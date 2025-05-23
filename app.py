from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
admin = Admin(app, name='Quản trị', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
