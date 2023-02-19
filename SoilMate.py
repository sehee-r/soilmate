from tkinter import *
from PIL import Image, ImageTk


def ph_level():
    ph = float(phInput.get())

    if ph < 7.0:
        result_label.config(text="Acidic. Vegetables such as carrots, cauliflower, cucumbers, garlic, peppers, potatoes,"
                                 " pumpkins, squash, and tomatoes can grow in pH 5 level in soil. If desired, the soil "
                                 "acidity of 5.5 can be corrected by liming, a process of adding a basic substance to "
                                 "neutralize the pH and achieve the ideal pH of 7. The desired pH level for mineral soil "
                                 "is 6.0 to 7.0. The desired pH level for organic soil is 5.0 to 5.5.")

    elif ph == 7.0:
        result_label.config(text="Neutral. The desired pH level for mineral soil is 6.0 to 7.0. The desired pH level for"
                                 " organic soil is 5.0 to 5.5.")
    else:
        result_label.config(text="Basic. The desired pH level for mineral soil is 6.0 to 7.0. The desired pH level for "
                                 "organic soil is 5.0 to 5.5.")


def cation_ex_cap():
    cecRate = float(cecInput.get())

    if cecRate <= 10:
        result2_label.config(text="Low CEC. A low CEC means that nutrients such as magnesium, sodium,  potassium, and "
                                 "calcium cannot bind well with the soil. Soil in this level of CEC have a low organic "
                                 "matter content, and are poor at retaining nutrients. CEC levels can be increased by "
                                 "adding organic matter, or implementing crop rotation.")
    elif cecRate <= 50:
        result2_label.config(text="High CEC. A high CEC means that nutrients such as magnesium, sodium,  potassium, and "
                                 "calcium bind well with the soil. Soil in this level of CEC have a high organic matter "
                                 "content, and are good at retaining nutrients.")


def phosphorus_soil_test():
    pTest = float(pTestInput.get())
    info1 = "\nTip: Phosphorus is a vital source of nutrients for seed germination and growth of roots. Low phosphorus " \
            "levels lead to poor development of roots and leaves of your crop."

    if pTest < 15:
        result3_label.config(text="Very Low" + info1)
    elif pTest < 31:
        result3_label.config(text="Low" + info1)
    elif pTest < 61:
        result3_label.config(text="Moderate" + info1)
    elif pTest <= 100:
        result3_label.config(text="High" + info1)
    elif pTest > 100:
        result3_label.config(text="Very High" + info1)


def potassium_level_test():
    potLevel = float(potLevelInput.get())
    info2 = "\nTip: Potassium helps with the survival of perennial crops during the winter, and improves growth of the " \
            "plant and resistance to diseases. Potassium levels in soil also influences the taste and colour of produce.\n"

    if potLevel < 20:
        result4_label.config(text="Very Low" + info2)
    elif potLevel < 25:
        result4_label.config(text="Low" + info2)
    elif potLevel < 50:
        result4_label.config(text="Medium" + info2)
    elif potLevel <= 80:
        result4_label.config(text="High" + info2)
    elif potLevel > 80:
        result4_label.config(text="Very High" + info2)


root = Tk()
root.title("SoilMate")
# set dimension and colour of the background
root.geometry("750x850")
root.configure(bg="#c7eef9")

# insert header picture
open = (Image.open("soilmate_logo.png"))
resize_image = open.resize((510, 180))
img = ImageTk.PhotoImage(resize_image)

logo = Label(image=img)
logo.image = img
logo.configure(bg="#c7eef9", highlightbackground="#c7eef9")
logo.pack()


# create a label for user input
label = Label(root, text="Enter the pH value: ", fg="#401807", font=('', 16))
label.configure(bg="#c7eef9", highlightbackground="#c7eef9")
label.pack()
phInput = Entry(root)
phInput.configure(bg="white", fg="black", highlightbackground="#70822f")
phInput.pack()

submitButton = Button(root, text="Submit", command=ph_level)
submitButton.configure(bg="#c7eef9", highlightbackground="#c7eef9")
submitButton.pack()

result_label = Label(root, text="", wraplength=600, bg="#dce897", fg="black")
result_label.pack()


# create label for cation exchange capacity
label = Label(root, text="\nEnter the cation exchange capacity (CEC): ", fg="#401807", font=('', 16))
label.configure(bg="#c7eef9", highlightbackground="#c7eef9")
label.pack()
cecInput = Entry(root)
cecInput.configure(bg="white", fg="black", highlightbackground="#70822f")
cecInput.pack()

submitButton = Button(root, text="Submit", command=cation_ex_cap)
submitButton.configure(bg="#c7eef9", highlightbackground="#c7eef9")
submitButton.pack()

result2_label = Label(root, text="", wraplength=600, bg="#dce897", fg="black")
result2_label.pack()


# create label for phosphorus soil test
label = Label(root, text="\nEnter the Phosphorus Soil Test result in ppm: ", fg="#401807", font=('', 16))
label.configure(bg="#c7eef9", highlightbackground="#c7eef9")
label.pack()
pTestInput = Entry(root)
pTestInput.configure(bg="white", fg="black", highlightbackground="#70822f")
pTestInput.pack()

submitButton = Button(root, text="Submit", command=phosphorus_soil_test)
submitButton.configure(bg="#c7eef9", highlightbackground="#c7eef9")
submitButton.pack()

result3_label = Label(root, text="", wraplength=600, bg="#dce897", fg="black")
result3_label.pack()


# create label for potassium levels
label = Label(root, text="\nEnter the Phosphorus (P) pounds per acre (lb/ac): ", fg="#401807", font=('', 16))
label.configure(bg="#c7eef9", highlightbackground="#c7eef9")
label.pack()
potLevelInput = Entry(root)
potLevelInput.configure(bg="white", fg="black", highlightbackground="#70822f")
potLevelInput.pack()

submitButton = Button(root, text="Submit", command=potassium_level_test)
submitButton.configure(bg="#c7eef9", highlightbackground="#c7eef9")
submitButton.pack()

result4_label = Label(root, text="", wraplength=600, bg="#dce897", fg="black")
result4_label.pack()


root.mainloop()
