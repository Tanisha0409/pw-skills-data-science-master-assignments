#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython import display
display.Image("1.png")


# Ans. A database is a collection of organized data that is stored and managed on a computer system. It allows for efficient storage, retrieval, and manipulation of large amounts of data. A database system typically consists of software that manages the data, a database server that stores the data, and one or more applications that access the data.
# 
# SQL (Structured Query Language) and NoSQL (Not only SQL) are two different types of database management systems that use different methods for storing and retrieving data. Here are some key differences between the two:
# 
# Feature :
# 
# SQL databases
# 
# 1. Data model- Relational data model
# 2. Query language-	SQL
# 3. Scalability-	Vertically scalable
# 4. Consistency-	Strong consistency
# 5. Usage-	Complex queries and transactions
# 
# 
# NoSQL databases
# 1. Data model- Flexible data model
# 2. Query language- Database-specific query language
# 3. Scalability- Horizontally scalable
# 4. Consistency- May offer weaker consistency models
# 5. Usage- Fast and flexible data processing
# 
# 
# Here are some examples of each databases:
# 
# SQL Databases:
# mySQL
# Oracle
# PostgreSQL
# Microsoft SQL Server
# SQLite
# NoSQL Databases:
# MongoDB (document-oriented)
# Cassandra (column-family)
# Redis (key-value)
# Neo4j (graph)
# Amazon DynamoDB (document-oriented)
# It's worth noting that there are many different types of NoSQL databases, each with their own strengths and weaknesses. For example, document-oriented databases like MongoDB are great for storing unstructured data such as JSON documents, while graph databases like Neo4j are ideal for modeling complex relationships between data points.
# 
# Similarly, there are many different types of SQL databases, each with their own features and benefits. For example, MySQL is a popular choice for web applications due to its fast performance and scalability, while PostgreSQL is often used for data warehousing and business intelligence applications due to its advanced query optimization capabilities.
# 
# Ultimately, the choice between SQL and NoSQL databases will depend on the specific requirements of your application and the type of data you need to store and process.

# In[2]:


from IPython import display
display.Image("2.png")


# Ans. DDL stands for Data Definition Language, which is a subset of SQL used to create, modify, and delete database objects such as tables, indexes, and views.
# 
# Establishing Connection with SQLite3
# 
# Dependencies required : ipython-sql
# 
# Using !pip install to install above package through this jupyter notebook

# In[3]:


get_ipython().system('pip install  ipython-sql')


# In[4]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[5]:


import csv, sqlite3
con = sqlite3.connect("test.db")
cur = con.cursor()


# In[6]:


get_ipython().run_line_magic('sql', 'sqlite:///test.db')


# With above a connection is now established to test.db and we can directly write a query with %%sql magic command using above
# 
# Note: The %%sql command is a Jupyter Notebook magic command that allows you to execute SQL queries directly in a notebook cell. Provided that database connection is established
# 
# Below are DDL Commands executed with %%sql magic command
# 
# 1. CREATE: The CREATE command is used to create a new database object, such as a table, index, or view. For example, to create a new table called "employee" with columns for a employee_code, name, salary, phone_number, and sex, you would use the following SQL statement:

# In[7]:


get_ipython().run_cell_magic('sql', '', 'CREATE TABLE if not exists employee\n(employee_code INT PRIMARY KEY, \nname VARCHAR(20) NOT NULL,\nsalary FLOAT NOT NULL,\nphone_number char(10));')


# In[8]:


# Viewing Above table
get_ipython().run_line_magic('sql', 'SELECT * FROM employee;')


# 2.DROP: The DROP command is used to delete an existing database object. For example, to delete the "employee" table created in the previous example, you would use the following SQL statement:

# In[9]:


get_ipython().run_line_magic('sql', 'DROP TABLE employee;')


# In[10]:


#this code shows that the table employee has been deleted i.e table does not exist
get_ipython().run_line_magic('sql', 'SELECT * FROM employee;')


# 3. ALTER: The ALTER command is used to modify an existing database object, such as a table, index, or view. For example, to add a new column to the "employee" table to track a availability_status.

# In[11]:


get_ipython().run_cell_magic('sql', '', 'CREATE TABLE if not exists employee\n(employee_code INT PRIMARY KEY, \nname VARCHAR(20) NOT NULL,\nsalary FLOAT NOT NULL,\nphone_number char(10));')


# In[12]:


get_ipython().run_line_magic('sql', 'SELECT * FROM employee;')


# In[13]:


#this code will show that one column availability staus has been added
get_ipython().run_line_magic('sql', 'ALTER TABLE employee ADD COLUMN availability_status BOOLEAN;')


# In[14]:


get_ipython().run_line_magic('sql', 'SELECT * FROM employee;')


# 4. TRUNCATE: The TRUNCATE command is used to delete all the rows in a table, while keeping the table structure intact. For example, to delete all the data in the "employee" table but keep the table structure, you would use the following SQL statement:
# Please note that SQLite has command : DELETE FROM table_name instead of TRUNCATE from mySQL

# In[15]:


get_ipython().run_line_magic('sql', 'SELECT * FROM employee;')


# In[16]:


get_ipython().run_cell_magic('sql', '', "\nINSERT INTO employee VALUES (101, 'RAM', 70000.00 , '7525459675', True);\nINSERT INTO employee VALUES (102, 'RAVI', 60000.00 , '7554247675', True);\nINSERT INTO employee VALUES (103, 'RAKESH', 80000.00 , '7536578675', False);")


