from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from .models.seller import Seller


from flask import Blueprint
bp = Blueprint('sellers', __name__)

@bp.route('/seller/login/<u_userkey>', methods=['GET', 'POST'])
def seller_login(u_userkey):
    # Fetch the user's name and corresponding seller key
    seller_key = Seller.get_sellerkey(u_userkey)
    return "login", 400


@bp.route('/seller/<s_sellerkey>', methods=['GET', 'POST'])
def seller_homepage(s_sellerkey):
    user_info = Seller.get_seller_information(s_sellerkey)
    # Check if user_info is not empty and contains user's name
    if user_info:
        seller_name = user_info[0]['first_name'] + user_info[0]['last_name']
    else:
        # Handle case where user_info is empty or invalid seller key
        seller_name = "User Not Found"
    # Render the HTML template with the fetched data
    return render_template('seller_homepage.html', seller_name=seller_name, seller_key=s_sellerkey)


@bp.route('/seller/<s_sellerkey>/inventory', methods=['GET', 'POST'])
def seller_inventory(s_sellerkey):
    # Get the current page from the query parameters or default to page 1
    page = int(request.args.get('page', 1))

    # Define the number of products per page
    products_per_page = 10

    # Calculate the offset for the query based on the current page
    offset = (page - 1) * products_per_page

    # Get product information for the specified sellerkey, limited by pagination
    product_info = Seller.get_product_info(s_sellerkey, limit=products_per_page, offset=offset)

    # Calculate the total number of products
    total_products = Seller.get_total_product_count(s_sellerkey)

    # Calculate the total number of pages
    total_pages = (total_products + products_per_page - 1) // products_per_page

    # Render the template with the product information and pagination details
<<<<<<< HEAD
    return render_template('seller_inventory.html', product_info=product_info, current_page=page, total_pages=total_pages)
=======
    return render_template('seller_inventory.html', seller_key=s_sellerkey, product_info=product_info, current_page=page, total_pages=total_pages)
>>>>>>> a1bf68067653a094b07c2951eb100c320146f30a


@bp.route('/seller/<s_sellerkey>/order', methods=['GET', 'POST'])
def seller_order(s_sellerkey):
    # Get order information for the specified sellerkey
    order_info = Seller.get_order_info(s_sellerkey)
    
    # Render the template with the order information
    return render_template('seller_order.html', seller_key=s_sellerkey, order_info=order_info)


@bp.route('/seller/<s_sellerkey>/review', methods=['GET', 'POST'])
def seller_review(s_sellerkey):
    seller_review = Seller.get_seller_review(s_sellerkey)
    return render_template('seller_review.html', seller_key=s_sellerkey, seller_review=seller_review)


@bp.route('/seller/<s_sellerkey>/profile', methods=['GET', 'POST'])
def seller_profile(s_sellerkey):
    seller_profile = Seller.get_seller_information(s_sellerkey)
    return render_template('seller_profile.html', seller_key=s_sellerkey, seller_profile=seller_profile)
