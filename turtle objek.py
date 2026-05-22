import turtle  # Import library turtle

# Setup layar
screen = turtle.Screen()
screen.title("Objek Bergerak dengan Turtle")
screen.bgcolor("lightblue")  # Warna latar belakang
screen.setup(width=800, height=600)  # Ukuran layar
screen.tracer(0)  # Matikan auto-update untuk animasi halus (kita update manual)

# Buat objek (turtle berbentuk lingkaran)
bola = turtle.Turtle()
bola.shape("circle")  # Bentuk lingkaran (seperti bola)
bola.color("red")  # Warna merah
bola.penup()  # Jangan gambar garis saat bergerak
bola.goto(-350, 0)  # Posisi awal di kiri tengah
bola.speed(0)  # Kecepatan maksimal (untuk animasi)

# Variabel untuk gerakan
posisi_x = -350  # Posisi awal X
arah = 1  # 1 untuk ke kanan, -1 untuk ke kiri
kecepatan = 5  # Kecepatan gerak per frame

# Fungsi untuk update posisi (animasi)
def update_posisi():
    global posisi_x, arah
    
    # Update posisi
    posisi_x += kecepatan * arah
    
    # Cek batas layar (lebar layar sekitar 800, jadi batas -400 sampai 350)
    if posisi_x >= 350:
        arah = -1  # Balik ke kiri
    elif posisi_x <= -350:
        arah = 1  # Balik ke kanan
    
    # Pindahkan bola ke posisi baru
    bola.goto(posisi_x, 0)
    
    # Update layar dan jadwalkan frame berikutnya
    screen.update()
    screen.ontimer(update_posisi, 50)  # Delay 50ms per frame (20 FPS)

# Mulai animasi
update_posisi()

# Tutup layar saat klik
screen.exitonclick()
