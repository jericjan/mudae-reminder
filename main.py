from decimal import Decimal
import time
from pathlib import Path
import winsound

def play_sound(filename):
    winsound.PlaySound(str(filename), winsound.SND_FILENAME)


def get_curr_epoch():
    return Decimal(time.time_ns()) / (10**9)

stuff_folder = Path(__file__).resolve().with_name("stuff")
    
with open(stuff_folder / "next_epoch.txt", encoding="utf-8") as f:
    epoch = f.read()

epoch = int(epoch)

play_sound(stuff_folder / 'gamble.wav')

while True:

    print("Updating next epoch")    

    while epoch < get_curr_epoch():
        epoch += 3600*3

    with open(stuff_folder / "next_epoch.txt", "w", encoding="utf-8") as f:
        f.write(str(epoch))

    print(f"Next epoch is {epoch}")


    hours = [epoch - (3600 * i) for i in range(2, -1, -1)]
    for nth, ep in enumerate(hours):
        if get_curr_epoch() > ep:
            continue
        while get_curr_epoch() < ep:
            left = str(int(ep - get_curr_epoch())).zfill(4)
            print(f"[HOUR {nth+1}] {left} secs left", end="\r")
            time.sleep(0.1)
        play_sound(stuff_folder / 'gamble.wav')
    play_sound(stuff_folder / 'claim reset.wav')