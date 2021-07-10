from flask import Blueprint
from controllers.userController import UserController

user = Blueprint('userRoutes', __name__)

@user.route('/')
def index():
    return UserController.default()

@user.route('/getdata')
def getdata():
    return UserController.getdata()