# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:15:10 2020

@author: surya
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'SLSMAN_CD':60,'PROD_CD':50,'PLAN_MONTH':2,'TARGET_IN_EA':600})

print(r.json())
