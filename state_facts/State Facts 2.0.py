from tkinter import *
from PIL import ImageTk, Image
state_facts = {
    "Alabama": "\nAbbreviation: AL\nCapital: Montgomery\nAdmission into the Union: December 14, 1819\nNickname: "
               "Yellowhammer State\n",
    "Alaska": "\nAbbreviation: AK\nCapital: Juneau\nAdmission into the Union: January 3, 1959\nNickname: "
              "The Last Frontier\n",
    "Arizona": "\nAbbreviation: AZ\nCapital: Phoenix\nAdmission into the Union: February 14, 1912\nNickname: "
               "The Grand Canyon State\n",
    "Arkansas": "\nAbbreviation: AR\nCapital: Little Rock\nAdmission into the Union: June 15, 1836\nNickname: "
                "The Natural State\n",
    "California": "\nAbbreviation: CA\nCapital: Sacramento\nAdmission into the Union: September 9, 1850\nNickname: "
                  "Golden State\n",
    "Colorado": "\nAbbreviation: CO\nCapital: Denver\nAdmission into the Union: August 1, 1876\nNickname: "
                "The Centennial State\n",
    "Connecticut": "\nAbbreviation: CT\nCapital: Hartford\nAdmission into the Union: January 9, 1788\nNickname: "
                   "The Constitution State\n",
    "Delaware": "\nAbbreviation: DE\nCapital:Dover\nAdmission into the Union: December 7, 1787\nNickname: "
                "The First State\n",
    "Florida": "\nAbbreviation: FL\nCapital: Tallahassee\nAdmission into the Union: March 3, 1845\nNickname: "
               "Sunshine State\n",
    "Georgia": "\nAbbreviation: GA\nCapital: Atlanta\nAdmission into the Union: January 2, 1788\nNickname:"
               " Peach State\n",
    "Hawaii": "\nAbbreviation: HI\nCapital: Honolulu\nAdmission into the Union: August 21, 1959\nNickname: "
              "Aloha State\n",
    "Idaho": "\nAbbreviation: ID\nCapital: Boise\nAdmission into the Union: July 3, 1890\nNickname: Gem State\n",
    "Illinois": "\nAbbreviation: IL\nCapital: Springfield\nAdmission into the Union: December 3, 1818\nNickname: "
                "Prairie State\n",
    "Indiana": "\nAbbreviation: IN\nCapital: Indianapolis\nAdmission into the Union: December 11,1816\nNickname: "
               "Hoosier State\n",
    "Iowa": "\nAbbreviation: IA\nCapital: Des Moines\nAdmission into the Union: December 28, 1846\nNickname: "
            "Hawkeye State\n",
    "Kansas": "\nAbbreviation: KS\nCapital: Topeka\nAdmission into the Union: January 29, 1861\nNickname: "
              "Sunflower State\n",
    "Kentucky": "\nAbbreviation: KT\nCapital: Frankfort\nAdmission into the Union: June 1, 1792\nNickname: "
                "Bluegrass State\n",
    "Louisiana": "\nAbbreviation: LA\nCapital: Baton Rouge\nAdmission into the Union: April 30, 1812\nNickname: "
                 "Pelican State\n",
    "Maine": "\nAbbreviation: ME\nCapital: Augusta\nAdmission into the Union: March 15, 1820\nNickname: "
             "Pine Tree State\n",
    "Maryland": "\nAbbreviation: MD\nCapital: Annapolis\nAdmission into the Union: April 28, 1788\nNickname: "
                "Old Line State\n",
    "Michigan": "\nAbbreviation: MI\nCapital: Lansing\nAdmission into the Union: January 26, 1837\nNickname:"
                " Wolverine State / Great Lakes State\n",
    "Massachusetts": "\nAbbreviation: MA\nCapital: Boston\nAdmission into the Union: February 6, 1788\nNickname: "
                     "Bay State\n",
    "Mississippi": "\nAbbreviation: MS\nCapital: Jackson\nAdmission into the Union: December 10, 1817\nNickname: "
                   "Magnolia State\n",
    "Missouri": "\nAbbreviation: MO\nCapital: Jefferson City\nAdmission into the Union: August 10, 1821\nNickname: "
                "Show Me State\n",
    "Minnesota": "\nAbbreviation: MN\nCapital: Saint Paul\nAdmission into the Union: May 11, 1858\nNickname: "
                 "North Star State / Land of 10,000 Lakes\n",
    "Montana": "\nAbbreviation: MT\nCapital: Helena\nAdmission into the Union: November 8,1889\nNickname: "
               "Treasure State\n",
    "Nebraska": "\nAbbreviation: NE\nCapital: Lincoln\nAdmission into the Union: March 1, 1867\nNickname: "
                "Cornhusker State\n",
    "Nevada": "\nAbbreviation: NV\nCapital: Carson City\nAdmission into the Union: October 31, 1864\nNickname: "
              "The Silver State\n",
    "New Hampshire": "\nAbbreviation: NH\nCapital: Concord\nAdmission into the Union: June 21, 1788\nNickname: "
                     "Granite State\n",
    "New Jersey": "\nAbbreviation: NJ\nCapital: Trenton\nAdmission into the Union: December 18, 1787\nNickname: "
                  "Garden State\n",
    "New Mexico": "\nAbbreviation: NM\nCapital: Santa Fe\nAdmission into the Union: January 6, 1912\nNickname: "
                  "Land of Enchantment\n",
    "New York": "\nAbbreviation: NY\nCapital: Albany\nAdmission into the Union: July 26, 1788\nNickname: "
                "Empire State\n",
    "North Carolina": "\nAbbreviation: NC\nCapital: Raleigh\nAdmission into the Union: November 21, 1789\nNickname: "
                      "Old North State / Tar Heel State\n",
    "North Dakota": "\nAbbreviation: ND\nCapital: Bismarck\nAdmission into the Union: November 2,1889\nNickname: "
                    "Peace Garden State / Flickertail State / Roughrider State\n",
    "Ohio": "\nAbbreviation: OH\nCapital: Columbus\nAdmission into the Union: March 1, 1803\nNickname: Buckeye State\n",
    "Oklahoma": "\nAbbreviation: OK\nCapital: Oklahoma City\nAdmission into the Union: November 16, 1907\nNickname: "
                "Sooner State\n",
    "Oregon": "\nAbbreviation: OR\nCapital: Salem\nAdmission into the Union: February 14, 1859\nNickname: "
              "Beaver State\n",
    "Pennsylvania": "\nAbbreviation: PA\nCapital: Harrisburg\nAdmission into the Union: December 12, 1787\nNickname: "
                    "Keystone State\n",
    "Rhode Island": "\nAbbreviation: RI\nCapital: Providence\nAdmission into the Union: May 29, 1790\nNickname: "
                    "The Ocean State\n",
    "South Carolina": "\nAbbreviation: SC\nCapital: Columbia\nAdmission into the Union: May 23, 1788\nNickname: "
                      "Palmetto State\n",
    "South Dakota": "\nAbbreviation: SD\nCapital: Pierre\nAdmission into the Union: November 2, 1889\nNickname:"
                    " Mount Rushmore State\n",
    "Tennessee": "\nAbbreviation:TN\nCapital: Nashville\nAdmission into the Union: June 1, 1796\nNickname: "
                 "Volunteer State\n",
    "Texas": "\nAbbreviation: TX\nCapital: Austin\nAdmission into the Union: December 29, 1845\nNickname: "
             "Lone Star State\n",
    "Utah": "\nAbbreviation: UT\nCapital: Salt Lake City\nAdmission into the Union: January 4, 1896\nNickname: "
            "The Beehive State\n",
    "Vermont": "\nAbbreviation: VT\nCapital: Montpelier\nAdmission into the Union: March 4, 1791\nNickname: "
               "Green Mountain State\n",
    "Virginia": "\nAbbreviation: VA\nCapital: Richmond\nAdmission into the Union: June 25, 1788\nNickname: "
                "Old Dominion State\n",
    "Washington": "\nAbbreviation: WA\nCapital: Olympia\nAdmission into the Union: November 11, 1889\nNickname: "
                  "The Evergreen State\n",
    "West Virginia": "\nAbbreviation: WV\nCapital: Charleston\nAdmission into the Union: June 20, 1863\nNickname: "
                     "Mountain State\n",
    "Wisconsin": "\nAbbreviation: WI\nCapital: Madison\nAdmission into the Union: May 29, 1848 \nNickname: "
                 "Badger State\n",
    "Wyoming": "\nAbbreviation: WY\nCapital: Cheyenne\nAdmission into the Union: July 10, 1890\nNickname: "
               "Equality State\n"
}


