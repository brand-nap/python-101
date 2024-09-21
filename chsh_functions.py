
import random

# My own personal functions... Don't stress about these.
def reset_nums():
    return 3,2

def do_action():
    responses = ["I did an iteration", "another run", "just doin a random action", "codin codin codin", "*insert random response here*"]
    print(random.choice(responses), end=", ")
    
def check_condition():
    return random.choice([True, True, True, True, True, False])

def ending():
    print()
    print()
    print()
    print("----------------------------------------------------")
    print("      Press Enter when you're ready to Move on      ")
    input("----------------------------------------------------")
    
def ipo_intro():
    for i in range(50):
        print()
    intro = ["----------------------------------------------------",
             " This is the section on Input and Print Statements! ",
             "                                                    ",
             "  Please find this section in your cheatsheet, and  ",
             "     press Enter when you're ready to proceed.      ",
             "----------------------------------------------------",
             "",
             ""]
    for i in intro:
        print(i)
    input()

def if_intro():
    for i in range(50):
        print()
    intro = ["----------------------------------------------------",
             "   This is the section on If and Else Statements!   ",
             "                                                    ",
             "  Please find this section in your cheatsheet, and  ",
             "     press Enter when you're ready to proceed.      ",
             "----------------------------------------------------",
             "",
             ""]
    for i in intro:
        print(i)
    input()

def loops_intro():
    for i in range(50):
        print()
    intro = ["----------------------------------------------------",
             "     This is the section on For and While Loops!    ",
             "                                                    ",
             "  Please find this section in your cheatsheet, and  ",
             "     press Enter when you're ready to proceed.      ",
             "----------------------------------------------------",
             "",
             ""]
    for i in intro:
        print(i)
    input()

def try_intro():
    for i in range(50):
        print()
    intro = ["----------------------------------------------------",
             "  This is the section on Try and Except Statements! ",
             "                                                    ",
             "  Please find this section in your cheatsheet, and  ",
             "     press Enter when you're ready to proceed.      ",
             "----------------------------------------------------",
             "",
             ""]
    for i in intro:
        print(i)
    input()

def func_intro():
    for i in range(50):
        print()
    intro = ["----------------------------------------------------",
             "          This is the section on Functions!         ",
             "                                                    ",
             "  Please find this section in your cheatsheet, and  ",
             "     press Enter when you're ready to proceed.      ",
             "----------------------------------------------------",
             "",
             ""]
    for i in intro:
        print(i)
    input()

def file_intro():
    for i in range(50):
        print()
    intro = ["----------------------------------------------------",
             "   This is the section on File Writing / Reading!   ",
             "                                                    ",
             "  Please find this section in your cheatsheet, and  ",
             "     press Enter when you're ready to proceed.      ",
             "----------------------------------------------------",
             "",
             ""]
    for i in intro:
        print(i)
    input()

def class_intro():
    for i in range(50):
        print()
    intro = ["----------------------------------------------------",
             "      This is the section on Classes & Objects!     ",
             "                                                    ",
             "  Please find this section in your cheatsheet, and  ",
             "     press Enter when you're ready to proceed.      ",
             "----------------------------------------------------",
             "",
             ""]
    for i in intro:
        print(i)
    input()

def import_intro():
    for i in range(50):
        print()
    intro = ["----------------------------------------------------",
             "          This is the section on Importing!         ",
             "                                                    ",
             "  Please find this section in your cheatsheet, and  ",
             "     press Enter when you're ready to proceed.      ",
             "----------------------------------------------------",
             "",
             ""]
    for i in intro:
        print(i)
    input()
