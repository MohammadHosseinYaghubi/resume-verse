# ResumeVerse 

 **A Django-powered platform for professionals to showcase their skills, projects, and resumes in one place.**

ResumeVerse is a production-ready, full-featured web application designed to help professionals build and manage their online presence. Register, create comprehensive profiles, showcase your skills and projects, and share your professional journey with the world.

---

## Features

### Core Functionality
- **User Authentication System** – Secure registration, login, and profile management with JWT
- **Rich User Profiles** – Complete personal information, bio, and professional details
- **Resume Management** – Upload and manage multiple resume versions (PDF/DOC formats)
- **Skills Showcase** – Display technical and soft skills with proficiency levels
- **Project Portfolio** – Add and manage projects with descriptions, links, and images
- **Social Integration** – Connect LinkedIn, GitHub, Twitter, and other social platforms
- **Public Profiles** – Shareable profile pages visible to other users
- **Owner Dashboard** – Comprehensive admin panel for managing your content
- **Responsive Design** – Mobile-friendly interface built with modern frontend frameworks

### Future Enhancements
- ✅ Resume builder with drag-and-drop templates
- ✅ Advanced search and filter for skills/profiles
- ✅ Ratings and endorsements system
- ✅ Job posting and application tracking
- ✅ API endpoints for mobile apps
- ✅ Email notifications and reminders

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| **Backend** | Python, Django, Django REST Framework |
| **Database** | PostgreSQL, Redis (Cache) |
| **Task Queue** | Celery |
| **Containerization** | Docker, Docker Compose |
| **Web Server** | Gunicorn, Nginx |
| **Authentication** | JWT |
| **Documentation** | OpenAPI (Swagger) |
| **Testing** | Pytest |
| **CI/CD** | GitHub Actions |

---

## Table of Contents

- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Environment Variables](#-environment-variables)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/resume-verse.git
cd resume-verse

# Build and run with Docker
docker compose up -d

# Access the application
# Web: http://localhost:8000
# API: http://localhost:8000/api/v1/
# Docs: http://localhost:8000/api/docs/
```

---

## Installation

### Prerequisites
- Python 3.10+
- PostgreSQL 14+
- Redis 7+
- Docker & Docker Compose (optional)

### Local Development Setup

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment variables (see .env.example)
cp .env.example .env

# 4. Run migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Run development server
python manage.py runserver
```

### Docker Setup

```bash
# Build and start all services
docker compose up -d --build

# Run migrations inside container
docker compose exec web python manage.py migrate

# Create superuser
docker compose exec web python manage.py createsuperuser

# Stop services
docker compose down
```

---

## API Documentation

The API is fully documented using OpenAPI (Swagger).

| Endpoint | Description |
|----------|-------------|
| `/api/v1/` | API Root |
| `/api/schema/` | OpenAPI Schema |
| `/api/docs/` | Swagger UI Documentation |

### Main API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register/` | User registration |
| POST | `/api/v1/auth/login/` | JWT login |
| GET | `/api/v1/profiles/` | List user profiles |
| GET | `/api/v1/profiles/{id}/` | Get profile details |
| POST | `/api/v1/resumes/` | Upload resume |
| GET | `/api/v1/skills/` | List skills |
| POST | `/api/v1/projects/` | Create project |

---

## Project Structure

```
resume-verse/
├── src/
│   ├── apps/
│   │   ├── accounts/      # Authentication & user management
│   │   ├── profiles/      # User profiles management
│   │   ├── resumes/       # Resume upload & management
│   │   ├── skills/        # Skills & proficiency levels
│   │   └── projects/      # Project portfolio management
│   ├── core/              # Core settings & utilities
│   ├── api/               # API views & serializers
│   └── manage.py
├── docker/
│   ├── web/               # Django & Gunicorn config
│   └── nginx/             # Nginx configuration
├── tests/                 # Pytest test suite
├── docs/                  # Additional documentation
├── .env.example           # Environment variables template
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── LICENSE                # AGPL-3.0 License
```

---

## Environment Variables

Copy `.env.example` to `.env` and configure:

```env
# Django
DEBUG=0
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=resumeverse
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

# Redis
REDIS_URL=redis://localhost:6379/0

# Email (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=1
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

---

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_profiles.py

# Run tests in Docker
docker compose exec web pytest
```

---

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 coding standards
- Write unit tests for new features
- Update documentation accordingly
- Ensure all tests pass before submitting PR

---

## License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

### What does this mean?
- ✅ You can view, use, and modify the source code
- ✅ You can share and distribute the software
- ✅ Contributions must be shared under the same license
- ✅ If you use this software as a web service (SaaS), you must publish your modifications
- ❌ Commercial use requires publishing modified source code

For more details, see the [LICENSE](LICENSE) file or visit [GNU AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.en.html).

> **Why AGPL-3.0?** This license protects the project from being used as a closed-source service while ensuring the community benefits from all improvements.

---

## Contact

**Project Maintainer:** [Your Name](mailto:your.email@example.com)

- **GitHub:** [@yourusername](https://github.com/yourusername)
- **LinkedIn:** [Your LinkedIn](https://linkedin.com/in/yourprofile)
- **Twitter:** [@yourusername](https://twitter.com/yourusername)

---

## Acknowledgments

- Django and Django REST Framework community
- All open-source libraries used in this project
- Contributors and beta testers

---

## Star Us

If you find this project useful, please consider giving it a star on GitHub! It helps others discover the project and motivates continued development.

---

**Built with ❤️ using Django**