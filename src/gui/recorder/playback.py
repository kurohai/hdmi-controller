#!/usr/bin/env python

# playback.py
# 2014-04-24
# Public Domain

import os
import sys
import time

import pigpio

mapping = [None] * 32

def validate_gpioarg(arg):

   gpios = arg.split("=")

   if len(gpios) > 2:
      return (-1, -1)

   try:
      gt = int(gpios[0])
   except:
     return (-1, -1)

   gf = gt

   if len(gpios) > 1:
      try:
         gf = int(gpios[1])
      except:
        return (-1, -1)

   if gt < 0 or gt > 31 or gf < 0 or gf > 31:
      return (-1, -1)

   return (gt, gf)


def validate_args():

   ok = True

   args = len(sys.argv)

   if args < 2:
      print("Usage: {} file gpio *[gpio]".format(sys.argv[0]))
      return False

   filename = sys.argv[1]

   if not os.path.isfile(filename):
      print("Bad file: {}".format(filename))
      ok = False

   if args < 3:
      print("Usage: {} file gpio *[gpio]".format(sys.argv[0]))
      return False

   for i in range(args-2):

      arg = sys.argv[i+2]

      (gt, gf) = validate_gpioarg(arg)

      if gt == -1:
         print("Bad gpio: {}".format(arg))
         ok = False
      else:
         mapping[gt] = gf

   return ok

if not validate_args():
   exit(1)

# condense gpio assignments to a list

gpios = []

for i in range(32):
   if mapping[i] is not None:
      gpios.append((i, 1<<i, 1<<mapping[i]))

wf = []

with open(sys.argv[1], 'r') as f:
   first = True
   for line in f:

      if line[0] != '#':
         fields = line.split()
         stamp = int(fields[0])
         levels = int(fields[1],16)

         if first:
            first = False

            on = 0
            off = 0

            for g in gpios:
               if g[2] & levels:
                  on = on | g[1]
               else:
                  off = off | g[1]

            #wf.append(pigpio.pulse(off, on, 1000))

            last_on = off
            last_off = on

         else:

            if on == last_on and off == last_off:
               p = wf.pop()
               delay = p.delay
            else:
               delay = 0

            wf.append(pigpio.pulse(on, off, (stamp-last_stamp)+delay))

            last_on = on
            last_off = off

            on = 0
            off = 0

            for g in gpios:
                if g[2] & levels:
                   on = on | g[1]
                else:
                   off = off | g[1]

         last_stamp = stamp

   if on != last_on or off != last_off:
      wf.append(pigpio.pulse(on, off, 0))
   else:
      p = wf.pop()
      p.delay = 0
      wf.append(p)

   f.close()

pi = pigpio.pi() # Connect to local Pi.

pi.wave_clear()
pi.wave_add_generic(wf)
wid = pi.wave_create()

if wid >= 0:
   pi.wave_send_once(wid)
   pi.wave_delete(wid)
   while pi.wave_tx_busy():
      time.sleep(0.01)

pi.stop()
