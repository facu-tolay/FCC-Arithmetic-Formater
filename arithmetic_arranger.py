import re

def arithmetic_arranger(problems, show_result = False):
    arranged_problems = ''
    topLine = ''
    secondLine = ''
    dashLine = ''
    answerLine = ''

    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for problem in problems:
        if re.search('[/*]', problem) is not None:
            return "Error: Operator must be '+' or '-'." 
        elif re.search('[a-zA-Z]', problem) is not None:
            return 'Error: Numbers must only contain digits.'
        
        all_operands = problem.split(' ')
    
        for i in all_operands:
            if len(i) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            
        n1 = all_operands[0] 
        n2 = all_operands[2]
        operand = all_operands[1]

        if operand == '+':
            answer = int(n1) + int(n2)
        else: 
            answer = int(n1) - int(n2)
            
        width = max(len(n1),len(n2)) + 2
        topLine += str(n1.rjust(width))
        secondLine +=  str(operand + n2.rjust(width-1))
        dashLine += str("-" * width)
        answerLine += str(answer).rjust(width)

        if len(problems) > 2:
            topLine += '    '
            secondLine += '    '
            dashLine += '    '
            answerLine += '    '

    if show_result:
        arranged_problems = (topLine + "\n" + secondLine + "\n" + dashLine + "\n" + answerLine)
    else:
        arranged_problems = (topLine + "\n" + secondLine + "\n" + dashLine + "\n")

    return arranged_problems