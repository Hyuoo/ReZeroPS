ret = []
f = 0
buf = []
for s in input():
    if f or s == "<" or s == " ":
        if buf:
            ret.extend(buf[::-1])
            buf = []
        ret.append(s)
        if s in "<>":
            f ^= 1
    else:
        buf.append(s)
if buf:
    ret.extend(buf[::-1])
print("".join(ret))
