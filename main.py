print("\n========KALKULATOR MODIFIKASI========\n")

select = input("silakan pilih operasi kalkulator anda\noperasi aritmatika atau operasi logika boolean\t: ").lower().strip()

if select == "operasi aritmatika":
    pilih = input("pilih operator anda\n(+, -, *, /, **, %, //)\t: ").strip()
    # tambah, kurang, kali, bagi, pangkat, modulus, floor division.
    angka1 = int(input("\nmasukan angka\t\t: "))
    angka2 = int(input("masukan angka\t\t: "))

    if pilih == "+":
        hasil = angka1 + angka2
        print("hasil dari ", angka1, "+", angka2, "=", hasil)
    elif pilih == "-":
        hasil = angka1 - angka2
        print("hasil dari ", angka1, "-", angka2, "=", hasil)
    elif pilih == "*":
        hasil = angka1 * angka2
        print("hasil dari ", angka1, "*", angka2, "=", hasil)
    elif pilih == "/":
        hasil = angka1 / angka2
        print("hasil dari ", angka1, "/", angka2, "=", hasil)
    elif pilih == "**":
        hasil = angka1 ** angka2
        print("hasil dari ", angka1, "**", angka2, "=", hasil)
    elif pilih == "%":
        hasil = angka1 % angka2
        print("hasil dari ", angka1, "%", angka2, "=", hasil)
    elif pilih == "//":
        hasil = angka1 // angka2
        print("hasil dari ", angka1, "//", angka2, "=", hasil)
    else:
        print("mohon masukan data dengan tepat !")


elif select == "operasi logika boolean":
    pilih = input("pilih operator anda\n(or, and, xor, not)\t: ").lower().strip()
    
    sub1 = input("masukan pilihan pertama (True/False)\t: ").strip()
    subject1 = sub1.lower() == "true"
    
    if pilih == "not":
        hasil = not subject1
        print(f"hasil dari not {sub1} = {hasil}")
    elif pilih in ["or", "and", "xor"]:
        sub2 = input("masukan pilihan kedua (True/False)\t: ").strip()
        subject2 = sub2.lower() == "true"
        
        if pilih == "or":
            hasil = subject1 or subject2
            print(f"hasil dari {sub1} or {sub2} = {hasil}")
        elif pilih == "and":
            hasil = subject1 and subject2
            print(f"hasil dari {sub1} and {sub2} = {hasil}")
        elif pilih == "xor":
            hasil = subject1 ^ subject2 
            print(f"hasil dari {sub1} xor {sub2} = {hasil}")
    else:
        print("mohon masukan operator dengan tepat !")

else:
    print("Pilihan operasi tidak valid!")

print("\nFinish")
