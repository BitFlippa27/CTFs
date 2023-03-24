from pwn import *

context_log_level = "debug"

p = remote("165.232.100.46", 31713)

p.sendlineafter(b"> ", b"1")

while True:
    line = p.recvline().decode()
    print(line)
    if "]:" in line:
        line =  line.split(":")[-1][:-4].strip()
        print(line)
        try:
            foo = round(eval(line),2)
            print(foo)
            if foo >= -1337 and foo <= 1337:
                p.sendlineafter(b"> ", str(foo).encode()) 
            else:
                p.sendlineafter(b"> ", b"MEM_ERR") 
        except ZeroDivisionError:
            p.sendlineafter(b"> ", b"DIV0_ERR")
        except SyntaxError:
            p.sendlineafter(b"> ", b"SYNTAX_ERR")

       

