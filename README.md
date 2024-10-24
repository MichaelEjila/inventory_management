Inventory Management System API
===============================

A RESTful API for managing products, suppliers, and inventory levels. This project includes functionality for handling CSV uploads, inventory reporting, and background tasks with Celery. Dockerized for seamless deployment and development.

Features
--------

*   **Products Management**: CRUD operations for products with pagination and filtering.
    
*   **Suppliers Management**: CRUD operations for suppliers.
    
*   **Inventory Levels**: Check and update inventory for products.
    
*   **CSV File Handling**: Import products from CSV files.
    
*   **Reports Generation**: Generate inventory reports and supplier performance metrics with background tasks.
    
*   **Dockerized**: Ready to run in Docker containers for consistent environments.
    

Prerequisites
-------------

Ensure you have the following installed:

*   [Docker](https://docs.docker.com/get-docker/)
    
*   [Docker Compose](https://docs.docker.com/compose/install/)
    

Setup
-----

### 1\. Clone the repository

git clone https://github.com/your-username/inventory-management-api.git  cd inventory-management-api   `

### 2\. Docker Setup

To build and run the containers:

docker-compose up --build   `

Once the build is complete, start the services:

docker-compose up   `

### 3\. Database Setup

After the containers are running, apply migrations:

docker-compose exec web python manage.py migrate   `

### 4\. Running Tests

To run the unit tests:

docker-compose exec web python manage.py test   `

### 5\. Local Development Settings

If you are running the project locally, make sure to comment out the following line in settings.py:

SECURE_SSL_REDIRECT = True   `

This will prevent the application from redirecting HTTP to HTTPS, which is not necessary in local development environments.

CSV File Handling
-----------------

To import products from a CSV file, you can upload the file via the /products/upload endpoint. The system will validate and process the data, providing feedback on any errors or records processed.

If using Postman, send "file" as the key and the .csv file as the value.

Background Tasks
----------------

Long-running tasks, such as generating reports on inventory or supplier performance, are handled using Celery. These tasks run in the background and can be scheduled for periodic execution.

Dockerization
-------------

The application is fully Dockerized and includes the following services:

*   **Web**: The Django application.
    
*   **Database**: PostgreSQL database.
    

To spin up the environment, use:

docker-compose up --build  docker-compose up   `

To run migrations:

docker-compose exec web python manage.py migrate   `

To run tests:

docker-compose exec web python manage.py test   `

PostMan API Documentation: 
--------------------------
In order to make testing easier for you! -

https://elements.getpostman.com/redirect?entityId=18461030-35096e16-aa58-4243-9ac0-9ac49002b143&entityType=collection
