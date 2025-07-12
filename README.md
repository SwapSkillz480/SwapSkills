# Skill Swap Platform

A vibrant, student-themed Django web app for mutual skill exchange, built for Odoo Hackathon.

## Features
- User registration, login, logout
- Profile with location, photo, skills offered/wanted, and availability
- Search for public profiles by skills
- Mutual skill swap requests (choose what you want to learn and what you will teach)
- Accept/reject/delete swap requests
- Feedback system (rate/comment after swap)
- Beautiful, responsive UI with Bootstrap 5 and icons
- Colorful, student-made look

## Setup Instructions
1. Clone the repo and `cd` into the project directory.
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser (optional, for admin):
   ```bash
   python manage.py createsuperuser
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```
6. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to use the app.

## Team (Odoo Hackathon)
- **Jitesh Singhal** (Team Leader) - jiteshsinghal9050@gmail.com
- **Sridhar Manokaran** - srimanokaran2006@gmail.com
- **Shiv Thanmay** - shivthanmay06@gmail.com
- **Kumar Suryanshu** - img_2024026@iiitm.ac.in

---
Made with ❤️ by students, for students. 