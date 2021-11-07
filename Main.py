
import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title('Chess')
root.geometry()
root.config(bg='lightgray')
root.resizable(height=False, width=False)
root.iconbitmap('Icon_placeholder.ico')
for y in range(8):
    for x in range(8):
        Board = tkinter.Label(root)
        if y % 2 == 1:
            if x % 2 == 1:
                Board.config(padx=75, pady=70, bg="white")
                Board.grid(row=y, column=x)
            else:
                Board.config(padx=75, pady=70, bg='#505050')
                Board.grid(row=y, column=x)
        else:
            if x % 2 == 1:
                Board.config(padx=75, pady=70, bg="#505050")
                Board.grid(row=y, column=x)
            else:
                Board.config(padx=75, pady=70, bg='white')
                Board.grid(row=y, column=x)


def get_image(file):
    img = Image.open(rf"{file}")
    img = img.resize((150, 150), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(img)
    return image


def get_color():
    global color

    if not (c.grid_info()['row'] / 2).is_integer():
        if not (c.grid_info()['column'] / 2).is_integer():
            color = 'white'
        else:
            color = '#505050'
    if (c.grid_info()['row'] / 2).is_integer():
        if (c.grid_info()['column'] / 2).is_integer():
            color = 'white'
        else:
            color = '#505050'


black_pieces = []
white_pieces = []
black_pawn = get_image('bonde_svart.png')
for y in range(8):

    new_black_pawn = tkinter.Label(root, image=black_pawn, text='P')

    if y % 2 == 1:
        new_black_pawn.config(bg='white')

    else:
        new_black_pawn.config(bg='#505050')

    new_black_pawn.grid(row=1, column=y)
    black_pieces.append(new_black_pawn)
white_pawn = get_image('bonde_vit.png')
for y in range(8):

    new_black_pawn = tkinter.Label(root, image=white_pawn, text='P')

    if y % 2 == 1:
        new_black_pawn.config(bg='#505050')

    else:
        new_black_pawn.config(bg='white')

    new_black_pawn.grid(row=6, column=y)
    white_pieces.append(new_black_pawn)
black_castle = get_image('torn_svart.png')
for x in range(0, 14, 7):
    c = tkinter.Label(root, image=black_castle, text='C')
    c.grid(row=0, column=x)
    get_color()
    c.config(bg=color)
    black_pieces.append(c)
white_castle = get_image('torn_vit.png')
for x in range(0, 14, 7):
    c = tkinter.Label(root, image=white_castle, text='C')
    c.grid(row=7, column=x)
    get_color()
    c.config(bg=color)
    white_pieces.append(c)
black_bishop = get_image('Bishop_svart.png')
for x in range(2, 8, 3):
    c = tkinter.Label(root, image=black_bishop, text='B')
    c.grid(row=0, column=x)
    get_color()
    c.config(bg=color)
    black_pieces.append(c)
white_bishop = get_image('Bishop_vit.png')
for x in range(2, 8, 3):
    c = tkinter.Label(root, image=white_bishop, text='B')
    c.grid(row=7, column=x)
    get_color()
    c.config(bg=color)
    white_pieces.append(c)
black_queen = get_image('queen_svart.png')
for x in range(4, 10, 6):
    c = tkinter.Label(root, image=black_queen, text='Q')
    c.grid(row=0, column=x)
    get_color()
    c.config(bg=color)
    black_pieces.append(c)
white_queen = get_image('queen_vit.png')
for x in range(4, 10, 6):
    c = tkinter.Label(root, image=white_queen, text='Q')
    c.grid(row=7, column=x)
    get_color()
    c.config(bg=color)
    white_pieces.append(c)
black_knight = get_image('knight_svart.png')
for x in range(1, 11, 5):
    c = tkinter.Label(root, image=black_knight, text='H')
    c.grid(row=0, column=x)
    get_color()
    c.config(bg=color)
    black_pieces.append(c)
white_knight = get_image('knight_vit.png')
for x in range(1, 11, 5):
    c = tkinter.Label(root, image=white_knight, text='H')
    c.grid(row=7, column=x)
    get_color()
    c.config(bg=color)
    white_pieces.append(c)
black_king = get_image('kung_svart.png')
for x in range(3, 8, 5):
    c = tkinter.Label(root, image=black_king, text='K')
    c.grid(row=0, column=x)
    get_color()
    c.config(bg=color)
    black_pieces.append(c)
white_king = get_image('kung_vit.png')
for x in range(3, 8, 5):
    c = tkinter.Label(root, image=white_king, text='K')
    c.grid(row=7, column=x)
    get_color()
    c.config(bg=color)
    white_pieces.append(c)


def uppgrade_window():
    global upp_win
    upp_win = tkinter.Toplevel(root)


    upp_win.title('Välj din pjäs')
    if white:
        black_castle_pic = tkinter.Label(upp_win, image=white_castle, borderwidth=1,
                                     relief='solid')
        black_castle_pic.grid(row=0, column=0)
        black_knight_pic = tkinter.Label(upp_win, image=white_knight, borderwidth=1, relief='solid')
        black_knight_pic.grid(row=0, column=1)
        black_bishop_pic = tkinter.Label(upp_win, image=white_bishop, borderwidth=1, relief='solid')
        black_bishop_pic.grid(row=1, column=0)
        black_queen_pic = tkinter.Label(upp_win, image=white_queen, borderwidth=1, relief='solid')
        black_queen_pic.grid(row=1, column=1)
    else:
        black_castle_pic = tkinter.Label(upp_win, image=black_castle, borderwidth=1,
                                         relief='solid')
        black_castle_pic.grid(row=0, column=0)
        black_knight_pic = tkinter.Label(upp_win, image=black_knight, borderwidth=1, relief='solid')
        black_knight_pic.grid(row=0, column=1)
        black_bishop_pic = tkinter.Label(upp_win, image=black_bishop, borderwidth=1, relief='solid')
        black_bishop_pic.grid(row=1, column=0)
        black_queen_pic = tkinter.Label(upp_win, image=black_queen, borderwidth=1, relief='solid')
        black_queen_pic.grid(row=1, column=1)


    upp_win.bind('<Button 1>', upp_choice)


def upp_choice(event):
    global upp_win, color, white

    x = event.x_root - upp_win.winfo_rootx()
    y = event.y_root - upp_win.winfo_rooty()
    pos = root.grid_location(x=x, y=y)
    #Castle
    if pos[1] == 0:
        if pos[0] == 0:
            if not white:

                for c in white_pieces:
                    if c.grid_info()['row'] == 0:

                        if c.cget('text') == 'P':
                            print('C')
                            new = tkinter.Label(root, image=white_castle, text='C')
                            new.grid(row=c.grid_info()['row'], column=c.grid_info()['column'])
                            if not (c.grid_info()['row'] / 2).is_integer():
                                if not (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            if (c.grid_info()['row'] / 2).is_integer():
                                if (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            new.config(bg=color)

                            white_pieces.append(new)
                            white_pieces.remove(c)
                            c.destroy()
                            upp_win.destroy()

            else:
                for c in black_pieces:
                    if c.grid_info()['row'] == 7:

                        if c.cget('text') == 'P':
                            print('C')
                            new = tkinter.Label(root, image=black_castle, text='C')
                            new.grid(row=c.grid_info()['row'], column=c.grid_info()['column'])
                            if not (c.grid_info()['row'] / 2).is_integer():
                                if not (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            if (c.grid_info()['row'] / 2).is_integer():
                                if (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            new.config(bg=color)

                            black_pieces.append(new)
                            black_pieces.remove(c)
                            c.destroy()
                            upp_win.destroy()

    #Knight
    if pos[1] == 0:
        if pos[0] == 1:

            print('H')
            if not white:

                for c in white_pieces:
                    if c.grid_info()['row'] == 0:

                        if c.cget('text') == 'P':
                            print('H')
                            new = tkinter.Label(root, image=white_knight, text='H')
                            new.grid(row=c.grid_info()['row'], column=c.grid_info()['column'])
                            if not (c.grid_info()['row'] / 2).is_integer():
                                if not (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            if (c.grid_info()['row'] / 2).is_integer():
                                if (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            new.config(bg=color)

                            white_pieces.append(new)
                            white_pieces.remove(c)
                            c.destroy()
                            upp_win.destroy()

            else:
                for c in black_pieces:
                    if c.grid_info()['row'] == 7:

                        if c.cget('text') == 'P':
                            print('H')
                            new = tkinter.Label(root, image=black_knight, text='H')
                            new.grid(row=c.grid_info()['row'], column=c.grid_info()['column'])
                            if not (c.grid_info()['row'] / 2).is_integer():
                                if not (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            if (c.grid_info()['row'] / 2).is_integer():
                                if (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            new.config(bg=color)

                            black_pieces.append(new)
                            black_pieces.remove(c)
                            c.destroy()
                            upp_win.destroy()

    #Bishop
    if pos[1] == 1:
        if pos[0] == 0:
            if not white:

                for c in white_pieces:
                    if c.grid_info()['row'] == 0:

                        if c.cget('text') == 'P':
                            print('C')
                            new = tkinter.Label(root, image=white_bishop, text='B')
                            new.grid(row=c.grid_info()['row'], column=c.grid_info()['column'])
                            if not (c.grid_info()['row'] / 2).is_integer():
                                if not (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            if (c.grid_info()['row'] / 2).is_integer():
                                if (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            new.config(bg=color)

                            white_pieces.append(new)
                            white_pieces.remove(c)
                            c.destroy()
                            upp_win.destroy()

            else:
                for c in black_pieces:
                    if c.grid_info()['row'] == 7:

                        if c.cget('text') == 'P':
                            print('C')
                            new = tkinter.Label(root, image=black_bishop, text='B')
                            new.grid(row=c.grid_info()['row'], column=c.grid_info()['column'])
                            if not (c.grid_info()['row'] / 2).is_integer():
                                if not (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            if (c.grid_info()['row'] / 2).is_integer():
                                if (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            new.config(bg=color)

                            black_pieces.append(new)
                            black_pieces.remove(c)
                            c.destroy()
                            upp_win.destroy()

    #Queen
    if pos[1] == 1:
        if pos[0] == 1:
            if not white:

                for c in white_pieces:
                    if c.grid_info()['row'] == 0:

                        if c.cget('text') == 'P':
                            print('C')
                            new = tkinter.Label(root, image=white_queen, text='Q')
                            new.grid(row=c.grid_info()['row'], column=c.grid_info()['column'])
                            if not (c.grid_info()['row'] / 2).is_integer():
                                if not (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            if (c.grid_info()['row'] / 2).is_integer():
                                if (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            new.config(bg=color)

                            white_pieces.append(new)
                            white_pieces.remove(c)
                            c.destroy()
                            upp_win.destroy()

            else:
                for c in black_pieces:
                    if c.grid_info()['row'] == 7:

                        if c.cget('text') == 'P':
                            print('C')
                            new = tkinter.Label(root, image=black_queen, text='Q')
                            new.grid(row=c.grid_info()['row'], column=c.grid_info()['column'])
                            if not (c.grid_info()['row'] / 2).is_integer():
                                if not (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            if (c.grid_info()['row'] / 2).is_integer():
                                if (c.grid_info()['column'] / 2).is_integer():
                                    color = 'white'
                                else:
                                    color = '#505050'
                            new.config(bg=color)

                            black_pieces.append(new)
                            black_pieces.remove(c)
                            c.destroy()
                            upp_win.destroy()


selected = False
white = True
move = False


def movement(event):
    global white, move
    if white:
        global selected, c, save_pos, pawns, color
        if not selected:
            x = event.x_root - root.winfo_rootx()
            y = event.y_root - root.winfo_rooty()
            pos = root.grid_location(x=x, y=y)
            for c in white_pieces:
                if c.grid_info()['column'] == pos[0]:
                    if c.grid_info()['row'] == pos[1]:
                        c.config(bg='orange')
                        selected = True
                        save_pos = pos
                        break
        else:

            if selected:
                if c.cget('text') == 'P':
                    # Gets the gridlocation of where you pressed
                    x = event.x_root - root.winfo_rootx()
                    y = event.y_root - root.winfo_rooty()
                    pos = root.grid_location(x=x, y=y)

                    # Makes it so the pawns cant move on to each other
                    for clash in black_pieces:
                        if save_pos[1] - 1 == pos[1]:
                            if save_pos[0] == pos[0]:
                                if clash.grid_info()['row'] == pos[1]:
                                    if clash.grid_info()['column'] == pos[0]:
                                        print('you tried moving in to another piece')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return
                    for clash in black_pieces:
                        if save_pos[1] - 2 == pos[1]:
                            if save_pos[0] == pos[0]:
                                if clash.grid_info()['row'] == pos[1]:
                                    if clash.grid_info()['column'] == pos[0]:
                                        print('you tried moving in to another piece')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return
                    for clash in white_pieces:
                        if save_pos[1] - 1 == pos[1]:
                            if save_pos[0] == pos[0]:
                                if clash.grid_info()['row'] == pos[1]:
                                    if clash.grid_info()['column'] == pos[0]:
                                        print('you tried moving in to another piece')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return
                    for clash in white_pieces:
                        if save_pos[1] - 2 == pos[1]:
                            if save_pos[0] == pos[0]:
                                if clash.grid_info()['row'] == pos[1]:
                                    if clash.grid_info()['column'] == pos[0]:
                                        print('you tried moving in to another piece')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return

                    # if its you first move you can move the pawn 2 squares
                    if c.grid_info()['row'] == 6:
                        if save_pos[1] - 2 == pos[1]:
                            if save_pos[0] == pos[0]:
                                print('You moved 2 squares')

                                c.grid(row=pos[1], column=pos[0])
                                get_color()
                                c.config(bg=color)
                                selected = False
                                white = False
                                return

                    # Lets you upgrade the pawn if you reach the other side
                    if c.grid_info()['row'] == 1:
                        if save_pos[1] - pos[1] == 1:
                            global upp_win
                            print('you can now upgrade you pawn')

                            uppgrade_window()


                    # Makes the pawn be able to move forward
                    if save_pos[1] - 1 == pos[1]:
                        if save_pos[0] == pos[0]:
                            print('you moved you pawn forward')

                            c.grid(row=pos[1], column=pos[0])
                            get_color()

                            c.config(bg=color)

                            selected = False
                            white = False

                    # Checks and moves the whitepawns if they are able to capture a black piece
                    for x in black_pieces:
                        if pos[1] == x.grid_info()['row']:
                            if pos[0] == x.grid_info()['column']:
                                if save_pos[0] + 1 == pos[0]:
                                    if save_pos[1] - 1 == pos[1]:
                                        print('you captured an enemies peice (left)')
                                        c.grid(row=x.grid_info()['row'], column=x.grid_info()['column'])
                                        black_pieces.remove(x)
                                        x.destroy()
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = False
                                        break

                    for x in black_pieces:
                        if pos[1] == x.grid_info()['row']:
                            if pos[0] == x.grid_info()['column']:
                                if save_pos[0] - 1 == pos[0]:
                                    if save_pos[1] - 1 == pos[1]:
                                        print('you captured an enemies peice (left)')
                                        c.grid(row=x.grid_info()['row'], column=x.grid_info()['column'])
                                        black_pieces.remove(x)
                                        x.destroy()
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = False
                                        break
                    if pos[1] == c.grid_info()['row']:
                        if pos[0] == c.grid_info()['column']:
                            get_color()
                            c.config(bg=color)
                            selected = False

                if c.cget('text') == 'C':
                    # Makes it so you cant move on you own pieces

                    x = event.x_root - root.winfo_rootx()
                    y = event.y_root - root.winfo_rooty()
                    pos = root.grid_location(x=x, y=y)
                    if save_pos[1] - pos[1] > 0:
                        for x in white_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    selected = False
                                    return

                            if not c.grid_info()['column'] == x.grid_info()['column']:

                                print('They are not in the same row1')
                                # Makes it so you can move
                                if pos[0] == c.grid_info()['column']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(save_pos[1] - pos[1] + 1):

                                    if save_pos[1] == pos[1] + y:
                                        move = True
                                        print(1)

                                        selected = False

                                    if pos[1] + y == x.grid_info()['row']:
                                        if pos[0] == x.grid_info()['column']:
                                            print('You cant make that move your own piece is in the way1')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False

                                            return
                        for x in black_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    return

                            if not c.grid_info()['column'] == x.grid_info()['column']:

                                print('They are not in the same row1')
                                # Makes it so you can move
                                if pos[0] == c.grid_info()['column']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(save_pos[1] - pos[1] + 1):

                                    if save_pos[1] == pos[1] + y:
                                        move = True
                                        print(1)

                                        selected = False

                                    if pos[1] + y == x.grid_info()['row']:
                                        if pos[0] == x.grid_info()['column']:
                                            if pos[1] == x.grid_info()['row']:
                                                if pos[0] == x.grid_info()['column']:
                                                    x.destroy()
                                                    black_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    white = False
                                                    selected = False
                                                    return

                                            print('you cant make that move')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return

                    if save_pos[1] - pos[1] < 0:
                        for x in white_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    selected = False
                                    return

                            if not c.grid_info()['column'] == x.grid_info()['column']:

                                print('They are not in the same row2')
                                # Makes it so you can move
                                if pos[0] == c.grid_info()['column']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(pos[1] - save_pos[1] + 1):

                                    if save_pos[1] == pos[1] - y:
                                        print(2)
                                        move = True
                                        selected = False

                                    if pos[1] - y == x.grid_info()['row']:
                                        if pos[0] == x.grid_info()['column']:
                                            print('You cant make that move your own piece is in the way2')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return
                        for x in black_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    selected = False
                                    return

                            if not c.grid_info()['column'] == x.grid_info()['column']:

                                print('They are not in the same row1')
                                # Makes it so you can move
                                if pos[0] == c.grid_info()['column']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(pos[1] - save_pos[1] + 1):

                                    if save_pos[1] == pos[1] - y:
                                        move = True
                                        print(1)

                                        selected = False

                                    if pos[1] - y == x.grid_info()['row']:
                                        if pos[0] == x.grid_info()['column']:
                                            if pos[1] == x.grid_info()['row']:
                                                if pos[0] == x.grid_info()['column']:
                                                    x.destroy()
                                                    black_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    white = False
                                                    selected = False
                                                    return

                                            print('you cant make that move')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return

                    if save_pos[0] - pos[0] > 0:
                        for x in white_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    selected = False
                                    return

                            if not c.grid_info()['row'] == x.grid_info()['row']:

                                print('They are not in the same row1')
                                # Makes it so you can move
                                if pos[1] == c.grid_info()['row']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(save_pos[0] - pos[0] + 1):

                                    if save_pos[0] == pos[0] + y:
                                        print(3)
                                        move = True

                                        selected = False

                                    if pos[0] + y == x.grid_info()['column']:
                                        if pos[1] == x.grid_info()['row']:
                                            print('You cant make that move your own piece is in the way3')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return

                        for x in black_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    selected = False
                                    return

                            if not c.grid_info()['row'] == x.grid_info()['row']:

                                print('They are not in the same row1')
                                # Makes it so you can move
                                if pos[1] == c.grid_info()['row']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(save_pos[0] - pos[0] + 1):

                                    if save_pos[0] == pos[0] + y:
                                        print(3)
                                        move = True

                                        selected = False

                                    if pos[0] + y == x.grid_info()['column']:
                                        if pos[1] == x.grid_info()['row']:
                                            if pos[1] == x.grid_info()['row']:
                                                if pos[0] == x.grid_info()['column']:
                                                    x.destroy()
                                                    black_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    white = False
                                                    selected = False
                                                    return

                                            print('You cant make that move your own piece is in the way3')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return

                    if save_pos[0] - pos[0] < 0:
                        for x in white_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    selected = False
                                    return

                            if not c.grid_info()['row'] == x.grid_info()['row']:

                                print('They are not in the same row2')
                                # Makes it so you can move
                                if pos[1] == c.grid_info()['row']:
                                    move = True
                                    selected = False



                            else:
                                for y in range(pos[0] - save_pos[0] + 1):

                                    if save_pos[0] == pos[0] - y:
                                        if save_pos[1] == pos[1]:
                                            print(4)
                                            move = True
                                            selected = False

                                    if pos[0] - y == x.grid_info()['column']:
                                        if pos[1] == x.grid_info()['row']:
                                            print('You cant make that move your own piece is in the way4')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return
                        for x in black_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    selected = False
                                    return

                            if not c.grid_info()['row'] == x.grid_info()['row']:

                                print('They are not in the same row2')
                                # Makes it so you can move
                                if pos[1] == c.grid_info()['row']:
                                    move = True
                                    selected = False



                            else:
                                for y in range(pos[0] - save_pos[0] + 1):

                                    if save_pos[0] == pos[0] - y:
                                        if save_pos[1] == pos[1]:
                                            print(4)
                                            move = True
                                            selected = False

                                    if pos[0] - y == x.grid_info()['column']:
                                        if pos[1] == x.grid_info()['row']:
                                            if pos[1] == x.grid_info()['row']:
                                                if pos[0] == x.grid_info()['column']:
                                                    x.destroy()
                                                    black_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    white = False
                                                    selected = False
                                                    return

                                            print('You cant make that move your own piece is in the way4')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return

                    if move:
                        c.grid(row=pos[1], column=pos[0])
                        get_color()
                        c.config(bg=color)
                        move = False
                        white = False

                    # Deselect
                    if c.grid_info()['row'] == pos[1]:
                        if c.grid_info()['column'] == pos[0]:
                            get_color()

                            c.config(bg=color)
                            selected = False

                if c.cget('text') == 'B':

                    x = event.x_root - root.winfo_rootx()
                    y = event.y_root - root.winfo_rooty()
                    pos = root.grid_location(x=x, y=y)
                    if pos[0] == save_pos[0]:
                        if pos[1] == save_pos[1]:
                            get_color()
                            c.config(bg=color)
                            selected = False
                    # Uppåt Vänster
                    if pos[1] < save_pos[1]:
                        if pos[0] < save_pos[0]:

                            if pos[0] == save_pos[0]:
                                if pos[1] == save_pos[1]:
                                    get_color()
                                    c.config(bg=color)
                                    selected = False

                            # movement
                            if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                move = True

                            for x in white_pieces:
                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(save_pos[1] - pos[1] + 1):
                                    if pos[1] + y == x.grid_info()['row']:
                                        if pos[0] + y == x.grid_info()['column']:
                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return
                            for x in black_pieces:
                                # movement
                                if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                    move = True

                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(save_pos[1] - pos[1] + 1):
                                    if pos[1] + y == x.grid_info()['row']:
                                        if pos[0] + y == x.grid_info()['column']:
                                            if pos[0] == x.grid_info()['column']:
                                                if pos[1] == x.grid_info()['row']:
                                                    x.destroy()
                                                    black_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    selected = False
                                                    white = False

                                                    return

                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return

                    # Uppåt höger
                    if pos[1] < save_pos[1]:
                        if pos[0] > save_pos[0]:

                            if pos[0] == save_pos[0]:
                                if pos[1] == save_pos[1]:
                                    get_color()
                                    c.config(bg=color)
                                    selected = False

                            # movement
                            if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                move = True

                            for x in white_pieces:
                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(save_pos[1] - pos[1] + 1):
                                    if pos[1] + y == x.grid_info()['row']:
                                        if pos[0] - y == x.grid_info()['column']:
                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return

                            for x in black_pieces:
                                # movement
                                if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                    move = True

                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(save_pos[1] - pos[1] + 1):
                                    if pos[1] + y == x.grid_info()['row']:
                                        if pos[0] - y == x.grid_info()['column']:
                                            if pos[0] == x.grid_info()['column']:
                                                if pos[1] == x.grid_info()['row']:
                                                    x.destroy()
                                                    black_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    selected = False
                                                    white = False
                                                    return

                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return

                    # Ned vänster
                    if pos[1] > save_pos[1]:
                        if pos[0] < save_pos[0]:

                            if pos[0] == save_pos[0]:
                                if pos[1] == save_pos[1]:
                                    get_color()
                                    c.config(bg=color)
                                    selected = False

                            # movement
                            if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                move = True

                            for x in white_pieces:
                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(pos[1] - save_pos[1] + 1):
                                    if pos[1] - y == x.grid_info()['row']:
                                        if pos[0] + y == x.grid_info()['column']:
                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return
                            for x in black_pieces:
                                # movement
                                if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                    move = True

                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(pos[1] - save_pos[1] + 1):
                                    if pos[1] - y == x.grid_info()['row']:
                                        if pos[0] + y == x.grid_info()['column']:
                                            if pos[0] == x.grid_info()['column']:
                                                if pos[1] == x.grid_info()['row']:
                                                    x.destroy()
                                                    black_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    selected = False
                                                    white = False

                                                    return

                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return

                    # Ned höger
                    if pos[1] > save_pos[1]:
                        if pos[0] > save_pos[0]:

                            if pos[0] == save_pos[0]:
                                if pos[1] == save_pos[1]:
                                    get_color()
                                    c.config(bg=color)
                                    selected = False

                            # movement
                            if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                move = True

                            for x in white_pieces:
                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(pos[1] - save_pos[1] + 1):
                                    if pos[1] - y == x.grid_info()['row']:
                                        if pos[0] - y == x.grid_info()['column']:
                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return

                        for x in black_pieces:
                            # movement
                            if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                move = True

                            if c.winfo_name() == x.winfo_name():
                                continue

                            for y in range(pos[1] - save_pos[1] + 1):
                                if pos[1] - y == x.grid_info()['row']:
                                    if pos[0] - y == x.grid_info()['column']:
                                        if pos[0] == x.grid_info()['column']:
                                            if pos[1] == x.grid_info()['row']:
                                                x.destroy()
                                                black_pieces.remove(x)
                                                c.grid(row=pos[1], column=pos[0])
                                                get_color()
                                                c.config(bg=color)
                                                selected = False
                                                white = False

                                                return

                    if move:
                        c.grid(row=pos[1], column=pos[0])
                        get_color()
                        c.config(bg=color)
                        selected = False
                        move = False
                        white = False

                if c.cget('text') == 'Q':
                    pass



                if c.cget('text') == 'H':
                    x = event.x_root - root.winfo_rootx()
                    y = event.y_root - root.winfo_rooty()
                    pos = root.grid_location(x=x, y=y)

                    if pos[1] == save_pos[1]:
                        if pos[0] == save_pos[0]:
                            get_color()
                            c.config(bg=color)
                            selected = False
                    if abs(save_pos[1] - pos[1]) == 2:
                        if abs(save_pos[0] - pos[0]) == 1:
                            for x in white_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        print('Du kan inte köra över ditt eget skit')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return
                            for x in black_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        x.destroy()
                                        black_pieces.remove(x)
                                        c.grid(row=pos[1], column=pos[0])
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = False
                                        return

                            c.grid(row=pos[1], column=pos[0])
                            get_color()
                            c.config(bg=color)
                            white = False
                            selected = False

                    if abs(save_pos[0] - pos[0]) == 2:
                        if abs(save_pos[1] - pos[1]) == 1:
                            for x in white_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        print('Du kan inte köra över ditt eget skit')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return

                            for x in black_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        x.destroy()
                                        black_pieces.remove(x)
                                        c.grid(row=pos[1], column=pos[0])
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = False
                                        return

                            c.grid(row=pos[1], column=pos[0])
                            get_color()
                            c.config(bg=color)
                            white = False
                            selected = False

                if c.cget('text') == 'K':
                    x = event.x_root - root.winfo_rootx()
                    y = event.y_root - root.winfo_rooty()
                    pos = root.grid_location(x=x, y=y)

                    if pos[0] == c.grid_info()['column']:
                        if pos[1] == c.grid_info()['row']:
                            get_color()
                            c.config(bg=color)
                            selected = False

                    # Upp Höger och vänster
                    if abs(pos[1] - save_pos[1]) == 1:
                        if abs(pos[0] - save_pos[0]) <= 1:
                            for x in black_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        x.destroy()
                                        black_pieces.remove(x)
                                        c.grid(row=pos[1], column=pos[0])
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = False
                                        return
                            for x in white_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        print('Flytta inte på ditt eget skit')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return

                            c.grid(row=pos[1], column=pos[0])
                            get_color()
                            c.config(bg=color)
                            selected = False
                            white = False

                    if abs(pos[0] - save_pos[0]) == 1:
                        if pos[1] == save_pos[1]:
                            for x in black_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        x.destroy()
                                        black_pieces.remove(x)
                                        c.grid(row=pos[1], column=pos[0])
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = False
                                        return
                            for x in white_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        print('Flytta inte på ditt eget skit')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return

                            c.grid(row=pos[1], column=pos[0])
                            get_color()
                            c.config(bg=color)
                            selected = False
                            white = False


                    #Casteling
                    if pos[1] == 7:
                        if pos[0] == 0:
                            clear = True
                            for c in white_pieces:
                                for x in range(1, 3, 1):
                                    if pos[1] == c.grid_info()['row']:
                                        if x + pos[0] == c.grid_info()['column']:
                                            clear = False
                                            print('Du är ivägen')




                                            break

                            if clear:
                                for q in white_pieces:
                                    if q.cget('text') == 'C':
                                        if q.grid_info()['row'] == 7:
                                            if q.grid_info()['column'] == 0:
                                                q.grid(row=save_pos[1], column=save_pos[0]-1)
                                                get_color()
                                                q.config(bg='#505050')
                                c.grid(row=pos[1], column=pos[0]+1)
                                get_color()
                                c.config(bg=color)
                                white = False
                                selected = False






    if not white:

        if not selected:
            # Selects the piece you choose
            x = event.x_root - root.winfo_rootx()
            y = event.y_root - root.winfo_rooty()
            pos = root.grid_location(x=x, y=y)
            for c in black_pieces:
                if c.grid_info()['column'] == pos[0]:
                    if c.grid_info()['row'] == pos[1]:
                        c.config(bg='orange')
                        selected = True
                        save_pos = pos
                        break
        else:

            if selected:
                if c.cget('text') == 'P':

                    # Checks where you clicked
                    x = event.x_root - root.winfo_rootx()
                    y = event.y_root - root.winfo_rooty()
                    pos = root.grid_location(x=x, y=y)

                    # Makes it so the pawns cant move on to each other
                    for clash in black_pieces:
                        if save_pos[1] + 1 == pos[1]:
                            if save_pos[0] == pos[0]:
                                if clash.grid_info()['row'] == pos[1]:
                                    if clash.grid_info()['column'] == pos[0]:
                                        print('Du försökte flytta till en annans pjäs ruta')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return
                    for clash in white_pieces:
                        if save_pos[1] + 1 == pos[1]:
                            if save_pos[0] == pos[0]:
                                if clash.grid_info()['row'] == pos[1]:
                                    if clash.grid_info()['column'] == pos[0]:
                                        print('Du försökte flytta till en annans pjäs ruta')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return

                    # if its the first move they can move 2 squares
                    if c.grid_info()['row'] == 1:
                        if save_pos[1] + 2 == pos[1]:
                            if save_pos[0] == pos[0]:
                                print('På ditt första drag kan du flytta 2 rutor')
                                c.grid(row=pos[1], column=pos[0])
                                get_color()
                                c.config(bg=color)
                                selected = False
                                white = True
                                pass

                    # When the pawns reach the end they can be upgraded
                    if c.grid_info()['row'] == 6:
                        if save_pos[1] - pos[1] == -1:
                            global upp_win
                            print('you can now upgrade you pawn')

                            uppgrade_window()

                            selected = False
                            white = True
                            pass

                    # Checking and moving the pawn
                    if save_pos[1] + 1 == pos[1]:
                        if save_pos[0] == pos[0]:
                            print('Du flyttade fram ett steg')
                            c.grid(row=pos[1], column=pos[0])
                            get_color()

                            c.config(bg=color)

                            selected = False
                            white = True
                    # Checking and moving if the chosen blackpawn can capture a white pawn
                    for x in white_pieces:
                        if pos[1] == x.grid_info()['row']:
                            if pos[0] == x.grid_info()['column']:
                                if save_pos[0] + 1 == pos[0]:
                                    if save_pos[1] + 1 == pos[1]:
                                        print('you captured an enemies peice (left)')
                                        c.grid(row=x.grid_info()['row'], column=x.grid_info()['column'])
                                        white_pieces.remove(x)
                                        x.destroy()
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = True
                                        break

                    for x in white_pieces:
                        if pos[1] == x.grid_info()['row']:
                            if pos[0] == x.grid_info()['column']:
                                if save_pos[0] - 1 == pos[0]:
                                    if save_pos[1] + 1 == pos[1]:
                                        print('you captured an enemies peice (left)')
                                        c.grid(row=x.grid_info()['row'], column=x.grid_info()['column'])
                                        white_pieces.remove(x)
                                        x.destroy()
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = True
                                        break
                    if pos[1] == c.grid_info()['row']:
                        if pos[0] == c.grid_info()['column']:
                            get_color()
                            c.config(bg=color)
                            selected = False

                if c.cget('text') == 'C':
                    x = event.x_root - root.winfo_rootx()
                    y = event.y_root - root.winfo_rooty()
                    pos = root.grid_location(x=x, y=y)

                    if save_pos[1] - pos[1] > 0:
                        for x in black_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    selected = False
                                    return

                            if not c.grid_info()['column'] == x.grid_info()['column']:

                                print('They are not in the same row1')
                                # Makes it so you can move
                                if pos[0] == c.grid_info()['column']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(save_pos[1] - pos[1] + 1):

                                    if save_pos[1] == pos[1] + y:
                                        move = True
                                        print(1)

                                        selected = False

                                    if pos[1] + y == x.grid_info()['row']:
                                        if pos[0] == x.grid_info()['column']:
                                            print('You cant make that move your own piece is in the way1')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False

                                            return
                        for x in white_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    selected = False
                                    return

                            if not c.grid_info()['column'] == x.grid_info()['column']:

                                print('They are not in the same row1')
                                # Makes it so you can move
                                if pos[0] == c.grid_info()['column']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(save_pos[1] - pos[1] + 1):

                                    if save_pos[1] == pos[1] + y:
                                        move = True
                                        print(1)

                                        selected = False

                                    if pos[1] + y == x.grid_info()['row']:
                                        if pos[0] == x.grid_info()['column']:
                                            if pos[1] == x.grid_info()['row']:
                                                if pos[0] == x.grid_info()['column']:
                                                    x.destroy()
                                                    white_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    white = True
                                                    selected = False
                                                    return

                                            print('you cant make that move')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return

                    if save_pos[1] - pos[1] < 0:
                        for x in black_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    selected = False
                                    return

                            if not c.grid_info()['column'] == x.grid_info()['column']:

                                print('They are not in the same row2')
                                # Makes it so you can move
                                if pos[0] == c.grid_info()['column']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(pos[1] - save_pos[1] + 1):

                                    if save_pos[1] == pos[1] - y:
                                        print(2)
                                        move = True
                                        selected = False

                                    if pos[1] - y == x.grid_info()['row']:
                                        if pos[0] == x.grid_info()['column']:
                                            print('You cant make that move your own piece is in the way2')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return
                        for x in white_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    selected = False
                                    return

                            if not c.grid_info()['column'] == x.grid_info()['column']:

                                print('They are not in the same row1')
                                # Makes it so you can move
                                if pos[0] == c.grid_info()['column']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(pos[1] - save_pos[1] + 1):

                                    if save_pos[1] == pos[1] - y:
                                        move = True
                                        print(1)

                                        selected = False

                                    if pos[1] - y == x.grid_info()['row']:
                                        if pos[0] == x.grid_info()['column']:
                                            if pos[1] == x.grid_info()['row']:
                                                if pos[0] == x.grid_info()['column']:
                                                    x.destroy()
                                                    white_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    white = True
                                                    selected = False
                                                    return

                                            print('you cant make that move')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return

                    if save_pos[0] - pos[0] > 0:
                        for x in black_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    selected = False
                                    return

                            if not c.grid_info()['row'] == x.grid_info()['row']:

                                print('They are not in the same row1')
                                # Makes it so you can move
                                if pos[1] == c.grid_info()['row']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(save_pos[0] - pos[0] + 1):

                                    if save_pos[0] == pos[0] + y:
                                        print(3)
                                        move = True

                                        selected = False

                                    if pos[0] + y == x.grid_info()['column']:
                                        if pos[1] == x.grid_info()['row']:
                                            print('You cant make that move your own piece is in the way3')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return

                        for x in white_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    get_color()
                                    c.config(bg=color)
                                    selected = False
                                    return

                            if not c.grid_info()['row'] == x.grid_info()['row']:

                                print('They are not in the same row1')
                                # Makes it so you can move
                                if pos[1] == c.grid_info()['row']:
                                    move = True

                                    selected = False



                            else:
                                for y in range(save_pos[0] - pos[0] + 1):

                                    if save_pos[0] == pos[0] + y:
                                        print(3)
                                        move = True

                                        selected = False

                                    if pos[0] + y == x.grid_info()['column']:
                                        if pos[1] == x.grid_info()['row']:
                                            if pos[1] == x.grid_info()['row']:
                                                if pos[0] == x.grid_info()['column']:
                                                    x.destroy()
                                                    white_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    white = True
                                                    selected = False
                                                    return

                                            print('You cant make that move your own piece is in the way3')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return

                    if save_pos[0] - pos[0] < 0:
                        for x in black_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')
                                    selected = False
                                    return

                            if not c.grid_info()['row'] == x.grid_info()['row']:

                                print('They are not in the same row2')
                                # Makes it so you can move
                                if pos[1] == c.grid_info()['row']:
                                    move = True
                                    selected = False



                            else:
                                for y in range(pos[0] - save_pos[0] + 1):

                                    if save_pos[0] == pos[0] - y:
                                        if save_pos[1] == pos[1]:
                                            print(4)
                                            move = True
                                            selected = False

                                    if pos[0] - y == x.grid_info()['column']:
                                        if pos[1] == x.grid_info()['row']:
                                            print('You cant make that move your own piece is in the way4')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return
                        for x in white_pieces:
                            if x.winfo_name() == c.winfo_name():
                                continue

                            if c.grid_info()['row'] != pos[1]:
                                if c.grid_info()['column'] != pos[0]:
                                    print('Du försöker flytta diagonalt')

                                    return

                            if not c.grid_info()['row'] == x.grid_info()['row']:

                                print('They are not in the same row2')
                                # Makes it so you can move
                                if pos[1] == c.grid_info()['row']:
                                    move = True
                                    selected = False



                            else:
                                for y in range(pos[0] - save_pos[0] + 1):

                                    if save_pos[0] == pos[0] - y:
                                        if save_pos[1] == pos[1]:
                                            print(4)
                                            move = True
                                            selected = False

                                    if pos[0] - y == x.grid_info()['column']:
                                        if pos[1] == x.grid_info()['row']:
                                            if pos[1] == x.grid_info()['row']:
                                                if pos[0] == x.grid_info()['column']:
                                                    x.destroy()
                                                    white_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    white = True
                                                    selected = False
                                                    return

                                            print('You cant make that move your own piece is in the way4')
                                            get_color()
                                            c.config(bg=color)
                                            selected = False
                                            return

                    if move:
                        c.grid(row=pos[1], column=pos[0])
                        get_color()
                        c.config(bg=color)
                        move = False
                        white = True

                    # Deselect
                    if c.grid_info()['row'] == pos[1]:
                        if c.grid_info()['column'] == pos[0]:
                            get_color()

                            c.config(bg=color)
                            selected = False

                if c.cget('text') == 'B':
                    x = event.x_root - root.winfo_rootx()
                    y = event.y_root - root.winfo_rooty()
                    pos = root.grid_location(x=x, y=y)

                    if pos[0] == save_pos[0]:
                        if pos[1] == save_pos[1]:
                            get_color()
                            c.config(bg=color)
                            selected = False
                    # Uppåt Vänster
                    if pos[1] < save_pos[1]:
                        if pos[0] < save_pos[0]:

                            # movement
                            if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                move = True

                            for x in black_pieces:
                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(save_pos[1] - pos[1] + 1):
                                    if pos[1] + y == x.grid_info()['row']:
                                        if pos[0] + y == x.grid_info()['column']:
                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return
                            for x in white_pieces:
                                # movement
                                if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                    move = True

                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(save_pos[1] - pos[1] + 1):
                                    if pos[1] + y == x.grid_info()['row']:
                                        if pos[0] + y == x.grid_info()['column']:
                                            if pos[0] == x.grid_info()['column']:
                                                if pos[1] == x.grid_info()['row']:
                                                    x.destroy()
                                                    white_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    selected = False
                                                    white = True
                                                    return

                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return

                    # Uppåt höger
                    if pos[1] < save_pos[1]:
                        if pos[0] > save_pos[0]:

                            if pos[0] == save_pos[0]:
                                if pos[1] == save_pos[1]:
                                    get_color()
                                    c.config(bg=color)
                                    selected = False

                            # movement
                            if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                move = True

                            for x in black_pieces:
                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(save_pos[1] - pos[1] + 1):
                                    if pos[1] + y == x.grid_info()['row']:
                                        if pos[0] - y == x.grid_info()['column']:
                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return

                                for x in white_pieces:
                                    # movement
                                    if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                        move = True

                                    if c.winfo_name() == x.winfo_name():
                                        continue

                                    for y in range(save_pos[1] - pos[1] + 1):
                                        if pos[1] + y == x.grid_info()['row']:
                                            if pos[0] - y == x.grid_info()['column']:
                                                if pos[0] == x.grid_info()['column']:
                                                    if pos[1] == x.grid_info()['row']:
                                                        x.destroy()
                                                        white_pieces.remove(x)
                                                        c.grid(row=pos[1], column=pos[0])
                                                        get_color()
                                                        c.config(bg=color)
                                                        selected = False
                                                        white = True
                                                        return

                                                print('Du flyttar mot din egen pjäs')
                                                get_color()
                                                c.config(bg=color)
                                                move = False
                                                selected = False
                                                return

                    # Ned vänster
                    if pos[1] > save_pos[1]:
                        if pos[0] < save_pos[0]:

                            if pos[0] == save_pos[0]:
                                if pos[1] == save_pos[1]:
                                    get_color()
                                    c.config(bg=color)
                                    selected = False

                            # movement
                            if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                move = True

                            for x in black_pieces:
                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(pos[1] - save_pos[1] + 1):
                                    if pos[1] - y == x.grid_info()['row']:
                                        if pos[0] + y == x.grid_info()['column']:
                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return
                            for x in white_pieces:
                                # movement
                                if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                    move = True

                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(pos[1] - save_pos[1] + 1):
                                    if pos[1] - y == x.grid_info()['row']:
                                        if pos[0] + y == x.grid_info()['column']:
                                            if pos[0] == x.grid_info()['column']:
                                                if pos[1] == x.grid_info()['row']:
                                                    x.destroy()
                                                    white_pieces.remove(x)
                                                    c.grid(row=pos[1], column=pos[0])
                                                    get_color()
                                                    c.config(bg=color)
                                                    selected = False
                                                    white = True

                                                    return

                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return

                    # Ned höger
                    if pos[1] > save_pos[1]:
                        if pos[0] > save_pos[0]:

                            if pos[0] == save_pos[0]:
                                if pos[1] == save_pos[1]:
                                    get_color()
                                    c.config(bg=color)
                                    selected = False

                            # movement
                            if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                move = True

                            for x in black_pieces:
                                if c.winfo_name() == x.winfo_name():
                                    continue

                                for y in range(pos[1] - save_pos[1] + 1):
                                    if pos[1] - y == x.grid_info()['row']:
                                        if pos[0] - y == x.grid_info()['column']:
                                            print('Du flyttar mot din egen pjäs')
                                            get_color()
                                            c.config(bg=color)
                                            move = False
                                            selected = False
                                            return

                        for x in white_pieces:
                            # movement
                            if abs(save_pos[1] - pos[1]) == abs(save_pos[0] - pos[0]):
                                move = True

                            if c.winfo_name() == x.winfo_name():
                                continue

                            for y in range(pos[1] - save_pos[1] + 1):
                                if pos[1] - y == x.grid_info()['row']:
                                    if pos[0] - y == x.grid_info()['column']:
                                        if pos[0] == x.grid_info()['column']:
                                            if pos[1] == x.grid_info()['row']:
                                                x.destroy()
                                                white_pieces.remove(x)
                                                c.grid(row=pos[1], column=pos[0])
                                                get_color()
                                                c.config(bg=color)
                                                selected = False
                                                white = True

                                                return

                    if move:
                        c.grid(row=pos[1], column=pos[0])
                        get_color()
                        c.config(bg=color)
                        selected = False
                        move = False
                        white = True

                if c.cget('text') == 'Q':
                    pass












                if c.cget('text') == 'H':
                    x = event.x_root - root.winfo_rootx()
                    y = event.y_root - root.winfo_rooty()
                    pos = root.grid_location(x=x, y=y)

                    if pos[1] == save_pos[1]:
                        if pos[0] == save_pos[0]:
                            get_color()
                            c.config(bg=color)
                            selected = False
                    if abs(save_pos[1] - pos[1]) == 2:
                        if abs(save_pos[0] - pos[0]) == 1:
                            for x in black_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        print('Du kan inte köra över ditt eget skit')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return
                            for x in white_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        x.destroy()
                                        white_pieces.remove(x)
                                        c.grid(row=pos[1], column=pos[0])
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = True
                                        return

                            c.grid(row=pos[1], column=pos[0])
                            get_color()
                            c.config(bg=color)
                            white = True
                            selected = False

                    if abs(save_pos[0] - pos[0]) == 2:
                        if abs(save_pos[1] - pos[1]) == 1:
                            for x in black_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        print('Du kan inte köra över ditt eget skit')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return

                            for x in white_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        x.destroy()
                                        white_pieces.remove(x)
                                        c.grid(row=pos[1], column=pos[0])
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = True
                                        return

                            c.grid(row=pos[1], column=pos[0])
                            get_color()
                            c.config(bg=color)
                            white = True
                            selected = False

                if c.cget('text') == 'K':
                    x = event.x_root - root.winfo_rootx()
                    y = event.y_root - root.winfo_rooty()
                    pos = root.grid_location(x=x, y=y)

                    if pos[0] == c.grid_info()['column']:
                        if pos[1] == c.grid_info()['row']:
                            get_color()
                            c.config(bg=color)
                            selected = False

                    # Upp Höger och vänster
                    if abs(pos[1] - save_pos[1]) == 1:
                        if abs(pos[0] - save_pos[0]) <= 1:
                            for x in white_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        x.destroy()
                                        white_pieces.remove(x)
                                        c.grid(row=pos[1], column=pos[0])
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = True
                                        return
                            for x in black_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        print('Flytta inte på ditt eget skit')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return

                            c.grid(row=pos[1], column=pos[0])
                            get_color()
                            c.config(bg=color)
                            selected = False
                            white = True

                    if abs(pos[0] - save_pos[0]) == 1:
                        if pos[1] == save_pos[1]:
                            for x in white_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        x.destroy()
                                        white_pieces.remove(x)
                                        c.grid(row=pos[1], column=pos[0])
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        white = True
                                        return

                            for x in black_pieces:
                                if pos[1] == x.grid_info()['row']:
                                    if pos[0] == x.grid_info()['column']:
                                        print('Flytta inte på ditt eget skit')
                                        get_color()
                                        c.config(bg=color)
                                        selected = False
                                        return

                            c.grid(row=pos[1], column=pos[0])
                            get_color()
                            c.config(bg=color)
                            selected = False
                            white = True
                    #Castleing

                    if pos[1] == 0:
                        if pos[0] == 0:
                            clear = True
                            for c in black_pieces:
                                for x in range(1, 3, 1):
                                    if pos[1] == c.grid_info()['row']:
                                        if x + pos[0] == c.grid_info()['column']:
                                            clear = False
                                            print('Du är ivägen')


                                            break

                            if clear:
                                for q in black_pieces:
                                    if q.cget('text') == 'C':
                                        if q.grid_info()['row'] == 0:
                                            if q.grid_info()['column'] == 0:
                                                q.grid(row=save_pos[1], column=save_pos[0]-1)
                                                get_color()
                                                q.config(bg='white')
                                c.grid(row=pos[1], column=pos[0]+1)
                                get_color()
                                c.config(bg=color)
                                white = True
                                selected = False


root.bind('<Button 1>', movement)

root.mainloop()
