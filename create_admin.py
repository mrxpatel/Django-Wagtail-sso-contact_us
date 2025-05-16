import os
import django
from django.contrib.auth import get_user_model

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sites.settings')
django.setup()

def create_superuser():
    User = get_user_model()
    
    # Check if a superuser already exists
    if not User.objects.filter(is_superuser=True).exists():
        # Create superuser
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        print('Superuser created successfully!')
    else:
        print('Superuser already exists.')

if __name__ == '__main__':
    create_superuser()