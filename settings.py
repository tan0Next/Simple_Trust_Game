from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.01, participation_fee=200)
SESSION_CONFIGS = [dict(name='trust_game_session', num_demo_participants=2, app_sequence=['Trust_Game'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'Tk'
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
ROOMS = [dict(name='Trust_Game_room', display_name='Players')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


