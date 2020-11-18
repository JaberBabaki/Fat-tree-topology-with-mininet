from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.modules.mac_learner import mac_learner as act_like_switch
import csv, os
policy_file = "%s/pyretic/pyretic/examples/blocked_hosts.csv" % os.environ[ 'HOME' ]

def main():
    not_allowed = none
    with open(policy_file, 'rb') as f:
        reader = csv.DictReader(f)
        for row in reader:
            not_allowed = not_allowed match(srcmac=MAC(row['mac_0']), dstmac=MAC(row['mac_1'])) match(srcmac=MAC(row['mac_1']), dstmac=MAC(row['mac_0']))

    allowed = ~not_allowed
    return  allowed>>act_like_switch()