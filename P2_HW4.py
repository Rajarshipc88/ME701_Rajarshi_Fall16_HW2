# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:30:31 2016

@author: rajarshi
"""

import re 

P=r'[p-s][^to|ea]' #Search String

S_l=[r'pit', r'spot',r'spate', r'slap two', r'respite'] # Destination string Left Column

S_r=[r'pt', r'Pot', r'peat', r'part']  # Destination string right column
m1=re.search(P,S_l[0])
m2=re.search(P,S_l[1])
m3=re.search(P,S_l[2])
m4=re.search(P,S_l[3])
m5=re.search(P,S_l[4])

print m1.span()
print m2.span()
print m3.span()
print m4.span()
print m5.span()

n1=re.search(P,S_r[0])
n2=re.search(P,S_r[1])
n3=re.search(P,S_r[2])
n4=re.search(P,S_r[3])


print n1.span()
print n2.span()
print n3.span()
print n4.span()


