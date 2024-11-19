import os
from ..swen610_db_utils import *


#INSERT INTO services (title, content, price, user_id) VALUES
#('Web Development', 'Custom web development service', 500.00, 1),
#('Graphic Design', 'Logo and branding services', 300.00, 2),
#('SEO Optimization', 'Search engine optimization service', 200.00, 3);
# likes title
# likes price <
def list_of_services():
    SQL = '''
        SELECT * 
        FROM Services;
    '''
    return exec_get_all(SQL, ), 200

# Handles Multiple conditions: 
# BETWEEN PRICE RANGE AND SERVICE NAME 
# SERVICE NAME, PRICE RANGE, AND/OR
def all_services(params):
    query = "SELECT * FROM services WHERE 1=1"
    values = []

    if 'service' in params and params['service']:
        query += " AND title LIKE %s"
        values.append(f"%%{params['service']}%%")

    if  params['priceMin'] is not None and params['priceMax'] is not None:
        query += " AND price BETWEEN %s AND %s"
        values.extend([params['priceMin'], params['priceMax']])
    elif 'priceMin' in params and params['priceMin'] is not None:
        query += " AND price >= %s"
        values.append(params['priceMin'])
    elif 'priceMax' in params and params['priceMax'] is not None:
        query += " AND price <= %s"
        values.append(params['priceMax'])
    elif 'price' in params and params['price'] is not None:
        query += " AND price = %s"
        values.append(params['price'])
    return exec_get_all(query, values), 200


def get_all_function(params):
    if 'service' in params and params['service'] == "":
        return list_of_services()
    elif 'service' in params and params['service']:
        return get_services(params), 200
    elif 'service' in params and 'price' in params and params['service'] and params['price']:
        return get_services_prices(params), 200
    if ('price' in params and params['price'] != ""):
        return get_prices(), 200
    elif 'priceMin' in params and 'priceMax' in params:
        return get_services_by_range(params), 200
    elif 'priceMin' in params:
        return get_services_under(params), 200
    

def get_services(params):  # if price = '' error ... fix this
    SQL = ''' 
        SELECT * 
        From services
        WHERE title LIKE '%%{title}%%';
    '''.format(title=params['service'])
    return exec_get_all(SQL)

def get_prices(params):
    SQL = ''' 
        SELECT * 
        From services
        WHERE price = %s;
    '''
    return exec_get_all(SQL, (params['price'],))

def get_services_prices(params):
    SQL = ''' 
        SELECT * 
        From services
        WHERE price = %s
        OR title LIKE %s;
    '''
    args = (params['price'], params['service'])
    return exec_get_all(SQL, args)

def get_services_by_range(params):
    SQL = '''
        SELECT * 
        FROM services
        WHERE price BETWEEN {priceMin} AND {priceMax};
    '''.format(priceMin=params['priceMin'], priceMax=params['priceMax'])
    return exec_get_all(SQL)

def get_services_under(params):
    SQL = '''
        SELECT *
        FROM services
        WHERE price BETWEEN 0 AND {priceMin};
    '''.format(priceMin=params['priceMin'])
    return exec_get_all(SQL)
