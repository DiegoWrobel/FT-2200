#import binascii
comando = '0000000008'
print(comando)
cmd_bytes = bytearray.fromhex(comando)
print(cmd_bytes)