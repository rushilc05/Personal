from pathlib import Path

run = ''
contents = ''
while run != 'q':
    run = input("Please enter the name of your guest or enter q to exit: ")
    if run == 'q':
        break
    else:
        contents += f"{run.title()}\n"

path = Path("guest_book.txt")
path.write_text(contents)

