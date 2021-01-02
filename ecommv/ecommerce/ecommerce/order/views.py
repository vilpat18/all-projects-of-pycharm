from flask import Blueprint,jsonify,request
from ecommerce.order.model import Cart,Wishlist,Myorders
from ecommerce import db
from ecommerce.product.model import Product
from ecommerce.admin.model import PaymentType
from datetime import datetime
from reportlab.pdfgen import canvas
mod = Blueprint('order',__name__,url_prefix='/order')

@mod.route('/add_cart',methods=['POST'])
def add_cart():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')
    cust_id = request.form.get('cust_id')
    product = Product.query.get(product_id)
    if int(quantity) > product.product_avail_stock:
        return "available stock is less than the quantity available stock is "+str(product.product_avail_stock)
    else:
        total_price = product.product_cost * int(quantity)
        c = Cart.query.filter(Cart.cart_customer_id == cust_id,Cart.cart_product_id == product_id).first()
        if c is None:
            cart = Cart(
            cart_product_id = product_id,
            cart_quantity_to_buy = quantity,
            cart_customer_id = cust_id,
            cart_total_price =int(total_price)
            )
            db.session.add(cart)
            db.session.commit()
            return "cart details added"
        else :
            return "already in cart"

@mod.route('/add_wishlist',methods=['POST'])
def add_wishlist():
    product_id = request.form.get('product_id')
    quantity = request.form.get('quantity')
    cust_id = request.form.get('cust_id')
    product = Product.query.get(product_id)
    if int(quantity) > product.product_avail_stock:
        return "available stock is less than the quantity available stock is " + str(product.product_avail_stock)
    else:
        total_price = product.product_cost * int(quantity)
        w = Wishlist.query.filter(Wishlist.wishlist_customer_id == cust_id,
                                  Wishlist.wishlist_product_id == product_id).first()
        if w is None:
            wishlist = Wishlist(
                wishlist_product_id=product_id,
                wishlist_quantity_to_buy=quantity,
                wishlist_customer_id=cust_id,
                wishlist_total_price=int(total_price)
            )
            db.session.add(wishlist)
            db.session.commit()
            return "wishlist details added"
        else:
            return "already in wishlist"

@mod.route('/add_cart_to_wishlist',methods=['POST'])
def add_cart_to_wishlist():
    cart_id = request.form.get('cart_id')
    cart = Cart.query.get(cart_id)
    if cart:
        w = Wishlist.query.filter(Wishlist.wishlist_customer_id == cart.cart_customer_id,
                                  Wishlist.wishlist_product_id == cart.cart_product_id).first()
        if w is None:
            wishlist = Wishlist(
                wishlist_product_id=cart.cart_product_id,
                wishlist_quantity_to_buy=cart.cart_quantity_to_buy,
                wishlist_customer_id=cart.cart_customer_id,
                wishlist_total_price=cart.cart_total_price
                )
            db.session.add(wishlist)
            db.session.delete(cart)
            db.session.commit()
            return "data added"
        else:
            return "already in wishlist"
    else:
        return "cart not exist"

@mod.route('/add_wishlist_to_cart',methods=['POST'])
def add_wishlist_to_cart():
    wishlist_id = request.form.get('wishlist_id')
    wishlist = Wishlist.query.get(wishlist_id)
    if wishlist:
        c = Cart.query.filter(Cart.cart_customer_id == wishlist.wishlist_customer_id,Cart.cart_product_id==wishlist.wishlist_product_id).first()
        if c is None:
            cart = Cart(
                cart_product_id=wishlist.wishlist_product_id,
                cart_quantity_to_buy=wishlist.wishlist_quantity_to_buy,
                cart_customer_id=wishlist.wishlist_customer_id,
                cart_total_price=wishlist.wishlist_total_price
                )
            db.session.add(cart)
            db.session.delete(wishlist)
            db.session.commit()
            return "data added"
        else:
            return "already in cart"
    else:
        return "wishlist not exist"

@mod.route('/confirm_order_from_cart',methods=['POST'])
def confirm_order_from_cart():
    confirm_order = request.form.get('confirm_order[y/n]')
    payment_id = request.form.get('payment_id')
    cart_id = request.form.get('cart_id')
    cart = Cart.query.get(cart_id)
    product = Product.query.get(cart.cart_product_id)
    if confirm_order == "y":
        product.product_avail_stock = product.product_avail_stock-cart.cart_quantity_to_buy
        myorder = Myorders(
            myorders_quantity = cart.cart_quantity_to_buy,
            myorders_product_id = cart.cart_product_id,
            myorders_customer_id = cart.cart_customer_id,
            myorders_payment_type_id = payment_id,
            myorders_total_price = cart.cart_total_price,
            order_date = datetime.now().strftime("%m/%d/%Y")
        )
        db.session.add(myorder)
        db.session.delete(cart)
        db.session.commit()
        pdf = canvas.Canvas('bill.pdf')
        pdf.setTitle('Your Invoice')
        pdf.setFont('Courier', 36)
        pdf.drawCentredString(300, 750, 'Your Invoice')
        pdf.setFont('Courier', 20)
        pdf.drawCentredString(200, 650, 'Product Name : ')
        pdf.drawString(300, 650, product.product_name)
        pdf.drawCentredString(223, 600, 'Product Quantity : ')
        pdf.drawString(340, 600, str(cart.cart_quantity_to_buy))
        pdf.drawCentredString(200, 550, 'Product Cost : ')
        pdf.drawString(300, 550, str(product.product_cost))
        pdf.line(30, 710, 550, 710)
        pdf.line(30, 510, 550, 510)
        pdf.drawCentredString(200, 450, 'Total Price : ')
        pdf.drawString(300, 450, str(cart.cart_total_price))
        pdf.setFont('Courier', 10)
        pdf.drawString(490, 800, 'Date :')
        pdf.drawString(530, 800, datetime.now().strftime("%m/%d/%Y"))
        pdf.save()
        return "confirmed"
    else:
        w = Wishlist.query.filter(Wishlist.wishlist_customer_id == cart.cart_customer_id,
                                  Wishlist.wishlist_product_id == cart.cart_product_id).first()
        if w is None:
            wishlist = Wishlist(
                wishlist_product_id=cart.cart_product_id,
                wishlist_quantity_to_buy=cart.cart_quantity_to_buy,
                wishlist_customer_id=cart.cart_customer_id,
                wishlist_total_price=cart.cart_total_price
            )
            db.session.add(wishlist)
            db.session.delete(cart)
            db.session.commit()
            return "wishlist added"
        else:
            return "already in wishlist"

