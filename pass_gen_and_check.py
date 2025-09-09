# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 17:03:41 2025

@author: nwetherby
"""

import random
import hashlib
import requests

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.?!@#$%^&*'

length = int(input('Password Length? '))

password = ''
for c in range(length):
    password += random.choice(chars)
print(password)

def check_password(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    first5, tail = sha1_hash[:5], sha1_hash[5:]
    # Cross check with 'Have I got Pwnd' to see any leaks
    response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
    
    # Results
    if tail in response.text:
        print("THIS PASSWORD HAS BEEN FOUND IN A DATA BREACH! Choose a stronger password.")
    else:
        print("This password has not been found in leaks. Should be safe to use.")
        
check_password(password)

