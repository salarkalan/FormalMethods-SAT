#############################################################################################################################
# This class Execute a formula in Limboole executor and retures the result as a string   
# Two arguments will be passed to this Method, (formula, "s") for cheking Satisfiability, (formula, "v") for cheking Validity
#############################################################################################################################
import os
import subprocess

# defining the path of Limboole.exe in the Computer, "here the file is in the Project folder"
path = 'limboole.exe'

def LimbooleExecutor(formula, check):
    
  # deleting the files if any exists
  if os.path.exists("in.txt"):
    os.remove("in.txt")
  if os.path.exists("out.txt"):
    os.remove("out.txt")
  if os.path.exists("error.txt"):
    os.remove("error.txt")    

  # creating new files
  inFile = open('in.txt', 'x')
  inFile.close()
  outFile = open('out.txt', 'x')
  outFile.close()
  errorFile = open('error.txt', 'x')
  errorFile.close()

  # writing the formula to inFile- ( Limboole executor only works with text files )
  inFile = open('in.txt', 'w')
  inFile.write(formula)
  inFile.close()

  # check the formula for Satisfiability
  if check == "s":
    execution = subprocess.run([path,'in.txt', '-s'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  # check the formula for Validity
  elif check == "v":
    execution = subprocess.run([path,'in.txt', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

  # writing the output to outFile
  outFile = open('out.txt', 'w')
  outFile.write(execution.stdout.decode())
  outFile.close()
  outFile = open('out.txt', 'r')
  result = outFile.read()
  outFile.close()

  #checking if there is an error while running Limboole
  if len(execution.stderr.decode()) != 0:
    errorFile = open('error.txt', 'w')
    errorFile.write('Limboole call produced errors:\n'+ execution.stderr.decode())
    errorFile.close()
    errorFile = open('error.txt', 'r')
    result = errorFile.read()
    errorFile.close()

  return result