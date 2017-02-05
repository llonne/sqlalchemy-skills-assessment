"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions

# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries

# Get the brand with the ``id`` of "ram."
q1 = "Brand.query.filter_by(brand_id='ram').one()"

# Get all models with the name "Corvette" and the brand_id "che."
q2 = "db.session.query(Model).filter_by(name='Corvette',brand_id='che').all()"

# Get all models that are older than 1960.
q3 = "db.session.query(Model).filter(Model.year > 1960).all()"

# Get all brands that were founded after 1920.
q4 = "db.session.query(Brand).filter(Brand.founded > 1920).all()"

# Get all models with names that begin with "Cor."
q5 = "db.session.query(Model).filter(Model.name.like('Cor%')).all()"

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = "db.session.query(Brand).filter(Brand.founded == 1903, Brand.discontinued == None).all()"

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = "db.session.query(Brand).filter((Brand.founded > 1950) | (Brand.discontinued != None)).all()"

# Get any model whose brand_id is not "for."
q8 = "db.session.query(Model).filter(Model.brand_id != 'for').all()"


# -------------------------------------------------------------------
# Part 4: Write Functions

def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    model_year = int(year)

    year_models = db.session.query(Model.name, Brand.name, Brand.headquarters).join(Brand).filter(Model.year == model_year).all()

    for ymodel in year_models:
        if ymodel.brand.headquarters is not None:
            print ymodel.name, ymodel.brand.name, ymodel.brand.headquarters
        else:
            print ymodel.name, ymodel.brand.name, "-"

    return year_models


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""


    all_cars = db.session.query(Brand.name, Model.name, Model.year).join(Model).all()

    for car in all_cars:
        print name, model, year
        # print car.name, car.model.name, car.model.year

    return all_cars

    # emps = db.session.query(Employee,
    #                     Department).outerjoin(Department).all()

# for emp, dept in emps:
#     if dept is not None:
#         print emp.name, dept.dept_name, dept.phone
#     else:
#         print emp.name, "-", "-"
        


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brand_name = mystr
    brand_list = db.session.query(Brand).filter(Brand.name.like('%brand_name%')).all()

    return brand_list


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    start_year = int(start_year)
    end_year = int(end_year)

    models_between = db.session.query(Model).filter((Model.year >= start_year) & (Model.year < end_year)).all()

    return models_between
