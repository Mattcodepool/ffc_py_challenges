def arithmetic_arranger(problems, show = False):
  
  if len(problems) > 5:
    return "Error: Too many problems."
  
  first_line = ""
  second_line = ""
  dashes = ""
  results = ""
  
  for prob in problems:
    
    try:
      elem = prob.split()
      first = int(elem[0])
      op = elem[1]
      second = int(elem[2])
      if op != "+" and op != "-":
        return "Error: Operator must be '+' or '-'."
    except:
      return "Error: Numbers must only contain digits."
    
    if first > 9999 or second > 9999:
      return "Error: Numbers cannot be more than four digits."

    if op == "+":
      res = first + second
    else:
      res = first - second
    
    if len(elem[2]) <= len(elem[0]):
      first_line += str("  " + elem[0] + 4*" ")
      second_line += str(op + " "*(1 + len(elem[0]) - len(elem[2])) + elem[2] + 4*" ")
      dashes += str("-"*(2+len(elem[0])) + 4*" ")
      results += str(" "*(2+len(elem[0]) - len(str(res))) + str(res) + 4*" ")
    else:
      first_line += str((2 + len(elem[2]) - len(elem[0]))*" " + elem[0] + 4*" ")
      second_line += str(op + " " + elem[2] + 4*" ")
      dashes += str("-"*(2+len(elem[2])) + 4*" ")
      results += str(" "*(2+len(elem[2]) - len(str(res))) + str(res) + 4*" ")
    
  arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + dashes.rstrip()
    
  if show == True:
    arranged_problems += "\n" + results.rstrip()
    
  return arranged_problems

