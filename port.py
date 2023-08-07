#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 16:05:44 2023

@author: Locos
"""

import socket

def is_port_available(port):
    try:
        # Crée une socket et essaie de l'associer au port spécifié
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', port))
            return True
    except OSError:
        return False

# Essayez de trouver un port disponible dans la plage 49152 à 65535
for port in range(49152, 65536):
    if is_port_available(port):
        print(f"Port disponible : {port}")
        break
