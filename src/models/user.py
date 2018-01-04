import uuid
import datetime

from flask import session

from src.common.database import Database
from src.models.blog import Blog


class User(object):

    def __init__(self, author, email, password, _id=None):
        self.author = author
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    @staticmethod
    def get_by_name(email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return data['author']

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})

        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email=email)
        if user is not None:
            return user.password == password
        return None

    @classmethod
    def register(cls, author, email, password):
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(author, email, password)
            new_user.save_to_mongo()
            session['email'] = email
            return True
        else:
            return False


    @classmethod
    def update_name(cls, author):
        user = cls.get_by_email(session['email'])

        Database.update(collection="users", query={'author': user.author}, updated={'$set': {'author': author}})

    @classmethod
    def update_email(cls, email):
        user = cls.get_by_email(session['email'])

        Database.update(collection="users", query={'email': user.email}, updated={'$set': {'email': email}})

    @classmethod
    def update_password(cls, password):
        user = cls.get_by_email(session['email'])

        Database.update(collection="users", query={'password': user.password}, updated={'$set': {'password': password}})

    @staticmethod
    def login(user_email):
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def new_blog(self, title, description):
        blog = Blog(author=self.author, title=title, description=description, author_id=self._id)

        blog.save_to_mongo()

    @staticmethod
    def new_post(blog_id, title, content, date=datetime.datetime.utcnow()):
        blog = Blog.from_mongo(blog_id)
        blog.new_post(title, content, date )

    def json(self):
        return {
            "author":self.author,
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }

    def save_to_mongo(self):
        Database.insert("users", self.json())



