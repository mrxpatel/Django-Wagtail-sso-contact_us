from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.files.base import ContentFile
import requests

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        
        if sociallogin.account.provider == 'google':
            picture_url = sociallogin.account.extra_data.get('picture')
        elif sociallogin.account.provider == 'github':
            picture_url = sociallogin.account.extra_data.get('avatar_url')
            
        if picture_url:
            response = requests.get(picture_url)
            if response.status_code == 200:
                filename = f"profile_picture_{user.username}.jpg"
                user.userprofile.profile_picture.save(
                    filename,
                    ContentFile(response.content),
                    save=True
                )
        
        return user