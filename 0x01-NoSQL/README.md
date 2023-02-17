# 0. List all databases
A script that lists all databases in MongoDB

# 1. Create a database
A script that creates or uses the database my_db

# 2. Insert document
A script that inserts a document in the collection school:

* The document must have one attribute name with value “Holberton school”
* The database name will be passed as option of mongo command

# 3. All documents
A script that lists all documents in the collection school:

* The database name will be passed as option of mongo command

# 4. All matches
A script that lists all documents with name="Holberton school" in the collection school:

* The database name will be passed as option of mongo command

# 5. Count
A script that displays the number of documents in the collection school:

* The database name will be passed as option of mongo command

# 6. Update
A script that adds a new attribute to a document in the collection school:

* The script updates only document with name="Holberton school" (all of them)
* The update adds the attribute address with the value “972 Mission street”
* The database name will be passed as option of mongo command

# 7. Delete by match
A script that deletes all documents with name="Holberton school" in the collection school:

* The database name will be passed as option of mongo command

# 8. List all documents in python
A Python function that lists all documents in a collection:

* Prototype: def list_all(mongo_collection):
* The function returns an empty list if there's no document in the collection
* mongo_collection will be the pymongo collection object

# 9. Insert a document in Python
A Python function that inserts a new document in a collection based on kwargs:

* Prototype: def insert_school(mongo_collection, **kwargs):
* mongo_collection is a pymongo collection object
* Returns the new _id
