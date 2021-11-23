# **** Unit Conversion tool ****
# A GUI unit conversion tool based on Python 3.7/Tkinter library 
# Version: 1.0.0
# 2019
# By: Kodai64
#===============================================================

import tkinter as tk


# **** functions **** 

def result(*args):
    # displays the new (converted) value in 'Result' label when 'Enter' key is pressed or 'Calculate' button is clicked.
    scale = scale_vars.get()
    unit1 = unit1_vars.get()
    unit2 = unit2_vars.get()


    try:
        num_value = float(value_entry.get())
        new_value = num_value * all_units[scale][unit1] / all_units[scale][unit2]


        result_display = tk.Label(root, text = '{:5.5}'.format(new_value), font= 12, width= 12, padx= 3, bg= 'white',
                       relief=tk.GROOVE)

        result_display.place(x=20, y=360)

        unit2_display= tk.Label(root, text = unit2, font= 12, width= 14, padx= 3, anchor= tk.W, relief= tk.GROOVE)
        unit2_display.place (x=140, y= 360)


    except ValueError:
        result_display = tk.Label(root, text = '', font= 12, width= 12, padx= 3, bg= 'white', relief=tk.GROOVE)
        result_display.place(x=20, y=360)


def units(*args):
    # updates 'unit1' and 'unit2' OptionMenus based on the choice in 'scale' menu.

    unit1_options = all_units[scale_vars.get()]
    unit1_vars.set(list(all_units[scale_vars.get()])[0])

    unit1_menu = tk.OptionMenu(root, unit1_vars, *unit1_options)
    unit1_menu.config(anchor= tk.W, font= 12, width= 14)
    unit1_menu.place(x= 110, y= 166)

    unit2_options = all_units[scale_vars.get()]
    unit2_vars.set(list(all_units[scale_vars.get()])[1])

    unit2_menu = tk.OptionMenu(root, unit2_vars, *unit2_options)
    unit2_menu.config(anchor= tk.W, font= 12, width= 14)
    unit2_menu.place(x= 110, y= 206)



# =====================================
# **** dictionary (unit conversion) ****

all_units = {'Length': {'Millimeter': 0.1, 'Centimeter': 1, 'Meter': 100, 'Kilometer': 10**5, 'Inch': 1* 2.54,
                        'Feet': 12* 2.54, 'Yard': 36* 2.54, 'Mile': 63360* 2.54},
             'Area': {'Square millimeter': 1e-6, 'Square centimeter':1e-4, 'Square meter': 1, 'Square kilometer': 1e6,
                      'Square inch': 6.4516e-4, 'Square feet': 0.09290304, 'Square yard': 0.83612736,
                      'Square mile': 2589988, 'Acre': 4046.86, 'Hectare': 1e4},
             'Volume': {'Cubic millimeter': 1e-3, 'Cubic centimeter': 1, 'Cubic meter': 1e6, 'Millilitre': 1,
                        'Litre': 1000, 'Cubic inch': 16.38706, 'Cubic foot': 28316.85, 'Cubic yard': 764554.9,
                        'Fluid ounce': 28.4131},
            }


# =====================================
# **** GUI elements ****
# =====================================

# **** main window ****

root = tk.Tk()
root.title('Units Conversion tool')
root.geometry('300x410+100+100')
root.resizable(False, False)

# to provide a little space above the welcome message
tk.Label(root, height= 0,).pack()

welcome = tk.Label(root, text= 'Unit conversion tool\n  by: Kodai64',
               font= 14, padx = 6, pady= 8, relief=tk.GROOVE)
welcome.pack()


measure_units = tk.Label(root, text= 'Measuring scale', font= 12,)
measure_units.place(x= 10, y= 110)


# =====================================
# **** OptionMenus ****

# 'vars' == 'variables'
scale_vars = tk.StringVar(root)
scale_menu = tk.OptionMenu(root, scale_vars, *list(all_units.keys()), command= units)

scale_menu.config(font= 12, width= 10)
scale_menu.place(x= 140, y= 106)


unit1 = tk.Label(root, text= 'Original unit:', font= 12)
unit1.place(x= 10, y= 170)

unit1_vars = tk.StringVar(root)

unit1_menu = tk.OptionMenu(root, unit1_vars, '')
unit1_menu.config(anchor= tk.W, font= 12, width= 14)
unit1_menu.place(x= 110, y= 166)



unit2 = tk.Label(root, text= 'Convert to:', font= 12)
unit2.place(x= 10, y= 210)

unit2_vars = tk.StringVar(root)

unit2_menu = tk.OptionMenu(root, unit2_vars, '')
unit2_menu.config(anchor= tk.W, font= 12, width= 14)
unit2_menu.place(x= 110, y= 206)


# =====================================
# **** 'value' entry box ****

value = tk.Label(root, text= 'Value:', font= 12)
value.place(x= 10, y= 250)

value_entry = tk.Entry(root, bd= 3)
value_entry.place(x= 110, y= 252)


# =====================================
# **** 'calculate' button + 'result' box ****

calculate = tk.Button(root, text= 'Calculate', font= 12, command= result)
calculate.place(x= 95,y= 295)


result_label= tk.Label(root, text= 'Result:', font= 12)
result_label.place(x= 10, y= 330)


result_display = tk.Label(root, font= 12, width= 12, padx= 3, bg= 'white', relief=tk.GROOVE)
result_display.place(x=20, y=360)

unit2_display= tk.Label(root, font= 12, width= 14, padx= 3, relief= tk.GROOVE)
unit2_display.place (x=140, y= 360)


value_entry.focus()

root.bind('<Return>', result)


root.mainloop()
