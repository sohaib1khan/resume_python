# 💼 Dynamic Portfolio Engine

<div align="center">

[![Portfolio Engine Interactive Documentation](https://img.shields.io/badge/💼_INTERACTIVE-DOCUMENTATION-667eea?style=for-the-badge&labelColor=0f0f0f&color=764ba2&logoColor=white)](https://sohaib1khan.github.io/resume_python/)

**🌐 Live Production Website | ⚡ Full-Stack Platform | 🚀 Enterprise Ready | 📊 Real Analytics**

*💼 Professional Portfolio • 🔒 Production Security • 📱 Responsive Design*

---

</div>

🌐 **Live Resume & Portfolio** - A professional portfolio website built with Flask, Python, Tailwind CSS, and Markdown, featuring dynamic content, visitor tracking, and automated deployment.

## 📌 Features

- **📜 Dynamic Content** – Uses Markdown files for easy content updates.
- **📊 Visitor Counter** – Tracks the number of site visits and logs data for analysis.
- **📑 Resume Download** – Generates a downloadable resume on demand in PDF format.
- **🔗 Cloudflare Tunnel** – Enables public access without complex networking setups.
- **📦 Docker & Kubernetes Support** – Easily deployable as a containerized app with full scalability.
- **🖼️ Custom Styling** – Implemented with Tailwind CSS for an optimized and responsive UI.
- **🔧 CI/CD Ready** – Supports integration with automated deployment pipelines.

## 📂 Project Structure

```
.
├── app.py                 # Main Flask application
├── content                # Markdown files for site content
│   ├── contact.md
│   ├── experience.md
│   ├── home.md
│   ├── projects.md
│   └── techstack.md
├── Dockerfile             # Docker configuration
├── k8s                    # Kubernetes deployment files
│   ├── deployment.yaml
│   ├── hpa.yaml
│   └── service.yaml
├── requirements.txt       # Python dependencies
├── restart_app.sh         # Script to restart the app with proper environment setup
├── skaffold.yaml          # Skaffold config for Kubernetes deployment
├── static                 # Static assets (CSS, images, resume)
│   ├── images
│   │   └── profile.jpg
│   ├── resume
│   │   └── Sohaib_Resume.pdf
│   └── style.css
└── templates              # Jinja2 HTML templates
    ├── base.html
    ├── contact.html
    ├── experience.html
    ├── home.html
    ├── projects.html
    ├── resume_template.html
    └── techstack.html
```

## 🛠️ Installation & Setup

### 🔹 Running the App with Python (Manual Setup)

1. Clone the repository:
   ```bash
   git clone https://github.com/sohaib1khan/resume_python.git
   cd resume_python
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. The app will be available at `http://127.0.0.1:8888`
6. Optional: Enable **Cloudflare Tunnel** for external access by running:
   ```bash
   cloudflared tunnel run flask-tunnel
   ```

---

### 🐳 Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t resume_python .
   ```
2. Run the container:
   ```bash
   docker run -d -p 8888:8888 resume_python
   ```
3. Access the application at `http://localhost:8888`



---

### ☸️ Deploying on Kubernetes

1. Ensure your **Kubernetes cluster** is running and `kubectl` is configured.
2. Apply the deployment and service:
   ```bash
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```
3. Verify the deployment:
   ```bash
   kubectl get pods
   kubectl get svc
   ```
4. If using **MetalLB**, access the app via the assigned **external IP**.
5. If using **port-forwarding**, run:
   ```bash
   kubectl port-forward svc/resume-service 8888:8888
   ```
   Then, visit `http://localhost:8888`
6. Optional: Use **Skaffold** for continuous development and deployment:
   ```bash
   skaffold dev
   ```

---

## 🔗 Additional Notes

- **Cloudflare Tunnel** can be used for secure, external access with minimal setup.
- The app supports **Markdown-based content updates**, making it easy to manage and scale.
- Supports **containerization and orchestration**, enabling seamless deployment across different environments.
- Can be extended to integrate with **CI/CD pipelines** for automated deployments.
- Future enhancements may include **database integration** and **enhanced analytics**.

### 📌 Repository: [GitHub - resume\_python](https://github.com/sohaib1khan/resume_python)

