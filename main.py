#!/usr/bin/python

import os
import sys
from time import sleep

write = sys.stdout.write


def check():
    error = False
    for nl, l in letters.items():
        for nt, t in enumerate(l):
            if len(t) != 11:
                print(f"{nl}_{nt}: {len(t)}")
                error = True
    if not error:
        print("everything fine")


def print_sequence(s: str, t: int):
    s_split = s.split("\n")
    for s_current in s_split:
        print("\n" * s_current.count("+"), end="")
        s_current = s_current.replace("+", "")
        for line in range(11):
            for char in s_current:
                print(letters[char][t][line], end="  ")
            print("")
        print("")


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_alternating(s: str, d: int):
    t_order = [0, 1, 3, 2]
    t = 0
    try:
        while True:
            clear()
            print_sequence(s, t)
            sleep(d)
            t = t_order[(t_order.index(t) + 1) % 4]
    except KeyboardInterrupt:
        print("")
        print("Alles Gute!! ;)")


letter_h = [
    [r"      ___      ",
     r"     /\__\     ",
     r"    /:/  /     ",
     r"   /:/__/      ",
     r"  /::\  \ ___  ",
     r" /:/\:\  /\__\ ",
     r" \/__\:\/:/  / ",
     r"      \::/  /  ",
     r"      /:/  /   ",
     r"     /:/  /    ",
     r"     \/__/     "],
    [r"      ___      ",
     r"     /\  \     ",
     r"     \:\  \    ",
     r"      \:\  \   ",
     r"  ___ /::\  \  ",
     r" /\  /:/\:\__\ ",
     r" \:\/:/  \/__/ ",
     r"  \::/__/      ",
     r"   \:\  \      ",
     r"    \:\__\     ",
     r"     \/__/     "],
    [r"      ___      ",
     r"     /__/\     ",
     r"     \  \:\    ",
     r"      \__\:\   ",
     r"  ___ /  /::\  ",
     r" /__/\  /:/\:\ ",
     r" \  \:\/:/__\/ ",
     r"  \  \::/      ",
     r"   \  \:\      ",
     r"    \  \:\     ",
     r"     \__\/     "],
    [r"      ___      ",
     r"     /  /\     ",
     r"    /  /:/     ",
     r"   /  /:/      ",
     r"  /  /::\ ___  ",
     r" /__/:/\:\  /\ ",
     r" \__\/  \:\/:/ ",
     r"      \__\::/  ",
     r"      /  /:/   ",
     r"     /__/:/    ",
     r"     \__\/     "]
]
letter_a = [
    [r"      ___      ",
     r"     /\  \     ",
     r"    /::\  \    ",
     r"   /:/\:\  \   ",
     r"  /::\~\:\  \  ",
     r" /:/\:\ \:\__\ ",
     r" \/__\:\/:/  / ",
     r"      \::/  /  ",
     r"      /:/  /   ",
     r"     /:/  /    ",
     r"     \/__/     "],
    [r"      ___      ",
     r"     /\  \     ",
     r"    /::\  \    ",
     r"   /:/\:\  \   ",
     r"  /:/ /::\  \  ",
     r" /:/_/:/\:\__\ ",
     r" \:\/:/  \/__/ ",
     r"  \::/__/      ",
     r"   \:\  \      ",
     r"    \:\__\     ",
     r"     \/__/     "],
    [r"      ___      ",
     r"     /  /\     ",
     r"    /  /::\    ",
     r"   /  /:/\:\   ",
     r"  /  /:/~/::\  ",
     r" /__/:/ /:/\:\ ",
     r" \  \:\/:/__\/ ",
     r"  \  \::/      ",
     r"   \  \:\      ",
     r"    \  \:\     ",
     r"     \__\/     "],
    [r"      ___      ",
     r"     /  /\     ",
     r"    /  /::\    ",
     r"   /  /:/\:\   ",
     r"  /  /::\ \:\  ",
     r" /__/:/\:\_\:\ ",
     r" \__\/  \:\/:/ ",
     r"      \__\::/  ",
     r"      /  /:/   ",
     r"     /__/:/    ",
     r"     \__\/     "]
]
letter_p = [
    [r"               ",
     r"      ___      ",
     r"     /\  \     ",
     r"    /::\  \    ",
     r"   /:/\:\  \   ",
     r"  /::\~\:\  \  ",
     r" /:/\:\ \:\__\ ",
     r" \/__\:\/:/  / ",
     r"      \::/  /  ",
     r"       \/__/   ",
     r"               "],
    [r"      ___    ",
     r"     /\  \   ",
     r"    /::\  \  ",
     r"   /:/\:\__\ ",
     r"  /:/ /:/  / ",
     r" /:/_/:/  /  ",
     r" \:\/:/  /   ",
     r"  \::/__/    ",
     r"   \:\  \    ",
     r"    \:\__\   ",
     r"     \/__/   "],
    [r"      ___    ",
     r"     /  /\   ",
     r"    /  /::\  ",
     r"   /  /:/\:\ ",
     r"  /  /:/~/:/ ",
     r" /__/:/ /:/  ",
     r" \  \:\/:/   ",
     r"  \  \::/    ",
     r"   \  \:\    ",
     r"    \  \:\   ",
     r"     \__\/   "],
    [r"               ",
     r"      ___      ",
     r"     /  /\     ",
     r"    /  /::\    ",
     r"   /  /:/\:\   ",
     r"  /  /::\ \:\  ",
     r" /__/:/\:\_\:\ ",
     r" \__\/  \:\/:/ ",
     r"      \  \::/  ",
     r"       \__\/   ",
     r"               "]
]
letter_y = [
    [r"             ",
     r"    ___      ",
     r"   |\__\     ",
     r"   |:|  |    ",
     r"   |:|  |    ",
     r"   |:|__|__  ",
     r"   /::::\__\ ",
     r"  /:/~~/~    ",
     r" /:/  /      ",
     r" \/__/       ",
     r"             "],
    [r"             ",
     r"      ___    ",
     r"     /|  |   ",
     r"    |:|  |   ",
     r"    |:|  |   ",
     r"  __|:|__|   ",
     r" /::::\  \   ",
     r" ~~~~\:\  \  ",
     r"      \:\__\ ",
     r"       \/__/ ",
     r"             "],
    [r"             ",
     r"      ___    ",
     r"     /__/|   ",
     r"    |  |:|   ",
     r"    |  |:|   ",
     r"  __|__|:|   ",
     r" /__/::::\   ",
     r"    ~\~~\:\  ",
     r"      \  \:\ ",
     r"       \__\/ ",
     r"             "],
    [r"             ",
     r"    __       ",
     r"   |  |\     ",
     r"   |  |:|    ",
     r"   |  |:|    ",
     r"   |__|:|__  ",
     r"   /  /::::\ ",
     r"  /  /:/~~~~ ",
     r" /__/:/      ",
     r" \__\/       ",
     r"             "]
]
letter_b = [
    [r"      ___      ",
     r"     /\  \     ",
     r"    /::\  \    ",
     r"   /:/\:\  \   ",
     r"  /::\~\:\__\  ",
     r" /:/\:\ \:|__| ",
     r" \:\~\:\/:/  / ",
     r"  \:\ \::/  /  ",
     r"   \:\/:/  /   ",
     r"    \::/__/    ",
     r"     ~~        "],
    [r"               ",
     r"     _____     ",
     r"    /::\  \    ",
     r"   /:/\:\  \   ",
     r"  /:/ /::\__\  ",
     r" /:/_/:/\:|__| ",
     r" \:\/:/ /:/  / ",
     r"  \::/_/:/  /  ",
     r"   \:\/:/  /   ",
     r"    \::/  /    ",
     r"     \/__/     "],
    [r"               ",
     r"     _____     ",
     r"    /  /::\    ",
     r"   /  /:/\:\   ",
     r"  /  /:/~/::\  ",
     r" /__/:/ /:/\:| ",
     r" \  \:\/:/~/:/ ",
     r"  \  \::/ /:/  ",
     r"   \  \:\/:/   ",
     r"    \  \::/    ",
     r"     \__\/     "],
    [r"      ___      ",
     r"     /  /\     ",
     r"    /  /::\    ",
     r"   /  /:/\:\   ",
     r"  /  /::\ \:\  ",
     r" /__/:/\:\_\:| ",
     r" \  \:\ \:\/:/ ",
     r"  \  \:\_\::/  ",
     r"   \  \:\/:/   ",
     r"    \__\::/    ",
     r"        ~~     "]
]
letter_d = [
    [r"      ___      ",
     r"     /\  \     ",
     r"    /::\  \    ",
     r"   /:/\:\  \   ",
     r"  /:/  \:\__\  ",
     r" /:/__/ \:|__| ",
     r" \:\  \ /:/  / ",
     r"  \:\  /:/  /  ",
     r"   \:\/:/  /   ",
     r"    \::/__/    ",
     r"     ~~        "],
    [r"               ",
     r"     _____     ",
     r"    /::\  \    ",
     r"   /:/\:\  \   ",
     r"  /:/  \:\__\  ",
     r" /:/__/ \:|__| ",
     r" \:\  \ /:/  / ",
     r"  \:\  /:/  /  ",
     r"   \:\/:/  /   ",
     r"    \::/  /    ",
     r"     \/__/     "],
    [r"     _____     ",
     r"    /  /::\    ",
     r"   /  /:/\:\   ",
     r"  /  /:/  \:\  ",
     r" /__/:/ \__\:| ",
     r" \  \:\ /  /:/ ",
     r"  \  \:\  /:/  ",
     r"   \  \:\/:/   ",
     r"    \  \::/    ",
     r"     \__\/     ",
     r"               "],
    [r"      ___      ",
     r"     /  /\     ",
     r"    /  /::\    ",
     r"   /  /:/\:\   ",
     r"  /  /:/  \:\  ",
     r" /__/:/ \__\:| ",
     r" \  \:\ /  /:/ ",
     r"  \  \:\  /:/  ",
     r"   \  \:\/:/   ",
     r"    \__\::/    ",
     r"        ~~     "]
]
letter_space = [[" " * 8 for _ in range(11)] for _ in range(4)]
letter_singel_space = [[" " for _ in range(11)] for _ in range(4)]
letter_single_newline = [["\n" for _ in range(11)] for _ in range(4)]
letters = {
    "h": letter_h,
    "a": letter_a,
    "p": letter_p,
    "y": letter_y,
    "b": letter_b,
    "d": letter_d,
    " ": letter_space,
    "#": letter_singel_space
    # + for a single newline
}


