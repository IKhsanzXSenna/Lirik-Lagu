import turtle

# Buat layar
screen = turtle.Screen()
screen.title("Objek Bergerak Sederhana")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)  # Matikan animasi otomatis untuk kontrol manual

# Buat objek (lingkaran/ball)
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()  # Jangan gambar garis saat bergerak 
ball.goto(0, 0)  #Posisi awal di tengah 
ball.speed(0)  # Kecepatan maksimal

# Variabel untuk gerakan 
dx = 2 # Kecepatan horizontal (akan berubah arah saat memantul)
dy = 0 # kecepatan vertikal (untuk sekarang, gerak horizontal saja)

# Fungsi untuk update posisi
def update():
    # Hapus jejak lama
    screen.clear()

    # Update posisi
    x = ball.xcor() + dx
    y = ball.ycor() + dy

    # Cek batas layar dan pantulkan
    if x > 390: # Tepi kanan
        x = 390 
        dx = -dx
    elif x < -390: # Tepi kiri
        x = -390
        dx = -dx

    # Gerakan bola
    ball.goto(x, y)

    # Update layar
    screen.update()

    # Ulangi terus-menerus
    screen.ontimer(update, 10)  # Update seriap 10ms

# Mulai animasi
update()

# Tutup layar saat klik
screen.exitonclick() 