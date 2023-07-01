import tkinter as tk

digits = [
    [' 11111 ',
     '1     1',
     '1     1',
     '1     1',
     '1     1',
     '1     1',
     ' 11111 '],

    ['   11  ',
     '  111  ',
     '    11 ',
     '    11 ',
     '    11 ',
     '    11 ',
     '  11111'],

    [' 11111 ',
     '1     1',
     '      1',
     '     11',
     '   11  ',
     ' 11    ',
     '1111111'],

    [' 11111 ',
     '1     1',
     '      1',
     '  1111 ',
     '      1',
     '1     1',
     ' 11111 '],

    ['   11  ',
     '  111  ',
     ' 1  11 ',
     '1   11 ',
     '1111111',
     '    11 ',
     '    11 '],

    ['1111111',
     '11     ',
     '11     ',
     '111111 ',
     '     11',
     '1     1',
     ' 11111 '],

    [' 11111 ',
     '1     1',
     '11     ',
     '111111 ',
     '1     1',
     '1     1',
     ' 11111 '],

    ['1111111',
     '     11',
     '    11 ',
     '   11  ',
     '  11   ',
     ' 11    ',
     '11     '],

    [' 11111 ',
     '1     1',
     '1     1',
     ' 11111 ',
     '1     1',
     '1     1',
     ' 11111 '],

    [' 11111 ',
     '1     1',
     '1     1',
     ' 111111',
     '      1',
     '1     1',
     ' 11111 ']
]


def print_number(num):
    digs = str(num)
    lines = ['' for _ in range(7)]

    for d in digs:
        dig_lines = digits[int(d)]

        for i in range(7):
            lines[i] += dig_lines[i] + ' '

    return lines


def update_display():
    number = int(entry.get())
    lines = print_number(number)
    display.config(text='\n'.join(lines))


root = tk.Tk()
root.title("Números")

entry = tk.Entry(root)
entry.pack()

display = tk.Label(root, font=('Courier New', 14), width=60, height=7)
display.pack()

update_button = tk.Button(root, text="Actualizar", command=update_display)
update_button.pack()

root.mainloop()
