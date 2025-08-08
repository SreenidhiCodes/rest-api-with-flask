# Task 4: REST API with Flask

# Objective
Build a RESTful API using Flask that performs basic CRUD operations on user data.


# Tools & Technologies
- Python 3.x
- Flask
- Postman or Curl (for API testing)


# Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/flask-user-api.git
   cd flask-user-api
2.Install required packages:
pip install Flask
3.Run the Flask application:
python app.py
4.The server will start at:
http://127.0.0.1:5000/

#  API Endpoints

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| GET    | /users             | Get all users     |
| GET    | /users/\<user\_id> | Get user by ID    |
| POST   | /users             | Create a new user |
| PUT    | /users/\<user\_id> | Update user by ID |
| DELETE | /users/\<user\_id> | Delete user by ID |



# Response Samples
📥 GET /users

json
Copy
Edit
{
  "101": "Alice"
}
# GET /users/999


{
  "error": "User not found"
}
# POST /users

{
  "message": "User added successfully"
}
# Testing with Postman
Open Postman

Create a new Collection (e.g., Flask User API)

Add each request:

Use the correct method (GET, POST, PUT, DELETE)

Set the request URL (e.g., http://127.0.0.1:5000/users)

For POST and PUT, go to Body → raw → JSON and paste the sample payload

Click "Send" to test each endpoint

# Outcome
Developed a working REST API using Flask

Practiced CRUD operations with in-memory data

Learned API structure and HTTP method handling

vbnet
Copy
Edit
