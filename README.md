# google-cloud-test-project
Problem Statement : 
 Create api in Python program to get customers information from google cloud datastore.

Solution : 
  Created a python code to fetch data from GCP datastore for below functionalities.
  
1. Get data for all customers : 
   Function : get_customers()
   Result : Will return all the customers in the Json format
   Example : 
          https://test-project-130887.appspot.com/getCustomers
          
          Response:
          [{"name": "customer5", "id": 105, "age": "33"}, {"name": "customer2", "id": 102, "age": "25"}, {"name": "customer4", "id": 104, "age": "22"}, {"name": "customer1", "id": 101, "age": 30}, {"id": 103, "age": "34", "name": "customer3"}, {"name": "customer7", "id": 107, "age": "57"}, {"id": 106, "age": "52", "name": "customer6"}, {"name": "customer8", "id": 108, "age": "34"}]
          
2. Get data for a single customer filtered by id : 
   Function : get_customer_by_id()
   Result : Will fetch a result for a particular given id in Json format.
   Example : 
          https://test-project-130887.appspot.com/getCustomer?id=102
          
          Response:
          [{"id": 102, "age": "25", "name": "customer2"}]
          
3. Add a new customer.
   Function : add_customer()
   Result : This will add a customer given id,name,age into the datastore.
   Example : 
          https://test-project-130887.appspot.com/add?id=109&name=customer9&age=32
          
          Response:
          [{"id": 109, "age": "32", "name": "customer9"}] 
