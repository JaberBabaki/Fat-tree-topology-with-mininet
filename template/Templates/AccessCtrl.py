from pox.core import core
from pox.lib.addresses import IPAddr, EthAddr
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import EventHalt


فهرستی تعریف کنید.
در این فهرست کاربر ۱ را اضافه کنید.


class ACModule(object):
  لیستی را که تعریف کرده بودید به‌طور سراسری تعری
  ف کنید تا بقیه توابع بتوانند به آن دسترسی داشته باشند.

  def __init__ (self, connection):
    self.connection = connection
    برای ارتباط، شنونده با اولویت بالا  کنید.

  def _handle_PacketIn (self, event):
    رویدادی که رخ داده است را تجزیه کرده و آن را داخل یک بسته قرار دهید.

    یک تابع برای دراپ بنویسید.
	
    حالت‌های مختلفی که در صورت سوال گفته شده را در گزاره‌های شرطی چک کرده
	و برای هر مورد مشخص کنید چه عملی باید انجام شود.

class AccessControl (object):

  def __init__ (self):
    core.openflow.addListeners(self)

  def _handle_ConnectionUp (self, event):
    کانکشنی که دریافت کرده‌اید را به کلاس کنترل دسترسی تحویل دهید.


def launch ():
  ماژول جدید را در مولفه‌ی 
  Core
  رجیستر کنید.


