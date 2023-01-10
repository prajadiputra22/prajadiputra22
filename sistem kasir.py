from FUNGSI import*

print('='*15, 'DAFTAR MENU', '='*15)
for i in menu:
    print(i, '\t :', menu[i])

while True :
    beli = input('\nPilih menu : ')
    jumlah = int(input('Jumlah : '))
    total = bayar(jumlah,beli)

    nota = open("nota.txt", "w")
    nota.write("\n===== NOTA PEMBAYARAN =====\n")
    nota.write("Nama Barang: " + beli + "\n")
    nota.write("Harga: Rp" + str(menu[beli]) + "\n")
    nota.write("Jumlah: " + str(jumlah) + "\n")
    nota.write("Total: Rp" + str(total) + "\n")

    nota = open("nota.txt", "r")
    for i in nota :
        print(i)
    nota.close()
    
    tanya = input('Mau pilih lagi? y/n : ')
    if tanya == 'n' :
        print('Terimakasih sudah berbelanja')
        break

