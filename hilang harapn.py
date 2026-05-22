import sys
import time


def jalanin_lirik () :
        lirik = [
            ("Sebelum gelap kita tertawa", 0.1),
            ("Berjanji setia sampai ujung masa", 0.09),
            ("Meski kau dan aku jauh di sana", 0.09),
            ("Ingat janji kita untuk selamanya", 0.09),
            ("Hilang harapan", 0.07),
            ("Saat kau katakan semua telah usai", 0.09),
            ("Kau menemukan", 0.11),
            ("Yang baru kini aku kau tinggalkan", 0.09),
            ("Meski sendiri aku 'kan bertahan", 0.07),
            ("Memegang janji yang kita ucapkan", 0.09),
            ("Berat rasanya hatiku berkata", 0.09),
            ("Semoga bahagia engkau dengannya", 0.09),
        ]
        delay = [0.3, 0.3, 0.3, 2.4, 0.7, 1.4, 0.3, 0.3, 0.3, 0.8, 0.3, 0.3]
        print("\n==Hilang Harapan - Stand Here Alone==")
        time.sleep(2)
        for i, (baris_lagu, delay_karakter) in enumerate(lirik):
            for karakter in baris_lagu :
                print(karakter, end='')
                sys.stdout.flush()
                time.sleep(delay_karakter)
            time.sleep(delay[i])
            print('')
        print("// Code by Ikhsan Kopi Tubruk")
    
jalanin_lirik()
