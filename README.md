# DevOpsII-Microservices
<h4> I add "id" in "item" table so it will be alot easy to distingush between PRIMARY KEY and FOREIGN KEY </h4>
<h4> "id" is PRIMARY KEY </h4>

Microservices:
1. GET
- Put http://127.0.0.1:5001/get in url box to see the list of items
- Put http://127.0.0.1:5001/get/"id" to see the specific item

2. POST
1) Put http://127.0.0.1:5002/post in url box 
2) Next click on "Body"
3) Then tick on "form-data"
4) Put the KEY words ("id", "name", "category", "price", "instock") and value in each KEY
5) Check the result by GET

3. PUT
1) Put http://127.0.0.1:5003/put/"id" in url box 
2) Next click on "Body"
3) Then tick on "form-data"
4) Put the KEY words ("name", "category", "price", "instock") and value in each KEY
5) Check the result by GET again

4. DELETE
- Put http://127.0.0.1:5004/delete/"id" to delete the specific item
- Check the result by GET again
