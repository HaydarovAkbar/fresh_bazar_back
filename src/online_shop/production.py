DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<database_name>',
        'USER': '<database_user>',
        'PASSWORD': '<database_password>',
        'HOST': '<database_host>',
        'PORT': '<database_port>',
        'OPTIONS': {
            'sslmode': 'require',  # Enable SSL
        },
    }
}