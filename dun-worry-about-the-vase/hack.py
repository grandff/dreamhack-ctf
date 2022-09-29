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