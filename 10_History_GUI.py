from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:
    def __init__(self, parent):
        # Formatting variables...
        background_colour = "light blue"

        # In actual program this is blank and is populated with user calculations
        self.all_calc_list = ['12 degrees C is 53.6 degrees F',
                                 '43 degrees C is 6.1 degrees F',
                                 '-34 degrees C is -29.2 degrees F',
                                 '-23 degrees C is -30.6 degrees F']

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history Button (row 1)
        self.history_button = Button(self.converter_frame, text="History", padx=10, pady=10,
                                     font=("Arial", "11", "bold"),
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)

class History:
    def __init__(self, partner, calc_history):
        background = "pale green"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box,
                                   bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame,
                                 text="History / Instructions",
                                 font="arial 10 bold",
                                 bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="", justify=LEFT, bg='maroon', width=40, wrap=250,
                                  padx=10, pady=10, font="arial 10 italic")

        self.history_text.grid(row=1)

        history_string = ""

        if len(calc_history) >= 7:
            for i in range(0,7):
                history_string += calc_history[len(calc_history) - i - 1]+"\n"

        else:
            for i in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(i) - 1]+"\n"

                self.history_text.config(text="Here is your calculation history. "
                                              "You can use the export button to "
                                              "save this data to a text file if desired")
        self.calc_label = Label(self.history_frame,
                                text=history_string,
                                bg=background,
                                font="Arial 12",
                                justify=LEFT)
        self.calc_label.grid(row=2)

        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        self.export_button = Button(self.export_dismiss_frame, text="Export", font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", font="Arial 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    app = Converter(root)
    root.mainloop()
