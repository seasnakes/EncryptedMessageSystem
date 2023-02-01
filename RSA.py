import rsa
import base64

# 生成密钥
(pubkey, privkey) = rsa.newkeys(1024)

# 保存密钥
with open('public.pem', 'w+') as f:
    f.write(pubkey.save_pkcs1().decode())
with open('private.pem', 'w+') as f:
    f.write(privkey.save_pkcs1().decode())


# 私钥签名
def sign(message):
    with open('private.pem', 'r') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

        signature = rsa.sign(message.encode(), privkey, 'SHA-1')
        signature = base64.b64encode(signature)
        print("生成的签名:")
        print(signature)
        return signature


# 公钥验证
def Verify(message, signature):
    with open('public.pem', 'r') as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
        signature = base64.b64decode(signature)

        v = rsa.verify(message.encode(), signature, pubkey)
        print("验签结果:")
        print(v)
        return v
        
