🏦 *SBI Bank – Flask + Docker Bank Application*

A simple, modern, and fully containerized SBI Bank Web Application built using Flask, Docker, HTML, CSS, and JavaScript.
This mini-banking system supports account creation, deposit, withdrawal, and balance checks — with persistent storage using Docker volumes.

⭐ Features

✔ Create new bank accounts

✔ Deposit money

✔ Withdraw money

✔ Check account balance

✔ Clean & modern UI

✔ Flask backend

✔ Persistent data using Docker Volumes

✔ Easy to deploy anywhere

📸 Home Page Screenshot
<img width="1857" height="847" alt="image" src="https://github.com/user-attachments/assets/00b4d05e-8f84-4d15-b312-383159cee0d4" />



This screenshot is from the running application’s home page.

🚀 How to Run the Project (Step-by-Step)
### 1️⃣ Clone the Repository
git clone https://github.com/Manozz-888/sbi-app.git
cd sbi-app

2️⃣ Build the Docker Image
docker build -t sbi-app .

3️⃣ Create Persistent Volume
docker volume create sbi-data

4️⃣ Run the Application
docker run -p 5001:5000 -v sbi-data:/app --name sbi-app-container sbi-app


App will run at:

👉 http://localhost:5001

5️⃣ Stop the App
docker stop sbi-app-container

6️⃣ Start Again (Data remains saved!)
docker start sbi-app-container

📂 Project Structure
sbi-app/
│── app.py
│── Dockerfile
│── requirements.txt
│── static/
│   ├── style.css
│   └── script.js
│── templates/
│   ├── home.html
│   ├── about.html
│   └── contact.html

🎯 Technologies Used

Python 3.9

Flask

HTML / CSS / JavaScript

Docker

Docker Volumes

👍 Author

Manozz
SBI Bank Mini Project (Flask + Docker)
