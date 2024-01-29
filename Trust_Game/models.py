from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'Demo'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 4
    X = 1000
    M = 8
    K = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    greputation = models.FloatField(initial=0)
    n = models.IntegerField(initial=0)

class Player(BasePlayer):
    Name = models.StringField(label='What is your name?',initial="",blank=True)
    Paticipant_Id = models.IntegerField(label='What is your ID?',initial=0)
    Age = models.IntegerField(label='What is your age?',initial=0)
    Gender = models.StringField(label='What is your gender?',blank=True,choices=[["Male","Male"],["Female","Female"]])
    Education = models.StringField(label='What is your education status?',blank=True,choices=[["SSC","SSC"],["HSC","HSC"],["Undergrad","Undergrad"],["Graduate","Graduate"],["Masters","Masters"],["PhD","PhD"]])
    trust_level = models.FloatField(label='If you distrust your partner, write 0, otherwise write any value from 1 to 100(percentage)',initial=0,min=0, max=100)
    trust_expectation = models.FloatField(label="What percentage of your partner's points are you expecting?",initial=0,min=0, max=100)
    sent = models.FloatField(initial=0)
    reputation = models.FloatField(initial=0)
    endowment = models.FloatField(initial=0)
    avgReputation = models.FloatField(initial=0)
    finalPayoff = models.CurrencyField(initial=20000)
    skipcounter = models.IntegerField(initial=0)
    skipflag = models.BooleanField(initial=False)