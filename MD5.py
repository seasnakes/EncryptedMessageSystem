from hashlib import md5, sha1, sha224, sha256, sha384, sha512

hash_md5 = md5()  # MD5 hash对象
hash_sha1 = sha1()  # SHA1 hash对象
hash_sha224 = sha224()  # SHA224 hash对象
hash_sha256 = sha256()  # SHA256 hash对象
hash_sha384 = sha384()  # SHA384 hash对象
hash_sha512 = sha512()  # SHA512 hash对象



def md5(str):

    print('将要生成摘要的字符串:', str)

    # MD5 加密
    h_md5 = hash_md5.copy()  # 复制一个对象，避免频繁创建对象消耗性能
    h_md5.update(str.encode('utf-8'))  # 需要将字符串进行编码，编码成二进制数据
    md5_str = h_md5.hexdigest()  # 获取16进制的摘要
    print('MD5生成摘要结果:',md5_str)  # 输出结果
    return md5_str

