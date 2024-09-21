
from chsh_functions import *

def main():
    '''
           This is a cheatsheet of all the topics.
    Basically come back to this for any general questions.
    '''

    # --------------------------------------------------
    # ------------------- Variables --------------------
    # --------------------------------------------------

    '''
      variables contain some kind of object/data
      they all start out as Null

      common types are ints, doubles, strings, booleans,
      lists, dicts, and Objects/Instances 
    '''

    # --------------------------------------------------
    # --------------- Declaring Integers ---------------
    # --------------------------------------------------

    num = 3
    num2 = 2

    num3 = 3
    num4 = 2


    # --------------------------------------------------
    #  ------------- Basic Math Operators --------------
    # --------------------------------------------------

    sum_of_nums = num + num2       # 5
    diff_of_nums = num - num2      # 1

    product_of_nums = num * num2   # 6
    quotient_of_nums = num / num2  # 0.667

    modulus_of_nums = num % num2   # 1
    power_of_nums = num ** num2    # 9
    root_of_nums = num ** (1/num2) # 1.732


    # --------------------------------------------------
    #  ------------- Faster Math Operators --------------
    # --------------------------------------------------

    num3 += num4                   # addition
    num3, num4 = reset_nums()

    num3 -= num4                   # subtraction
    num3, num4 = reset_nums()

    num3 *= num4                   # multiplication
    num3, num4 = reset_nums()

    num3 /= num4                   # division
    num3, num4 = reset_nums()

    num3 %= num4                   # modulus
    num3, num4 = reset_nums()

    num3 **= num4                  # exponents
    num3, num4 = reset_nums()

    # --------------------------------------------------
    #  ------ Declaring Strings, Lists, & Dicts --------
    # --------------------------------------------------


    my_string = "World"
    my_f_string = f"Hello, {my_string}" # "Hello, World"

    my_list = ["Hello", "World"]
    my_dictionary = {23: "Hello", 82: "World"}

    # Special String Characters:
    # \n (new line), \" or \' (quote as text, not end of string), \\ (single backslash)

    '''   Important Notes abt Strings, Lists, & Dicts

            string '' or ""     is a list of characters with special functions
              - iterate with indeces [0, size-1]
              - loop through it's values just like a list
              - special functions - .lower(), .join(), .upper(), .split()
              - substring with indeces - my_string[0,5] = "Hello"
                  - notice that 0 ("H") is included and 5 (",") is excluded
              - can concatenate with + or +=

            list []       is a list of any object type
              - iterate with indeces [0, size-1]
              - loop through it's values
              - substring with indeces - my_string[0,1] = ["Hello"]
                 - notice that 0 (["Hello"]) is included and 1 (["World"]) is excluded
              - can concatenate with + or +=

            dictionary {}  is a *PAIRED* list of *UNORDERED* objects
              - can't iterate through it!!!
              - key value pair!
              - you find a VALUE using a KEY
              - every key has 1 value! (but that doesn't mean the value can't be a list *wink wink*)
              - example: og sentence - Ben ate Dan's birthday cake
                         task - make a dict that alphabetizes our sentence
                         result - {
                                    "a": ["ate"],
                                    "b": ["Ben", "birthday"],
                                    "c": ["cake"],
                                    "d": ["Dan's"]
                                  }
    '''
        

    # --------------------------------------------------
    # --------------- Declaring Booleans ---------------
    # --------------------------------------------------

    # Booleans are statements/variables that are True or False

    true_b = True
    false_b = False

    true_b2 = not False
    true_b3 = not false_b

    true_and = True and True
    false_and = True and False

    true_or = True or False
    false_or = False or False

    # comparisons

    ex_int = 1

    true_comp = 1 == 1
    true_c2 = 1 > 0
    true_c3 = 1 == ex_int

    # --------------------------------------------------
    # ------------- Input/Print Statements -------------
    # --------------------------------------------------
    ipo_intro()


    # prompt user to input variables
    name = input("name: ")
    grade = input("grade you're going into: ")
    phrase = "Hey , good luck with year"


    # print a generic sentence
    print("Hey, good luck with this upcoming year (generic)")

    # or splice our phrase
    print(phrase[0:4] + name + phrase[4:-4] + grade + phrase[-5:] + " (spliced)")

    # or format in with f string
    print(f"Hey {name}, good luck with {grade} year (f-string)")

    # we can also make a print statement not start a new line by changing the "end" variable
    print("Hey ", end="")
    print(name, end = "")
    print(", good luck with ", end = "")
    print(grade, end="")
    print(" year (end-l)")


    ending()
    # --------------------------------------------------
    # --------------- If-Else Statements ---------------
    # --------------------------------------------------
    if_intro()


    condition = False
    condition_2 = False

    if condition == True:
        print("if case passed")
              
    elif condition_2 == True:
        print("elif case passed")
        
    else:
        print("both if and elif were false")

    # you can replace the conditions with any booleans/boolean phrases
    print("\nplease remember that when you press run, those are the variables considered.\nchanging variables after you press run does nothing until you save+run again")

    ending()
    # --------------------------------------------------
    #  -------------------- Loops ----------------------
    # --------------------------------------------------
    loops_intro()
    ex_list = ["first", "idk", "item", "second to last", "last"]


    # --- While loops ----

    print("generic while results: ", end="")
    condition = True
    while (condition == True):     # generic while 
        do_action()
        condition = check_condition()
    print()

    print("counting while results: ", end="")
    x = 0
    while x < 5:                   # loop counts from 0 to 4 
        print(x, end=", ")
        x += 1
    print()

    print("indexing while results: ", end="")
    i = 0
    while i < len(ex_list):        # loop iterates through each index of list 
        print(ex_list[i], end=", ")
        i+=1
    print("\n")

    # ---- For loops -----

    print("counting for results: ", end="")
    for i in range(10):            # loop counts from 0 to 9 
        print(i, end=", ")    
    print()

    print("iterative for results: ", end="") 
    for i in ex_list:              # loop iterates through each obj in list 
        print(i, end = ", ")
    print()

    print("indexing for results: ", end="")
    for i in range(len(ex_list)):  # loop iterates through each index of list 
        print(ex_list[i], end = ", ")
    print()

    ending()
    # --------------------------------------------------
    # --------------- Error Try & Except ---------------
    # --------------------------------------------------
    try_intro()


    # when you're uncertain if something will throw an error,
    # you can try it in a try/except statement

    while True:
        try:
            number = int(input("Please give me a number (or be a smartass and enter a letter): "))
            print("Oh... you actually entered a number... lame.")
            break
        except ValueError:
            print('Ok, very funny, but seriously...')  
        except Exception as e:
            print(f'Unexpected Error: {e}');
            break 

    # Common Errors to Except include:
    # NameError, ValueError, IndexError, ZeroDivisionError, TypeError, FileNotFoundError


    ending()
    # --------------------------------------------------
    # ------------------- Functions --------------------
    # --------------------------------------------------
    func_intro()

    # when you're coding a big project, you can break it into
    # smaller, easier to understand pieces.

    def prompt_name():
        name = input("name: ")
        return name

    def turn_to_pig_latin(name):
        rearranged = name[1:] + name[0]
        fix_capitalization = rearranged[0].upper() + rearranged[1:].lower()
        pig_latin = fix_capitalization + "ay"
        return pig_latin
        

    # now our code is much more clear
    try:
        name = prompt_name()
        pig_latin = turn_to_pig_latin(name)
        print(f"Hey {name}, did you know your name in pig latin is {pig_latin}?")
    except:
        print("You entered something incorrect... not cool, dude")


    ending()
    # --------------------------------------------------
    # -------------------- Importing -------------------
    # --------------------------------------------------
    import_intro()

    # when you make files with working code, you can import those files
    # there are lots of public libraries and files that are very useful

    import math # just one
    import matplotlib, random # or multiple

    import importing_functions as i_f # or even personal files

    i_f.secret_function()


    ending()
    # --------------------------------------------------
    # ------------- File Writing / Reading -------------
    # --------------------------------------------------
    file_intro()



    ending()
    # --------------------------------------------------
    # ---------------- Classes / Objects ---------------
    # --------------------------------------------------
    class_intro()

    # making classes is a powerful tool for representing objects
    # a class is like a blueprint, an object is like the building
    
    # you can have a blueprint for a dunkin donuts, but then you can build as many dunkin donuts as you want

    class Student:

        # Constructor
        def __init__(self, name, age, grades = None):
            self.name = name
            self.age = age
            self.grades = [] if grades is None else grades

        # Adds individual grades
        def add_grade(self, grade):
            self.grades.append(grade)

        # Prints student info in a legible format
        def print_student(self):
            print(f'\n{self.name} - {self.age} years old:\n{str(self.grades)[1:-1]}')



    ending()







