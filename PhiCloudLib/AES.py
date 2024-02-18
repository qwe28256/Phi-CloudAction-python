# 萌新写的代码喵，可能不是很好喵，但是已经尽可能注释了喵，希望各位大佬谅解喵=v=
# ----------------------- 导包区 -----------------------
from Crypto.Cipher.AES import new, MODE_CBC, block_size
from Crypto.Util.Padding import unpad, pad
from base64 import b64decode

# ---------------------- 定义赋值区 ----------------------

aes_key = b64decode('6Jaa0qVAJZuXkZCLiOa/Ax5tIZVu+taKUN1V1nqwkks=')
aes_iv = b64decode('Kk/wisgNYwcAV8WVGMgyUw==')


def decrypt(data: bytes):
    """AES CBC解密\n
    data：要解密的数据"""
    data = new(aes_key, MODE_CBC, aes_iv).decrypt(data)
    return unpad(data, block_size)


def encrypt(data: bytes):
    """AES CBC加密\n
    data：要加密的数据"""
    data = pad(data, block_size)
    return new(aes_key, MODE_CBC, aes_iv).encrypt(data)
