import random


def get_user_choice():
    # Bu fonksiyon kullanıcının Taş, Kağıt veya Makas seçimini öğrenir.
    user_input = input("Taş, Kağıt, Makas: ").lower()
    if user_input in ["taş", "kağıt", "makas"]:
        return user_input
    else:
        print("Geçersiz seçim, lütfen Taş, Kağıt veya Makas girin.")
        return get_user_choice()


def get_computer_choice():
    # Bu fonksiyon bilgisayarın rastgele bir seçim yapmasını sağlar.
    return random.choice(["taş", "kağıt", "makas"])


def determine_winner(user_choice, computer_choice):
    # Bu fonksiyon kullanıcı ve bilgisayar seçimlerinin sonucunu belirler.
    if user_choice == computer_choice:
        return "Dostluk kazandı, berabere!", None
    elif (user_choice == "taş" and computer_choice == "makas") or \
         (user_choice == "kağıt" and computer_choice == "taş") or \
         (user_choice == "makas" and computer_choice == "kağıt"):
        return "Kazandınız!", "user"
    else:
        return "Kaybettiniz!", "computer"


def ask_play_again():
    # Bu fonksiyon kullanıcının yeniden oynamak isteyip istemediğini sorar.
    user_input = input("Oynamak ister misiniz? (Evet/Hayır): ").lower()
    if user_input in ["evet", "hayır"]:
        return user_input == "evet"
    else:
        print("Geçersiz seçim, lütfen Evet veya Hayır girin.")
        return ask_play_again()


def computer_play_again():
    # Bu fonksiyon bilgisayarın yeniden oyun oynamak isteyip istemediğini rastgele belirler.
    return random.choice(["evet", "hayır"])


def tas_kagit_makas_umut_renas_yuksel():
    # Bu fonksiyon Taş-Kağıt-Makas oyununu başlatan ana fonksiyondur.
    print("Hoşgeldiniz! Taş-Kağıt-Makas oyununa başlıyoruz.")
    print("Oyun Kuralları:")
    print("1. Taş, makası yener (Taş, makası kırar).")
    print("2. Kağıt, taşı yener (Kağıt, taşı sarar).")
    print("3. Makas, kağıdı yener (Makas, kağıdı keser).")
    print("4. Önce 2 olan kazanır.")
    print("5. Oyunu oynamak için 'Evet', oyundan çıkmak için 'Hayır' seçeneğini girin.\n")

    start_input = input("Hazır mısınız? En iyi hamlenizi yapın! (Evet/Hayır): ").lower()
    if start_input == "hayır":
        print("Oyun başlamadan çıkış yaptınız.")
        return
    elif start_input != "evet":
        print("Geçersiz seçim, lütfen Evet veya Hayır girin.")
        return tas_kagit_makas_umut_renas_yuksel()

    while True:
        user_score = 0
        computer_score = 0

        while user_score < 2 and computer_score < 2:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()

            print(f"Siz: {user_choice.capitalize()}, Bilgisayar: {computer_choice.capitalize()}")

            result, winner = determine_winner(user_choice, computer_choice)
            print(result)

            if winner == "user":
                user_score += 1
            elif winner == "computer":
                computer_score += 1

            print(f"Skor - Siz: {user_score}, Bilgisayar: {computer_score}\n")

        if user_score == 2:
            print("Çok şanslısın, bu seferlik kazandın.")
        else:
            print("Üzgünüm, bilgisayar oyunu kazandı.")

        if ask_play_again():
            if computer_score == 2 and user_score < 2:  # Kullanıcı kaybettiğinde
                print("Yenilen pehlivan güreşe doymaz.")

            computer_response = computer_play_again()
            print(f"Bilgisayarın cevabı: {computer_response.capitalize()}")
            if computer_response == "hayır":
                print("Maalesef şu an oynayamıyorum ancak başka bir zaman kazanmak için tekrar döneceğim.")
                break
            else:
                print("Peki madem, oyuna devam ediliyor...\n")
        else:
            print("Oyun sona erdi.")
            break


if __name__ == "__main__":
    tas_kagit_makas_umut_renas_yuksel()



