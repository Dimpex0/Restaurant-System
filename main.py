import tkinter as tk
from food_and_drinks_classes import *

TABLES = {}
MENU = {
    'Soup': Soup(),
    'Pizza': Pizza(),
    'Chicken': Chicken(),
    'Water': Water(),
    'Cola': Cola(),
    'Beer': Beer(),
    'Wine': Wine()
}

for number in range(1, 21):
    TABLES[number] = {
        'number': number,
        'reserved': False,
        'free': True,
        'bill': 0.00,
        'orders': {}
    }

print(TABLES)


def get_dish_info(dish, bill, table, total_lbl):
    current_dish = MENU[dish]
    if current_dish not in table['orders']:
        table['orders'][current_dish] = 0
    table['orders'][current_dish] += 1
    bill.delete('1.0', 'end')
    total_lbl.configure(text='')

    for order in table['orders']:
        bill.insert('end', order.name + ' X ' + str(table["orders"][order]) + f' - {table["orders"][order]*order.price}' + ' BGN' + '\n')

    table['bill'] += current_dish.price
    total_lbl.configure(text=f'Total - {table["bill"]} BGN')


def create_dish(frame, index, bill, table, total_lbl):
    try:
        dish = list(MENU)[index]
        button = tk.Button(frame, text=dish, width=7, command=lambda: get_dish_info(dish, bill, table, total_lbl))
    except IndexError:
        return None
    return button


def reserve_table(table, button):
    if table['reserved']:
        table['reserved'] = False
        button.configure(bg='green', fg='white', text='Reserve table')
        button.place(x=257)
    else:
        table['reserved'] = True
        button.configure(bg='yellow', fg='black', text='RESERVED')
        button.place(x=265)


def free_table(table, free_button, bill, total_lbl):
    if table['free']:
        free_button.configure(text='Free Table', bg='red', fg='white')
        table['free'] = False
    else:
        bill.delete('1.0', 'end')
        total_lbl.configure(text='Total - 0 BGN')
        table['orders'] = {}
        table['bill'] = 0
        free_button.configure(text='Start Table', bg='green', fg='white')
        table['free'] = True


def open_table(table_number, frame, root_frame, window):
    for widget in frame.winfo_children():
        widget.destroy()

    table = TABLES[table_number]

    table_number_lbl = tk.Label(root_frame, text=f'Table: {table_number}', font=('Helvetica', 18))
    table_number_lbl.place(x=250, y=100)

    bill_frame = tk.Frame(root_frame, bg='lightgrey')
    bill = tk.Text(bill_frame)
    bill.delete('1.0', 'end')
    for order in table['orders']:
        bill.insert('end', order.name + ' X ' + str(table["orders"][order]) + f' - {table["orders"][order]*order.price}' + ' BGN' + '\n')
    bill.place(x=0, y=0, width=195, height=300)
    bill_frame.place(x=350, y=200, width=195, height=300)

    total_lbl = tk.Label(root_frame, text=f'Total - {table["bill"]} BGN', font=('Helvetica', 14))
    total_lbl.place(x=400, y=520)

    menu_frame = tk.Frame(root_frame, bg='grey')
    count = 0
    for r in range(4):
        for c in range(3):
            try:
                create_dish(menu_frame, count, bill, table, total_lbl).grid(row=r, column=c, padx=3, pady=2)
                count += 1
            except AttributeError:
                break
    menu_frame.place(x=50, y=200, width=195, height=300)
    
    if table['free']:
        free_button = tk.Button(root_frame, text='Start Table', bg='green', fg='white',
                                command=lambda: free_table(table, free_button, bill, total_lbl))
        free_button.place(x=265, y=310)
    else:
        free_button = tk.Button(root_frame, text='Free Table', bg='red', fg='white',
                                command=lambda: free_table(table, free_button, bill, total_lbl))
        free_button.place(x=265, y=310)
    
    if table['reserved']:
        reserved_button = tk.Button(root_frame, text='RESERVED', bg='yellow', fg='black',
                                    command=lambda: reserve_table(table, reserved_button))
        reserved_button.place(x=265, y=350)
    else:
        reserved_button = tk.Button(root_frame, text='Reserve Table', bg='green', fg='white',
                                    command=lambda: reserve_table(table, reserved_button))
        reserved_button.place(x=257, y=350)

    back_button = tk.Button(root_frame, text='<-', font=('Helvetica', 25), command=lambda: main_window(window))
    back_button.place(x=25, y=520)


def create_table(frame, table_number, root_frame, window):
    table = TABLES[table_number]
    if table['free'] and not table['reserved']:
        button = tk.Button(frame, text=f'Table {table_number}', width=10, bg='grey', fg='white',
                           command=lambda: open_table(table_number, frame, root_frame, window))
        return button
    elif table['reserved']:
        button = tk.Button(frame, text=f'Table {table_number}', width=10, bg='yellow', fg='black',
                           command=lambda: open_table(table_number, frame, root_frame, window))
        return button
    elif not table['free']:
        button = tk.Button(frame, text=f'Table {table_number}', width=10, bg='green', fg='white',
                           command=lambda: open_table(table_number, frame, root_frame, window))
        return button


def main_window(window):
    root = tk.Frame(window)
    root.place(x=0, y=0, width=600, height=600)

    lbl_name = tk.Label(root, text='Restaurant Name', font=('Helvetica', 25))
    lbl_name.place(x=170, y=50)

    tables_frame = tk.Frame(root)
    tables_frame.place(x=90, y=250, width=500)
    count = 1
    for r in range(4):
        for c in range(5):
            create_table(tables_frame, count, root, window).grid(row=r, column=c, pady=3, padx=2)
            count += 1


if __name__ == '__main__':
    mainWindow = tk.Tk()
    mainWindow.title('Restaurant Name')
    mainWindow.geometry('600x600')
    main_window(mainWindow)
    mainWindow.mainloop()
