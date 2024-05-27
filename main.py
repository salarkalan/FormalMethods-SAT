from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from WFF import wff_checker
from Limboole import LimbooleExecutor 
import string

class MainApp:
    def __init__(self, window):
        self.window = window
        #Window setting
        app_width = 900
        app_height = 550
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width/2) - (app_width/2)
        y = (screen_height/2) - (app_height/2)
        #Putting the window at center of the screen
        self.window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.window.resizable(0,0)
        self.window.title("Formal Method for Software Engineering")

        # top frame
        down_frame = Frame(self.window, width=880, height=60, bg="#0C84A4")
        down_frame.place(x=10, y=10)
        label1 = Label(down_frame, text="SAT Course", font=("Times new roman", 20), background="#0C84A4")
        label1.place(x=20, y=15)
        
        # pages frame
        pages_frame = Frame(self.window, width=880, height=410, bg="#0C84A4")
        pages_frame.place(x=10, y=80)

        #==================
        # page Introduction
        #==================
        pageIntro = Frame(pages_frame)
        pageIntro_label = Label(pageIntro, text="This course provides some teaching materials about SAT solvers and check input"
                                                " \npropositional logic formula for Well-formedness and give feedback to the user."
                                                "\nIt also runs Limboole in background and checks the satisfiability and validity of formula."
                                                "\n\nSome rules exist for using this application:"
                                                "\n\nPropositional variable/atom should be One letter: e.g. a, b, P, Q"
                                                "\nlogical NOT:                     !"
                                                "\nlogical AND:                    &"
                                                "\nlogical OR:                        |"
                                                "\nlogical implication:       - > or < -"
                                                "\nlogical bi-implication:    < - >"
                                                "\nparenthesis:                    ) or ("
                                          ,font=("Times new roman", 18), justify="left")
        pageIntro_label.pack()
        pageIntro.pack()

        #========
        # page 1
        #========
        page1 = Frame(pages_frame)
        page1_label = Label(page1, text=" Well-formed formula (WFF)"
                                        "\n\nA Well-formed formula means that the formula belong to the language and make sense in"
                                        "\nthe language or it should be syntactically correct."
                                        "\n\nWell-formed formulas are:"
                                        "\n\n                           - propositional atoms p, q, r, …"
                                        "\n                           - ¬ ϕ for well-formed ϕ"
                                        "\n                           - ϕ ^ ψ for well-formed ϕ and ψ"
                                        "\n                           - ϕ v ψ for well-formed ϕ and ψ"
                                        "\n                           - ϕ → ψ for well-formed ϕ and ψ"
                                 ,font=("Times new roman", 18), justify="left")
        page1_label.pack()
       
        #========
        # page 2
        #========
        page2 = Frame(pages_frame)
        page2_label = Label(page2, text="Equivalence and Validity"
                                         "\n\n • φ and ψ are semantically equivalent iff φ ⊧ ψ and ψ ⊧ φ hold. In that"
                                         "\n    case we write φ ≡ ψ."
                                         "\n\n • φ is valid if ⊧ φ holds."
                                 ,font=("Times new roman", 18), justify="left")
        page2_label.pack()

        #========
        # page 3
        #========
        page3 = Frame(pages_frame)
        page3_label = Label(page3, text="SAT solvers"
                                         "\n\n • SAT solvers determine satisfiability for propositional logic formulas."
                                         "\n • They require the input to be in conjunctive normal form (CNF)."
                                         "\n • The satisfiability problem is NP-complete."
                                         "\n\n\nLimboole"
                                         "\n\n• Limboole is a tool to take as input propositional logic formulas"
                                         "\n      • translates to CNF internally"
                                         "\n      • executes a SAT solver"
                                         "\n      • reports validity, satisfiability, and solutions"
                                 ,font=("Times new roman", 18), justify="left")
        page3_label.pack()

        #===================
        # page 4 - The Tool
        #===================
        page4 = Frame(pages_frame)
        page4_label = Label(page4, text="The Tool\n", font=("Times new roman", 20))
        page4_label.grid(row=0, column=0, sticky=W)
        
        page4_input_label = Label(page4, text="Input", font=("Times new roman", 20))
        page4_input_label.grid(row=1, column=0, sticky=W)
        page4_input = Entry(page4, width=25,font=("Times new roman", 20))
        page4_input.grid(row=2, column=0, sticky=NW)

        page4_output_label = Label(page4, text="Output",font=("Times new roman", 20))
        page4_output_label.grid(row=1, column=2, sticky=W)
        page4_output = Label(page4,text="",width=60, height=12, bg="white")
        page4_output.grid(row=2, column=2, sticky=W)

        page4_option_lable = Label(page4, text="WFF/ SAT/ VAL",font=("Times new roman", 18))
        page4_option_lable.grid(row=3, column=0, sticky=W)
        page4_option = ttk.Combobox(page4, values=["Well-formedness Check","Satisfiability Check", "Validity Check"])
        page4_option.grid(row=4, column=0, sticky=W)
        
        def checkAnswer():
            formula = page4_input.get()
            #If there is no formula entered
            if len(formula) == 0:
                messagebox.showerror("Error", "Please enter a formula")
            #Check the formula for Well-formedness
            if page4_option.get() == "Well-formedness Check":
                try:
                    result_wff = wff_checker(formula)
                except:
                    messagebox.showerror("Error", "Invocation of WFF on the following formula failed: " + formula)
                #If the formula is Well-formed
                if len(result_wff) == 1:
                    page4_output = Label(page4,text="",width=60, height=12, bg="white")
                    page4_output.grid(row=2, column=2, sticky=W)
                    answer1_lable = Label(page4_output, text=result_wff[0], width=60, height=11, bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                #else if the formula is NOT Well-fomred and has 2 lines of error
                elif len(result_wff) == 2:
                    page4_output = Label(page4,text="",width=60, height=12, bg="white")
                    page4_output.grid(row=2, column=2, sticky=W)
                    answer1_lable = Label(page4_output, text=result_wff[0],bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    answer2_lable = Label(page4_output, text=result_wff[1], width=60, height=10, bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0,sticky=W)
                #else if the formula is NOT Well-fomred and has 3 lines of error
                elif len(result_wff) == 3:
                    page4_output = Label(page4,text="",width=60, height=12, bg="white")
                    page4_output.grid(row=2, column=2, sticky=W)
                    answer1_lable = Label(page4_output, text=result_wff[0], bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    answer2_lable = Label(page4_output, text=result_wff[1], bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0,sticky=W)
                    answer3_lable = Label(page4_output, text=result_wff[2], width=60, height=9, bg="white", anchor=NW)
                    answer3_lable.grid(row=2, column=0,sticky=W)
            #Check the formula for Satisfiability    
            elif page4_option.get() == "Satisfiability Check":
                try:
                    result_wff = wff_checker(formula)
                except:
                    messagebox.showerror("Error", "Invocation of WFF on the following formula failed: " + formula)
                #If the formula is Well-fromed
                if len(result_wff) == 1:
                    page4_output = Label(page4,text="",width=60, height=12, bg="white")
                    page4_output.grid(row=2, column=2, sticky=W)
                    answer1_lable = Label(page4_output, text=result_wff[0],bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    try:
                        result_limboole = LimbooleExecutor(formula, "s")
                        answer2_lable = Label(page4_output, text=result_limboole, width=60, height=10, bg="white", anchor=NW)
                        answer2_lable.grid(row=1, column=0,sticky=W)
                    except:
                        messagebox.showerror("Error", "Invocation of Limboole on the following formula failed: " + formula)
                else:
                    #else if the formula is NOT Well-fomred and has 2 lines of error
                    if len(result_wff) == 2:
                        page4_output = Label(page4,text="",width=60, height=12, bg="white")
                        page4_output.grid(row=2, column=2, sticky=W)
                        answer1_lable = Label(page4_output, text="Formula should be Well-formed for Satisfiability Check.",bg="white", anchor=NW)
                        answer1_lable.grid(row=0, column=0,sticky=W)
                        answer2_lable = Label(page4_output, text=result_wff[0],bg="white", anchor=NW)
                        answer2_lable.grid(row=1, column=0,sticky=W)
                        answer3_lable = Label(page4_output, text=result_wff[1], width=60, height=9, bg="white", anchor=NW)
                        answer3_lable.grid(row=2, column=0,sticky=W)
                    #else if the formula is NOT Well-fomred and has 3 lines of error
                    elif len(result_wff) == 3:
                        page4_output = Label(page4,text="",width=60, height=12, bg="white")
                        page4_output.grid(row=2, column=2, sticky=W)
                        answer1_lable = Label(page4_output, text="Formula should be Well-formed for Satisfiability Check.",bg="white", anchor=NW)
                        answer1_lable.grid(row=0, column=0,sticky=W)
                        answer2_lable = Label(page4_output, text=result_wff[0], bg="white", anchor=NW)
                        answer2_lable.grid(row=1, column=0,sticky=W)
                        answer3_lable = Label(page4_output, text=result_wff[1], bg="white", anchor=NW)
                        answer3_lable.grid(row=2, column=0,sticky=W)
                        answer4_lable = Label(page4_output, text=result_wff[2], width=60, height=7, bg="white", anchor=NW)
                        answer4_lable.grid(row=3, column=0,sticky=W)
            #Check the formula for Validity
            elif page4_option.get() == "Validity Check" :
                try:
                    result_wff = wff_checker(formula)
                except:
                    messagebox.showerror("Error", "Invocation of WFF on the following formula failed: " + formula)
                #If the formula is Well-formed
                if len(result_wff) == 1:
                    page4_output = Label(page4,text="",width=60, height=12, bg="white")
                    page4_output.grid(row=2, column=2, sticky=W)
                    answer1_lable = Label(page4_output, text=result_wff[0],bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    try:
                        result_limboole = LimbooleExecutor(formula, "v")
                        answer2_lable = Label(page4_output, text=result_limboole, width=60, height=10, bg="white", anchor=NW)
                        answer2_lable.grid(row=1, column=0,sticky=W)
                    except:
                        messagebox.showerror("Error", "Invocation of Limboole on the following formula failed: " + formula)
                else:
                    #else if the formula is NOT Well-fomred and has 2 lines of error
                    if len(result_wff) == 2:
                        page4_output = Label(page4,text="",width=60, height=12, bg="white")
                        page4_output.grid(row=2, column=2, sticky=W)
                        answer1_lable = Label(page4_output, text="Formula should be Well-formed for Validity Check.",bg="white", anchor=NW)
                        answer1_lable.grid(row=0, column=0,sticky=W)
                        answer2_lable = Label(page4_output, text=result_wff[0],bg="white", anchor=NW)
                        answer2_lable.grid(row=1, column=0,sticky=W)
                        answer3_lable = Label(page4_output, text=result_wff[1], width=60, height=9, bg="white", anchor=NW)
                        answer3_lable.grid(row=2, column=0,sticky=W)
                    #else if the formula is NOT Well-fomred and has 3 lines of error
                    elif len(result_wff) == 3:
                        page4_output = Label(page4,text="",width=60, height=12, bg="white")
                        page4_output.grid(row=2, column=2, sticky=W)
                        answer1_lable = Label(page4_output, text="Formula should be Well-formed for Validity Check.",bg="white", anchor=NW)
                        answer1_lable.grid(row=0, column=0,sticky=W)
                        answer2_lable = Label(page4_output, text=result_wff[0], bg="white", anchor=NW)
                        answer2_lable.grid(row=1, column=0,sticky=W)
                        answer3_lable = Label(page4_output, text=result_wff[1], bg="white", anchor=NW)
                        answer3_lable.grid(row=2, column=0,sticky=W)
                        answer4_lable = Label(page4_output, text=result_wff[2], width=60, height=7, bg="white", anchor=NW)
                        answer4_lable.grid(row=3, column=0,sticky=W)
            #If there is no option WFF/SAT/VAL selected
            else:
                messagebox.showerror("Error", "Please select WFF/SAT/VAL")

        page4_Run = Button(page4, text="Check",font=("Arial", 12), bg="light blue", command= checkAnswer)
        page4_Run.grid(row=4, column=1, sticky=W)
        
        #================
        # page 5 - Task 1
        #================
        page5 = Frame(pages_frame)
        page5_label = Label(page5, text="Task 1"
                                        "\n\nProvide a Well-formed formula with '3 atoms'.\n"
                                    , font=("Times new roman", 16), justify="left")
        page5_label.grid(row=0, column=0, sticky=W)
        
        page5_input_label = Label(page5, text="Input", font=("Times new roman", 18))
        page5_input_label.grid(row=1, column=0, sticky=W)
        page5_input = Entry(page5, width=20,font=("Times new roman", 24))
        page5_input.grid(row=2, column=0, sticky=NW)

        page5_output_label = Label(page5, text="Output",font=("Times new roman", 18))
        page5_output_label.grid(row=1, column=1, sticky=W)
        page5_output = Label(page5,text="",width=60, height=15, bg="white")
        page5_output.grid(row=2, column=1, sticky=W)
        
        def page5_checkAnswer():
            formula = ""
            formula = page5_input.get()
            if len(formula) == 0:
                messagebox.showerror("Error", "Please enter a formula")
            #Checking the well-formedness of formula
            try:
                result_wff = wff_checker(formula)
            except:
                messagebox.showerror("Error", "Invocation of WFF on the following formula failed: " + formula)

            #Counting number of atoms in formula
            letter_list = list(string.ascii_letters)
            set_atoms = set()  
            for i in formula:
                if i in letter_list:
                    set_atoms.add(i)
            
            #If the formula is Well-formed
            if len(result_wff) == 1:
                #If the formula has right number of atoms
                if len(set_atoms) ==3:
                    page5_output = Label(page5,text="",width=60, height=15, bg="white")
                    page5_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page5_output, text="Your answer is Correct.",bg="white",width=60, height=15, anchor=NW)
                    answer1_lable.grid(row=0, column=0, sticky=W)
                    result_wff.clear()
                #If the formula has NOT right number of atoms
                else:
                    page5_output = Label(page5,text="",width=60, height=15, bg="white")
                    page5_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page5_output, text="Your answer is Wrong!.",bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0, sticky=W)
                    answer2_lable = Label(page5_output, text=result_wff[0],bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0, sticky=W)
                    answer3_lable = Label(page5_output, text="But You should use '3' atoms!",bg="white",width=60, height=12, anchor=NW)
                    answer3_lable.grid(row=2, column=0, sticky=W)
                    result_wff.clear()
            else: 
                #else if the formula is NOT Well-fomred and has 2 lines of error
                if len(result_wff) == 2:
                    page5_output = Label(page5,text="",width=60, height=15, bg="white")
                    page5_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page5_output, text=result_wff[0],bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    answer2_lable = Label(page5_output, text=result_wff[1], width=60, height=14, bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0,sticky=W)
                #else if the formula is NOT Well-fomred and has 3 lines of error
                elif len(result_wff) == 3:
                    page5_output = Label(page5,text="",width=60, height=15, bg="white")
                    page5_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page5_output, text=result_wff[0], bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    answer2_lable = Label(page5_output, text=result_wff[1], bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0,sticky=W)
                    answer3_lable = Label(page5_output, text=result_wff[2], width=60, height=12, bg="white", anchor=NW)
                    answer3_lable.grid(row=2, column=0,sticky=W)
                result_wff.clear()
            result_wff.clear()
           
        check_answer_button = Button(page5, text="Check Answer",font=("Arial", 12), bg="light blue", command= page5_checkAnswer)
        check_answer_button.grid(row=2, column=0, sticky=W)

        #================
        # page 6 - Task 2
        #================
        page6 = Frame(pages_frame)
        page6_label = Label(page6, text="Task 2"
                                        "\n\nProvide a Well-formed formula with '2 atoms'\nand '3 different operators'.\n"
                                    , font=("Times new roman", 16), justify="left")
        page6_label.grid(row=0, column=0, sticky=W)
        
        page6_input_label = Label(page6, text="Input", font=("Times new roman", 18))
        page6_input_label.grid(row=1, column=0, sticky=W)
        page6_input = Entry(page6, width=20,font=("Times new roman", 24))
        page6_input.grid(row=2, column=0, sticky=NW)

        page6_output_label = Label(page6, text="Output",font=("Times new roman", 18))
        page6_output_label.grid(row=1, column=1, sticky=W)
        page6_output = Label(page6,text="",width=60, height=15, bg="white")
        page6_output.grid(row=2, column=1, sticky=W)
        
        def page6_checkAnswer():
            formula = ""
            formula = page6_input.get()
            if len(formula) == 0:
                messagebox.showerror("Error", "Please enter a formula")
            #Checking the well-formedness of formula
            try:
                result_wff = wff_checker(formula)
            except:
                messagebox.showerror("Error", "Invocation of WFF on the following formula failed: " + formula)

            #Counting number of atoms and number of operators in formula
            letter_list = list(string.ascii_letters)
            operators_list = ["!", "&", "|", ">", "<", "="]
            formula = formula.replace("<->","=") 
            formula = formula.replace("->",">")
            formula = formula.replace("<-","<")
            set_atoms = set() 
            set_operators = set() 
            for i in formula:
                if i in letter_list:
                    set_atoms.add(i)
                if i in operators_list:
                    set_operators.add(i)    
            #If the formula is Well-formed
            if len(result_wff) == 1:
                #If the formula has right number of atoms and oerators
                if len(set_atoms) ==2 and len(set_operators) == 3:
                    page6_output = Label(page6,text="",width=60, height=15, bg="white")
                    page6_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page6_output, text="Your answer is Correct.",bg="white",width=60, height=15, anchor=NW)
                    answer1_lable.grid(row=0, column=0, sticky=W)
                    result_wff.clear()
                #If the formula has NOT right number of atoms and oerators
                else:
                    page6_output = Label(page6,text="",width=60, height=15, bg="white")
                    page6_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page6_output, text="Your answer is Wrong!.",bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0, sticky=W)
                    answer2_lable = Label(page6_output, text=result_wff[0],bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0, sticky=W)
                    answer3_lable = Label(page6_output, text="But You should use '2 atoms' and '3 different operators' !",bg="white",width=60, height=12, anchor=NW)
                    answer3_lable.grid(row=2, column=0, sticky=W)
                    result_wff.clear()
            else: 
                #else if the formula is NOT Well-fomred and has 2 lines of error
                if len(result_wff) == 2:
                    page6_output = Label(page6,text="",width=60, height=15, bg="white")
                    page6_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page6_output, text=result_wff[0],bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    answer2_lable = Label(page6_output, text=result_wff[1], width=60, height=14, bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0,sticky=W)
                #else if the formula is NOT Well-fomred and has 3 lines of error
                elif len(result_wff) == 3:
                    page6_output = Label(page6,text="",width=60, height=15, bg="white")
                    page6_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page6_output, text=result_wff[0], bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    answer2_lable = Label(page6_output, text=result_wff[1], bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0,sticky=W)
                    answer3_lable = Label(page6_output, text=result_wff[2], width=60, height=12, bg="white", anchor=NW)
                    answer3_lable.grid(row=2, column=0,sticky=W)
                result_wff.clear()
            result_wff.clear()
           
        check_answer_button = Button(page6, text="Check Answer",font=("Arial", 12), bg="light blue", command= page6_checkAnswer)
        check_answer_button.grid(row=2, column=0, sticky=W)

        #=================
        # page 7 - Task 3
        #=================
        page7 = Frame(pages_frame)
        page7_label = Label(page7, text="Task 3"
                                        "\n\nProvide a 'Satisfiable' formula.                       \n"
                                    , font=("Times new roman", 16), justify="left")
        page7_label.grid(row=0, column=0, sticky=W)
        
        page7_input_label = Label(page7, text="Input", font=("Times new roman", 18))
        page7_input_label.grid(row=1, column=0, sticky=W)
        page7_input = Entry(page7, width=20,font=("Times new roman", 24))
        page7_input.grid(row=2, column=0, sticky=NW)

        page7_output_label = Label(page7, text="Output",font=("Times new roman", 18))
        page7_output_label.grid(row=1, column=1, sticky=W)
        page7_output = Label(page7,text="",width=60, height=15, bg="white")
        page7_output.grid(row=2, column=1, sticky=W)
        
        def page7_checkAnswer():
            formula = ""
            formula = page7_input.get()
            if len(formula) == 0:
                messagebox.showerror("Error", "Please enter a formula")
            #Checking the well-formedness of formula
            try:
                result_wff = wff_checker(formula)
            except:
                messagebox.showerror("Error", "Invocation of WFF on the following formula failed: " + formula)
            
            #If the formula is Well-formed
            if len(result_wff) == 1:
                try:
                        result_limboole = LimbooleExecutor(formula, "s")
                except:
                    messagebox.showerror("Error", "Invocation of Limboole on the following formula failed: " + formula)
                #If the formula is Satisfiable
                if result_limboole.startswith("% SATISFIABLE formula"):
                    page7_output = Label(page7,text="",width=60, height=15, bg="white")
                    page7_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page7_output, text="Your answer is Correct.",bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0, sticky=W)
                    answer2_lable = Label(page7_output, text=result_wff[0],bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0, sticky=W)
                    answer3_lable = Label(page7_output, text=result_limboole,bg="white",width=60, height=14, anchor=NW)
                    answer3_lable.grid(row=2, column=0, sticky=W)
                    result_wff.clear()
                #If the formula is NOT Satisfiable
                else:
                    page7_output = Label(page7,text="",width=60, height=15, bg="white")
                    page7_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page7_output, text="Your answer is Wrong!",bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0, sticky=W)
                    answer2_lable = Label(page7_output, text=result_wff[0],bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0, sticky=W)
                    answer3_lable = Label(page7_output, text=result_limboole,bg="white",width=60, height=12, anchor=NW)
                    answer3_lable.grid(row=2, column=0, sticky=W)
                    result_wff.clear()
            else: 
                #else if the formula is NOT Well-fomred and has 2 lines of error
                if len(result_wff) == 2:
                    page7_output = Label(page7,text="",width=60, height=15, bg="white")
                    page7_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page7_output, text="Your answer is Wrong!",bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    answer2_lable = Label(page7_output, text="Formula should be Well-formed for Satisfiability Check.",bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0,sticky=W)
                    answer3_lable = Label(page7_output, text=result_wff[0],bg="white", anchor=NW)
                    answer3_lable.grid(row=2, column=0,sticky=W)
                    answer4_lable = Label(page7_output, text=result_wff[1], width=60, height=13, bg="white", anchor=NW)
                    answer4_lable.grid(row=3, column=0,sticky=W)
                #else if the formula is NOT Well-fomred and has 3 lines of error
                elif len(result_wff) == 3:
                    page7_output = Label(page7,text="",width=60, height=15, bg="white")
                    page7_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page7_output, text="Your answer is Wrong!",bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    answer2_lable = Label(page7_output, text="Formula should be Well-formed for Satisfiability Check.",bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0,sticky=W)
                    answer3_lable = Label(page7_output, text=result_wff[0], bg="white", anchor=NW)
                    answer3_lable.grid(row=2, column=0,sticky=W)
                    answer4_lable = Label(page7_output, text=result_wff[1], bg="white", anchor=NW)
                    answer4_lable.grid(row=3, column=0,sticky=W)
                    answer5_lable = Label(page7_output, text=result_wff[2], width=60, height=11, bg="white", anchor=NW)
                    answer5_lable.grid(row=4, column=0,sticky=W)
                result_wff.clear()
            result_wff.clear()
           
        check_answer_button = Button(page7, text="Check Answer",font=("Arial", 12), bg="light blue", command= page7_checkAnswer)
        check_answer_button.grid(row=2, column=0, sticky=W)
      
        #=================
        # page 8 - Task 4
        #=================
        page8 = Frame(pages_frame)
        page8_label = Label(page8, text="Task 4"
                                        "\n\nProvide a formula φ, where╞ φ holds.            \n"
                                    , font=("Times new roman", 16), justify="left")
        page8_label.grid(row=0, column=0, sticky=W)
        
        page8_input_label = Label(page8, text="Input", font=("Times new roman", 18))
        page8_input_label.grid(row=1, column=0, sticky=W)
        page8_input = Entry(page8, width=20,font=("Times new roman", 24))
        page8_input.grid(row=2, column=0, sticky=NW)

        page8_output_label = Label(page8, text="Output",font=("Times new roman", 18))
        page8_output_label.grid(row=1, column=1, sticky=W)
        page8_output = Label(page8,text="",width=60, height=15, bg="white")
        page8_output.grid(row=2, column=1, sticky=W)
        
        def page8_checkAnswer():
            formula = ""
            formula = page8_input.get()
            if len(formula) == 0:
                messagebox.showerror("Error", "Please enter a formula")
            #Checking the well-formedness of formula
            try:
                result_wff = wff_checker(formula)
            except:
                messagebox.showerror("Error", "Invocation of WFF on the following formula failed: " + formula)
            
            #If the formula is well-formed
            if len(result_wff) == 1:
                try:
                        result_limboole = LimbooleExecutor(formula, "v")
                except:
                    messagebox.showerror("Error", "Invocation of Limboole on the following formula failed: " + formula)
                #If the formula is Satisfiable
                if result_limboole.startswith("% SATISFIABLE formula"):
                    page8_output = Label(page8,text="",width=60, height=15, bg="white")
                    page8_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page8_output, text="Your answer is Correct.",bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0, sticky=W)
                    answer2_lable = Label(page8_output, text=result_wff[0],bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0, sticky=W)
                    answer3_lable = Label(page8_output, text=result_limboole,bg="white",width=60, height=14, anchor=NW)
                    answer3_lable.grid(row=2, column=0, sticky=W)
                    result_wff.clear()
                #If the formula is NOT Satisfiable
                else:
                    page8_output = Label(page8,text="",width=60, height=15, bg="white")
                    page8_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page8_output, text="Your answer is Wrong!",bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0, sticky=W)
                    answer2_lable = Label(page8_output, text=result_wff[0],bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0, sticky=W)
                    answer3_lable = Label(page8_output, text=result_limboole,bg="white",width=60, height=12, anchor=NW)
                    answer3_lable.grid(row=2, column=0, sticky=W)
                    result_wff.clear()
            else: 
                #else if the formula is NOT Well-fomred and has 2 lines of error
                if len(result_wff) == 2:
                    page8_output = Label(page8,text="",width=60, height=15, bg="white")
                    page8_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page8_output, text="Your answer is Wrong!",bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    answer2_lable = Label(page8_output, text="Formula should be Well-formed for Validity Check.",bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0,sticky=W)
                    answer3_lable = Label(page8_output, text=result_wff[0],bg="white", anchor=NW)
                    answer3_lable.grid(row=2, column=0,sticky=W)
                    answer4_lable = Label(page8_output, text=result_wff[1], width=60, height=13, bg="white", anchor=NW)
                    answer4_lable.grid(row=3, column=0,sticky=W)
                #else if the formula is NOT Well-fomred and has 3 lines of error
                elif len(result_wff) == 3:
                    page8_output = Label(page8,text="",width=60, height=15, bg="white")
                    page8_output.grid(row=2, column=1, sticky=W)
                    answer1_lable = Label(page8_output, text="Your answer is Wrong!",bg="white", anchor=NW)
                    answer1_lable.grid(row=0, column=0,sticky=W)
                    answer2_lable = Label(page8_output, text="Formula should be Well-formed for Validity Check.",bg="white", anchor=NW)
                    answer2_lable.grid(row=1, column=0,sticky=W)
                    answer3_lable = Label(page8_output, text=result_wff[0], bg="white", anchor=NW)
                    answer3_lable.grid(row=2, column=0,sticky=W)
                    answer4_lable = Label(page8_output, text=result_wff[1], bg="white", anchor=NW)
                    answer4_lable.grid(row=3, column=0,sticky=W)
                    answer5_lable = Label(page8_output, text=result_wff[2], width=60, height=11, bg="white", anchor=NW)
                    answer5_lable.grid(row=4, column=0,sticky=W)
                result_wff.clear()
            result_wff.clear()
           
        check_answer_button = Button(page8, text="Check Answer",font=("Arial", 12), bg="light blue", command= page8_checkAnswer)
        check_answer_button.grid(row=2, column=0, sticky=W)
    
        #====================
        # main pages settings 
        #====================

        # list of all pages
        pages = [pageIntro, page1, page2, page3, page4, page5, page6, page7, page8]
        global count
        count = 0

        #function for the next_page button
        def move_next_page():
            global count
            if not count > len(pages) - 2:
                for p in pages:
                    p.pack_forget()
                count += 1
                page = pages[count]
                page.pack()

        #function for the back_page button
        def move_back_page():
            global count
            if not count == 0:
                for p in pages:
                    p.pack_forget()
                count -= 1
                page = pages[count]
                page.pack()
   
        #Quit Button in Main page
        quit_button = Button(self.window, text="Quit ", font=("Arial", 14), bg="light blue", command = self.window.destroy)
        quit_button.place(x=90, y=500)
        #Back Button in Main page
        back_button = Button(self.window, text="Back", font=("Arial", 14), bg="light blue", command = move_back_page)
        back_button.place(x=710, y=500)
        #Next Button in Main page
        next_button = Button(self.window, text="Next ", font=("Arial", 14), bg="light blue", command = move_next_page)
        next_button.place(x=800, y=500)
                
def root():
    window = Tk()
    MainApp(window)
    window.mainloop()

if __name__ == "__main__":
    root()  