def wait(x):
    while x > 0:
        sleep(1)
        x -= 1
        print(x)


clear()
print("Terminal fullscreen?")
print("Alle bereit?")
print("Gleich gehts los (15 Sekunden)")
print("Wenn nicht strg-c und nochmal starten")
sleep(4)
wait(11)
clear()


def cursed_print(s: str):
    for char in s:
        if char == ".":
            sleep(0.5)
            continue
        elif char == ",":
            sleep(0.2)
            continue
        elif char == "-":
            sleep(0.05)
            continue
        print(char, end="", flush=True)


cprint = cursed_print
cprint("\n,"*10+".")
cprint("H.a.p.y.\b.py\b.y")
cprint(". .")
cprint(
    "b.\b \b.B.y.r..-\b \b,,\b \b.-i.r,-h,-t,-d.,a.y.\b \b,\b \b-\b \b-\b \b-\b \b-\b \b..r.t.h.d.a.y-y,,\b \b.!")
cprint("... , , , , ,.:..)")

sleep(2)

cprint("\n,\n,\n")
cprint(".")
cprint("A.l.l.w,\b \b.,e.-s. .,G.u.t.e..\n.\n.u-s-w.,")
print("")
print("Das ersparen wir uns ;)")
sleep(3)
print("Aber Achtung")
sleep(1)
print("Noch nicht aus")
sleep(2)
print(3)
wait(3)

print_alternating("+" * 6 + "   happy\n" + "#" * 3 + "   bday", 1)

# check()
