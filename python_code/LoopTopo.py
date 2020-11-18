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

    link1=dict(bw=100,delay='5ms')
    link2=dict(bw=50,delay='10ms')
    link3=dict(bw=10,delay='15ms')

    #addefd switches and hosts to the topology
    CS1= self.addSwitch('s1')
    CS2= self.addSwitch('s2')
    AggS1= self.addSwitch('s3')
    AggS2= self.addSwitch('s4')
    EdgS1= self.addSwitch('s5')                  
    EdgS2= self.addSwitch('s6')
    EdgS3= self.addSwitch('s7')
    EdgS4= self.addSwitch('s8')
    H1 = self.addHost('h1')                   
    H2 = self.addHost('h2')
    H3 = self.addHost('h3')
    H4 = self.addHost('h4')
    H5 = self.addHost('h5')
    H6 = self.addHost('h6')
    H7 = self.addHost('h7')
    H8 = self.addHost('h8')

    #connect switches and hosts together with links
    self.addLink(CS1, AggS1,**link1)
    self.addLink(CS1, AggS2,**link1)
    self.addLink(CS2, AggS1,**link1)
    self.addLink(CS2, AggS2,**link1)

    self.addLink(AggS1, EdgS1,**link2)
    self.addLink(AggS1, EdgS2,**link2)
    self.addLink(AggS2, EdgS3,**link2)
    self.addLink(AggS2, EdgS4,**link2)

    self.addLink(H1, EdgS1,**link3)
    self.addLink(H2, EdgS1,**link3)
    self.addLink(H3, EdgS2,**link3)
    self.addLink(H4, EdgS2,**link3)
    self.addLink(H5, EdgS3,**link3)
    self.addLink(H6, EdgS3,**link3)
    self.addLink(H7, EdgS4,**link3)
    self.addLink(H8, EdgS4,**link3)
   


if __name__ == '__main__':
        topo= DCTreeTopo()
	net= Mininet(topo,link=TCLink,autoSetMacs=True)#create the mininet
        net.addController(name='jaber',controller=RemoteController, ip='127.0.0.1',port=6633)#add pox controller 
	net.start()#start mininet 
	CLI(net)#up mininet command line 
	net.stop()#stop mininet


