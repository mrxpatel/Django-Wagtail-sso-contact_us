


          
I'll help you add a contact form to your home page. Here's the updated code for your home page template with a styled contact form:

```html:c:\Users\Keval\Documents\Templates\Django-Wagtail-sso-contact_us\templates\home\home_page.html
{% extends "base.html" %}
{% load wagtailcore_tags %}

{% block title %}Welcome to My Portfolio{% endblock %}

{% block content %}
<div class="bg-white dark:bg-gray-800 shadow rounded-lg p-6">
    <div class="max-w-3xl mx-auto">
        <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-4">{{ page.title }}</h1>
        <div class="prose dark:prose-invert max-w-none">
            {{ page.body|richtext }}
        </div>
    </div>
</div>

<div class="mt-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- Featured Projects Section -->
    <div class="bg-white dark:bg-gray-800 shadow rounded-lg p-6">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">{{ page.featured_projects_title }}</h2>
        <div class="prose dark:prose-invert">
            {{ page.featured_projects_content|richtext }}
        </div>
    </div>

    <!-- Skills Section -->
    <div class="bg-white dark:bg-gray-800 shadow rounded-lg p-6">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">{{ page.skills_title }}</h2>
        <div class="prose dark:prose-invert">
            {{ page.skills_content|richtext }}
        </div>
    </div>

    <!-- Contact Section -->
    <div class="bg-white dark:bg-gray-800 shadow rounded-lg p-6">
        <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">{{ page.contact_title }}</h2>
        <div class="prose dark:prose-invert">
            {{ page.contact_content|richtext }}
        </div>
        
        <!-- Contact Form -->
        <form method="POST" class="mt-6 space-y-4">
            {% csrf_token %}
            <div>
                <label for="name" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Name</label>
                <input type="text" name="name" id="name" required 
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white">
            </div>
            
            <div>
                <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Email</label>
                <input type="email" name="email" id="email" required 
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white">
            </div>
            
            <div>
                <label for="message" class="block text-sm font-medium text-gray-700 dark:text-gray-300">Message</label>
                <textarea name="message" id="message" rows="4" required 
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white"></textarea>
            </div>
            
            <div>
                <button type="submit" 
                    class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                    Send Message
                </button>
            </div>
        </form>
    </div>
</div>
{% endblock %}
```

Now you'll need to update your HomePage model to handle the form submission. Add this to your `home/models.py` file:

```python:c:\Users\Keval\Documents\Templates\Django-Wagtail-sso-contact_us\home\models.py
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.response import TemplateResponse


class HomePage(Page):
    # Main content
    body = RichTextField(blank=True)
    
    # Featured Projects section
    featured_projects_title = models.CharField(max_length=255, default="Featured Projects")
    featured_projects_content = RichTextField(blank=True)
    
    # Skills section
    skills_title = models.CharField(max_length=255, default="Skills")
    skills_content = RichTextField(blank=True)
    
    # Contact section
    contact_title = models.CharField(max_length=255, default="Get in Touch")
    contact_content = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        MultiFieldPanel([
            FieldPanel('featured_projects_title'),
            FieldPanel('featured_projects_content'),
        ], heading="Featured Projects Section"),
        MultiFieldPanel([
            FieldPanel('skills_title'),
            FieldPanel('skills_content'),
        ], heading="Skills Section"),
        MultiFieldPanel([
            FieldPanel('contact_title'),
            FieldPanel('contact_content'),
        ], heading="Contact Section"),
    ]

    def serve(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            # Send email
            send_mail(
                f'Contact Form Submission from {name}',
                f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                email,  # From email
                ['your-email@example.com'],  # Replace with your email address
                fail_silently=False,
            )
            
            # Add a success message
            from django.contrib import messages
            messages.success(request, 'Thank you for your message. We\'ll get back to you soon!')
            
        return super().serve(request)

    class Meta:
        verbose_name = "Home Page"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
```

Finally, make sure to configure your email settings in `settings.py`. Add these settings:

```python:c:\Users\Keval\Documents\Templates\Django-Wagtail-sso-contact_us\sites\settings.py
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Or your SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your-app-password'  # Replace with your email password or app-specific password
```

Don't forget to:
1. Replace 'your-email@example.com' in the HomePage model with your actual email address
2. Configure your email settings in settings.py with your actual SMTP server details
3. Run migrations if you made any model changes

The contact form is now integrated into your home page with a clean design that matches your existing theme. When users submit the form, it will send you an email with their message.
        