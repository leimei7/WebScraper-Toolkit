# import requests
#
# cookies = {
#     'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22195ef9e32471194-02a6cdc88409d52-4c657b58-1474560-195ef9e32483343%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%22195ef9e32471194-02a6cdc88409d52-4c657b58-1474560-195ef9e32483343%22%7D',
#     'sajssdk_2015_cross_new_user': '1',
#     '_gid': 'GA1.2.66424947.1743481879',
#     'Hm_lvt_2663761a9226999365054376b04969e1': '1743481878,1743485969',
#     'HMACCOUNT': '4F01C978615D7DB2',
#     'acw_tc': '1a0c660317434859706955284e004ad752bcddc543a1f44a10d1aa30fdfd8f',
#     'acw_sc__v2': '67eb7c122c15ae8d5367e89d531781fc5ea4867a',
#     'queryKey': 'KEH2R4NQEN8',
#     '_ga_2TQ4PLYBNK': 'GS1.1.1743485969.2.1.1743486094.59.0.0',
#     '_ga': 'GA1.2.1788631146.1743481879',
#     'Hm_lpvt_2663761a9226999365054376b04969e1': '1743486094',
#     '_fp_': 'eyJpcCI6IjIxOC4yMDAuMjI1LjE1OSIsImZwIjoiNTQzMDFlMzFkM2QyNWFhNTc0YTljMjYyNjcwNzA1MDgiLCJocyI6IiQyYSQwOCQubWJZN2ZrU0tHaEY5VHVzOU5URC8uWVk5eGNSSFNSMTNmTW9IWEc2ZC9HSU9WRTVFZEdIaSJ9',
#     'ssxmod_itna': 'YqAx2DBDyD9D0Dfr=Dz=DUBUaw+DIhDgxYvNbbK3Pe3qD/QGADnqD=GFDK40o3CrtjB7DmYizOlwdYs7l3pqAozhYndE4H4B3DEx06NCWxYYzDt4DTD34DYDixibsxi5GRD0KDF8NVt/yDi3DbENDmLdDIT04xDdM8MQqxYQDGuIUD7jehuxD0uhi1GQPYuh4xGAUQnUQEMqW=0G9D0UexBdYUch9feH11GNWha9xsgQDzqODtqNYvdudGuXlKn44zED3e8GFiRGNbGe4C0o4CheY3RwN/7KRaGANi0xR1gzq9KDAW7KteD=',
#     'ssxmod_itna2': 'YqAx2DBDyD9D0Dfr=Dz=DUBUaw+DIhDgxYvNbbK3PeG98VGDBwG0x7PXM7OmCboM/nky65R0hkijxnWb7vxOKCDpxnN==7G2=Ym9Ec05XBR9LdGFKBG2GkwZQd=gcy7LG9=ubTMKjxeQG4BDxqQG+QExhHMmvxMPIQ3CT8iz9Fab9OXhqoNKE=YPOGqhwpgQemIrRWrFGqehS5q=DmH3aGyPp+QW57qlgiA4oxu79t69EiRjjYRiKLU8FTtwiurzPnr8BnyYSR1MjRh4fOfI16rbM9WX=f+F5UXHCUatVfbFykvP6mX=dEYNIxIP2dKpKw2Yq7LLgv32X/ipccedcPy6K3rEum0U7DK22NioKRQd2Nop03hPEC3474wBD5fLUebRCE3K+Mh2tWE=F2NFoi/TAmKsfY++Pnhw6YP3O59gnY+=yx0yGDbn4DQK4A4o+cer0boxxI0=BfqlSWGW7hu7ddqhDDFqD+gDxD==',
#     '_ga_S8P7R6WH5V': 'GS1.1.1743485969.2.0.1743486175.0.0.0',
# }
#
# headers = {
#     'Accept': '*/*',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/json',
#     'Origin': 'https://www.veer.com',
#     'Referer': 'https://www.veer.com/search-image/shouzhijia/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
#     'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     # 'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22195ef9e32471194-02a6cdc88409d52-4c657b58-1474560-195ef9e32483343%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%22195ef9e32471194-02a6cdc88409d52-4c657b58-1474560-195ef9e32483343%22%7D; sajssdk_2015_cross_new_user=1; _gid=GA1.2.66424947.1743481879; Hm_lvt_2663761a9226999365054376b04969e1=1743481878,1743485969; HMACCOUNT=4F01C978615D7DB2; acw_tc=1a0c660317434859706955284e004ad752bcddc543a1f44a10d1aa30fdfd8f; acw_sc__v2=67eb7c122c15ae8d5367e89d531781fc5ea4867a; queryKey=KEH2R4NQEN8; _ga_2TQ4PLYBNK=GS1.1.1743485969.2.1.1743486094.59.0.0; _ga=GA1.2.1788631146.1743481879; Hm_lpvt_2663761a9226999365054376b04969e1=1743486094; _fp_=eyJpcCI6IjIxOC4yMDAuMjI1LjE1OSIsImZwIjoiNTQzMDFlMzFkM2QyNWFhNTc0YTljMjYyNjcwNzA1MDgiLCJocyI6IiQyYSQwOCQubWJZN2ZrU0tHaEY5VHVzOU5URC8uWVk5eGNSSFNSMTNmTW9IWEc2ZC9HSU9WRTVFZEdIaSJ9; ssxmod_itna=YqAx2DBDyD9D0Dfr=Dz=DUBUaw+DIhDgxYvNbbK3Pe3qD/QGADnqD=GFDK40o3CrtjB7DmYizOlwdYs7l3pqAozhYndE4H4B3DEx06NCWxYYzDt4DTD34DYDixibsxi5GRD0KDF8NVt/yDi3DbENDmLdDIT04xDdM8MQqxYQDGuIUD7jehuxD0uhi1GQPYuh4xGAUQnUQEMqW=0G9D0UexBdYUch9feH11GNWha9xsgQDzqODtqNYvdudGuXlKn44zED3e8GFiRGNbGe4C0o4CheY3RwN/7KRaGANi0xR1gzq9KDAW7KteD=; ssxmod_itna2=YqAx2DBDyD9D0Dfr=Dz=DUBUaw+DIhDgxYvNbbK3PeG98VGDBwG0x7PXM7OmCboM/nky65R0hkijxnWb7vxOKCDpxnN==7G2=Ym9Ec05XBR9LdGFKBG2GkwZQd=gcy7LG9=ubTMKjxeQG4BDxqQG+QExhHMmvxMPIQ3CT8iz9Fab9OXhqoNKE=YPOGqhwpgQemIrRWrFGqehS5q=DmH3aGyPp+QW57qlgiA4oxu79t69EiRjjYRiKLU8FTtwiurzPnr8BnyYSR1MjRh4fOfI16rbM9WX=f+F5UXHCUatVfbFykvP6mX=dEYNIxIP2dKpKw2Yq7LLgv32X/ipccedcPy6K3rEum0U7DK22NioKRQd2Nop03hPEC3474wBD5fLUebRCE3K+Mh2tWE=F2NFoi/TAmKsfY++Pnhw6YP3O59gnY+=yx0yGDbn4DQK4A4o+cer0boxxI0=BfqlSWGW7hu7ddqhDDFqD+gDxD==; _ga_S8P7R6WH5V=GS1.1.1743485969.2.0.1743486175.0.0.0',
# }
#
# json_data = {
#     'page': 3,
#     'urlPhrase': 'shouzhijia',
#     'phrase': '手指甲',
#     'graphicalStyle': '',
#     'perpage': 100,
#     'key': 'KEH2R4NQEN8',
#     'page_type': 6,
#     'isGraphicalStyleChange': False,
#     'isPhraseChange': False,
#     'anonyUid': 'FN6B13C01ID9',
#     'favorid': '',
# }
#
# response = requests.post('https://www.veer.com/ajax/search', cookies=cookies, headers=headers, json=json_data)
#
# print(response.text)
# # Note: json_data will not be serialized by requests
# # exactly as it was in the original request.
# #data = '{"page":1,"urlPhrase":"shouzhijia","phrase":"手指甲","graphicalStyle":"","perpage":100,"key":"KEH2R4NQEN8","page_type":6,"isGraphicalStyleChange":false,"isPhraseChange":false,"anonyUid":"FN6B13C01ID9","favorid":""}'.encode()
# #response = requests.post('https://www.veer.com/ajax/search', cookies=cookies, headers=headers, data=data)