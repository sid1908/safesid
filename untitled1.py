# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:48:46 2020

@author: Aumento 101
"""

import pandas
import matplotlib.pyplot as plt
dataset = pandas.read_csv('airline-passengers.csv', usecols=[1], engine='python')
plt.plot(dataset)
plt.show()