menu = {
    "Nasi goreng" : 15000,
    "Nasi uduk": 17000,
    "Nasi liweut" : 15000,
    "Mie goreng" : 10000,
    "Mie kuah" : 9000,
    "Lemon tea" : 5000,
    "Kopi susu" : 7000,
    "Kopi hitam" : 5000,
    "Jus stroberi" : 10000,
    "Jus alpukat" : 10000
}

def bayar(jumlah=0,beli=0) :
    return jumlah*menu[beli]



