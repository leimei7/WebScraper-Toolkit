import requests

response = requests.get('https://www.zhipin.com/wapi/zpgeek/search/joblist.json')
data = response.json()
print(data)
name = data['zpData']['name']
seed = data['zpData']['seed']
t = data['zpData']['ts']

print('__zp_sname__:',name)
print('__zp_sseed__:',seed)
print('__zp_sts__:',t)

"""
__zp_sseed__: s6APuaMEn2Ng7TtuzwzX5zyI7hDBj42/VSmgLkOVZxg=
__zp_sname__: 3bff01f6
__zp_sts__: 1749113554083
"""