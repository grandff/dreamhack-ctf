# L0g1n=cf0ko0KOK2U%3DskHLGTBeqPg%3D
# cf0ko0KOK2U=
# skHLGTBeqPg=

# 끝이 =로 끝나고 base64로 인코딩 되어서 두분으로 나눠져 있음
# base64 인코딩 기준이 머임...?
# 해당문제에서는 앞에꺼가 IV고, 뒤에꺼가 암호문 블록1임


from urllib.parse import quote, unquote
import base64
import binascii
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from collections import OrderedDict
import requests

# 페이로드 전송
def send_payload(s, payload) :
    # variable init
    url = ""
    headers = {}
    params = {}
    data = {}
    
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
    headers['Cookie'] = f'L0g1n={payload};'
    
    # param settings
    params = OrderedDict()
    
    # data settings
    data = OrderedDict()
    
    # send packet
    r = s.get(url, headers=headers, params=params, data=data, verify=False)
    return r.text

# xor 함수
def xor(data, key) :
    output = bytearray()
    for i, ch in enumerate(data) :  # 인덱스와 값 형태로 나눠줌
        output.append(ch ^ key[i % len(key)])
    return bytes(output)    # bytes형태로 리턴

# cookie 생성하는 함수
def make_cookie(iv, enc) :
    return quote(base64.b64encode(iv)) + quote(base64.b64encode(enc))

# hex로 변환해주는 함수
# 00 00 00 00 00 00 00 00 <- 형태로 보고 쉽게 표현
def hex_view(data) :
    temp = data.hex()   # temp = data를 hex로 변환
    ret = ""
    for i in range(0, len(temp), 2) :   # range(0, len(temp), 2) <- 0부터 temp길이만큼 2개씩
        ret += temp[i:i+2] + " "
    return ret  # ret 에다가 2개씩 잘라 넣고 return

# 초기값설정
cookie = "cf0ko0KOK2U%3DskHLGTBeqPg%3D"
iv = base64.b64decode(unquote("cf0ko0KOK2U%3D"))
enc = base64.b64decode(unquote("skHLGTBeqPg%3D"))
inter = b'' # 암호화 중간값으로 byte 형태로 비워둠
s = requests.Session()

# 현재 IV와 ENC 출력
print(f"IV => {hex_view(iv)}")
print(f"ENC => {hex_view(enc)}")

# iv 생성 1~iv길이 +1 까지
for i in range(1, len(iv) + 1):
    # iv 시작점 지정 / 1일 경우 맨앞에서부터 뒤에 1글자 빼고 2일 경우 뒤 2글자 빼고..
    start = iv[:len(iv)-1]
    for j in range(0, 0xff+1) :
        # target = start + (0x00 ~ 0xff 중 1개) + xor(inter 뒤집은거 , i)
        target = start + bytes([j]) + xor(inter[::-1], bytes([i]))
        cookie = make_cookie(target,enc)
        res = send_payload(s, cookie)
        print(hex_view(target), "->", cookie)
        print(res)
        if 'padding error' not in res:
            break
        
    # padding error 가 안뜨면 정상이므로 구한 값 j와 현재 패딩값 중 하나를 xor해서 inter 파악
    inter += bytes([i ^ j])    
    # inter는 뒤부터 구하는 거라서 뒤집어서 다시 구함
    print(hex_view(inter[::-1]))

# 다 구해진 인터를 뒤집어서 리얼 인터로 만듬
inter = inter[::-1]    
plain = xor(inter ,iv)  # iv와 inter를 xor해서 plain 구함
print(plain)

mod = b"admin\x03\x03\x03"
print(make_cookie(mod, enc))