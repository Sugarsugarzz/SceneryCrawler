import requests

url = 'http://www.dianping.com/ajax/member/checkin/checkinList'
data = {
    'memberId': '1897964',
    'page': '2'
}
headers = {
    'Cookie': '_lxsdk_cuid=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _lxsdk=1756254e31dc8-0dbb2f5b84c02a-31687304-1aeaa0-1756254e31dc8; _hc.v=a497ceb2-53d2-fcc1-b83f-acb8e5671083.1603672532; s_ViewType=10; ctu=5fecefa74ea59558a4d9dddd24fb293b8f9710fb8079edab2e1f02e28d5987bd; aburl=1; cityid=2; baidusearch_ab=citybranch%3AA%3A1%7Cindex%3AA%3A1; switchcityflashtoast=1; source=m_browser_test_33; seouser_ab=shop%3AA%3A1%7Cindex%3AA%3A1; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1603678545,1603716657,1603884877,1603885103; fspop=test; dper=de0737b36330e4ebe65a08979b56c834b9020731acf79d6aae685c0bbefeca5bc4205bf71d4f5a33c35d70527104c462df39847a925a9ee6747233fae317b45843f66dee209f0d3adc800e3649c5ea26a29bead0cc8dcd8a5dc28d09f2d61c40; ll=7fd06e815b796be3df069dec7836c3df; ua=13001230577; cy=2; cye=beijing; dplet=d287b71f69703f1693ceeabcf334ea07; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1604304985; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=175877db0d2-41d-944-e0e%7C%7C1376',
    'Origin': 'http://www.dianping.com',
    'Referer': 'http://www.dianping.com/',
}
print(data)
response = requests.request("POST", url, headers=headers, data=data)

print(response.text.encode('utf8'))