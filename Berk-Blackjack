import random
import time

global_kart_destesi = []
oyuncu_kartlari = []
dealer_kartlari = []
oyuncu_kartlari_toplam = []
dealer_kartlari_toplam = []
kart_cesidi = ["Kupa", "Karo", "Sinek", "Maça"]
kart_degerleri_dic= {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,"J":10,"Q":10,"K":10,"A":1}
kart_degerleri = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
oyuncu_adi = input("Merhaba!Lütfen oyuna başlamadan önce isminizi giriniz:")
time.sleep(1)
print("Hoşgeldin", oyuncu_adi)
time.sleep(1)
print("Oyun oluşturuluyor...")
time.sleep(3)
print("Oyun oluşturuldu!")
time.sleep(2)


class Oyuncu :


    def kart_cekme_oyuncu(self):
        time.sleep(1)
        print("Kartınız dağıtılıyor,lütfen bekleyiniz...")
        time.sleep(3)
        kart_l_oyuncu_cesid = random.choice(kart_cesidi)
        kart_l_oyuncu_deger = random.choice(kart_degerleri)
        kart_oyuncu_1 = (kart_l_oyuncu_cesid,kart_l_oyuncu_deger)
        if kart_oyuncu_1 in global_kart_destesi :
            kart_l_oyuncu_cesid = random.choice(kart_cesidi)
            kart_l_oyuncu_deger = random.choice(kart_degerleri)
            kart_oyuncu_1 = (kart_l_oyuncu_cesid,kart_l_oyuncu_deger)
        oyuncu_kartlari.append(kart_oyuncu_1)
        global_kart_destesi.append(kart_oyuncu_1)
        print("Çektiğiniz kartınız:",kart_oyuncu_1)
class Dealer :


    def kart_cekme_dealer(self):
        time.sleep(1)
        print("Dağıtıcı kart çekiyor,lütfen bekleyiniz...")
        time.sleep(3)
        kart_1_dealer_cesid = random.choice(kart_cesidi)
        kart_1_dealer_deger = random.choice(kart_degerleri)
        kart_dealer_1 = (kart_1_dealer_cesid,kart_1_dealer_deger)
        if kart_dealer_1 in global_kart_destesi :
            kart_1_dealer_cesid = random.choice(kart_cesidi)
            kart_1_dealer_deger = random.choice(kart_degerleri)
            kart_dealer_1 = (kart_1_dealer_cesid,kart_1_dealer_deger)
        dealer_kartlari.append(kart_dealer_1)
        global_kart_destesi.append(kart_dealer_1)
        print("Dağıtıcı kartını çekti!")


#Round başlangıcı


