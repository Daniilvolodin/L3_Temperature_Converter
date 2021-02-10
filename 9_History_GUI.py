from tkinter import *
# To prevent unwanted windows
from functools import partial
import random

test_list = []


def round_it(to_round):
    if to_round % 1 == 0:
        rounded = int(to_round)
    else:
        rounded = round(to_round, 1)

    return rounded


class Converter:
    def __init__(self):

        # Formatting variables
        background_colour = "light blue"

        # Initialise list to hold calculation history
        self.all_calculations = ['12 degrees C is 53.6 degrees F',
                                 '43 degrees C is 6.1 degrees F',
                                 '-34 degrees C is -29.2 degrees F',
                                 '-23 degrees C is -30.6 degrees F']


        # Converter Frame
        self.converter_frame = Frame(width=300,
                                     bg=background_colour,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font="Arial 16 bold",
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be"
                                             "converted and then push one of the buttons below...",
                                             font="Arial 10 italic",
                                             wrap=250,
                                             justify=LEFT,
                                             bg=background_colour,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame,
                                      width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)
        # Conversion buttons frame (row 3), orchid3 | khaki1
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade",
                                  font="Arial 10 bold",
                                  bg="Khaki1",
                                  padx=10,
                                  pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit",
                                  font="Arial 10 bold",
                                  bg="Orchid1",
                                  padx=10,
                                  pady=10,
                                  command=lambda: self.temp_convert(-273)
                                  )
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame,
                                     font="Arial 14 bold",
                                     fg="purple",
                                     pady=10,
                                     bg=background_colour,
                                     text="Conversion goes here")
        self.converted_label.grid(row=4)

        # History / history button frame (row 5)
        self.hist_history_frame = Frame(self.converter_frame)
        self.hist_history_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_history_frame,
                                       font="Arial 12 bold",
                                       text="Calculation History",
                                       width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.history_button = Button(self.hist_history_frame,
                                     font="Arial 12 bold",
                                     text="history",
                                     width=5)
        self.history_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)
        error = "#ffafaf"  # Pale pink background for when entry box has errors

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            # Check amount is a valid number
            to_convert = float(to_convert)
            has_errors = "no"

            # Convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = round_it(to_convert)
                fahrenheit = round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = round_it(to_convert)
                celsius = round_it(celsius)
                answer = "{} degrees C is {} degrees F".format(to_convert, celsius)

            else:
                # Input is invalid (too cold)
                answer = "Too Cold"
                has_errors = "yes"

            # Display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")

            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add Answer to list for history
            if answer != "Too Cold":
                self.all_calculations.append(answer)
                print(self.all_calculations)

        except ValueError:
            self.converted_label.configure(text="Enter a number", fg="red")
            self.to_convert_entry.configure(bg=error)


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    window = Converter()
    root.mainloop()
