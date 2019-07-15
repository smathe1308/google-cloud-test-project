# google-cloud-test-project
Problem Statement : 
 Create api in Python program to get customers information from google cloud datastore.

Solution : 
  Created a python code to fetch data from GCP datastore for below functionalities.
  
1. Get data for all customers : 
   Function : get_customers()
   Result : Will return all the customers in the Json format
   Example : 
          /getCustomers will fetch all the customers
          
          [{"id": 105, "age": "33", "name": "customer5"}, {"id": 102, "age": "25", "name": "customer2"}, {"id": 104, "age": "22", "name": "customer4"}, {"id": 101, "age": 30, "name": "customer1"}, {"id": 103, "age": "34", "name": "customer3"}]
          
2. Get customer by Id : 
   Function : get_customer_by_id()
   Result : Will fetch a result for a particular given id in Json format.
   Example : 
          /getCustomer?id=101
          
          [{"id": 101, "age": 30, "name": "customer1"}]
          
3. add a new customer into the datastore.
   Function : add_customer()
   Result : This will add a customer given id,name,age into the datastore.
   Example : 
          /add?id=107&name=customer7&age=57
          
          A message will be shown on the webpage as "New Entity Created for Name : customer7" 
