import math
import matplotlib.pyplot as plt

# Fungsi EOQ
def hitung_eoq(D, S, H):
    EOQ = math.sqrt((2 * D * S) / H)
    jumlah_pemesanan = D / EOQ
    total_biaya = (jumlah_pemesanan * S) + ((EOQ / 2) * H)
    return EOQ, jumlah_pemesanan, total_biaya

# Data penjualan ikan
permintaan_tahunan = 10000  # unit ikan per tahun
biaya_pemesanan = 250       # biaya pemesanan (Rp)
biaya_penyimpanan = 20      # biaya simpan per unit per tahun (Rp)

# Hitung EOQ dan hasil lainnya
EOQ, jumlah_pemesanan, total_biaya = hitung_eoq(permintaan_tahunan, biaya_pemesanan, biaya_penyimpanan)

# Simulasi berbagai jumlah Q
Q_values = range(100, 2000, 100)
biaya_total_list = []
biaya_pemesanan_list = []
biaya_penyimpanan_list = []

for Q in Q_values:
    biaya_pemesanan_total = (permintaan_tahunan / Q) * biaya_pemesanan
    biaya_penyimpanan_total = (Q / 2) * biaya_penyimpanan
    biaya_total = biaya_pemesanan_total + biaya_penyimpanan_total

    biaya_total_list.append(biaya_total)
    biaya_pemesanan_list.append(biaya_pemesanan_total)
    biaya_penyimpanan_list.append(biaya_penyimpanan_total)

# Plot grafik
plt.figure(figsize=(10, 6))
plt.plot(Q_values, biaya_total_list, label='Total Biaya Persediaan', color='blue', linewidth=2)
plt.plot(Q_values, biaya_pemesanan_list, label='Biaya Pemesanan', linestyle='--', color='green')
plt.plot(Q_values, biaya_penyimpanan_list, label='Biaya Penyimpanan', linestyle='--', color='red')
plt.axvline(x=EOQ, color='purple', linestyle=':', label=f'EOQ = {round(EOQ)} unit')

plt.title('Analisis EOQ - Penjualan Ikan')
plt.xlabel('Kuantitas Pemesanan per Kali (Q)')
plt.ylabel('Biaya (Rp)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Tampilkan hasil perhitungan
print(f"EOQ: {round(EOQ, 2)} unit")
print(f"Jumlah Pemesanan per Tahun: {round(jumlah_pemesanan, 2)} kali")
print(f"Total Biaya Persediaan: Rp {round(total_biaya, 2)}")
