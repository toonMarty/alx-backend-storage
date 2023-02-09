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
