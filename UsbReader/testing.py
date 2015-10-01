__author__ = 'mikedanylov'

from UsbReader import *

usb = UsbReader('/dev/ttyUSB0', 4800)

usb.read_continuously()
