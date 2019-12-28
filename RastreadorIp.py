#!/usr/bin/env python
import os ,platform
os.system("clear")
print ("""
(Solamente Para Termux)
        _____
  _____/     \ IP RASTREADOR
(@)_______(@)|=  BY ALEJO


""")
ip = raw_input ('Ip Victima: ')
os.system("termux-open https://aruljohn.com/track.pl?ip=" + ip)
