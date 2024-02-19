
s#Input

Gaji = int(input("Gaji perjam yang anda inginkan: "))
JamKerja = int(input("Jam kerja selama seminggu : "))

#Proses

print()
GajiSeminggu = Gaji * JamKerja
LamaKerja = 5
PajakPenghasilan = 0.14
Baju = 0.1
AlatTulis = 0.01
PersenSedekah = 0.25

TanpaPajak = GajiSeminggu * LamaKerja
SetelahPajak = TanpaPajak - (TanpaPajak * PajakPenghasilan)
HargaBaju = SetelahPajak * Baju
SetelahBaju = SetelahPajak - HargaBaju
AlatTulis = SetelahPajak * AlatTulis
SetelahAT = SetelahBaju - AlatTulis
Sedekah = SetelahAT * PersenSedekah
AnakYatim = Sedekah // 1000 * 1000 * 0.3
Dhuafa = Sedekah - AnakYatim

#Output

print("Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak", TanpaPajak, "Rupiah.")
print("Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak adalah", SetelahPajak, "Rupiah.")
print("Uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris adalah", HargaBaju, "Rupiah.")
print("uang yang akan Budi habiskan untuk membeli alat tulis adalah", AlatTulis, "Rupiah.")
print("Uang yang Budi sedekahkan totalnya ada", Sedekah, "Rupiah.")
print("uang yang akan diterima anak yatim sejumlah", AnakYatim, "Rupiah.")
print("uang yang akan diterima kaum dhuafa sejumlah", Dhuafa, "Rupiah.")

