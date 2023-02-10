This directory contains a project on advanced mySQL concepts
# 0. We are all unique!
This task creates a table users with attributes:
* id, integer, never null, auto increment and primary key
* email, string (255 characters), never null and unique
* name, string (255 characters)


# 1. In and not out
This task creates a SQL script that creates a table users following the requirements:

With these attributes:
* id, integer, never null, auto increment and primary key
* email, string (255 characters), never null and unique
* name, string (255 characters)
* country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)

# 2. Best band ever!
a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

### Requirements:

* Import this table dump: metal_bands.sql.zip
* Column names are: origin and nb_fans
* This script can be executed on any database

# 3. Old school band
A SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

### Requirements:
* Column names are: band_name and lifespan (in years)
* This script uses attributes formed and split for computing the lifespan
* This script can be executed on any database

# 4. Buy buy buy
a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
Quantity in the table items can be negative.

# 5. Email validation to sent
a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
# 6. Add bonus
a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

### Requirements:

* Procedure AddBonus is taking 3 inputs (in this order):
* user_id, a users.id value (you can assume user_id is linked to an existing users)
* project_name, a new or already exists projects - if no projects.name found in the table, you should create it
* score, the score value for the correction

# 7. Calculating the Average Score using a stored procedure
a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. 
*** Note: An average score can be a decimal ***
# 8. Optimize simple searchOptimize simple search
a SQL script that creates an index idx_name_first on the table names and the first letter of name
# 9. Optimize search and score
a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.
# 10. Safe divide
a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
# 11. No table for a meeting
a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.
