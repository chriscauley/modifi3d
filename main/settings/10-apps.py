INSTALLED_APPS = (
  'main',
  'suit',

  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',

  'compressor',
  'crop_override',
  'sorl.thumbnail',

  'jscad',
)

# Django Suit configuration example
SUIT_CONFIG = {
  # header
  'ADMIN_NAME': 'Modifi3d',
  # 'HEADER_DATE_FORMAT': 'l, j. F Y',
  # 'HEADER_TIME_FORMAT': 'H:i',

  # forms
  # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
  # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

  # menu
  # 'SEARCH_URL': '/admin/auth/user/',
  # 'MENU_ICONS': {
  #  'sites': 'icon-leaf',
  #  'auth': 'icon-lock',
  # },
  # 'MENU_OPEN_FIRST_CHILD': True, # Default True
  # 'MENU_EXCLUDE': ('auth.group',),
  #'MENU': (
  #  {'app': 'auth', 'label': 'Authorization', 'icon':'icon-lock'},
  #),

  # misc
  # 'LIST_PER_PAGE': 15
}