# In[17]:


get_ipython().run_line_magic('sql', 'SELECT * FROM employee;')


# In[18]:


#this code will show that all the values has been deleted but the format of the table is there
get_ipython().run_line_magic('sql', 'DELETE FROM employee;')


# In[19]:


get_ipython().run_line_magic('sql', 'SELECT * FROM employee;')


# In[20]:


from IPython import display
display.Image("3.png")


# Ans. Answer : DML stands for "Data Manipulation Language," and it is a subset of SQL (Structured Query Language) that is used to manipulate data within a database. The three main commands in DML are INSERT, UPDATE, and DELETE.

# In[21]:


get_ipython().run_cell_magic('sql', '', 'CREATE Table if not exists student_details\n(name VARCHAR(50) ,\n emil_id VARCHAR(50),\nage INT ,\ncourse VARCHAR(20));')


# In[22]:


get_ipython().run_line_magic('sql', 'SELECT * FROM student_details')


# 1.INSERT - The INSERT command is used to add new data to a database table.

# In[23]:


get_ipython().run_line_magic('sql', "INSERT INTO student_details VALUES('Tanisha', 'tanisha@gmail.com', 22, 'data_science')")
get_ipython().run_line_magic('sql', "INSERT INTO student_details VALUES('Akash', 'akash@gmail.com', 24, 'web_development')")
get_ipython().run_line_magic('sql', "INSERT INTO student_details VALUES('Shipra', 'shipra@gmail.com', 22, 'upsc/bpsc')")


# In[24]:


get_ipython().run_line_magic('sql', 'SELECT * FROM student_details')


# 2. UPDATE: The UPDATE command is used to modify existing data in a database table

# In[25]:


get_ipython().run_line_magic('sql', "UPDATE student_details SET age = 23 WHERE name = 'Shipra';")


# In[26]:


get_ipython().run_line_magic('sql', 'SELECT * FROM student_details')


# 3. DELETE: The DELETE command is used to remove data from a database table.

# In[27]:


get_ipython().run_line_magic('sql', "DELETE FROM student_details WHERE name = 'Shipra';")


# In[28]:


get_ipython().run_line_magic('sql', 'SELECT * FROM student_details')


# In[29]:


from IPython import display
display.Image("4.png")


# Ans. DQL stands for "Data Query Language," and it is a subset of SQL (Structured Query Language) that is used to retrieve data from a database. The main command in DQL is SELECT.

# In[70]:


get_ipython().run_cell_magic('sql', '', 'CREATE TABLE if not exists child\n(name VARCHAR(50),  \nage INT, \ngrade VARCHAR(2));')


# In[71]:


get_ipython().run_line_magic('sql', 'SELECT * FROM child')


# In[72]:


get_ipython().run_cell_magic('sql', '', "INSERT INTO child VALUES ('Tanisha', 8, 'A');\nINSERT INTO child VALUES ('Pragya', 5, 'B');\nINSERT INTO child VALUES ('Pragati', 6, 'A');\nINSERT INTO child VALUES ('Sudh', 9, 'C');")


# In[73]:


get_ipython().run_line_magic('sql', 'SELECT * FROM child')
#selecting all column


# In[74]:


get_ipython().run_line_magic('sql', 'SELECT name, age FROM child')
#selecting only name and age group


# In[78]:


get_ipython().run_line_magic('sql', "SELECT * FROM child WHERE grade = 'A';")


# In[5]:


from IPython import display
display.Image("5.png")


# Ans. Primary Key: In a database table, a primary key is a column or a set of columns that uniquely identifies each row in the table. The primary key is used to ensure that each row in the table is unique, and it is often used as a reference by other tables. The primary key is also used to enforce data integrity, which means that it ensures that there are no duplicate or null values in the key column(s).
# 
# 
# 
# 
# Foreign Key: A foreign key is a column or a set of columns in a table that refers to the primary key of another table. The foreign key is used to establish a relationship between two tables, and it ensures that the data in the foreign key column(s) of one table matches the data in the primary key column(s) of the other table.

# In[6]:


from IPython import display
display.Image("6.png")


# In[84]:


get_ipython().system('pip install mysql-connector-python')


# In[2]:


import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tanisha@123#pw"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)


# 1. In above code, we first establish a connection to a MySQL database using the mysql.connector.connect() method, which takes the host, user, password as arguments.
# 
# 2. Next, we create a cursor object using the cursor() method of the connection object. The cursor object allows us to execute queries and fetch results.
# 
# 3. We then execute a SQL query using the execute() method of the cursor object, which takes the SQL query as an argument.

# In[7]:


from IPython import display
display.Image("7.png")


# Ans. Answer: In an SQL query, the clauses are executed in the following order:
# 
# 1. FROM clause: Specifies the table or tables from which to retrieve data.
# 
# 2. JOIN clause: Specifies how to join multiple tables together, if needed.
# 
# 3. WHERE clause: Specifies which rows to retrieve based on a set of conditions.
# 
# 4. GROUP BY clause: Specifies how to group rows based on one or more columns.
# 
# 5. HAVING clause: Specifies which groups to retrieve based on a set of conditions.
# 
# 6. SELECT clause: Specifies which columns to retrieve.
# 
# 7. DISTINCT clause: Specifies to retrieve only distinct values of the specified columns.
# 
# 8. ORDER BY clause: Specifies how to sort the retrieved rows based on one or more columns.
# 
# 9. LIMIT clause: Specifies the maximum number of rows to retrieve.

# In[ ]:




