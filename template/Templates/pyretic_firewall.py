
from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.modules.mac_learner import mac_learner as act_like_switch
import csv, os

policy_file = "%s/pyretic/pyretic/examples/firewall-policies.csv" % os.environ[ 'HOME' ]

def main():

    # start with a policy that doesn't match any packets
    not_allowed = none
    # and add traffic that isn't allowed
    for <each pair of MAC address in firewall-policies.csv>:
        not_allowed = not_allowed + ( <traffic going in one direction> ) + ( <traffic going in the other direction> )

    # express allowed traffic in terms of not_allowed - hint use '~'
    allowed = <...>

    # and only send allowed traffic to the mac learning (act_like_switch) logic
    return allowed >> act_like_switch()



