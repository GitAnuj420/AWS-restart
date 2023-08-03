# reply = input("Do you need tp ship a package (yes/no)")
# if reply == "yes":
#     print("We can help you ship that package !")
# else:
#     print("Please come back when you need to ship a package. Thank you.")
    
reply2 = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy)")
if reply2 =="stamps":
    print("We have many stamp designs to choose from")
elif reply2 =="enevelope":
    print("We have many envelope designs to choose from")
elif reply2 == "copy":
    copies = input("How many copies would you want. (Enter a number)")
    print("Here are {} copies".format(copies))
else:
    print("Thanku and come again")