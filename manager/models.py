from manager import db
import os

cwd = os.getcwd()

class User(db.Model):
    '''
    name, userName, password, character
    '''
    userID = db.Column(db.Integer(), nullable=False, unique=True, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    userName = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    character = db.Column(db.String(60), nullable=False)
    settings = db.relationship('Setting', backref='owned_settings', lazy=True
    )
    def __repr__(self):
        return f'{self.name}@{self.userName}'

class Setting(db.Model):
    '''
    showHiddenFile, rootFolder
    '''
    id = db.Column(db.Integer(), nullable=False, unique=True, primary_key=True)
    showHiddenFile = db.Column(db.Boolean(), nullable=False, default=False)
    rootFolder = db.Column(db.String(10000), nullable=False, default=cwd)
    userID = db.Column(db.Integer(), db.ForeignKey('user.userID'))

    def __repr__(self):
        return f'{self.userID}'

def addUser(name, userName, password_hash, character, rootFolder=cwd):
    user1 = User(name=name,
    userName=userName,
    password_hash=password_hash,
    character=character)
    db.session.add(user1)
    db.session.commit()

    setting1 = Setting(rootFolder=rootFolder)
    db.session.add(setting1)
    db.session.commit()
    setting1.userID = User.query.filter_by(userName=userName).first().userID
    db.session.commit()

def func():
    name = input('name:\t')
    userName = input('userName:\t')
    password_hash = input('userName:\t')
    character = input('character:\t')
    addUser(name, userName, password_hash, character)