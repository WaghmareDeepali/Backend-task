# User Registration System

This project provides endpoints for user registration, retrieval of user details, and retrieval of user referrals.

## Endpoints

1. **User Registration Endpoint**
    - **Endpoint:** `http://127.0.0.1:8000/api/user/register/`
    - **Method:** `POST`
    - **Description:** Registers a new user with the system.
    - **Request Body:**
      ```json
      {
        "name": "rupali",
        "email": "rupali@example.com",
        "password": "rupali",
        "referral_code":"po"
      }
      ```
    - **Response Body:**
      ```json
      {
          "token": {
              "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMjU4ODAzMywiaWF0IjoxNzEyNTAxNjMzLCJqdGkiOiIzYjAyOTBkOWM4MzQ0NGU1ODg4ZjY4ZWIyY2FmODU5NSIsInVzZXJfaWQiOjh9.Vd784-tCtgW9pCvTT6M3dGEHppC7r2DAtWksBOqIfNQ",
              "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyNTAzNDMzLCJpYXQiOjE3MTI1MDE2MzMsImp0aSI6ImMwYTNhOTA3YmQzYjQ5ZWFiNGI3YjVjMDA4YzU1YmFmIiwidXNlcl9pZCI6OH0.RJi-JHRsazRtai5n9Np1NbVDNu_WHygtGv4sPQBxa_s"
          },
          "msg": "Registration Successful"
      }
      ```

2. **User Details Endpoint**
    - **Endpoint:** `http://127.0.0.1:8000/api/user/details/`
    - **Method:** `GET`
    - **Description:** Retrieves details of the authenticated user.
    - **Authorization:** Requires a valid token in the Authorization header.
    - **Response Body:**
      ```json
      {
          "name": "rupali",
          "email": "rupali@example.com",
          "referral_code": "po",
          "created_at": "2024-04-07T14:53:52.936173Z"
      }
      ```

3. **Referrals Endpoint**
    - **Endpoint:** `http://localhost:8000/api/user/referrals/`
    - **Method:** `GET`
    - **Description:** Retrieves a list of users who registered using the current user's referral code.
    - **Authorization:** Requires a valid token in the Authorization header.
    - **Response Body:**
      ```json
      {
          "count": 1,
          "next": null,
          "previous": null,
          "results": [
              {
                  "name": "rupali",
                  "email": "rupali@example.com",
                  "registration_timestamp": "2024-04-07T14:53:52.936173Z"
              }
          ]
      }
      ```

## Setup

***To run the project locally, follow these steps:***

1. clone the repository.
2. Go to the Backend-task folder
3. Install requirements.txt file
4. Go to the UserAuth folder
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver


🚀 Happy coding!


