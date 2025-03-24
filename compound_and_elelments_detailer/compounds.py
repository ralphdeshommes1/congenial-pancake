from elements import *
from tkinter import *
from new_compounds import *








# compound functions
def compound_element_count(compound_name):
    # I use the list to check if I alrealy provided the information with a  certain element so I dont repeat the same element multiple times
    check = []
    details = ""
    compound = compounds[compound_name]
    for element in compound:
        if element not in check:
            details += f"({compound.count(element)} {element.name})\n"
            check.append(element)
    return(details)
# want to count the amount of elements inside of the compound dictonary so I can use that to calculate other stuff

def compound_element_details(compound_name):
    if compound_name not in compounds:
        return()
    details = ""
    compound = compounds[compound_name]
    details += (f"Compound {compound_name} elemental makeup:\n") 
    details += compound_element_count(compound_name)
    check = []
    for element in compound:     
        if element.name not in check:
            details += (f"{element.name}({element.symbol})\natomic number: {element.atomic_number}\natomic mass: {element.atomic_mass}\n")
            check.append(element.name)
    details += mol_conversion(compound_name)
    return(details)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
          
def mol_conversion(compound_name):
    details = ""
    compound = compounds[compound_name]
    total = 1
    for element in compound:
        total += element.atomic_mass
    
    details += (f"the total mass : {compound_name} {total:.2f}")
    return(details)


def element_details(name):
    details = ""
    details += f"Symbol {element_list[name].symbol}\n"
    details += f"{name} makeup:\n"
    details += f"atomic number: {element_list[name].atomic_number}\n"
    details += f"atomic mass: {element_list[name].atomic_mass}\n"

    return(details)



def main():
    def compound_detail_entry():
        if entry.get() not in compounds:
            label_blank_name.config(font="1",text="Not in the list please try again")
            detail_label.config(text="")
        else: 
            label_blank_name.config(text=f"{entry.get().upper()}")
            detail_label.config(text=f"{compound_element_details(entry.get())}")
        
       
    
    def element_detail_entry():
        if entry.get() not in element_list:  
            label_blank_name.config(font="1",text="Not in the list please try again")
            detail_label.config(text="")
        else:
            label_blank_name.config(font="1", text=f"{entry.get().upper()}")
            detail_label.config(text=f"{element_details(entry.get())}")
        



    window = Tk()
    window.geometry("300x300")
    window.title("Compound/Element details")
    label = Label(window,text="Enter Element or compound")
    label.pack()
    entry = Entry(window)
    entry.pack()
    testing = entry.get()
    print(testing)
    frame = Frame(window)
    frame.pack()
    element_button = Button(frame, text="Element",command=element_detail_entry)
    element_button.pack(side=LEFT)
    compound_button = Button(frame, text="Compound", command= compound_detail_entry)
    compound_button.pack(side=RIGHT)
    label_blank_name = Label(window,font="80")
    label_blank_name.pack()
    detail_label = Label(window)
    detail_label.pack()
    
    window.mainloop()



main()



