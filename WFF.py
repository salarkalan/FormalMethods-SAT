###########################################################################################################
# This class checks if a formula is a well-formed formula or not, based on well-formed formula rules.
# A formula as a String is passed to this class, 
# The out put of this class is a list of string, containing the result of the well-formed formula checking.
###########################################################################################################

import string
from unittest import result
from Limboole import LimbooleExecutor

# list of all alphabet letters
letter_list = list(string.ascii_letters)
# list of allowed operatiors
operator_list = ["&", "|", ">", "<","="]

#wff_algorihtm is a recursive loop that reads the formula and checks each character in sequence.
#It checks the current character and if the next character is valid, based on WFF rules.
#If there is a problem in the formula, it will add the error as String in the errorResult. 
def recursive_loop_algorithm(formula):

    global index
    global errorResult
    global openBracketNumber
    global closeBracketNumber  
           
    if index <= len(formula):

        #Checks if the character is letter
        #=================================
        if formula[index] in letter_list:
            #checks if there is next character
            if (index+1) < len(formula):
                #Checks if the next character is an operator
                if formula[index + 1] in operator_list:
                    index += 1
                    recursive_loop_algorithm(formula)
                #Checks if the next character is a negation 
                elif formula[index + 1] == "!":
                    errorResult.append("This is NOT a Well-formed Formula.")
                    errorResult.append("There is a mistake in part: '"+formula[index]+formula[index+1]+"'")
                    errorResult.append("Negation can NOT be after a propositional atom.")
                #Checks is the next character is a letter
                elif formula[index + 1] in letter_list:
                    errorResult.append("This is NOT a Well-formed Formula.")
                    errorResult.append("There is a mistake in: "+formula[index]+" "+formula[index+1])
                    errorResult.append("Every propositional atom should be defined with ONE letter")
                #Checks if the next character is an open bracket
                elif formula[index + 1] == "(":
                    errorResult.append("This is NOT a Well-formed Formula.")
                    errorResult.append("There is a mistake in: "+formula[index]+formula[index+1])
                    errorResult.append("A propositionla atom and a open bracket '(' can NOT be next to each other\n-without any operator between them.")
                #Checks if the next character is an close bracket
                elif formula[index + 1] == ")":
                    index += 1
                    recursive_loop_algorithm(formula)
                        
        #Checks if the charector is operator
        #===================================
        elif formula[index] in operator_list:
            #Checks if the first character is an operator
            if index == 0:
                errorResult.append("This is NOT a Well-formed Formula.")
                errorResult.append("Formula can NOT starts with operator "+formula[index])
            else:
                #checks if there is next character
                if (index+1) < len(formula):
                    #Checks if the next character is a letter
                    if formula[index + 1] in letter_list:
                        index += 1
                        recursive_loop_algorithm(formula)
                    #Checks if the next character is a negation
                    elif formula[index + 1] == "!":
                        index += 1
                        recursive_loop_algorithm(formula)
                    #Checks if the next character is an operator
                    elif formula[index + 1] in operator_list:
                        errorResult.append("This is NOT a Well-formed Formula.")
                        errorResult.append("There is a problem in part: "+formula[index]+formula[index+1])
                        errorResult.append("Operator "+formula[index]+ " and operator "+formula[index+1]+" can NOT\n-be next to each other "
                        "without any proposetional atom between them.")
                    #Checks if the next character is a open bracket
                    elif formula[index + 1] == "(":
                        index += 1
                        recursive_loop_algorithm(formula)
                    #Checks if the next character is a close bracket
                    elif formula[index + 1] == ")":
                        errorResult.append("This is NOT a Well-formed Formula.")
                        errorResult.append("There is a problem in part: "+formula[index]+formula[index+1])
                        errorResult.append("An operator and a close bracket can NOT be next to each other any\n-propositional atom between them.")    
                #If the character is a operator and it's the last character
                else:
                    errorResult.append("This is NOT a Well-formed Formula.")
                    errorResult.append("Formula can NOT ends with operator "+formula[index])
                        
        #Checks if the charector is a negation
        #=====================================
        elif formula[index] == "!":
            #Checks if the negation is the last character
            if index == len(formula) - 1 :
                errorResult.append("This is NOT a Well-formed Formula.")
                errorResult.append("There is a mistake in: "+formula[index-1]+formula[index])
                errorResult.append("Formula can NOT ends with a negation.")
            #Checks if there is next character
            if (index+1) < len(formula):
                #Checks if the next character is a letter
                if formula[index + 1] in letter_list:
                    index += 1
                    recursive_loop_algorithm(formula)
                #Checks if the next character is an operator
                elif formula[index + 1] in operator_list:
                    errorResult.append("This is NOT a Well-formed Formula.")
                    errorResult.append("There is a mistake in: "+formula[index]+formula[index+1])
                    errorResult.append("Negation can NOT be before operator "+ formula[index+1])
                #Checks if the next charcter is a negation
                elif formula[index + 1]:
                    index += 1
                    recursive_loop_algorithm(formula)
                #Checks if the next character is a open bracket
                elif formula[index + 1] == "(":
                    index += 1
                    recursive_loop_algorithm(formula)
                #Checks if the next character is a close bracket  
                elif formula[index + 1] == ")":
                    errorResult.append("This is NOT a Well-formed Formula.")
                    errorResult.append("There is a mistake in: "+formula[index]+formula[index+1])
                    errorResult.append("A negation can NOT be before a close bracket")
        
        #Checks if the character is a open bracket
        #=========================================
        elif formula[index] == "(":
            #Checks if the open bracket is the last character
            if index == len(formula) - 1 :
                errorResult.append("This is NOT a Well-formed Formula.")
                errorResult.append("There is a mistake in: "+formula[index-1]+formula[index])
                errorResult.append("Formula can NOT ends with an open bracket '('")
            #Checks if there is next character
            if (index+1) < len(formula):
                #Checks if the next character is a letter
                if formula[index + 1] in letter_list:
                    index += 1
                    recursive_loop_algorithm(formula)
                #Checks if the next character is a negation
                elif formula[index + 1] == "!":
                    index += 1
                    recursive_loop_algorithm(formula)
                #Checks if the next character is an operator
                elif formula[index + 1] in operator_list:
                    errorResult.append("This is NOT a Well-formed Formula.")
                    errorResult.append("There is a mistake in: "+formula[index]+formula[index+1])
                    errorResult.append("An open bracket '(' and an operator can NOT be next to each other without\n-any propositional atom between them.")    
                #Checks if the next character is a open bracket
                elif formula[index + 1] == "(":
                    index += 1
                    recursive_loop_algorithm(formula)
                #Checks if the next character is a close bracket  
                elif formula[index + 1] == ")":
                    errorResult.append("This is NOT a Well-formed Formula.")
                    errorResult.append("There is a mistake in: "+formula[index]+formula[index+1])
                    errorResult.append("An open bracket '(' and a close bracket ')' can NOT be next to each other\n-without any propositional atoms and operator between them.")
        
        #Checks if the character is a close bracket
        #==========================================                                             
        elif formula[index] == ")":
            #Checks if the close bracket is the first character
            if index == 0:
                errorResult.append("This is NOT a Well-formed Formula.")
                errorResult.append("There is a mistake in: "+formula[index]+formula[index+1])
                errorResult.append("Formula can NOT starts with a close bracket '(' ")
            #Checks if there is next character
            if (index+1) < len(formula):
                #Checks if the next character is a letter
                if formula[index + 1] in letter_list:
                    errorResult.append("This is NOT a Well-formed Formula.")
                    errorResult.append("There is a mistake in: "+formula[index]+formula[index+1])
                    errorResult.append("A close bracket ')' and a propositional can NOT be next to each other without\n-any operators between them.")
                #Checks if the next character is a negation
                elif formula[index + 1] == "!":
                    errorResult.append("This is NOT a Well-formed Formula.")
                    errorResult.append("There is a mistake in: "+formula[index]+formula[index+1])
                    errorResult.append("A close bracket ')' and a negation can NOT be next to each other without any\n-operators between them.")
                #Checks if the next character is an operator
                elif formula[index + 1] in operator_list:
                    index += 1
                    recursive_loop_algorithm(formula)
                #Checks if the next character is a open bracket
                elif formula[index + 1] == "(":
                    errorResult.append("This is NOT a Well-formed Formula.")
                    errorResult.append("There is a mistake in: "+formula[index]+formula[index+1])
                    errorResult.append("A close bracket ')' and a open bracket '(' can NOT be next to each other without\n-any operators between them.")
                #Checks if the next character is a close bracket  
                elif formula[index + 1] == ")":
                    index += 1
                    recursive_loop_algorithm(formula)

