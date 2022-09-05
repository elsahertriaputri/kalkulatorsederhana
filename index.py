#membuat fungsi-fungsi untuk setiap operasi bilangan
def jumlah(bil1, bil2):
    penjumlahan = bil1 + bil2
    print('Hasil dari', bil1, '+', bil2, '=', penjumlahan)
    return penjumlahan

def kurang(bil1, bil2):
    pengurangan = bil1 - bil2
    print('Hasil dari', bil1, '-', bil2, '=', pengurangan)
    return pengurangan

def kali(bil1, bil2):
    perkalian = bil1 * bil2
    print('Hasil dari', bil1, '*', bil2, '=', perkalian)
    return perkalian

def bagi(bil1, bil2):
    pembagian = bil1 / bil2
    print('Hasil dari', bil1, '/', bil2, '=', pembagian)
    return pembagian

def kalkulator():
        #perulangan untuk meminta pengguna memasukan ketentuan perhitungan
        while True:

            #input operasi bilangan
            operasi = input('Pilih +, -, *, atau / ? ')

            #memastikan agar pengguna memasukkan operasi bilangan yang tepat
            if operasi == '+' or operasi == '-'\
               or operasi == '*' or operasi == '/':
                pass
            else:
                print('Error')
                continue

            #memastikan pengguna memasukan bilangan untuk variabel bil1
            while True:
                try:
                    bil1 = float(input('Masukkan bilangan pertama: '))
                    while True:
                        try:
                            bil2 = float(input('Masukkan bilangan kedua: '))
                            break
                        except ValueError:
                            print('Error')
                            continue
                except ValueError:
                    print('Error')
                    continue

                #kondisi percabangan untuk menentukan fungsi yang sesuai dengan permintaan operasi bilangan dari pengguna
                if operasi == '+':
                    jumlah(bil1, bil2)
                elif operasi == '-':
                    kurang(bil1, bil2)
                elif operasi == '*':
                    kali(bil1, bil2)
                else:
                    bagi(bil1, bil2)
                break

            ulang = input('Apakah Anda ingin menghitung kembali (y/n)? ')
            ulangi = ulang.lower()
            if ulangi == 'y':
                continue
            elif ulangi == 'n':
                print('Terima kasih telah menggunakan kalkulator sederhana!')
                break
            else:
                print('Error')
                break

kalkulator()