#Sample settings for a staging server

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

STATIC_ROOT = os.path.join(BASE_DIR,'../shared/static')
MEDIA_ROOT = os.path.join(BASE_DIR,'../shared/media')

SITE_URL = "http://.6ft.io"
