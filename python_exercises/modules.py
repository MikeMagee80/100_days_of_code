# Module: file that contains some python code.
# Should contain highly-related objects (like aisles in a supermarket)

# app.py and sales.py


# # Move the calc functions from app.py to sales.py
# def calc_tax():
#     pass


# def calc_shipping():
#     pass

# # in app.py
# from sales import calc_shipping, calc_tax

# calc_shipping()
# calc_tax()

# # or
# import sales

# sales.calc_shipping()

# Package: a container for one or more modules (plus __init__.py)
# import ecommerce.sales (where ecommerce is the folder/package holding the sales module)
# ecommerce.sales.calc_tx()

# # or
# from ecommerce.sales import calc_tax


# from ..customer import contact