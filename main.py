import os
from flask import Flask, request
import json
from google.cloud import datastore


app = Flask(__name__)

#############################################################################################
# Defining Global variables                                                                 #
#############################################################################################

DS_KIND = 'customer'
client = datastore.Client()

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello, Welcome to customers database : Enter /getCustomers to list all customers or /getCustomer?id={id} to get a single customer detail'

	
#############################################################################################################
# Get all customers from the datastore.                                                                     #
# https://test-project-130887.appspot.com/getCustomers will give a json string of all the customers from    #
# the datastore.                                                                                            #
#############################################################################################################
@app.route('/getCustomers')
def get_customers():
    try:
        query = client.query(kind=DS_KIND)
        customers = list(query.fetch())
        return json.dumps(customers)
    except Exception as e:
        return [{"Error : %s" % e}]


#############################################################################################################
# Get customer filtered by id                                                                               #
# https://test-project-130887.appspot.com/getCustomer?id={id} will show all customers by the name xyz       #
#############################################################################################################
@app.route('/getCustomer')
def get_customer_by_id():

    try:
        id = int(request.args.get('id', None))
        query = client.query(kind=DS_KIND)
        query.add_filter(property_name='id', operator='=', value=id)
        customer_filter = list(query.fetch())
        result = json.dumps(customer_filter)
        return result
    except Exception as e:
        return [{"Error : %s" % e}]


####################################################################################################
# Adding new entry in the datastore                                                                #
# https://test-project-130887.appspot.com/add?id={id}&name={name}&age={age} will add a new entry.  #
####################################################################################################
@app.route('/add')
def add_customer():

    try:
        name = request.args.get('name', None)
        age = request.args.get('age', None)
        id = int(request.args.get('id', None))
        key = client.key(DS_KIND)
        key = client.allocate_ids(key, 1)[0]
        entity = datastore.Entity(key=key)
        entity.update({
            'name': name,
            'age': age,
            'id': id
        })
        client.put(entity)
        query = client.query(kind=DS_KIND)
        query.add_filter(property_name='id', operator='=', value=id)
        customer_filter = list(query.fetch())
        result = json.dumps(customer_filter)
        return result
    except Exception as e:
        return [{"Error : %s" % e}]


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
