# FILE STRUCTURE
# REQUIREMENTS
To install the required packages, run the following command
`pip install -r requirements.txt`

# MAKING MIGRATIONS
after modifying models, new migrations must be generated:
`python manage.py makemigrations`

# APPLYING MIGRATIONS
The generated migrated files must be applied to the database:
`python manage.py migrations`

# IMPORT DEMO DATA (OPTIONAL)
`python manage.py loaddata demo`

# RUNNING THE SERVER
`python manage.py runserver`

# STOPPING THE SERVER (TERMINAL)
`ctrl+c`

# RESET COMMAND (DESTRUCTIVE)
The following command deletes the database, creates and applies any migrations, loads demo data and runs the server. It is a destructive action and all data will be deleted.
## WINDOWS (LOCAL)
`rm db.sqlite3 | python manage.py makemigrations | python manage.py migrate | python manage.py loaddata demo | python manage.py runserver`
## Linux (python-anywhere)
`python manage.py makemigrations && python manage.py migrate && python manage.py loaddata demo`
