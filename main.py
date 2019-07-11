import os
from flask import Flask, request
import json
from google.cloud import datastore

###############################################################################################
# Setting up environ variables for connecting datastore on GCP                                #
###############################################################################################
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'E:\myWork\GCP\\test-project-130887-9cb782281074.json'
#os.environ['FLASK_ENV'] = 'development'

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello, Welcome to customers database : Enter /customers to list all customers or /customer?name=cust_name to get a single customer detail'

	
###############################################################################################
# Get all customers from the datastore.                                                       #
# http://127.0.0.1:5000/customers will give a json string of all the customers from           #
# the datastore.                                                                              #
###############################################################################################
@app.route('/customers')
def get_customers():
    client = datastore.Client()
    query = client.query(kind='Customer')
    customers = list(query.fetch())
    return json.dumps(customers)


###############################################################################################
# Get customer filtered by name                                                               #
# http://127.0.0.1:5000/customer?name=xyz will show all customers by the name xyz             #
###############################################################################################
@app.route('/customer')
def get_customer_by_name():
    name = request.args.get('name', None)
    client = datastore.Client()
    query = client.query(kind='Customer')
    query.add_filter(property_name='name', operator='=',value=name)
    customer_filter = list(query.fetch())
    result = json.dumps(customer_filter)
    return result


###############################################################################################
# Adding new entry in the datastore                                                           #
# http://127.0.0.1:5000/add?name=xyz&age=20 will add a new entry with name = xyz and age = 20 #
###############################################################################################
@app.route('/add')
def add_customer():
    name = request.args.get('name', None)
    age = request.args.get('age', None)
    client = datastore.Client()
    entity_kind = 'Customer'
    key = client.key(entity_kind)
    key = client.allocate_ids(key, 1)[0]
    entity = datastore.Entity(key=key)
    entity.update({
        'name': name,
        'age': age
    })
    client.put(entity)
    return "New Entity Created for Name : %s" %name


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)