from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64
# 由于MD5模块在python3中被移除
# 在python3中使用hashlib模块进行md5操作
import hashlib


def rsa_encode(data, public_key):
    cipher = PKCS1_v1_5.new(public_key)
    encoded_data = cipher.encrypt(data.encode('utf-8'))
    encoded_data = base64.b64encode(encoded_data).decode('utf-8')
    return encoded_data


# 使用示例
pub = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgWHCTjYTz4r8+shMiGKZKNnqYMSxeZQBQpONez3KXDlTNqwabwA1SVrDzeMofoACg+phknVQQFV0CtXdExcVwPhcTvp1E4estHjgK7yrJKiYD50FGM75b3mO+G8wA18dEvFuOFGZY/zyGr2IPaVPDsceCRP51UNtNjp6z7tiQ/F5iBqUZziTJy6pjlJ5qdyXQg/ZunziPjW1UpW4e0oW9QElGA2CmfkfVt97g6DlrsUW0+/STDNeVwtVXlNYNmR08t6b626UgY7nB80TfNTxiYKxd7CeW0itLZHSEJrYDgWK5haOKVkQ1BeMkprZ4j3wpFHC55gKwFiBoJVWlMOhawIDAQAB"
pub_key = "-----BEGIN RSA PUBLIC KEY-----\n" + \
    pub + "\n-----END RSA PUBLIC KEY-----"
public_key = RSA.import_key(pub_key)
data = '12345'
# 创建md5对象
hl = hashlib.md5()
# 更新hash对象的值，如果不使用update方法也可以直接md5构造函数内填写
hl.update(data.encode("utf-8"))
print('MD5加密前为 ：' + data)
print('MD5加密后为 ：' + hl.hexdigest())
encoded_data = rsa_encode(hl.hexdigest(), public_key)
print('rsa加密后为 ：' + encoded_data)
