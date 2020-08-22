"""
TIPE DATA DICTIONARY MENGHUBUNGKAN ANTARA KEY DAN VALUE
KVP = KEY VALUE PAIR
DICTIONAY = KAMUS
"""

kamu_ind_eng = {'anak': 'son', 'ayah': 'father', 'ibu': 'mother', 'istri': 'wife'}

print(kamu_ind_eng)
print(kamu_ind_eng['ayah'])
print(kamu_ind_eng['ibu'])
print(kamu_ind_eng['anak'])

print('data ini dikirimkan oleh server gojek,untuk memberikan info disekitar pemakai aplikasi')

data_dari_server_gojek = {
    'tanggal': '2020-8-22',
    'driver_list': [{'nama': 'eko', 'jarak': 5}, {'nama': 'dwi', 'jarak': 10}, {'nama': 'tri', 'jarak': 15},
                    {'nama': 'fur', 'jarak': 100}]

}

print(data_dari_server_gojek)
print(f"driver sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"driver #3 {data_dari_server_gojek['driver_list'][2]}")
print(f"jarak driver terdekat #1 {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
