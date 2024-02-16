# multikeys and nested dictionary
import datetime
print("\n=== Multikeys & Nested Dictionary ===")

mahasiswa1 = {
    'nama': 'andhieka',
    'nim': '15860031',
    'sks_lulus': '130',
    'beasiswa': False,
    'lahir': datetime.datetime(1999, 4, 13)
}

mahasiswa2 = {
    'nama': 'otong',
    'nim': '15860032',
    'sks_lulus': '140',
    'beasiswa': True,
    'lahir': datetime.datetime(1998, 11, 14)
}

mahasiswa3 = {
    'nama': 'asep',
    'nim': '15860033',
    'sks_lulus': '100',
    'beasiswa': False,
    'lahir': datetime.datetime(2000, 2, 29)
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3,

}

print(F"{'KEY':<6} {'Nama':<17} {'NIM':<6} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':<10}")
print('_'*55)

for mahasiswa in data_mahasiswa:

    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')

    print(F"{KEY:<6} {NAMA:<17} {NIM:<1}  {SKS:<6} {BEASISWA:^9} {LAHIR:<10}")
