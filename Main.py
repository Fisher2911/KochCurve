import tkinter as tk
from Button_Frame import Button_Frame_Class
from Drawing_Canvas import Canvas_Class
from the_curve_file import the_curve_class

main_dlg = tk.Tk()
main_dlg.title('Your title goes here')
main_dlg.state('zoomed')
main_dlg.resizable(0,0)
main_dlg.update()

main_dlg.rowconfigure(0, weight=1)
main_dlg.rowconfigure(2, weight=1)
main_dlg.columnconfigure(0, weight=1)
main_dlg.columnconfigure(3, weight=1)

maximum_width = main_dlg.winfo_width()
maximum_height = main_dlg.winfo_height()

canvas_width = int(maximum_width*.8)
button_frame_width = maximum_width - canvas_width

the_curve = the_curve_class()
drawing_area = Canvas_Class(the_curve, main_dlg, name='our_canvas', width=canvas_width, height=maximum_height)
# these lines can be here or in the drawing_area __init__ function
# drawing_area.grid(row=1, column=2, sticky='nsew')
# drawing_area.config(bg='white')
# drawing_area.grid_propagate(0)
button_frame = Button_Frame_Class(the_curve, main_dlg, name='button_frame', width=button_frame_width, height=maximum_height)
# these lines can be here or in the button_frame __init__ function
# button_frame = tk.Frame(main_dlg, name='button_frame', width=button_frame_width, height=maximum_height)
# button_frame.grid(row=1, column=1, sticky='nsew')
# button_frame.config(bg='red')
# button_frame.grid_propagate(0)
# one_button = tk.Button(button_frame, text='Press This')
# one_button.grid(row=1, column=1)



main_dlg.mainloop()
