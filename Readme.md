# Portfolio Website with Django and Wagtail

A modern portfolio website built with Django, Wagtail CMS, and TailwindCSS.

## Technologies Used

- Python 3.11+
- Django 5.1.x
- Wagtail 6.4.x
- TailwindCSS (via CDN)
- PostgreSQL (optional, SQLite for development)

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

The requirements include:
- Django>=5.1,<5.2
- wagtail>=6.4,<6.5
- django-extensions
- djangorestframework
- python-dotenv
- whitenoise
- psycopg2-binary>=2.9.10
- gunicorn>=23.0.0
- Pillow>=10.0.0
- wagtail-modeladmin

4. Create a `.env` file in the root directory:
```plaintext
SECRET_KEY=your_secret_key_here
DEBUG=True
```

5. Initialize the database:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The site will be available at `http://localhost:8000`

## Project Structure

```
portfolio/
├── home/                 # Home app for main page
├── portfolio/           # Main project settings
├── portfolio_content/   # Content management app
├── search/             # Search functionality
├── static/            # Static files
├── media/            # User uploaded files
└── templates/        # HTML templates
```

## Features

- Responsive design with TailwindCSS
- Wagtail CMS for content management
- REST API support
- Resume page with PDF viewer
- Skills and projects showcase
- Contact form
- Social media integration
- Dark theme

## Development

To work on the project:

1. Make sure you're in the virtual environment
2. Run migrations after model changes:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Access the Wagtail admin at:
```
http://localhost:8000/wagtail-cms-admin/
```

## Production Deployment

1. Update `.env` for production:
```plaintext
DEBUG=False
SECRET_KEY=your_secure_secret_key
ALLOWED_HOSTS=your-domain.com
```

2. Configure your web server (e.g., Nginx, Apache)
3. Use gunicorn for serving the application
4. Set up static files serving with whitenoise

## License

[Your License Here]

## Author

[Your Name]

## Project Setup Commands

1. Create a new Django project:
```bash
django-admin startproject portfolio .

pip install wagtail django-extensions djangorestframework python-dotenv whitenoise psycopg2-binary gunicorn Pillow wagtail-modeladmin

wagtail start home .

python manage.py startapp site_content
python manage.py startapp search

```
```
INSTALLED_APPS = [
    'home',
    'search',
    'portfolio_content',
    
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.api.v2',

    'modelcluster',
    'taggit',
    'django_extensions',
    'rest_framework',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
 ```
MIDDLEWARE = [
    # ... existing middleware ...
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]
```
```
mkdir -p static/css static/js static/images media templates/home templates/search
```