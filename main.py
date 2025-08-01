from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import smtplib
from email.mime.text import MIMEText

app = FastAPI()

# Serve static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "vn.nawal02@gmail.com"
SENDER_PASSWORD = "ezxgtndjewflinya"
RECEIVER_EMAIL = "vn.nawal02@gmail.com"  # Can be same or different

# Home route
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Contact form page (GET)
@app.get("/contact", response_class=HTMLResponse)
async def contact_form(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

# Contact form submission (POST)
@app.post("/contact")
async def submit_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    
    subject = f"New Contact Form Submission from {name}"
    body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        return RedirectResponse(url="/?success=1", status_code=303)
    except Exception as e:
        return templates.TemplateResponse("error.html", {"request": request, "error": str(e)})

        response = RedirectResponse(url="/?success=1", status_code=303)
        return response

    except Exception as e:
        return templates.TemplateResponse("error.html", {"request": request, "error": str(e)})


    # print("📬 Contact Form Submitted:")
    # print(f"Name: {name}")
    # print(f"Email: {email}")
    # print(f"Message: {message}")

    # # Optional: redirect to homepage
    # return RedirectResponse(url="/", status_code=303)
