# Anna University Facility Booking System



A full-stack web application designed to streamline the booking and management of university facilities such as classrooms, labs, projectors, seminar halls, and auditoriums.



---



## Features



### Facility Management



* Classroom Booking

* Laboratory Booking

* Projector Booking

* Seminar Hall Booking

* Auditorium Booking



### Academic Management



* Faculty Timetable Management

* Course Enrollment Management

* Automatic Weekly Timetable Generation



### User Management



* JWT-based Authentication

* Role-Based Access Control

* Bulk User Registration

* User Account Management



### Approval Workflow



* Hall Request Approval

* Auditorium Request Approval

* Booking History Tracking



---



## Technology Stack



### Frontend



* React 19

* Vite

* Tailwind CSS



### Backend



* Node.js

* Express.js

* MongoDB

* Mongoose



### Authentication



* JSON Web Tokens (JWT)



### Deployment



* Frontend: Vercel

* Backend: Render

* Database: MongoDB Atlas



---



## Prerequisites



Before running the project, ensure the following are installed:



* Node.js (v18 or later recommended)

* npm

* Git

* MongoDB Atlas Account (or local MongoDB instance)



---



# Environment Configuration



## Frontend Environment Variables



Create a `.env` file inside the `frontend` folder:



```env

VITE_BACKEND_URL=http://localhost:5000

```



---



## Backend Environment Variables



Create a `.env` file inside the `backend` folder:



```env

MONGODB_PROD_URI=*********

JWT_SECRET=*********

MAIL_USER=*********

MAIL_PASS=*********

ADMIN_USERID=*********

ADMIN_PASSWORD=*********

ADMIN_EMAIL=*********

```



### Important



Do not commit `.env` files to GitHub.



---



# Installation



Clone the repository:



```bash

git clone https://github.com/Durai-Bharath/Facility_Booking.git

cd Facility_Booking

```



---



## Backend Setup



```bash

cd backend

npm install

```



---



## Frontend Setup



```bash

cd frontend

npm install

```



---



# Running the Application



Open two terminals.



## Terminal 1 – Backend



```bash

cd backend

npm run dev

```



Expected output:



```text

MongoDB connected

Server running on port 5000

```



---



## Terminal 2 – Frontend



```bash

cd frontend

npm run dev

```



Expected output:



```text

Local: http://localhost:5173

```



Open:



```text

http://localhost:5173

```



---

# User Roles

| Role                   | Description                                 |
|------------------------|---------------------------------------------|
| Admin                  | Full system access and management           |
| Secretary              | Approve hall and auditorium requests        |
| Faculty                | Facility booking and timetable management   |
| Student Representative | Facility booking and request management     |
| Student                | View booking information                    |

---



# Troubleshooting



### Backend not starting



Verify:



* MongoDB Atlas connection string is valid.

* Environment variables are configured correctly.

* Port 5000 is available.



### Frontend API errors



Verify:

- `VITE_BACKEND_URL` is correctly configured.  
  - If running locally, set it to: `http://localhost:8080/api`

- Backend service is running.

- CORS configuration allows frontend access.



### Authentication issues



Verify:



* `JWT_SECRET` is configured.

* Browser localStorage contains a valid token.



---



# Contributing

1. Create a feature branch (if needed).

2. Commit changes with meaningful commit messages.

3. Push the developed code to the `dev` branch. If a suitable branch does not exist, create a new branch first and push your changes there.

4. Create a Pull Request.



---



# License



This project is developed for academic and learning purposes.







