#Programmer: Alfredo Yebra Jr.
#Date:  September 11, 2015
#Description:    This program simulates an RPN (Reverse Polish Notation) Calculator. It implements a stack of 
#       integers and reads a file and determines if the data is an operation or an number value. It then evaluates 
#       an expression and calculates an answer.

from rpn import RPN
import time

def main():
    start_time = time.time()
    print("\n------------  Reverse Polish Notation Calculator  ------------\n")
    #Dict of calculator operation defintions
    operation_dict = {
        'ADD': lambda stack: round(stack[0] + stack[1], 2),  #Add
        'SUB': lambda stack: round(stack[1] - stack[0], 2),  #Subtract
        'DIV': lambda stack: round(stack[1] / stack[0], 2),  #Divide
        'MUL': lambda stack: round(stack[0] * stack[1], 2),  #Multiply
    }

    #Name of the file to be processed
    rpn_file = 'rpn_file.txt'
    #Create Lab1 instance
    rpn = RPN(rpn_file, operation_dict)
    #Process and store file data
    file_data = rpn.get_file_data()
    #Display final answer, and execution time
    rpn.get_result()

    print("\tTime:\t", round(time.time() - start_time, 3), "s")
    print('-' * 62)
main()
