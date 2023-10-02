"""
Problem 1
Tuan Kil memiliki barang yang akan dijual dan sejumlah tabungan.
Tuan Kil ingin membeli sebuah barang baru dari tabungannya beserta barang yang akan dia jual.
Namun, barang yang dia miliki tersebut hanya akan dia jual jika dia tidak merugi dari modal yang dia keluarkan.
Bantulah Tuan Kil menentukan apakah dia dapat membeli barang yang dia inginkan atau tidak!    
"""

duit_beli = int(input("Masukkan harga beli barang yang akan dijual: "))
duit_jual = int(input("Masukkan harga jual barang yang akan dijual: "))
duit_barang = int(input("Masukkan harga barang yang ingin dibeli: "))
tabungan = int(input("Masukkan tabungan Tuan Kil: "))

profit = duit_jual - duit_beli

# kalau untung
if (profit >= 0):
    tabungan = tabungan + duit_jual

if (duit_barang <= tabungan):
    print("Tuan Kil dapat membeli barang yang diinginkan.")
else:
    print("Tuan Kil tidak dapat membeli yang diinginkan.")
