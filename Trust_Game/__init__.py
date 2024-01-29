from otree.api import *
from .models import *
from .Pages.pages import *

c = cu
doc = ''

class Page(Page):
    subsession: Subsession
    group: Group
    player: Player


class WaitPage(WaitPage):
    subsession: Subsession
    group: Group

