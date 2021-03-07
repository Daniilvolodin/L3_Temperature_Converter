class GameStats:
    def __init__(self, partner, game_history, game_stats):
        print(game_history)
        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="Arial 14 bold")
        self.how_heading.grid(row=0)

        help_text = "Choose an amount to play with and then choose the stakes. " \
                    "Higher stakes cost more per round but you can win more as " \
                    "well.\n\n" \
                    "When you enter the play area, you will see three mystery " \
                    "boxes. To reveal the contents of the boxes, click the " \
                    "'Open Boxes' button. If you don't have enough money to play, " \
                    "the button will turn red and you will need to quit the game.\n\n" \
                    "The contents of the boxes will be added to your balance. " \
                    "The boxes could containt...\n\n" \
                    "Low: Lead ($0) | Copper ($1) | Silver ($2) | Gold ($10)\n" \
                    "Medium: Lead ($0) | Copper ($2) | Silver ($4) | Gold ($25)\n" \
                    "High: Lead ($0) | Copper ($5) | Silver ($10) | Gold ($50)\n\n" \
                    "If each box contains gold, you earn $30 (low stakes). If " \
                    "they contained copper, silver and gold, you would receive " \
                    "$13 ($1 + $2 + $10) and so on."

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text, justify=LEFT,
                               wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="grey", fg="white",
                                  font="Arial 15 bold", command=lambda: self.close_help)
        self.dismiss_btn.grid(row=2)

    def close_help(self, partner):
        self.help_box.quit()


class Stats:
    def __init__(self):
        # Formatting variables..
        self.game_stats_list = [50, 6]

        # In actual program this is blank and is populated with user
        # Calculations
        self.round_stats_list = ['silver ($4) | silv']