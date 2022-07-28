### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  - PostgreSQL is a relational database management system.

- What is the difference between SQL and PostgreSQL?
  - SQL is the language used by PostgreSQL to organize, configure and manage databases.

- In `psql`, how do you connect to a database?
  - There are 2 ways. First and easiest way is by typing `psql DATABASE_NAME`. Or you can initialize PostgreSQL and then type
  - `\c DATABASE_NAME`

- What is the difference between `HAVING` and `WHERE`?
  - `WHERE` is used to filter the records from the table based on the specified condition.
  - `HAVING` is used to filter the record from the groups based on the specified condition.

- What is the difference between an `INNER` and `OUTER` join?
  - An `INNER` join will filter the data from two tables and returns the resulting data that overlaps between the 2 tables.
  - An `OUTER` join (depending on what type of `OUTER` join) will filter the data from two tables and returns data that DOES NOT overlap between the 2 tables (can still return data that DOES overlap)

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  - A `LEFT OUTER` and `RIGHT OUTER` join are sessentially the same thing, depending on how the SQL query is structured. A `LEFT OUTER` join will return all data from table 1 as well as the overlapping data shared in table 2. A `RIGHT OUTER` join will return all data from table 2 as well as the overlapping data shared in table 1. 

- What is an ORM? What do they do?
- An ORM is a technique that lets you query and manipulate data from a database using an object-oriented paradigm. It stands for Object Relational Mapping and it allows you to make SQL queries by interacting with the model in the same language you've already been using.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  - One of the main differences that would make someone use a server side library like `requests` is if an app is making an api call that requires a key/password. This would not be performed through axios because the key/password would be available to anyone who opens up the developer console.

- What is CSRF? What is the purpose of the CSRF token?
  - CSRF (Cross Site Request Forgery) is a secret, unique and unpredictable value a server-side application generates in order to protect CSRF vulnerable resources.

- What is the purpose of `form.hidden_tag()`?
  - The form. hidden_tag() template argument generates a hidden field that includes a token that is used to protect the form against CSRF attacks.
