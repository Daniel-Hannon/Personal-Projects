import sqlite3
import datetime

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('Taskmaster/taskmaster.db')
cursor = conn.cursor()

# #Drop all the tables:
# cursor.execute("DROP TABLE IF EXISTS points")
# cursor.execute("DROP TABLE IF EXISTS tasks")
# cursor.execute("DROP TABLE IF EXISTS episodes")
# cursor.execute("DROP TABLE IF EXISTS competitors")
# cursor.execute("DROP TABLE IF EXISTS series")


# Create the "series" table
cursor.execute('''
CREATE TABLE series (
    id INTEGER PRIMARY KEY,
    series TEXT,
    series_winner_id INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (series_winner_id) REFERENCES competitors(id)
)
''')

# Create the "competitors" table
cursor.execute('''
CREATE TABLE competitors (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender_identity TEXT,
    created_at TIMESTAMP
)
''')

# Create the "episodes" table
cursor.execute('''
CREATE TABLE episodes (
    id INTEGER PRIMARY KEY,
    episode_num INTEGER,
    series_id INTEGER,
    episode_winner_id INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (series_id) REFERENCES series(id)
    FOREIGN KEY (episode_winner_id) REFERENCES competitors(id)
)
''')

# Create the "tasks" table
cursor.execute('''
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    description TEXT,
    episode_id INTEGER,
    type TEXT,
    category TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (episode_id) REFERENCES episodes(id)
)
''')

# Create the "points" table
cursor.execute('''
CREATE TABLE points (
    task_id INTEGER,
    competitor_id INTEGER,
    points_awarded INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(id),
    FOREIGN KEY (competitor_id) REFERENCES competitors(id)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Tables with connections created successfully.")
