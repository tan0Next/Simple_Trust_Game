from otree.api import *
from ..models import *
from ..financials import *

class Waiting1(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        player_list = group.get_players()
        p1 = player_list[0]
        p2 = player_list[1]
        if group.round_number %2 != 0:
            sender_transaction(p1,p2)
        else:
            sender_transaction(p2,p1)


class Waiting2(WaitPage):
    def after_all_players_arrive(group: Group):
        player_list = group.get_players()
        p1 = player_list[0]
        p2 = player_list[1]
        if group.round_number %2 != 0:
            if p2.skipflag == False:
                receiver_transaction(p1,p2)
            else:
                group.greputation += p2.avgReputation
        else:
            if p1.skipflag == False:
                receiver_transaction(p2,p1)
            else:
                group.greputation += p1.avgReputation


class Arrival(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        return 


class ArrivalforallGroupsAtMiddle(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def is_displayed(self):
        return self.subsession.round_number == 2
    

class Arrival2(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = calculate
    @staticmethod
    def is_displayed(self):
        return self.subsession.round_number == C.NUM_ROUNDS