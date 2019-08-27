#!/usr/bin/python3
from flask import Flask, render_template, request, g
from flask import redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Categories, Base, CatalogItem, User
from flask import session as login_session
import random
import string
from functools import wraps
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog Menu Application"


# Connect to Database and create database session
engine = create_engine(
    'sqlite:///catalogwithusers.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in login_session:
            return f(*args, **kwargs)
        else:
            flash("You are not allowed to access here")
            return redirect(url_for('showLogin'))
    return wrap

# CRUD for Categories
# showcategories


@app.route('/')
@app.route('/catalog/')
def showCategories():
    categories = session.query(
                Categories).order_by(asc(Categories.name))
    if 'username' not in login_session:
        return render_template('publiccatalogs.html', categories=categories)
    else:
        return render_template('catalogs.html', categories=categories)


# Create NEW Categories
@app.route('/catalog/new/', methods=['GET', 'POST'])
@login_required
def newCategory():
    if request.method == 'POST':
        newCategory = Categories(
            name=request.form['name'], user_id=login_session['user_id'])
        session.add(newCategory)
        session.commit()
        flash('New Categories %s Successfully Created' % newCategory.name)
        return redirect(url_for('showCategories'))
    else:
        return render_template('newcatagory.html')


# EDIT a Catalog
@app.route('/catalog/<int:categories_id>/edit/', methods=['GET', 'POST'])
@login_required
def editCategory(categories_id):
    editedCatalog = session.query(
        Categories).filter_by(id=categories_id).one()
    if editedCatalog.user_id != login_session['user_id']:
        return """
        <script>
         function myFunction(){alert(
             'You are not authorized to edit this catagory.
             Please create your own restaurant in order to edit.')}
             </script> < body onload = 'myFunction()''> """
    if request.method == 'POST':
        if request.form['name']:
            editedCatalog.name = request.form['name']
            flash('Catalog Successfully Edited %s' % editedCatalog.name)
            return redirect(url_for('showCategories'))
    else:
        return render_template('editcatagory.html', catagory=editedCatalog)


# Delete catalog
@app.route('/catalog/<int:categories_id>/delete/', methods=['GET', 'POST'])
@login_required
def deleteCategroy(categories_id):
    categoryToDelete = session.query(
        Categories).filter_by(id=categories_id).one()
    if categoryToDelete.user_id != login_session['user_id']:
        return """<script>
        function myFunction(){alert(
            'You are not authorized to delete this restaurant.Please create
            your own restaurant in order to delete.')}
            </script> <body onload = 'myFunction()' >"""
    if request.method == 'POST':
        session.delete(categoryToDelete)
        flash('%s Successfully Deleted' % categoryToDelete.name)
        session.commit()
        return redirect(url_for('showCategories', categories_id=categories_id))
    else:
        return render_template(
            'deletecatagory.html', categories=categoryToDelete)


# CRUD for ITEM
# SHOW a catalog item

@app.route('/catalog/<int:categories_id>/')
@app.route('/catalog/<int:categories_id>/catalog_items/')
def showMenu(categories_id):
    categories = session.query(Categories).filter_by(id=categories_id).one()
    creator = getUserInfo(categories.user_id)
    item = session.query(CatalogItem).filter_by(
        categories_id=categories_id).all()
    if 'username' not in login_session or creator.id != login_session[
            'user_id']:
        return render_template(
            'publicmenu.html', item=item, categories=categories,
            creator=creator)
    else:
        return render_template(
            'menu.html', categories=categories, item=item, creator=creator)


# Create a NEW catalog item
@app.route('/catalog/<int:categories_id>/catalog_item/new/', methods=[
    'GET', 'POST'])
@login_required
def newMenuItem(categories_id):
    categories = session.query(Categories).filter_by(id=categories_id).one()
    if login_session['user_id'] != categories.user_id:
        return"""
        <script>
        function myFunction() {alert(
            'You are not authorized to add menu items to this restaurant.
            Please create your own restaurant in order to add items.')}
            </script> < body onload = 'myFunction()''>"""
    if request.method == 'POST':
        newItem = CatalogItem(categories_id=categories_id,
                              user_id=categories.user_id)
        if request.form['name'] == "" or request.form[
                         'description'] == "" or request.form['price'] == "":
            flash('All input fields required')
        else:
            newItem.name = request.form['name']
            newItem.description = request.form['description']
            newItem.price = request.form['price']
            session.add(newItem)
            session.commit()
            flash('New Catalog %s Item Successfully Created' % (newItem.name))
        return redirect(url_for('showMenu', categories_id=categories_id))
    else:
        return render_template('newmenuitem.html', categories_id=categories_id)


# EDIT a catalog item
@app.route(
    '/catalog/<int:categories_id>/catalog_item/<int:catalog_item>/edit',
    methods=['GET', 'POST'])
@login_required
def editMenuItem(categories_id, catalog_item):
    editedItem = session.query(CatalogItem).filter_by(id=catalog_item).one()
    categories = session.query(Categories).filter_by(id=categories_id).one()
    if login_session['user_id'] != categories.user_id:
        return"""
        <script>function myFunction() {alert(
            'You are not authorized to edit menu items to this restaurant.
            Please create your own restaurant in order to edit items.')}
            </script> <body onload = 'myFunction()'' >"""
    if request.method == 'POST':
        if request.form['name'] == "" or request.form[
                         'description'] == "" or request.form['price'] == "":
            flash('All input fields required')
        else:
            editedItem.name = request.form['name']
            editedItem.description = request.form['description']
            editedItem.price = request.form['price']
            session.add(editedItem)
            session.commit()
            flash('Menu Item Successfully Edited')
        return redirect(url_for('showMenu', categories_id=categories_id))
    else:
        return render_template(
            'editmenuitem.html', categories_id=categories_id,
            catalog_item=catalog_item, item=editedItem)


# Delete a menu item
@app.route(
    '/catalog/<int:categories_id>/catalog_item/<int:catalog_item>/delete',
    methods=['GET', 'POST'])
@login_required
def deleteMenuItem(categories_id, catalog_item):
    categories = session.query(Categories).filter_by(id=categories_id).one()
    itemToDelete = session.query(CatalogItem).filter_by(id=catalog_item).one()
    if login_session['user_id'] != categories.user_id:
        return"""
        <script>function myFunction() {alert(
            'You are not authorized to delete menu items to this restaurant.
            Please create your own restaurant in order to delete items.')}
            </script> <body onload = 'myFunction()'' >"""
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('showMenu', categories_id=categories_id))
    else:
        return render_template(
            'deletemenuitem.html',
            item=itemToDelete,
            categories_id=categories_id)

