from tkinter import *
from functools import partial  # To prevent unwanted windows


class Start:
    def __init__(self, parent):
        # GUI to get starting balance and stakes

        self.parent = parent
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading
        self.mystery_box_label = Label(self.start_frame,
                                       text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=1)

        # Entry box... (row 1)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=2)

        # Play Button
        self.lowstakes_button = Button(text="Low ($5)", command=lambda: self.to_game(1))
        self.lowstakes_button.grid(row=2, pady=10)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()

        Game(self, stakes, starting_balance)


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)
        self.stakes = stakes
        partner.lowstakes_button.config(state=DISABLED)

        # initialise variables
        self.balance = IntVar()

        # Set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # New Window
        self.new_window = Toplevel()
        self.new_win_frame = Frame(self.new_window, padx=40, pady=20)
        self.new_win_frame.grid()

        # Heading Row
        self.new_win_head = Label(self.new_win_frame, text="Heading", font="Arial 16 bold")
        self.new_win_head.grid(row=0)

        # Balance Label
        self.b_text = Label(self.new_win_frame, text="Balance: {}".format(stakes))
        self.b_text.grid(row=1)

        self.gain_button = Button(self.new_window, padx=10, pady=10, text="Gain", command=self.reveal_boxes)
        self.gain_button.grid(row=3)

    def reveal_boxes(self):

        # retrieve the balance from the initial function...
        current_balance = self.balance.get()

        # Adjust the balance (subtract game cost and add pay out)
        # For testing purposes, add 2

        current_balance += 2

        # Set balance to adjusted balance
        self.balance.set(current_balance)

        # Edit label so user can see their balance
        self.b_text.configure(text="Balance: {}".format(current_balance))
# Main Routine

if __name__ == "__main__":
    root = Tk()
    Start(root)
    root.title("Mystery Box")
    root.mainloop()
