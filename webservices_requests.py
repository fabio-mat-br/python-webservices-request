# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 09:22:11 2016

@author: brolesi
"""
import requests, time, copy

def access(url, method, payload, wrong_params):
    results = []
    for key in payload:
        new_palyoad = copy.copy(payload)
        new_params = copy.copy(wrong_params)
        new_params.append(payload[key])
        for i in xrange(0, len(new_params)):
            new_palyoad[key] = new_params[i]
            start = time.time()
            q = requests.request(method, url, params = payload)
            done = time.time()
            elapsed = done - start
            current_result = {
                'url':     url,
                'method': 'POST',
                'start':   start,
                'elapsed': elapsed,
                'header':  q.headers,
                'status':  q.status_code,
                'body':    q.text
            }
            results.append(current_result)
    return results