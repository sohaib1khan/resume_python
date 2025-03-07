from flask import Flask, render_template, request, send_file, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import json
import markdown
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Contact Form (kept for UI purposes, but no email functionality)
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")

@app.route("/contact")
def contact():
    content = load_markdown("contact.md")  # Load Markdown content
    return render_template("contact.html", content=content)


@app.route("/download-resume")
def download_resume():
    from weasyprint import HTML
    pdf_file = "resume.pdf"

    # Render the HTML template to a file
    html_content = render_template("resume_template.html")
    HTML(string=html_content).write_pdf(pdf_file)

    return send_file(pdf_file, as_attachment=True)

@app.route("/")
def home():
    content = load_markdown("home.md")  # Load Markdown content
    return render_template("home.html", content=content)

@app.route("/projects")
def projects():
    content = load_markdown("projects.md")  # Load Markdown content
    return render_template("projects.html", content=content)


@app.route("/techstack")
def techstack():
    content = load_markdown("techstack.md")  # Load Markdown content
    return render_template("techstack.html", content=content)

def load_markdown(filename):
    """Reads a Markdown file and converts it to HTML"""
    with open(os.path.join("content", filename), "r", encoding="utf-8") as f:
        return markdown.markdown(f.read())

@app.route("/experience")
def experience():
    content = load_markdown("experience.md")  # Load Markdown content
    return render_template("experience.html", content=content)


# Main entry point
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
