# Program cek umur dengan kondisi
umur = int(input("Masukkan umur: "))

if umur >= 60:
    print("Kamu sudah lanjut usia ")
elif umur >= 17:
    print("Kamu sudah dewasa, boleh bikin KTP ")
elif umur >= 13:
    print("Kamu masih remaja ")
else:
    print("Kamu masih anak-anak ")