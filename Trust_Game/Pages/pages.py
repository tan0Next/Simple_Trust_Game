from otree.api import *
import random

from ..models import *
from .waitpages import *

class Disclaimer(Page):
    template_name = "Disclaimer.html"
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    
class PariticipantInfoPage(Page):
    form_model = 'player'
    form_fields = ['Name', 'Paticipant_Id','Age','Gender','Education']
    template_name = 'PariticipantInfoPage.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    def before_next_page(player: Player, timeout_happened):
        if player.Name == "":
            player.Name = str(player.group.id_in_subsession)+str(player.id_in_group)


class Retreiver(Page):
    timeout_seconds = 1
    template_name = 'Retreiver.html'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if (player.id_in_group == 1 and player.round_number %2 != 0):
            player.group.n = random.randint(1,4)
            player.endowment = C.X*player.group.n
        elif (player.id_in_group == 2 and player.round_number %2 == 0):
            player.group.n = random.randint(1,4)
            player.endowment = C.X*player.group.n
        if player.round_number > 1:
            prev_player = player.in_round(player.round_number - 1)
            player.Name = prev_player.Name
            player.Paticipant_Id = prev_player.Paticipant_Id
            player.Age = prev_player.Age
            player.Gender = prev_player.Gender
            player.Education = prev_player.Education
            player.reputation = prev_player.reputation
            player.avgReputation = prev_player.avgReputation
            player.skipcounter = prev_player.skipcounter
            player.payoff = prev_player.payoff
            player.payoff += cu(prev_player.endowment)

            # For players playing with their remainder of points in even number of rounds
            # if player.round_number % 2 == 0:
            #     player.endowment = prev_player.endowment
            #     player.payoff = prev_player.payoff
            # else:
            #     player.payoff = cu(prev_player.endowment)


class RateOfReturn(Page):
    template_name = 'RateOfReturn.html'
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number %2 != 0:
            return player.id_in_group == 1
        else:
            return player.id_in_group == 2
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.round_number %2 == 0:
            p2 = player.group.get_player_by_id(2)
            if p2.endowment == 0:
                p2.skipcounter += 1
                p2.skipflag = True
 
    
class SenderChoicePage(Page):
    form_model = 'player'
    form_fields = ['trust_level','trust_expectation']
    template_name = 'SenderChoicePage.html'
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number %2 != 0:
            return player.id_in_group == 1
        else:
            p2 = player.group.get_player_by_id(2)
            if p2.skipflag == False:
                return player.id_in_group == 2
            else:
                player.group.greputation = p2.avgReputation

class SenderConfirmationPage(Page):
    template_name = 'SenderConfirmationPage.html'
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number %2 != 0:
            return player.id_in_group == 1
        else:
            return player.id_in_group == 2


class ReceiverEndowment(Page):
    template_name = 'ReceiverEndowment.html'
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number %2 != 0:
            return player.id_in_group == 2
        else:
            return player.id_in_group == 1
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.round_number %2 != 0:
            p2 = player.group.get_player_by_id(2)
            if p2.endowment == 0:
                p2.skipcounter += 1
                p2.skipflag = True
        else:
            p1 = player.group.get_player_by_id(1)
            if p1.endowment == 0:
                p1.skipcounter += 1
                p1.skipflag = True
    @staticmethod
    def vars_for_template(player: Player):
        other_player = player.get_others_in_group()[0]
        tempv = other_player.sent * C.K
        tempv = round(tempv, 2)
        return {
            "endowment": tempv
        }


class ReceiverChoicePage(Page):
    form_model = 'player'
    form_fields = ['trust_level','trust_expectation']
    template_name = 'ReceiverChoicePage.html'
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number %2 != 0:
            p2 = player.group.get_player_by_id(2)
            if p2.skipflag == False:
                return player.id_in_group == 2
        else:
            p1 = player.group.get_player_by_id(1)
            if p1.skipflag == False:
                return player.id_in_group == 1
            
            
class ReceiverConfirmationPage(Page):
    template_name = 'ReceiverConfirmationPage.html'
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number %2 != 0:
            return player.id_in_group == 2
        else:
            return player.id_in_group == 1
            

class SenderEndowment(Page):
    template_name = 'SenderEndowment.html'
    @staticmethod
    def is_displayed(player: Player):
        if player.round_number %2 != 0:
            p2 = player.group.get_player_by_id(2)
            if p2.skipflag == False:
                return player.id_in_group == 1
        else:
            return player.id_in_group == 2
    @staticmethod
    def vars_for_template(player: Player):
        other_player = player.get_others_in_group()[0]
        tempv = round(other_player.sent, 2)
        return {
            "endowment": tempv
        }
    
    
class PerRound(Page):
    template_name = 'PerRound.html'
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.round_number %2 == 0:
            player.group.greputation = round(player.group.greputation, 2)
        if player.round_number == C.NUM_ROUNDS:
            player.payoff += cu(player.endowment)


class Result_At_Middle(Page):
    template_name = 'Result_At_Middle.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2


class Result(Page):
    template_name = 'Result.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


class FinalResult(Page):
    template_name = 'FinalResult.html'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS
    @staticmethod
    def vars_for_template(player: Player):
        groups = player.subsession.get_groups()
        sortedGroups = sorted(groups, key=lambda group: group.greputation, reverse=True)
        number_of_groups = len(sortedGroups)
        rank = []
        for i in range(1,number_of_groups+1):
            rank.append(i)
        return {
            "groups": sortedGroups,
            "ranks": rank
        }

page_sequence = [Disclaimer,PariticipantInfoPage, Retreiver, RateOfReturn, SenderChoicePage, Waiting1, SenderConfirmationPage, ReceiverEndowment, ReceiverChoicePage, 
                 Waiting2, ReceiverConfirmationPage, SenderEndowment, PerRound, Arrival, Result_At_Middle, Result, Arrival2, FinalResult]