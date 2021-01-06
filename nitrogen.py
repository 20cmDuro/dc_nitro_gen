import random

finalizar = 1

print("      ___  _                   _   _  _ _ _              ___                       _                ")
print("     |   \(_)___ __ ___ _ _ __| | | \| (_) |_ _ _ ___   / __|___ _ _  ___ _ _ __ _| |_ ___ _ _      ")
print("     | |) | (_-</ _/ _ \ '_/ _` | | .` | |  _| '_/ _ \ | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|     ")
print("     |___/|_/__/\__\___/_| \__,_| |_|\_|_|\__|_| \___/  \___\___|_||_\___|_| \__,_|\__\___/_|       ")
print("                             ___ _            _         _      _____                                ")
print("                            / __| |_ ___ __ _| |___ _ _( )___ |_   _|__ __ _ _ __                   ")
print("                            \__ \  _/ -_) _` | / -_) '_|/(_-<   | |/ -_) _` | '  \                  ")
print("                            |___/\__\___\__,_|_\___|_|   /__/   |_|\___\__,_|_|_|_|                 ")
print("                                                                                                    ")
print("                                                                                      ~Jhin Scripter")
print("                                                                                                    ")

sgl = open("links_nitro.sst", "a")
nogc = int(input("Quantia: "))

if input("Limpo [y/n]? ") == "y":
	gl = "https://discordapp.com/gifts/"
else:
	gl = "[#SST] - https://discordapp.com/gifts/"

while finalizar <= nogc:
	generated_gift_2np = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", k=16))
	fc = gl + generated_gift_2np
	sgl.write(f"{fc}\n")
	print(fc)
	finalizar += 1
