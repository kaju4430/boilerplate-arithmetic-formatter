def arithmetic_arranger(problems, display_answer=False):
    
    upper_nums = list()
    lower_nums = list()
    dashes = list()
    answers = list()
    arranged_problems = ""

    #Check to see if number of problems more than four.
    if len(problems) > 5:
        arranged_problems += "Error: Too many problems."
        return arranged_problems

    for problem in problems:

        problem = problem.split()

        #Only addition and subtraction allowed
        print(problem[1])
        if problem[1] != '+':
            if problem[1] != '-':
                arranged_problems += "Error: Operator must be '+' or '-'."
                return arranged_problems

        #Check if operands are numbers
        if problem[0].isnumeric() and problem[2].isnumeric():
            #Only 4 or fewer digits accepted
            if len(problem[0]) <= 4 and len(problem[2]) <= 4:
                #Width is 2 larger than the number of digits of the larger number for space & operator.
                width = max(len(problem[0]), len(problem[2])) + 2
                #Upper number occupies entire width
                upper_nums.append(problem[0].rjust(width))
                #Reduce width by one to append operator to beginning of lower row
                lower_nums.append(problem[1] + problem[2].rjust(width - 1))

                #Calculate answers from strings
                if problem[1] == '+':
                    answers.append(
                        str(int(problem[0]) + int(problem[2])).rjust(width))
                else:
                    answers.append(
                        str(int(problem[0]) - int(problem[2])).rjust(width))

                #Dashes according to width of the problem
                tmp_dash = ""
                while (width > 0):
                    tmp_dash += "-"
                    width -= 1
                dashes.append(tmp_dash)

            else:
                arranged_problems += "Error: Numbers cannot be more than four digits."
                return arranged_problems
        else:
            arranged_problems += "Error: Numbers must only contain digits."
            return arranged_problems

    #Concatenate string with all rows
    arranged_problems += "    ".join(upper_nums) + '\n' + "    ".join(
        lower_nums) + '\n' + "    ".join(dashes)

    if display_answer:
        arranged_problems += '\n' + "    ".join(answers)

    return arranged_problems
