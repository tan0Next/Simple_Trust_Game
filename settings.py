from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.01, participation_fee=150)
SESSION_CONFIGS = [dict(name='trust_game_session', num_demo_participants=2, app_sequence=['Trust_Game'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'BDT'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
ROOMS = [
    dict(
        name='ESS_Lab',
        display_name='ESS Lab',
        participant_label_file='_rooms/ess_lab.txt',
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
