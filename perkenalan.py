# Program perkenalan tentang Python 3.13
# Kompatibel dengan Python 3.13.x
# Jalankan dengan Python 3.13 untuk hasil optimal

import sys

# Tampilkan versi Python
print(f"Selamat datang! Ini adalah perkenalan tentang Python {sys.version}")
print("=" * 50)

# Perkenalan singkat tentang Python 3.13
print("Python 3.13 adalah versi terbaru Python (dirilis Oktober 2024).")
print("Fitur baru yang menarik:")
print("- Peningkatan pesan error yang lebih jelas dan informatif.")
print("- Dukungan eksperimental untuk free-threaded build (untuk performa lebih baik tanpa GIL).")
print("- Optimasi kecepatan dan pengurangan ukuran bytecode.")
print("- Lebih banyak dukungan untuk type hints dan pattern matching yang lebih kuat.")
print("\nPython 3.13 membuat pengembangan lebih cepat dan mudah!")

# Interaksi sederhana
nama = input("\nSiapa nama kamu? ")
print(f"Halo, {nama}! Apakah kamu sudah mencoba Python 3.13?")
jawaban = input("Ya/Tidak? (tekan Enter untuk Ya): ").strip().lower()

if jawaban in ['tidak', 'no']:
    print("Coba install dari python.org dan jalankan kode ini! Kamu akan suka fitur barunya. 🚀")
else:
    print("Bagus! Python 3.13 punya banyak inovasi. Selamat belajar! 📚")

print("\nTerima kasih telah membaca perkenalan ini. Semoga bermanfaat! 😊")
