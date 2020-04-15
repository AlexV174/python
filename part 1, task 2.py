sec = int(input())
h = (sec // 3600) % 24
m = (sec % 3600) // 60
s = sec % 3600 % 60
if h < 10:
    h = '0'+str(h)
else:
    h = str(h)
if m < 10:
    m = '0'+str(m)
else:
    m = str(m)
if s < 10:
    s = '0'+str(s)
else:
    s = str(s)
print(f'{h}:{m}:{s}')