# Login Handling
# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception:
        return None


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


# CONNECT - Google login get token
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    # ADD PROVIDER TO LOGIN SESSION
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ''' "style = "width: 300px;
                            height: 300px;
                            border-radius: 150px;
                            - webkit-border-radius: 150px;
                            - moz - border-radius: 150px; ">'''
    flash("you are now logged in as %s" % login_session['username'])
    print("done!")
    return output


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        print('Access Token is None')
        response = make_response(json.dumps(
            'Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    url = '''https://accounts.google.com/o/
                oauth2/revoke?token=%s''' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            del login_session['gplus_id']
            del login_session['access_token']

        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showCategories'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showCategories'))


# JSON APIs to view Categorie Catalogitems Information
@app.route('/catalog/<int:categories_id>/catalog_item/JSON')
def categoryCatalogItemsJSON(categories_id):
    items = session.query(CatalogItem).filter_by(
        categories_id=categories_id).all()
    return jsonify(CatalogItems=[i.serialize for i in items])


@app.route('/catalog/catalog_item/<int:id>/JSON')
def catalogItemJSON(id):
    catalogItem = session.query(CatalogItem).filter_by(id=id).one()
    return jsonify(CatalogItem=catalogItem.serialize)


@app.route('/catalog/JSON')
def catalogJSON():
    categories = session.query(Categories).all()
    return jsonify(Categories=[r.serialize for r in categories])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
app.debug = True
app.run(host='0.0.0.0', port=8000)