@mod.route('/confirm_order_from_wishlist',methods=['POST'])
def confirm_order_from_wishlist():
    confirm_order = request.form.get('confirm_order[y/n]')
    payment_id = request.form.get('payment_id')
    wishlist_id = request.form.get('wishlist_id')
    wishlist = Wishlist.query.get(wishlist_id)
    product = Product.query.get(wishlist.wishlist_product_id)
    if confirm_order == "y":
        product.product_avail_stock = product.product_avail_stock - wishlist.wishlist_quantity_to_buy
        myorder = Myorders(
            myorders_quantity = wishlist.wishlist_quantity_to_buy,
            myorders_product_id = wishlist.wishlist_product_id,
            myorders_customer_id = wishlist.wishlist_customer_id,
            myorders_payment_type_id = payment_id,
            myorders_total_price = wishlist.wishlist_total_price,
            order_date = datetime.now().strftime("%m/%d/%Y")
        )
        pdf = canvas.Canvas('bill.pdf')
        pdf.setTitle('Your Invoice')
        pdf.setFont('Courier', 36)
        pdf.drawCentredString(300, 750, 'Your Invoice')
        pdf.setFont('Courier', 20)
        pdf.drawCentredString(200, 650, 'Product Name : ')
        pdf.drawString(300, 650, product.product_name)
        pdf.drawCentredString(223, 600, 'Product Quantity : ')
        pdf.drawString(340, 600, wishlist.wishlist_quantity_to_buy)
        pdf.drawCentredString(200, 550, 'Product Cost : ')
        pdf.drawString(300, 550, str(product.product_cost))
        pdf.line(30, 710, 550, 710)
        pdf.line(30, 510, 550, 510)
        pdf.drawCentredString(200, 450, 'Total Price : ')
        pdf.drawString(300, 450, str(wishlist.wishlist_total_price))
        pdf.setFont('Courier', 10)
        pdf.drawString(490, 800, 'Date :')
        pdf.drawString(530, 800, datetime.now().strftime("%m/%d/%Y"))
        pdf.save()
        db.session.add(myorder)
        db.session.delete(wishlist)
        db.session.commit()
        return "confirmed"
    else:
        return "can't buy"
@mod.route('/confirm_order_from_product',methods=['POST'])
def confirm_order_from_product():
    confirm_order = request.form.get('confirm_order[y/n]')
    payment_id = request.form.get('payment_id')
    product_id = request.form.get('product_id')
    cust_id = request.form.get('cust_id')
    product = Product.query.get(product_id)
    quantity = request.form.get('quantity')
    total_price = product.product_cost * int(quantity)
    if confirm_order == "y":
        if int(quantity) > product.product_avail_stock:
            return "available stock is less than the quantity available stock is " + str(product.product_avail_stock)
        else:
            product.product_avail_stock = product.product_avail_stock - int(quantity)
            myorder = Myorders(
                myorders_quantity=quantity,
                myorders_product_id=product_id,
                myorders_customer_id=cust_id,
                myorders_payment_type_id=payment_id,
                myorders_total_price=total_price,
                order_date = datetime.now().strftime("%m/%d/%Y")
            )
            db.session.add(myorder)
            db.session.commit()
            pdf = canvas.Canvas('bill.pdf')
            pdf.setTitle('Your Invoice')
            pdf.setFont('Courier',36)
            pdf.drawCentredString(300,750,'Your Invoice')
            pdf.setFont('Courier', 20)
            pdf.drawCentredString(200, 650, 'Product Name : ')
            pdf.drawString(300, 650, product.product_name)
            pdf.drawCentredString(223, 600, 'Product Quantity : ')
            pdf.drawString(340, 600, quantity)
            pdf.drawCentredString(200, 550, 'Product Cost : ')
            pdf.drawString(300, 550, str(product.product_cost))
            pdf.line(30,710,550,710)
            pdf.line(30, 510, 550, 510)
            pdf.drawCentredString(200, 450, 'Total Price : ')
            pdf.drawString(300, 450, str(total_price))
            pdf.setFont('Courier',10)
            pdf.drawString(490,800,'Date :')
            pdf.drawString(530, 800, datetime.now().strftime("%m/%d/%Y"))
            pdf.save()
            return "confirmed"
    else:
        if int(quantity) > product.product_avail_stock:
            return "available stock is less than the quantity available stock is " + str(product.product_avail_stock)
        else:
            w = Wishlist.query.filter(Wishlist.wishlist_customer_id == cust_id,
                                      Wishlist.wishlist_product_id == product_id).first()
            if w is None:
                wishlist = Wishlist(
                    wishlist_product_id=product_id,
                    wishlist_quantity_to_buy=quantity,
                    wishlist_customer_id=cust_id,
                    wishlist_total_price=total_price
                )
                db.session.add(wishlist)
                db.session.commit()
                return "product added in wishlist"
            else:
                return "product is in wishlist for future reference"