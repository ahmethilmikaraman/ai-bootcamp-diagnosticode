import random

ship_positions = []
ship_positions = [(random.randint(1,5),random.randint(1,5)) for i in range(2) if (random.randint(1,5),random.randint(1,5)) not in ship_positions]

limit_counter = 0
true_count = 0

print("Amiral battı oyununa hoş geldin! 5x5 bir tahtada gemi gizledim hadi 5 tahmin içinde bulmaya çalış.")
print("-----" * 10)
while limit_counter < 5:

    print(f"{limit_counter + 1}. Tahmin ({len(ship_positions)} gemi kaldı.)")
    print("-----" * 5)

    guess_pos = tuple([int(input(f"{'Satır' if i == 0 else 'Sütun'} (1-5) : ")) for i in range(2)])

    print(guess_pos)

    if (guess_pos in ship_positions):
        print("Gemi alabora oldu ve yok oldu! Senden kaçış yok.")
        ship_positions.remove((guess_pos))
        true_count += 1
        if true_count == 2 : break

        limit_counter +=1
    else:
        print("Iska! Ama pes etmek yok, sıradaki atış daha iyi olacak!")
        limit_counter +=1

if limit_counter == 5: 
    print("Kaybettin, gemiler kaçmayı başardı.")
else:
    print("Tebrikler kazandın! Mürettabtın ve sana teşekkürler.")