from .models import *

def sender_transaction(sender,receiver):
    if (sender.trust_level > 0 and sender.trust_level <= 100):
        sender.sent = (sender.endowment * (sender.trust_level/100))
        sender.endowment -= sender.sent
        sender.endowment = round(sender.endowment, 2)
        receiver.endowment += (sender.sent * C.K)
        receiver.endowment = round(receiver.endowment, 2)
        sender.reputation += (sender.trust_level/100)
        sender.avgReputation = (sender.reputation/(sender.round_number-sender.skipcounter))
        sender.avgReputation = round(sender.avgReputation, 2)
        sender.group.greputation = sender.avgReputation
    else:
        sender.avgReputation = (sender.reputation/(sender.round_number-sender.skipcounter))
        sender.avgReputation = round(sender.avgReputation, 2)
        sender.group.greputation = sender.avgReputation

def receiver_transaction(sender,receiver):
    if (receiver.trust_level > 0 and receiver.trust_level <= 100):
        receiver.sent = receiver.endowment * (receiver.trust_level/100)
        sender.endowment += receiver.sent
        sender.endowment = round(sender.endowment, 2) 
        receiver.endowment -= receiver.sent
        receiver.endowment = round(receiver.endowment, 2)
        receiver.reputation += (receiver.trust_level/100)
        receiver.avgReputation = (receiver.reputation/(receiver.round_number-receiver.skipcounter))
        receiver.avgReputation = round(receiver.avgReputation, 2)
        receiver.group.greputation += receiver.avgReputation
    else:
        receiver.avgReputation = (receiver.reputation/(receiver.round_number-receiver.skipcounter))
        receiver.avgReputation = round(receiver.avgReputation, 2)
        receiver.group.greputation += receiver.avgReputation

def calculate(subsession: Subsession):
    if subsession.round_number == 4:
        groups = subsession.get_groups()
        highest_payoff_group = max(groups, key=lambda group: group.greputation)
        ph1, ph2 = highest_payoff_group.get_players()
        ph1.payoff += 2000
        ph2.payoff += 2000
        lowest_payoff_group = min(groups, key=lambda group: group.greputation)
        pl1, pl2 = lowest_payoff_group.get_players()
        if pl1.avgReputation < pl2.avgReputation:
            pl1.payoff -= 1000
        else:
            pl2.payoff -= 1000
        for g in groups:
            for p in g.get_players():
                # p.payoff = p.payoff.to_real_world_currency(p.session)
                # p.payoff = p.payoff_plus_participation_fee()
                p.finalPayoff += p.payoff
                p.finalPayoff = p.finalPayoff * 0.01
    return 