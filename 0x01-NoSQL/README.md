# alx-backend-storage - NoSQL

This repository contains scripts and Python functions for working with a MongoDB NoSQL database. The scripts perform various operations such as creating a database, inserting documents, querying data, and more.

## Table of Contents

- [Scripts](#scripts)
  - [Create Database](#create-database)
  - [Use or Create Database](#use-or-create-database)
  - [Insert Document](#insert-document)
  - [List All Documents](#list-all-documents)
  - [List Matching Documents](#list-matching-documents)
  - [Count Documents](#count-documents)
  - [Update Documents](#update-documents)
  - [Delete by Match](#delete-by-match)
  - [List All Documents in Python](#list-all-documents-in-python)
  - [Insert Document in Python](#insert-document-in-python)
  - [Update Topics in Python](#update-topics-in-python)
  - [Schools by Topic](#schools-by-topic)
  - [Log Stats](#log-stats)
  - [Regex Filter](#regex-filter)
  - [Top Students](#top-students)
  - [Log Stats - New Version](#log-stats-new-version)

## Scripts

### Create Database

- **File:** [0-list_databases](./0-list_databases)
- **Description:** Creates a MongoDB database.

```bash
cat 0-list_databases | mongo
```

### Use or Create Database

- **File:** [1-use_or_create_database](./1-use_or_create_database)
- **Description:** Switches to or creates a MongoDB database named `my_db`.

```bash
cat 1-use_or_create_database | mongo
```

### Insert Document

- **File:** [2-insert](./2-insert)
- **Description:** Inserts a document with the attribute `name` set to "Holberton school."

```bash
cat 2-insert | mongo my_db
```

### List All Documents

- **File:** [3-all](./3-all)
- **Description:** Lists all documents in the collection "school."

```bash
cat 3-all | mongo my_db
```

### List Matching Documents

- **File:** [4-match](./4-match)
- **Description:** Lists documents with `name` equal to "Holberton school" in the collection "school."

```bash
cat 4-match | mongo my_db
```

### Count Documents

- **File:** [5-count](./5-count)
- **Description:** Displays the number of documents in the collection "school."

```bash
cat 5-count | mongo my_db
```

### Update Documents

- **File:** [6-update](./6-update)
- **Description:** Adds a new attribute `address` with the value "972 Mission street" to documents with `name` equal to "Holberton school."

```bash
cat 6-update | mongo my_db
```

### Delete by Match

- **File:** [7-delete](./7-delete)
- **Description:** Deletes all documents with `name` equal to "Holberton school" in the collection "school."

```bash
cat 7-delete | mongo my_db
```

### List All Documents in Python

- **File:** [8-all.py](./8-all.py)
- **Description:** Python function that lists all documents in a collection.

```python
# Example usage in 8-main.py
```

### Insert Document in Python

- **File:** [9-insert_school.py](./9-insert_school.py)
- **Description:** Python function that inserts a new document in a collection based on kwargs.

```python
# Example usage in 9-main.py
```

### Update Topics in Python

- **File:** [10-update_topics.py](./10-update_topics.py)
- **Description:** Python function that changes all topics of a school document based on the name.

```python
# Example usage in 10-main.py
```

### Schools by Topic

- **File:** [11-schools_by_topic.py](./11-schools_by_topic.py)
- **Description:** Python function that returns the list of schools having a specific topic.

```python
# Example usage in 11-main.py
```

### Log Stats

- **File:** [12-log_stats.py](./12-log_stats.py)
- **Description:** Python script that provides stats about Nginx logs stored in MongoDB.

```bash
./12-log_stats.py
```

### Regex Filter

- **File:** [100-find](./100-find)
- **Description:** Lists all documents with names starting by "Holberton" in the collection school.

```bash
cat 100-find | mongo my_db
```

### Top Students

- **File:** [101-students.py](./101-students.py)
- **Description:** Python function that returns all students sorted by average score.

```python
# Example usage in 101-main.py
```

### Log Stats - New Version

- **File:** [102-log_stats.py](./102-log_stats.py)
- **Description:** Enhanced version of log_stats.py with the top 10 most present IPs.

```bash
./102-log_stats.py
```
