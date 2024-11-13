from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # password shouldn't be unique

    @classmethod
    def is_username_unique(cls, username):
        """Check if the username is unique."""
        return cls.query.filter_by(username=username).first() is None

    @classmethod
    def save(cls, username, password, email):
        """Save a new user with the given username, encrypted password, and email."""
        try:
            new_user = cls(username=username, password=password, email=email)
            db.session.add(new_user)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error saving user: {e}")
            return False
