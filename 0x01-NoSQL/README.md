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

# 10. Change school topics
A Python function that changes all topics of a school document based on the name:

* Prototype: def update_topics(mongo_collection, name, topics):
* mongo_collection is the pymongo collection object
* name (string) is the school name to update
* topics (list of strings) is the list of topics approached in the school

# 11. Where can I learn Python?
A Python function that returns the list of school having a specific topic:

* Prototype: def schools_by_topic(mongo_collection, topic):
* mongo_collection will be the pymongo collection object
* topic (string) will be topic searched

# 12.  Log stats
A Python script that provides some stats about Nginx logs stored in MongoDB:

* Database: logs
* Collection: nginx

#13. Regex filter
A script that lists all documents with name starting by Holberton in the collection school:

* The database name will be passed as option of mongo command

# 14. Top students
A Python function that returns all students sorted by average score:

* Prototype: def top_students(mongo_collection):
* mongo_collection will be the pymongo collection object
* The top is ordered
* The average score is part of each item returns with key = averageScore

# 15. Log stats - new version
Improving 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs:

* The IPs top must be sorted (like the example below)
