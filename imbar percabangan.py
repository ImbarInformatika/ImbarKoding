#percangan di python
umur = int(input("masukkan umur : "))

if umur >= 1 and umur <= 5 :
    print("usia balita")
elif umur >= 6 and umur <= 11 :
    print("usia anak anak")
elif umur >= 12 and umur <= 17 :
    print("usia remaja")
elif umur >= 18 and umur <= 29 :
    print("usia dewasa")
else :
    print("usia meranjak tua")
