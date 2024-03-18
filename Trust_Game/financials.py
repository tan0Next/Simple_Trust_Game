from .models import *

def sender_transaction(sender,receiver):
        sender.sent = (sender.endowment * (sender.trust_level/100))
        sender.payoff = sender.endowment - sender.sent
        sender.payoff = round(sender.payoff, 2)
        receiver.endowment += (sender.sent * C.K)
        receiver.endowment = round(receiver.endowment, 2)
        sender.reputation += (sender.trust_level/100)
        sender.avgReputation = (sender.reputation/(sender.round_number-sender.skipcounter))
        sender.avgReputation = round(sender.avgReputation, 2)
        sender.group.greputation = sender.avgReputation
        if receiver.endowment == 0:
                receiver.skipcounter += 1
                receiver.skipflag = True


def receiver_transaction(sender,receiver):
        receiver.sent = receiver.endowment * (receiver.trust_level/100)
        sender.payoff += receiver.sent
        sender.payoff = round(sender.payoff, 2)
        receiver.payoff = receiver.endowment - receiver.sent 
        receiver.payoff = round(receiver.payoff, 2)
        receiver.reputation += (receiver.trust_level/100)
        receiver.avgReputation = (receiver.reputation/(receiver.round_number-receiver.skipcounter))
        receiver.avgReputation = round(receiver.avgReputation, 2)
        receiver.group.greputation += receiver.avgReputation
        receiver.group.greputation = round(receiver.group.greputation, 2)


def calculate(subsession: Subsession):
    if subsession.round_number == 4:
        groups = subsession.get_groups()
        highest_payoff_group = max(groups, key=lambda group: group.greputation)
        ph1, ph2 = highest_payoff_group.get_players()
        ph1.participant.payoff *= 2
        ph2.participant.payoff *= 2
        lowest_payoff_group = min(groups, key=lambda group: group.greputation)
        pl1, pl2 = lowest_payoff_group.get_players()
        if pl1.avgReputation < pl2.avgReputation:
            pl1.participant.payoff *= 0.25
        else:
            pl2.participant.payoff *= 0.25
    return 