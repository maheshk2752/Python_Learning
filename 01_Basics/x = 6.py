#conditional statementes
menu = (input("select one item(biryani , pasta , paneer):"))
if menu == "biryani":
    print("rate = 80 ")
elif menu == "pasta":
    print("rate = 100 ")
elif menu == "paneer":
    print("rate = 500")
else:
    print("out of menu")