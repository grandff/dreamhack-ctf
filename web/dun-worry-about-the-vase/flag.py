from urllib.parse import quote, unquote
import base64
import binascii
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from collections import OrderedDict
import requests

# variable init
url = ""
headers = {}
params = {}
data = {}
s = requests.Session()

# url settings
scheme = "http"
url = f'{scheme}://host3.dreamhack.games:20565/main.php'

# headers setting
headers = OrderedDict()
headers['Connection'] = 'keep-alive'
headers['Cache-Control'] = 'max-age=0'
headers['Upgrade-Insecure-Requests'] = '1'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
headers['Accept-Encoding'] = 'gzip, deflate'
headers['Accept-Language'] = 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
# 쿠키변조
headers['Cookie'] = 'L0g1n=vgIkDr58xsA%3DS%2FTdimLAvdw%3D;'

# param settings
params = OrderedDict()

# data settings
data = OrderedDict()

# send packet
r = s.get(url, headers=headers, params=params, data=data, verify=False)
print(r.text)