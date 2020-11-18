#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink
from random import randint
from mininet.node import CPULimitedHost,RemoteController
from mininet.cli import CLI
import os
from mininet.node import Controller 

class DCTreeTopo(Topo):     
  def build(self):        
    CoreSwitch1 = self.addSwitch('s1')
    AggSwitch1 = self.addSwitch('s3')             
    self.addLink(CoreSwitch1, AggSwitch1,bw=100, delay='5ms')
    EdgeSwitch1 = self.addSwitch('s5')                  
    self.addLink(AggSwitch, EdgeSwitch1,bw=50, delay='10ms')                  
    host1 = self.addHost('h1')                   
    self.addLink(host1, EdgeSwitch1,bw=10, delay='15ms')
    توپولوژی را تکمیل کنید

if __name__ == '__main__':
    topo = DCTreeTopo()
    توپولوژی را به پکیج مینی‌نت بدهید تا شبکه را بسازد.
    در بخش آخر تمرین، به شبکه کنترلر اضافه کنید.
    شبکه را استارت بزنید.
    خط کدی بنویسید که خط فرمان مینی‌نت را در اختیارتان قرار دهد
    شبکه را متوقف کنید.

