# Single Sign-On (SSO) Implementation Guide for Luphonix Blog

This guide details how to implement and configure Single Sign-On (SSO) in your Django Wagtail project. Based on the project configuration, we'll be using django-allauth for SSO integration.

## Prerequisites

The following packages are already installed in your project (as seen in requirements.txt):
- django-allauth>=0.58.2
- pyjwt
- cryptography

## Current Configuration

Your project already has the basic SSO setup in place with the following providers:
- Google
- GitHub

## Configuration Steps

### 1. Django Settings

The following configurations are already in place in your `settings.py`:

```python
INSTALLED_APPS = [
    # ... existing code ...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]

MIDDLEWARE = [
    # ... existing code ...
    'allauth.account.middleware.AccountMiddleware'
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
```

### 2. Provider Setup

#### Google SSO

Your Google SSO is already configured with the following settings:

```python
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'APP': {
            'client_id': '538849210035-6cn9aki3u7kvom2o326frg7u9g2624ej.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}
```

#### GitHub SSO

The GitHub configuration is partially set up in your settings.py. You need to:

1. Create a new GitHub OAuth App at: https://github.com/settings/developers
2. Add the following callback URL: `http://localhost:5000/accounts/github/login/callback/`
3. Add your GitHub OAuth credentials to settings.py

### 3. URL Configuration

The URLs are already configured in your `urls.py`:

```python
urlpatterns = [
    # ... existing code ...
    path('accounts/', include('allauth.urls')),
]
```

### 4. Template Integration

Add these social login buttons to your login template:

```html
<div class="social-login">
    <a href="{% provider_login_url 'google' %}" class="btn btn-google">
        Sign in with Google
    </a>
    <a href="{% provider_login_url 'github' %}" class="btn btn-github">
        Sign in with GitHub
    </a>
</div>
```

### 5. Additional Settings

Add these settings to your `settings.py` for better SSO control:

```python
# AllAuth Configuration
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Luphonix Blog] '
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
```

## Security Considerations

1. **HTTPS**: In production, always use HTTPS. Update `ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'`
2. **Credentials**: Keep your OAuth credentials secure and never commit them to version control
3. **Scope**: Only request necessary permissions from OAuth providers
4. **Rate Limiting**: Implement rate limiting for authentication endpoints

## Testing SSO

1. Start your development server
2. Visit the login page
3. Click on either Google or GitHub login buttons
4. Authorize the application
5. Verify successful redirect to your application

## Troubleshooting

Common issues and solutions:

1. **Callback URL Mismatch**: Ensure your callback URLs match exactly in both provider settings and your application
2. **Email Verification**: If users can't login, check email verification settings
3. **Site ID**: Verify your site ID is correctly set in Django admin
4. **Provider Scope**: If missing permissions, check the scope settings for each provider

## Production Deployment

Before deploying to production:

1. Update OAuth credentials for production domain
2. Enable HTTPS
3. Update callback URLs
4. Set proper security headers
5. Enable proper logging for authentication events

## Monitoring

Monitor these aspects of your SSO implementation:

1. Failed login attempts
2. Provider availability
3. Session management
4. User authentication flow
5. Security events

This completes the SSO implementation guide for your Luphonix Blog project. The basic structure is already in place, and you can follow these steps to complete and customize the implementation according to your needs.

        