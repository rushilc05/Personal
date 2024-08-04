from pathlib import Path

name = input("WHat is your name: ")
path = Path("guests.txt")
path.write_text(name.title())