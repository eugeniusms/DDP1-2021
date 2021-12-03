from tkinter import *

root = Tk()

def create_bar(digit, ):
    # Convert every digit to bar
    canvas = Canvas(
        root,
        height=200,
        width=200,
        bg="#fff"
        )
        
    canvas.pack()

    canvas.create_rectangle(
        30, 30, 40, 120,
        outline="#fb0",
        fill="#fb0")
    canvas.create_rectangle(
        40, 30, 50, 120,
        outline="#fb0",
        fill="#ff0000")
    
def processing(start, first_group, middle, last_group, end):
    first_structure = {
        0 : "LLLLLL",
        1 : "LLGLGG",
        2 : "LLGGLG",
        3 : "LLGGGL",
        4 : "LGLLGG",
        5 : "LGGLLG",
        6 : "LGGGLL",
        7 : "LGLGLG",
        8 : "LGLGGL",
        9 : "LGGLGL"
    }
    digit_encoding = {
        "L" : ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"],
        "G" : ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"],
        "R" : ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1001000"]
    }

def main():
    root.geometry("465x560")
    welcome = Label(root, text = 'Save barcode to PS file [eg: EAN13.eps]:')
    save = Entry(root, width = 25)
    enter = Label(root, text = 'Enter code (first 12 decimal digits):')
    code = Entry(root, width = 25)
    
    welcome.place(x = 95, y = 10)
    save.place(x = 100, y = 40)
    enter.place(x = 108, y = 70)
    code.place(x = 100, y = 100)

    # disp_tf = Entry(root, font=('Arial', 14))
    # disp_tf.insert(0, "HAI")
    # disp_tf.place(x = 30, y = 140, width = 400, height = 400)
    check_number = code.get()
    
    check = Label(root, text = check_number)
    check.pack()


if __name__ == "__main__":
    main()

root.mainloop()
