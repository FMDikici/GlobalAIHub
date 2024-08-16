import random

def tas_kagit_makas_ADINIZ_SOYADINIZ():
    print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz!")
    print("Kurallar: Taş Makası Yener, Kağıt Taşı Yener, Makas Kağıdı Yener.")
    print("Oyundan çıkmak için 'q' tuşuna basın.")
    print("Haydi Baslayalim")
    
    # Seçenekler 
    choices = ["taş", "kağıt", "makas"]
    
    # Sayaçlar
    player_wins = 0
    computer_wins = 0
    
    # Ana oyun 
    while True:
        rounds = 0
        player_score = 0
        computer_score = 0
        
        # Turlar
        while player_score < 2 and computer_score < 2:
            player_choice = input("\nTaş, Kağıt, Makas? (taş/kağıt/makas): ").lower()
            
            if player_choice == 'q':
                print("Oyundan çıkılıyor.")
                return
            
            if player_choice not in choices:
                print("Lütfen taş, kağıt ya da makas seçin.")
                continue
            
            computer_choice = random.choice(choices)
            print(f"Bilgisayarın Seçimi: {computer_choice}")
            
            # Kazananı belirle
            if player_choice == computer_choice:
                print("Berabere!")
            elif (player_choice == "taş" and computer_choice == "makas") or \
                 (player_choice == "kağıt" and computer_choice == "taş") or \
                 (player_choice == "makas" and computer_choice == "kağıt"):
                print("Bu turu kazandınız!")
                player_score += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                computer_score += 1
            
            rounds += 1
        
        # Tur kazananını belirle
        if player_score > computer_score:
            print(f"\nTebrikler, {rounds} turda oyunu kazandınız!")
            player_wins += 1
        else:
            print(f"\nBilgisayar {rounds} turda oyunu kazandı!")
            computer_wins += 1
        
        # Oyun devam mı?
        play_again = input("Tekrar oynamak ister misiniz? (evet/hayır): ").lower()
        if play_again != "evet":
            print("Oyunu oynadığınız için teşekkürler!")
            print(f"Toplam Kazanılan Oyunlar: Siz {player_wins}, Bilgisayar {computer_wins}")
            break

tas_kagit_makas_ADINIZ_SOYADINIZ()