def wff_checker(formula):
    
    originalFormula = formula
    #Removing spaces from the formula
    formula = formula.replace(" ","")
    #Changing the operators for simplicity
    formula = formula.replace("<->","=") 
    formula = formula.replace("->",">")
    formula = formula.replace("<-","<")
    
    global index
    global errorResult
    global openBracketNumber
    global closeBracketNumber
    index = 0
    errorResult = []
    openBracketNumber = 0
    closeBracketNumber = 0

    #Counting elements of the formula
    numberOfAtoms = 0
    for c in formula:
        if c in letter_list:
            numberOfAtoms += 1
        elif c == "(":
            openBracketNumber += 1
        elif c == ")":
            closeBracketNumber += 1        

    #Checks if the formula is empty or not
    if index == len(formula):
        errorResult.append("This is NOT a Well-formed Formula.")
        errorResult.append("Formula can NOT be empty!")
        return errorResult
    
    #Checks if there is an invalid character in formula
    for c in formula:
        if c not in letter_list and c not in ["!","&", "|", ">", "<","=", ")", "("]:
            errorResult.append("This is NOT a Well-formed Formula.")
            errorResult.append("There is an invalid character in formula: " + c)
            return errorResult

    #Checks if the formula contians only operators
    if numberOfAtoms == 0:
        errorResult.append("This is NOT a Well-formed Formula.")
        errorResult.append("Formula must have at least one propositional atom.")
        return errorResult

    #Checks each character of formula recursively based on Well-formed formula rules        
    recursive_loop_algorithm(formula)

    #Checks the number of open brackets and close brackets
    if len(errorResult) == 0:
        if openBracketNumber != closeBracketNumber:
            errorResult.append("This is NOT a Well-formed Formula.")
            errorResult.append("Number of open brackets '(' and close brackets ')' should be equal.")
            if openBracketNumber > closeBracketNumber:
                errorResult.append("There are more open brackets '(' than close brackets ')'")
            else:
                errorResult.append("There are more cloes brackets ')' than open brackets '('")
   
    #As a last check, formula will be checked in "Limboole" and if there is an error, the error will be appended to errorResult.
    if len(errorResult) == 0:
        limbooleCheck = LimbooleExecutor(originalFormula, "s")
        if limbooleCheck.startswith("Limboole call produced errors:"):
            errorResult.append("This is NOT a Well-formed Formula.")
            errorResult.append(limbooleCheck)
    
    #If there is no error and the errorResult is empty, then the formual is a Well-formed formula
    if len(errorResult) == 0:
        errorResult.append("This is a Well-formed Formula.")
        
    return errorResult    