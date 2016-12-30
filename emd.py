#!/usr/bin/python
# demo.py - CMD Args Demo By nixCraft
import sys, json, ast
from pyemd import emd
import numpy as np
 
A=np.array(json.loads(sys.argv[1]))
B=np.array(json.loads(sys.argv[2]))
C=np.array(json.loads(sys.argv[3]))

print (emd(A,B,C))
