# import requests
# import pprint
#
# peyload = {'username': 'takkoe', 'password': 'ananas'}
# r = requests.get('https://httpbin.org/basic-auth/takkoe/ananas', auth=('takkoe', 'ananas'))
#
# print(r)
# print(r.status_code)
# print(r.text)

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
t = dir_path / "qwert"
print(t)
