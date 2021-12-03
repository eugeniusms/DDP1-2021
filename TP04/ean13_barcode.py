from tkinter import *
import tkinter.messagebox as tkmsg

root = Tk()

def manipulate(binary):
    # Len binary => 7 * 12 = 84
    # Manipulasi string index = 0, 41, 84
    strend = "101"
    mid = "01010"
    
    new_binary = strend + binary[:42] + mid + binary[42:] + strend
    return new_binary


def create_bar(start, number, binary, canvas):
    # Convert every digit to bar
    binary = manipulate(binary)

    canvas.create_text(175, 75, font = "Helvetica 20 bold", text = "EAN-13 Barcode:")

    pos_x = 50
    count = 0
    for bit in binary:
        # For mark
        if bit == "1":
            if (count < 3) or (count > 44 and count < 50) or (count > 90):
                canvas.create_rectangle(
                    pos_x, 100, pos_x + 1.5, 260,
                    outline="#FF8141",
                    fill="#FF8141")
            else:
                canvas.create_rectangle(
                    pos_x, 100, pos_x + 1.5, 250,
                    outline="#00C4FF",
                    fill="#00C4FF")
        
        pos_x += 2.5
        count += 1

    style_number = ""
    number = start + number
    for i in range(len(number)):
        if i == 0 or i == 6:
            style_number += number[i] + "   "
        else:
            style_number += number[i] + "  "

    canvas.create_text(165, 271, fill = "#1E5C9A", font = "Helvetica 17 bold", text = style_number)

    end = number[-1]
    canvas.create_text(168, 295, font = "Helvetica 20 bold", text = "Check Digit: {}".format(end))


    # canvas.create_rectangle(
    #     pos_x, 30, pos_x+10, 120,
    #     outline="#fb0",
    #     fill="#fb0")
    
def processing(start, first_group, last_group, end, canvas):
    print(start, first_group, last_group, end)

    # Penentuan struktur dipengaruhi oleh digit pertama (start)
    first_structure = {
        "0" : "LLLLLL",
        "1" : "LLGLGG",
        "2" : "LLGGLG",
        "3" : "LLGGGL",
        "4" : "LGLLGG",
        "5" : "LGGLLG",
        "6" : "LGGGLL",
        "7" : "LGLGLG",
        "8" : "LGLGGL",
        "9" : "LGGLGL"
    }

    structure = first_structure[start] + "RRRRRR"
    print(structure)
    number = first_group + last_group + str(end)
    print(number)

    digit_encoding = {
        "L" : ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"],
        "G" : ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"],
        "R" : ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1001000"]
    }

    binary = ""
    count = 0
    for lgr in structure:
        num = number[count]
        cod = digit_encoding[lgr]
        binary += cod[int(num)]
        count += 1

    print(binary)

    create_bar(start, number, binary, canvas)

def main():
    root.geometry("450x540")
    welcome = Label(root, text = 'Save barcode to PS file [eg: EAN13.eps]:')
    save = Entry(root, width = 25)
    enter = Label(root, text = 'Enter code (first 12 decimal digits):')
    code = Entry(root, width = 25)
    
    welcome.place(x = 95, y = 10)
    save.place(x = 100, y = 40)
    enter.place(x = 108, y = 70)
    code.place(x = 100, y = 100)

    canvas = Canvas(
        root,
        height=350,
        width=350,
        bg="#fff"
        )
    canvas.place(x = 43, y = 140)

    def func(event):
        check_number = code.get()
        filename = save.get()

        # Validasi angka harusnya 12 digit panjangnya
        if len(check_number) == 12:
            start = check_number[0]
            first_group = check_number[1:7]
            last_group = check_number[7:13]
            
            # end bertindak sebagai check digit
            end = 0
            for digit in range(len(check_number)):
                if digit % 2:
                    end += 3 * int(check_number[digit])
                else:
                    end += 1 * int(check_number[digit])
            end %= 10
            if end != 0:
                end = 10 - end
            else:
                end = end

            print(f"end : {end}")
            processing(start, first_group, last_group, end, canvas)

            # Proses menyimpan
            canvas.postscript(file = filename, colormode='color')

        else:
            tkmsg.showwarning("Wrong input!", "Please enter correct input code.")

    root.bind('<Return>', func)


if __name__ == "__main__":
    main()

root.mainloop()
