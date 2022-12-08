# Djangoの秘密キー
SECRET_KEY = ''

# DB接続情報
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db-test',
        'USER': 'admin',
        'PASSWORD': 'KAMATA-k019c',
        'HOST': 'db-test.ccva93nohvtb.ap-northeast-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}

# XXのキー
# XX = ''