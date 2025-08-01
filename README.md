# 🌐 FastAPI Contact Website
Live Preview : https://gymshala-static-website.onrender.com/

This is a responsive contact website built using **FastAPI**, **HTML**, **CSS**, and **Jinja2 templates**. It features a contact form that sends the user’s message via email and shows a success message on the home page after submission.

---

## 🚀 Features

- 🧠 Fast, asynchronous backend using FastAPI  
- 🎨 Responsive frontend using custom CSS and media queries  
- 📩 Contact form that sends emails  
- 🔔 Confirmation message after form submission  
- 🖥️ Mobile and desktop friendly  
- 📂 Easily deployable to Render  

---

## 📁 Project Structure
.
├── main.py # FastAPI app entry point
├── requirements.txt # Dependencies
├── static/
│ └── style.css # Custom styles
├── templates/
│ ├── index.html # Home page
│ └── thanks.html # Thank you page after form submission


---

## 🧰 Requirements

Install dependencies:

pip install -r requirements.txt

## ▶️ Running the App Locally
uvicorn main:app --reload

## 📬 Contact Email Setup
The contact form uses an email-sending feature via SMTP. Make sure to configure your credentials securely inside the app (use environment variables or .env in production).

## 🙏 Acknowledgements
FastAPI Docs

Render

Jinja2 Templates

## 📜 License
This project is licensed under the MIT License.

---

Let me know if you want to include:
- A live deployment link  
- Your name and GitHub profile  
- Badges (like deploy on render, python version, etc.)





