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
