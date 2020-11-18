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

net = Mininet(link=TCLink)

link1=dict(bw=100,delay='5ms')
link2=dict(bw=50,delay='10ms')
link3=dict(bw=10,delay='15ms')

#add switches and hosts to the topology
CS1= net.addSwitch('s1')
CS2= net.addSwitch('s2')
AggS1= net.addSwitch('s3')
AggS2= net.addSwitch('s4')
EdgS1= net.addSwitch('s5')                  
EdgS2= net.addSwitch('s6')
EdgS3= net.addSwitch('s7')
EdgS4= net.addSwitch('s8')
H1 = net.addHost('h1',mac='00:00:00:00:00:01')                   
H2 = net.addHost('h2',mac='00:00:00:00:00:02')
H3 = net.addHost('h3',mac='00:00:00:00:00:03')
H4 = net.addHost('h4',mac='00:00:00:00:00:04')
H5 = net.addHost('h5',mac='00:00:00:00:00:05')
H6 = net.addHost('h6',mac='00:00:00:00:00:06')
H7 = net.addHost('h7',mac='00:00:00:00:00:07')
H8 = net.addHost('h8',mac='00:00:00:00:00:08')

#connect switches and hosts together with links
net.addLink(CS1, AggS1,**link1)
net.addLink(CS1, AggS2,**link1)
net.addLink(CS2, AggS1,**link1)
net.addLink(CS2, AggS2,**link1)

net.addLink(AggS1, EdgS1,**link2)
net.addLink(AggS1, EdgS2,**link2)
net.addLink(AggS2, EdgS3,**link2)
net.addLink(AggS2, EdgS4,**link2)

net.addLink(H1, EdgS1,**link3)
net.addLink(H2, EdgS1,**link3)
net.addLink(H3, EdgS2,**link3)
net.addLink(H4, EdgS2,**link3)
net.addLink(H5, EdgS3,**link3)
net.addLink(H6, EdgS3,**link3)
net.addLink(H7, EdgS4,**link3)
net.addLink(H8, EdgS4,**link3)
 
net.addController(name='jaber',controller=RemoteController, ip='127.0.0.1',port=6633)   
net.start()
CLI(net)
net.stop()


