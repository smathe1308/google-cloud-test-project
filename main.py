import os
from flask import Flask, request
import json
from google.cloud import datastore

###############################################################################################
# Setting up environ variables for connecting datastore on GCP                                #
###############################################################################################
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'E:\myWork\GCP\\test-project-130887-9cb782281074.json'

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
        return 'Hello, Welcome to customers database : Enter /getCustomers to list all customers or /getCustomer?id=101 to get a single customer detail'

	
###############################################################################################
# Get all customers from the datastore.                                                       #
# http://127.0.0.1:5000/getCustomers will give a json string of all the customers from        #
# the datastore.                                                                              #
###############################################################################################
@app.route('/getCustomers')
def get_customers():
    client = datastore.Client()
    query = client.query(kind='customer')
    customers = list(query.fetch())
    return json.dumps(customers)


###############################################################################################
# Get customer filtered by name                                                               #
# http://127.0.0.1:5000/getCustomer?id={id} will show fetch customer by a particular id.      #
###############################################################################################
@app.route('/getCustomer')
def get_customer_by_id():
    id = int(request.args.get('id', None))
    client = datastore.Client()
    query = client.query(kind='customer')
    query.add_filter(property_name='id', operator='=', value=id)
    customer_filter = list(query.fetch())
    result = json.dumps(customer_filter)
    return result


##############################################################################################################
# Adding new entry in the datastore                                                           		     #
# http://127.0.0.1:5000/add?id={id}&name={name}&age={age} will add a new entry.				     #
##############################################################################################################
@app.route('/add')
def add_customer():
    name = request.args.get('name', None)
    age = request.args.get('age', None)
    id = int(request.args.get('id', None))
    client = datastore.Client()
    entity_kind = 'customer'
    key = client.key(entity_kind)
    key = client.allocate_ids(key, 1)[0]
    entity = datastore.Entity(key=key)
    entity.update({
        'name': name,
        'age': age,
        'id': id
    })
    client.put(entity)
    return "New Entity Created for Name : %s" % name


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