oyuncu_para = int(input("Oyun boyunca oynamak istediğiniz para miktarını giriniz:"))
time.sleep(2)
while oyuncu_para > 0 :


    oyuncu_bahis = int(input("Oynamak istediğiniz bahis miktarını giriniz:"))
    time.sleep(2)
    oyuncu_bahis_kat = float(input("Oynamak istediğiniz bahis katını giriniz(1.5/2/2.5/3/3.5/4/4.5/5/10):"))


    Oyuncu.kart_cekme_oyuncu(oyuncu_adi)
    time.sleep(1.5)
    Dealer.kart_cekme_dealer(oyuncu_adi)
    time.sleep(1.5)
    Oyuncu.kart_cekme_oyuncu(oyuncu_adi)
    time.sleep(1.5)
    Dealer.kart_cekme_dealer(oyuncu_adi)
    time.sleep(1.5)
    print("Dağıtıcı kartlarını kontrol ediyor...")
    time.sleep(2)
    for x,y in dealer_kartlari :
        dealer_kartlari_toplam.append(kart_degerleri_dic[str(y)])
    if sum(dealer_kartlari_toplam) < 16 :
        kart_1_cekilen_dealer_cesid = random.choice(kart_cesidi)
        kart_1_cekilen_dealer_deger = random.choice(kart_degerleri)
        kart_dealer_1_cekilen = (kart_1_cekilen_dealer_cesid,kart_1_cekilen_dealer_deger)
        if kart_dealer_1_cekilen in global_kart_destesi :
            kart_1_cekilen_dealer_cesid = random.choice(kart_cesidi)
            kart_1_cekilen_dealer_deger = random.choice(kart_degerleri)
            kart_dealer_1_cekilen = (kart_1_cekilen_dealer_cesid,kart_1_cekilen_dealer_deger)
        dealer_kartlari.append(kart_dealer_1_cekilen)
        global_kart_destesi.append(kart_dealer_1_cekilen)
        dealer_kartlari_toplam.append(kart_degerleri_dic[str(kart_1_cekilen_dealer_deger)])

    print("Kartlarınız:",oyuncu_kartlari)
    time.sleep(2)
    kart_cekme = input("Kart çekmek ister misiniz(E/H)?")
    while kart_cekme == "E" :
            istenen_kart_cesid = random.choice(kart_cesidi)
            istenen_kart_deger = random.choice(kart_degerleri)
            istenen_kart = (istenen_kart_cesid,istenen_kart_deger)
            if istenen_kart in global_kart_destesi :
                istenen_kart_cesid = random.choice(kart_cesidi)
                istenen_kart_deger = random.choice(kart_degerleri)
                istenen_kart = (istenen_kart_cesid,istenen_kart_deger)
            oyuncu_kartlari.append(istenen_kart)
            global_kart_destesi.append(istenen_kart)
            time.sleep(2)
            print("Çektiğiniz kart:",istenen_kart)
            time.sleep(2)
            print("Kartlarınız:",oyuncu_kartlari)
            time.sleep(2)
            kart_cekme = input("Kart çekmek ister misiniz(E/H)?")


    time.sleep(3)

    for x,y in oyuncu_kartlari :
            oyuncu_kartlari_toplam.append(kart_degerleri_dic[str(y)])

    if sum(oyuncu_kartlari_toplam) > 21 and sum(dealer_kartlari_toplam) > 21 :
        print("Kart değeleri toplamınız 21'i aştı,lütfen dağıtıcının hamlesini bekleyiniz...")
        time.sleep(3)
        print("Dağıtıcı kart değerleri toplamı da 21'i aştı!")
        time.sleep(1.8)
        print("Berabere,bahisiniz geri iade ediliyor...")
        time.sleep(1.5)
        print("Bahisiniz geri iade edildi.Güncel bakiye durumunuz:",oyuncu_para)

    elif sum(oyuncu_kartlari_toplam) > 21 and sum(dealer_kartlari_toplam) == 21 :
        print("Kart değeleri toplamınız 21'i aştı,lütfen dağıtıcının hamlesini bekleyiniz...")
        time.sleep(3)
        print("Dağıtıcı kart değerleri toplamı 21!")
        time.sleep(1.8)
        print("!!BLACKJACK!!")
        time.sleep(1)
        oyuncu_para -= (oyuncu_bahis*oyuncu_bahis_kat)
        print("Kaybettiniz.Güncel bakiye durumunuz:",oyuncu_para)

    elif sum(oyuncu_kartlari_toplam) > 21 and sum(dealer_kartlari_toplam) < 21 :
        print("Kart değerleri toplamınız 21'i aştı,lütfen dağıtıcının hamlesini bekleyiniz...")
        time.sleep(3)
        print("Dağıtıcı kart değerleri toplamı",sum(dealer_kartlari_toplam),"!")
        time.sleep(1.8)
        print("Kaybettiniz!")
        oyuncu_para -= (oyuncu_bahis_kat*oyuncu_bahis)
        print("Güncel bakiye durumunuz:",oyuncu_para)

    elif sum(oyuncu_kartlari_toplam) == 21 and sum(dealer_kartlari_toplam) > 21 :
        print("Kart değerleri toplamınız 21,lütfen dağıtıcının hamlesini bekleyiniz...")
        time.sleep(3)
        print("Dağıtıcının kart değerleri toplamı 21'i aştı!")
        time.sleep(1)
        print("!!BLACKJACK!!")
        oyuncu_para += (oyuncu_bahis*oyuncu_bahis_kat)
        print("Kazandınız!Güncel bakiye durumunuz:",oyuncu_para)
    elif sum(oyuncu_kartlari_toplam) == 21 and sum(dealer_kartlari_toplam) == 21 :
        print("Kart değerleri toplamınız 21,lütfen dağıtıcının hamlesini bekleyiniz...")
        time.sleep(3)
        print("Dağıtıcı kart değerleri toplamı 21!")
        print("Round berabere,bahisiniz iade ediliyor...")
        oyuncu_para += (oyuncu_bahis*oyuncu_bahis_kat)
        print("Bahisiniz iade edildi.Güncel bakiye durumunuz:",oyuncu_para)
    elif sum(oyuncu_kartlari_toplam) == 21 and sum(dealer_kartlari_toplam) < 21 :
        print("Kart değerleri toplamınız 21,lütfen dağıtıcının hamlesini bekleyiniz...")
        time.sleep(3)
        print("Dağıtıcı kart değerleri toplamı",sum(dealer_kartlari_toplam),"!")
        print("!!BLACKJACK!!")
        oyuncu_para += (oyuncu_bahis*oyuncu_bahis_kat)
        print("Kazandınız!Güncel bakiye durumunuz:",oyuncu_para)
    elif sum(oyuncu_kartlari_toplam) < 21 and sum(dealer_kartlari_toplam) > 21 :
        print("Kart değerleri toplamınız",sum(oyuncu_kartlari_toplam),"lütfen dağıtıcının hamlesini bekleyiniz...")
        time.sleep(3)
        oyuncu_para += (oyuncu_bahis*oyuncu_bahis_kat)
        print("Dağıtıcı kart değerleri toplamı 21'i aştı!")
        print("Kazandınız!Güncel bakiye durumunuz:",oyuncu_para)
    elif sum(oyuncu_kartlari_toplam) < 21 and sum(dealer_kartlari_toplam) == 21 :
        print("Kart değerleri toplamınız",sum(oyuncu_kartlari_toplam),"lütfen dağıtıcının hamlesini bekleyiniz...")
        time.sleep(3)
        print("Dağıtıcı kart değeleri toplamı 21!")
        print("!!BLACKJACK!!")
        oyuncu_para -= (oyuncu_bahis*oyuncu_bahis_kat)
        print("Kaybettiniz!Güncel bakiye durumunuz:",oyuncu_para)
    elif sum(oyuncu_kartlari_toplam) < 21 and sum(dealer_kartlari_toplam) < 21 :
        print("Kart değerleri toplamınız",sum(oyuncu_kartlari_toplam),"lütfen dağıtıcının hamlesini bekleyiniz...")
        time.sleep(3)
        print("Dağıtıcı kart değerleri toplamı",sum(dealer_kartlari_toplam),"!")
        if sum(oyuncu_kartlari_toplam) > sum(dealer_kartlari_toplam) :
            oyuncu_para += (oyuncu_bahis*oyuncu_bahis_kat)
            print("Kazandınız!Güncel bakiye durumunuz:",oyuncu_para)
        elif sum(oyuncu_kartlari_toplam) == sum(dealer_kartlari_toplam) :
            oyuncu_para += (oyuncu_bahis*oyuncu_bahis_kat)
            print("Berabere,bahisiniz geri iade ediiliyor...")
            print("Bahisiniz geri iade edildi.Güncel bakiye durumunuz:",oyuncu_para)
        elif sum(oyuncu_kartlari_toplam) < sum(dealer_kartlari_toplam) :
            oyuncu_para -= (oyuncu_bahis*oyuncu_bahis_kat)
            print("Kaybettiniz!Güncel bakiye durumunuz:",oyuncu_para)

    if oyuncu_para < 0 :
        sor = input("Bakiye yüklemek ister misiniz(E/H)?")
        if sor == "E" :
            yüklenen_bakiye = int(input("Yüklemek istediğiniz bakiye miktarını giriniz:"))
            oyuncu_para += yüklenen_bakiye

    global_kart_destesi.clear()
    oyuncu_kartlari.clear()
    dealer_kartlari.clear()
    oyuncu_kartlari_toplam.clear()
    dealer_kartlari_toplam.clear()

print("Oyun için teşekkürler",oyuncu_adi,",kendine iyi bak!")
