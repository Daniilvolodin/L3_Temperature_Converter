from tkinter import *
from functools import partial

import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_button = Button(self.start_frame, text="Push", command=self.to_game)
        self.push_button.grid(row=0, pady=10)

    def to_game(self):

        # retrieve starting balance
        starting_balance = 50
        stakes = 1

        self.start_frame.destroy()
        Game(self, stakes, starting_balance)

        root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_balance):

        # Initialise Variables
        self.new_window = Toplevel()

        # If users press cross at top, game quits
        self.new_window.protocol("WM_DELETE_WINDOW", self.to_quit)

        self.balance = IntVar()
        self.balance.set(starting_balance)

        # Get value of stakes (use it as multiplier when calculating winnings
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # List for holding statistics
        self.round_stats_list = []

        # GUI setup
        self.game_frame = Frame(self.new_window)
        self.game_frame.grid(row=0)

        # Heading Row

        # Instructions Label
        self.instructions_label = Label(self.new_window, wrap=300, justify=LEFT,
                                        text="Press <enter> or click the 'Open "
                                             "Boxes' button to reveal the contents "
                                             "of the mystery boxes.", font="Arial 10",
                                        padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes go here (row 2)
        box_text = "Arial 16 bold"
        box_back = "pale green"
        box_width = 5

        photo = PhotoImage(file="question.gif")
        photo.height()
        self.box_frame = Frame(self.new_window)
        self.box_frame.grid(row=2, pady=10)

        self.prize1_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, image=photo, padx=10,
                                  pady=10)
        self.prize1_label.photo = photo
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, padx=10,
                                  pady=10, image=photo)
        self.prize2_label.photo = photo
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, padx=10, pady=10,
                                  image=photo)
        self.prize3_label.photo = photo
        self.prize3_label.grid(row=0, column=2)

        # Play button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes", bg="grey",
                                  font="Arial 15 bold", width=20, padx=10, pady=10,
                                  command=self.reveal_boxes)

        # bind button to <enter> (users can push enter to reveal the boxes)

        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_button.grid(row=3)

        # Balance Label (row 4)
        start_text = "Game Cost: ${} \n""\nHow much " \
                     "will you win?".format(stakes * 5)

        self.balance_label = Label(self.game_frame, font="Arial 12 bold",
                                   fg="green", text=start_text, wrap=300,
                                   justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # Help and Game stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold", bg="grey", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.stats_button = Button(self.help_export_frame, text="Game Stats...",
                                   font="Arial 15 bold", bg="blue", fg="white")
        self.stats_button.grid(row=0, column=1, padx=2)

        # Quit Button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="DarkOrange4", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    def reveal_boxes(self):
        # retrieve the balance from the initial function...
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        backgrounds = []
        prize_pic = []
        for i in range(0, 3):
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = PhotoImage(file="gold_med.gif")
                prize_list = "gold\n(${})".format(5 * stakes_multiplier)
                back_color = "gold"
                round_winnings += 5 * stakes_multiplier

            elif 5 < prize_num <= 25:
                prize = PhotoImage(file="silver_med.gif")
                prize_list = "silver\n(${})".format(2 * stakes_multiplier)
                back_color = "seashell3"
                round_winnings += 2 * stakes_multiplier

            elif 25 < prize_num <= 65:
                prize = PhotoImage(file="copper_med.gif")
                prize_list = "copper\n(${})".format(1 * stakes_multiplier)
                round_winnings += stakes_multiplier
                back_color = "dark goldenrod"
            else:
                prize = PhotoImage(file="lead.gif")
                prize_list = "lead\n($0)"
                back_color = "dim gray"

            prize_pic.append(prize)
            prizes.append(prize_list)
            backgrounds.append(back_color)

        photo1 = prize_pic[0]
        photo2 = prize_pic[1]
        photo3 = prize_pic[2]

        # Display prizes...
        self.prize1_label.config(image=photo1)
        self.prize1_label.photo = photo1

        self.prize2_label.config(image=photo2)
        self.prize2_label.photo = photo2

        self.prize3_label.config(image=photo3)
        self.prize3_label.photo = photo3

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winnings
        current_balance += round_winnings

        # Set balance to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${}\nPayback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier,
                                                          round_winnings,
                                                          current_balance)

        # Add round results to statistics list
        round_summary = "{} | {} | {} - Cost: ${} | " \
                        "Payback: ${} | Current Balance: " \
                        "${}".format(prizes[0], prizes[1], prizes[2],
                                     5 * stakes_multiplier, round_winnings,
                                     current_balance)
        self.round_stats_list.append(round_summary)
        print(self.round_stats_list)

        # Edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.new_window.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current Balance ${}\n" \
                                "Your balance is too low. You can only quit " \
                                "or view your stats.".format(current_balance)

            self.balance_label.config(fg="DarkOrange4", font="Arial 10 bold",
                                      text=balance_statement)

    def to_quit(self):
        root.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    Start(root)
    root.title("Mystery Box")
    root.mainloop()
