# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:51:28 2016

@author: rajarshi
"""

import re

f=open('atomic_masses.txt')
s=f.read()
s1=s.split()[0::2]
r1=r'Atomic Number = \d+'
Z=re.findall(r1,s)


r2=r'Atomic Symbol = [a-z|A-Z]'
X=re.findall(r2,s)

r3=r'Mass Number = \d+'
A=re.findall(r3,s)


r4=r'Standard Atomic Weight = \d.\d\d\d\d\d\d+'
M=re.findall(r4,s)









