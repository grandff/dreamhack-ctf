import base64

iv_encoded = "uBMsFKR8xsA="
data_encoded = "S%2FTdimLAvdw="

iv = base64.b64decode(iv_encoded)
data = base64.b64decode(data_encoded)

data_expected = b"guest\x03\x03\x03"
data_target = b"admin\x03\x03\x03"

intermediary = [iv[i] ^ data_expected[i] for i in range(8)]
changed_iv = [intermediary[i] ^ data_target[i] for i in range(8)]

print(base64.b64encode(bytes(changed_iv)))
# vgIkDr58xsA=
# vgIkDr58xsA=S%2FTdimLAvdw=