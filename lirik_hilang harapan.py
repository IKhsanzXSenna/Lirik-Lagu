import sys
import time


def jalanin_lirik () :
        lirik = [
            ("Hilang harapan", 0.1),
            ("Saat kau katakan semua telah usai", 0.09),
            ("Kau menemukan", 0.09),
            ("Yang baru kini aku kau tinggalkan", 0.09),
            ("Meski sendiri aku 'kan bertahan", 0.09),
            ("Memegang janji yang kita ucapkan", 0.09),
            ("Berat rasanya hatiku berkata", 0.09),
            ("Semoga bahagia engkau dengannya", 0.09),
            ("Selama mataku bisa menatap", 0.09),
            ("Kukenang kau sebagai memori kelam", 0.09),
            ("Ingin rasanya hatiku berkata", 0.09),
            ("Ingat janji dulu kita bersama", 0.09),
        ]
        delay = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
        print("\n==Hilang Harapan - Stand Here Alone==")
        time.sleep(2)
        for i, (baris_lagu, delay_karakter) in enumerate(lirik):
            for karakter in baris_lagu :
                print(karakter, end='')
                sys.stdout.flush()
                time.sleep(delay_karakter)
            time.sleep(delay[i])
            print('')  
        print("// Code by Ikhsan")

jalanin_lirik()
