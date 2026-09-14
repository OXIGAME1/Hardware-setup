a = 0b10101010   
b = 0b11001100   
c = 0b11110000   
mask = 0xFF      

print("a =", bin(a), "=", a)
print("b =", bin(b), "=", b)
print("c =", bin(c), "=", c)
print()

print("a & b =", bin(a & b), "=", a & b)
print("a | b =", bin(a | b), "=", a | b)
print("a ^ b =", bin(a ^ b), "=", a ^ b)
print("~a =", bin(~a & mask), "=", ~a & mask)
print()

print("a << 2 =", bin(a << 2), "=", a << 2)
print("a >> 2 =", bin(a >> 2), "=", a >> 2)
print()

print("0x69 & 0x55 =", hex(0x69 & 0x55))
print("0x69 | 0x55 =", hex(0x69 | 0x55))
print("~0x41 =", hex(~0x41 & 0xFF))