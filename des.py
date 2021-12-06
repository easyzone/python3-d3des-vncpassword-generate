from d3des import * 

def vnc_encode(password):
    passpadd = (password + '\x00'*8)[:8]
    strkey = ''.join([ chr(x) for x in vnckey ])
    ekey = deskey(bytearray(strkey, encoding="ascii"), False)
    #return desfunc(bytearray(passpadd, encoding="ascii"), ekey)
    return desfunc(bytearray(passpadd, encoding="ascii"), ekey)


pwd = vnc_encode('123456')
print(pwd.hex())
print(pwd)


my_bytes = pwd.encode('utf-8')


print(my_bytes)    