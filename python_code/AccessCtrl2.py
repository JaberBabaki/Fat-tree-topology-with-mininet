from pox.core import core
from pox.lib.addresses import IPAddr, EthAddr
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import EventHalt
police_mac = [EthAddr('00:00:00:00:00:01')]

class ACModule(object):
  global police_mac

  def __init__(self, connection):
    self.connection = connection
    connection.addListeners(self,priority=23)   

  def _handle_PacketIn(self, event):
    packet = event.parsed
    def drop(duration=None):
      if duration is not None:
        if not isinstance(duration, tuple):
          duration = (duration, duration)
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout =14
        msg.hard_timeout =94
        msg.buffer_id = event.ofp.buffer_id
        self.connection.send(msg)
      elif event.ofp.buffer_id is not None:
        msg = of.ofp_packet_out()
        msg.buffer_id = event.ofp.buffer_id
        msg.in_port = event.port
        self.connection.send(msg) 
    if packet.type == packet.ARP_TYPE:
      return 
    if packet.src == EthAddr('00:00:00:00:00:01'):
      police_mac.append(packet.dst)
      return 
    if (packet.dst in police_mac and packet.src in police_mac) or packet.dst == '00:00:00:00:00:01':
      return
    if (packet.dst not in police_mac) or (packet.src not in police_mac):
      drop()
      return EventHalt
class AccessControl(object):
  def __init__(self):
    core.openflow.addListeners(self)

  def _handle_ConnectionUp(self, event):

    ACModule(event.connection)
       


def launch():
  core.registerNew(AccessControl)
