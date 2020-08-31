# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:40:10 2020

@author: diego
"""

S0 = 100. #initial index level
K = 105. # strike price
T = 1.0 # time-to-maturity
r = 0.05 # riskless short rate
sigma = 0.25 # volatility

from numpy import *

I = 100000

random.seed(1000)
z = random.standard_normal(I)
ST = S0 * exp(r * T + sigma * sqrt(T) * z)
hT = maximum(ST - K, 0)
C0 = exp(-r * T) * sum(hT) / I


print("Value of the European Call Option %5.3f" % C0)

