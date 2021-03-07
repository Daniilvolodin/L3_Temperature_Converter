from tkinter import *
from functools import partial  # To prevent unwanted windows


class Start:
    def __init__(self, parent):
        error_feedback = ""
        # GUI to get starting balance and stakes

        self.parent = parent
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        # Mystery Heading
        self.mystery_box_label = Label(self.start_frame,
                                       text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="Please enter a dollar amount "
                                               "(between $5 and $50) in the box "
                                               "below. Then choose the stakes. "
                                               "The higher the stakes, the more you "
                                               "can win.",
                                          wrap=275, justify=LEFT, padx=10, pady=10)

        self.mystery_instructions.grid(row=1)

        self.entry_error_frame = Frame(self.start_frame, width=12)
        self.entry_error_frame.grid(row=2)
        # Entry box... (row 1)

        self.start_amount_entry = Entry(self.entry_error_frame, font="Arial 19 bold", width=10)
        self.start_amount_entry.grid(row=0)

        self.add_funds = Button(self.entry_error_frame, font="Arial 14 bold",
                                text="Add Funds", command=lambda: self.check_funds())
        self.add_funds.grid(row=0, column=1)

        self.framefinal = Frame(self.entry_error_frame, bg='black')
        self.framefinal.grid(row=1, pady=10)

        self.amount_error_label = Label(fg="black",
                                        font="Arial 9 bold",
                                        justify=LEFT, text="")

        self.amount_error_label.grid(row=0, column=0)
        self.amount_error_label.place(x=20, y=175)

        # Button Frame
        self.button_frame = Frame(self.start_frame)
        self.button_frame.grid(row=3)

        button_font = "Arial 12 bold"

        # Play Button
        self.lowstakes_button = Button(self.button_frame, bg="DarkOrange1", font=button_font, text="Low ($5)",
                                       command=lambda: self.to_game(1))
        self.lowstakes_button.grid(row=0, pady=10, column=0)

        self.midstakes_button = Button(self.button_frame, text="Medium ($10)", font=button_font, bg="yellow",
                                       command=lambda: self.to_game(1))
        self.midstakes_button.grid(row=0, pady=10, column=1, padx=5)

        self.highstakes_button = Button(self.button_frame, text="High ($15)", font=button_font, bg="green1",
                                        command=lambda: self.to_game(1))
        self.highstakes_button.grid(row=0, pady=10, column=2, padx=5)

        self.lowstakes_button.config(state=DISABLED)
        self.midstakes_button.config(state=DISABLED)
        self.highstakes_button.config(state=DISABLED)

        self.help_button = Button(self.button_frame, text="How to Play", bg='grey', fg='white',
                                  font=button_font)
        self.help_button.grid(row=1, pady=10, column=1)

    def check_funds(self):
        starting_balance = self.start_amount_entry.get()

        # Set error background colours (assume there are
        # no errors at the start
        error_back = "coral"
        has_errors = "no"

        # change background to white
        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        self.lowstakes_button.config(state=DISABLED)
        self.midstakes_button.config(state=DISABLED)
        self.highstakes_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, least you can play is $5"

            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "The most you can risk is $50"

            elif starting_balance >= 15:
                # enable all buttons
                self.lowstakes_button.config(state=NORMAL)
                self.midstakes_button.config(state=NORMAL)
                self.highstakes_button.config(state=NORMAL)

            elif starting_balance >= 10:
                # enable low and medium stakes button
                self.lowstakes_button.config(state=NORMAL)
                self.midstakes_button.config(state=NORMAL)

            else:
                self.lowstakes_button.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (no text / decimals)"
        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            # set starting balance to amount entered by user
            self.starting_funds.set(starting_balance)

    def to_game(self, stakes):

        # retrieve starting balance
        starting_balance = self.starting_funds.get()
        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_balance):

        print(stakes)
        print(starting_balance)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    Start(root)
    root.title("Mystery Box")
    root.mainloop()