def get_fact():
    state = entry_1.get()
    if len(state.split()) == 2:
        (word_1, word_2) = state.split(" ")
        state = f"{word_1.capitalize()} {word_2.capitalize()}"
    else:
        state = state.capitalize()
    output = state_facts.get(state)
    if state == "":
        facts.set("Please type a state name")
    elif output is None:
        facts.set("Check your spelling")
    else:
        facts.set(output)


# Defining the widgets:
root = Tk()
root.title("State Facts Database")
facts = StringVar()
entry_1 = Entry(root)
label_1 = Label(root, text="Welcome to the State Facts Database!", font="bold")
img = ImageTk.PhotoImage(Image.open(r"USA.png"))
pic = Label(root, image=img)
label_2 = Label(root, text="Enter state name: ")
label_3 = Label(root, textvariable=facts)
button = Button(root, text="Get facts", command=get_fact)
Signature = Label(root, text="Made by Joshua Kitchen 5/16/19. Revised 1/2/20", bd=1, relief=SUNKEN, anchor=W)

# Placing the widgets inside the main window:

label_1.grid(row=0, column=0)
pic.grid(row=1, column=0)
label_2.grid(row=2, column=0)
entry_1.grid(row=3, column=0)
button.grid(row=5, column=0)
label_3.grid(row=6, column=0, padx=10, pady=10)
Signature.grid(row=7, columnspan=10, sticky=W + E)

root.mainloop()
