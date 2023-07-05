# TODO List App

This is a TODO list application built with Django. It allows users to manage their tasks by adding, deleting, marking as completed, and listing TODO items.

## Instructions for Running/Building the App

To run the app locally, follow these steps:

1. Clone the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Build the app using the following command: `docker-compose build`.
4. Run the app using the following command: `docker-compose up`.
5. Open up another terminal and load the initial data fixture file using the following command: `docker-compose run --rm app python manage.py loaddata initial-data.json` 
6. The app will be accessible at `http://127.0.0.1:4011` in your browser.

## Instructions for Testing the App

To run the test suite and perform automated tests, follow these steps:

1. Run the test command: `python manage.py test`.
2. The test suite will run and display the results in the console.

To test the app's API using the Django REST Framework interface, follow these steps:

1. Ensure that the app is running by following the instructions in the "Instructions for Running/Building the App" section.
2. Open a web browser and navigate to `http://127.0.0.1:4011/api/`.
3. The Django REST Framework interface will be displayed, showing a list of available endpoints and actions.
4. Click on an endpoint to view the available actions and parameters.
5. Use the interface to perform various actions on the API, such as creating, updating, deleting, or retrieving TODO items.
6. Fill in the required parameters and click the "POST," "PUT," "DELETE," or "GET" buttons to perform the corresponding action.
7. The interface will display the response from the server, including the HTTP status code and response data.
8. Continue testing the API by exploring different endpoints and actions in the interface.

Please note that some endpoints may require authentication. To authenticate, you need to sign up using Github at the following URL: `http://127.0.0.1:4011/`


## Interface Documentation

The app exposes the following API endpoints:

- `GET /api/todo/`: Retrieves a list of all TODO items.
- `POST /api/todo/`: Creates a new TODO item.
- `GET /api/todo/{pk}/`: Retrieves a specific TODO item.
- `PUT /api/todo/{pk}/`: Updates a specific TODO item.
- `DELETE /api/todo/{pk}/`: Deletes a specific TODO item.
- `PUT /api/todo/{pk}/complete/`: Marks a specific TODO item as completed.

The API requires authentication for most endpoints, except for the registration and login endpoints. To authenticate, you need to sign up using Github at the following URL: `http://127.0.0.1:4011/`

