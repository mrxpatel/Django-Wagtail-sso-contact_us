from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


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

    class Meta:
        verbose_name = "Home Page"