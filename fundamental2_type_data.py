print ('TIPE  DATA SKALAR => TIPE DATA SEDERHANA')
anak1 = 'eko'
anak2 = 'dwi'
anak3 = 'tri'
anak4 = 'fur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\nTIPE DATA LIST/daftar/array')
anak = ['eko', 'dwi', 'tri', 'fur']
print(anak)
anak.append('limo')
print(anak)

print('\nSAPA ANAK KE-2')
print(f'hai {anak[1]}!')

print('\nsapa semua anak')
for a in anak:
    print(f'hai {a}!')

print('\nsapa semua anak cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. hai {anak[a]} !!!!! hehehe')