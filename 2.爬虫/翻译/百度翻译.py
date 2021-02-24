# -*- coding:utf-8 -*-
import execjs
import requests
import json

def get_js_file(file):
    js_data = ''
    with open(file,'r') as f:
        js_data = f.read()
    return js_data
def get_js_data(js_data,method,*ags):
    return execjs.compile(js_data).call(method,*ags)


if __name__ == '__main__':
    flag = input('请输入中转英还是英转中--（中转英输入0，反之输入1）')
    query = input('请输入需要翻译的内容：')
    js_data = get_js_file('baidu.js')
    url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'Cookie' : 'BIDUPSID=0A33C475750E5684EC63E1F1975F1641; PSTM=1608869547; BAIDUID=0A33C475750E56848BDB1E0A4B137AF6:FG=1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; __yjs_duid=1_e3153986928b42b4cfcae1311a0ed0db1611493820577; BDSFRCVID_BFESS=wbPOJexroG3VKNbeBxRdudQ1VgKK0gOTDYLEiUd8QknPKv_Vg8XyEG0PtfO2fMtb7JsDogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJ48_CLMfC_3fP36q4rMM-LthfLX5-RLf5vBah7F54nKDp0R0nj5hRDsDpjULTcOabcaslvxQC3xsMTsQj8hqq48QR_ey-rJQeoOW4JN3KJmfbQaLTrP5-D35pbK2-biWbRM2MbdJqvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhhCGe6KBejO-eH-tqbbfb-oXXPt8Kb7VKROkenJD0M4pbq7H2M-eQe3w3J5PMUoffJbhDqjJyUnQbPnn0pcr3C5P0Inl2brmOPQ334tWWbFkQN3T-P59tDcuLn_5WtOUDn3oyT3JXp0nj4Rly5jtMgOBBJ0yQ4b4OR5JjxonDh83bG7MJUutfD7H3KCaJK0aMx2; H_PS_PSSID=33423_33582_33261_33272_33461_33392_33460_33320; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1612948727,1613046047,1613823756,1613836194; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1613836783; ab_sr=1.0.0_ZGNhZGU5YWRlYzJjMzZjODFlM2NjMWNjYTI1YjM1MzVhOThkYTgxODkyN2JiNjNkNzNjNzBhOWJkZGQxOWZiZGY2NGE4MzQ4ZjVkNTY0MGVkNzZhYjNmYmU0ZGRhNzE1; delPer=0; PSINO=7; BA_HECTOR=8l8ka0a40k8l20a4n21g32qnf0q; BAIDUID_BFESS=54FFC7394B8CDD7142F1DD0238C61F09:FG=1',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047'
    }
    data = {
        'from': 'zh' if flag=='0' else 'en',
        'to': 'en' if flag=='1' else 'zh',
        'query': query,
        'transtype': 'translang',
        'simple_means_flag': '3',
        'sign': get_js_data(js_data,'e',query),
        'token': '7c0df539955fc97b85d003f4e6287090',
        'domain': 'common'
    }
    # print(data)
    response = requests.post(url,data=data,headers=headers).json()
    print(response['trans_result']['data'][0]['result'][0][1])
    # print(response['trans_result']['data']['0']['dst'])




