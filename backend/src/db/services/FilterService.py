import os
from ..swen610_db_utils import *

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

    query = "SELECT title,content,price FROM services WHERE 1=1 "
    values = []
    if 'service' in params and params['service']:
        query += "AND title LIKE %s"
        values.append(f"%%{params['service']}%%")

    if 'price' in params and params['price'] is not None:
        if (params['service']):
            query += " OR price = %s"
        else:
            query += " AND price = %s"
        values.append(params['price'])

    if  params.get('priceMin') is not None and params.get('priceMax') is not None:
        query += "AND price BETWEEN %s AND %s"
        values.extend([params['priceMin'], params['priceMax']])
    elif 'priceMin' in params and params['priceMin'] is not None:
        query += " AND price >= %s"
        values.append(params['priceMin'])
    elif 'priceMax' in params and params['priceMax'] is not None:
        query += " AND price <= %s"
        values.append(params['priceMax'])
    
    return exec_get_all(query, values), 200

def get_services(params):
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
