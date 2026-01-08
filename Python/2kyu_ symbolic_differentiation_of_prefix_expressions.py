# In this kata your task is to differentiate a mathematical expression given as a string in prefix notation. The result should be the derivative of the expression returned in prefix notation.

# To simplify things we will use a simple list format made up of parentesis and spaces.

# The expression format is (func arg1) or (op arg1 arg2) where op means operator, func means function and arg1, arg2 are aguments to the operator or function. For example (+ x 1) or (cos x)

# The expressions will always have balanced parentesis and with spaces between list items.

# Expression operators, functions and arguments will all be lowercase.

# Expressions are single variable expressions using x as the variable.

# Expressions can have nested arguments at any depth for example (+ (* 1 x) (* 2 (+ x 1)))

# Examples of prefix notation in this format:

# (+ x 2)        // prefix notation version of x+2

# (* (+ x 3) 5)  // same as 5 * (x + 3)

# (cos (+ x 1))  // same as cos(x+1)

# (^ x 2)        // same as x^2 meaning x raised to power of 2
# The operators and functions you are required to implement are + - * / ^ cos sin tan exp ln where ^ means raised to power of. exp is the exponential function (same as e^x) and ln is the natural logarithm (base e).

# Example of input values and their derivatives:

# (* 1 x) => 1

# (^ x 3) => (* 3 (^ x 2))

# (cos x) => (* -1 (sin x))
# In addition to returning the derivative your solution must also do some simplifications of the result but only what is specified below.

# The returned expression should not have unecessary 0 or 1 factors. For example it should not return (* 1 (+ x 1)) but simply the term (+ x 1) similarly it should not return (* 0 (+ x 1)) instead it should return just 0

# Results with two constant values such as for example (+ 2 2) should be evaluated and returned as a single value 4

# Any argument raised to the zero power should return 1 and if raised to 1 should return the same value or variable. For example (^ x 0) should return 1 and (^ x 1) should return x

# No simplifications are expected for functions like cos, sin, exp, ln... (but their arguments might require a simplification).

# Think recursively and build your answer according to the rules of derivation and sample test cases.

# If you need to diff any test expressions you can use Wolfram Alpha however remember we use prefix format in this kata.

import re

operators = ["sin", "cos", "tan", "exp", "ln"]

def split_expr(s):
    args = []
    buf = ""
    depth = 0

    for c in s:
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1

        if c == ' ' and depth == 0:
            if buf:
                args.append(buf)
                buf = ""
        else:
            buf += c

    if buf:
        args.append(buf)

    return args

def derivative(x):
    if "sin" in x: # sin(x) -> cos(x)
        split = x.find("(") + 1

        if "^" in x:
            num = int(x.split("^")[1])
            split2 = x.find(")")
            return "(* (cos " + x[split:split2] + ") (* " + str(num) + " (^ (sin " + x[split:split2] + ") " + str(num - 1) + ")))"

        try:
            num = int(x[split:-1].split()[1])
            return "(* " + str(num) + " (cos " + x[split:-1] + "))"
        except:
            pass

        try:
            num = int(x[split:-1].split()[2])
            return "(* " + str(num) + " (cos " + x[split:-1] + "))"
        except:
            pass

        return "(cos " + x[split:-1] + ")"      
    
    elif "cos" in x: # cos(x) -> -sin(x)
        split = x.find("(") + 1

        try:
            num = int(x[split:-1].split()[1])
            return "(* " + str(num * -1) + " (sin " + x[split:-1] + "))"
        except:
            pass

        try:
            num = int(x[split:-1].split()[2])
            return "(* " + str(num * -1) + " (sin " + x[split:-1] + "))"
        except:
            pass

        return "(* -1 (sin " + x[split:-1] + "))"

    elif "tan" in x: # tan -> 1/cos^2(x)
        split = x.find("(") + 1

        try:
            num = int(x[split:-1].split()[1])
            return "(/ " + str(num) + " (^ (cos " + x[split:-1] + ") 2))"
        except:
            pass

        try:
            num = int(x[split:-1].split()[2])
            return "(/ " + str(num) + " (^ (cos " + x[split:-1] + ") 2))"
        except:
            pass

        return "(/ 1 (^ (cos " + x[split:-1] + ") 2))"
    elif "exp" in x: # exp -> e^x
        split = x.find("(") + 1

        try:
            num = int(x[split:-1].split()[1])
            return "(* " + str(num) + " (exp " + x[split:-1] + "))"
        except:
            pass

        try:
            num = int(x[split:-1].split()[2])
            return "(* " + str(num) + " (exp " + x[split:-1] + "))"
        except:
            pass

        return "(exp " + x[split:-1] + ")"
    elif "ln" in x: # ln(x) -> 1/x
        split = x.find("(") + 1
        return "(/ 1 " + x[split:-1] + ")"
    elif "^" in x:
        split = x.find("^")
        return "(* " + str((int(x[:split - 1]) if split - 1 != 0 else 1) * int(x[split + 1:])) + " " + ("x" if int(x[split + 1:]) == 2 else "(^ x " + str(int(x[split + 1:]) - 1) + ")") + ")"
    elif "/" in x:
        split = x.find("/")
        return "(/ -" + x[:split] + " (^ " + x[split + 1:] + " 2))"
    elif "x" in x:
        return x[:-1]
    else:
        return "0"

def func3(op, arg1, arg2):
    
    if "(" in arg1:
        fun = False
        for operator in operators:
            if arg1[1:].startswith(operator):
                fun = True
                break
        if fun:
            arg1 = func2(arg1[1:-1].split()[0], arg1[1:-1].split()[1])
        else:
            op1, a, b = split_expr(arg1[1:-1])
            arg1 = func3(op1, a, b)

    if "(" in arg2:
        fun = False
        for operator in operators:
            if arg2[1:].startswith(operator):
                fun = True
                break
        if fun:
            arg2 = func2(arg2[1:-1].split()[0], arg2[1:-1].split()[1])
        else:
            op2, a, b = split_expr(arg2[1:-1])
            arg2 = func3(op2, a, b)
        
    if op == "+":
        if "x" in arg1 and "x" in arg2:
            if "^" in arg1 or "^" in arg2:
                return arg1 + op + arg2
            else:
                if len(arg1) != 1 and len(arg2) != 1:
                    return str(int(arg1[:-1]) + int(arg2[:-1])) + "x" 
                elif len(arg1) != 1 and len(arg2) == 1:
                    return str(int(arg1[:-1]) + 1) + "x" 
                elif len(arg1) == 1 and len(arg2) != 1:
                    return str(int(arg2[:-1]) + 1) + "x" 
                else:
                    return "2x"
        elif "x" in arg1 and "x" not in arg2:
            return arg1 + "+" + arg2
        elif "x" not in arg1 and "x" in arg2:
            return arg2 + "+" + arg1
        else:
            return int(arg1) + int(arg2)
    elif op == "-":
        if "x" in arg1 and "x" in arg2:
            if "^" in arg1 or "^" in arg2:
                return arg1 + op + arg2
            else:
                if len(arg1) != 1 and len(arg2) != 1:
                    return str(int(arg1[:-1]) - int(arg2[:-1])) + "x" 
                elif len(arg1) != 1 and len(arg2) == 1:
                    return str(int(arg1[:-1]) - 1) + "x" 
                elif len(arg1) == 1 and len(arg2) != 1:
                    return str(int(arg2[:-1]) - 1) + "x" 
                else:
                    return "0"
        elif "x" in arg1 and "x" not in arg2:
            return arg1 + "-" + arg2
        elif "x" not in arg1 and "x" in arg2:
            return arg2 + "-" + arg1
        else:
            return int(arg1) - int(arg2)
    elif op == "*":
        if arg1 == "1":
            return arg2
        if arg2 =="1":
            return arg1
        if "x" in arg1 and "x" in arg2:
            if "^" in arg1 and "^" in arg2:
                split1 = arg1.find("^")
                split2 = arg2.find("^")
                return str(int(arg1[:split1 - 1]) * int(arg2[:split2 - 1])) + ("x^" + str(int(arg1[split1 + 1:]) + int(arg2[split2 + 1:])))
            elif "^" in arg1 and "^" not in arg2:
                split1 = arg1.find("^")
                split2 = arg2.find("x")
                return str(int(arg1[:split1 - 1]) * int(arg2[:split2])) + ("x^" + str(int(arg1[split1 + 1:]) + 1))
            elif "^" not in arg1 and "^" in arg2:
                split1 = arg1.find("x")
                split2 = arg2.find("^")
                return str(int(arg1[:split1]) * int(arg2[:split2 - 1])) + ("x^" + str(int(arg2[split2 + 1:]) + 1))
            else:
                return str(int(arg1[:-1]) * int(arg2[:-1])) + "x^2"
        elif "x" in arg1 and "x" not in arg2:
            if arg2 == "1":
                return arg1
            if "^" in arg1:
                split1 = arg1.find("^")
                return str(int((arg1[:split1 - 1] if split1 != 1 else 1)) * arg2) + ("x^" + str(int(arg1[split1 + 1:])))
            else:
                x = arg1.find("x")
                return str((int(arg1[:x]) if len(arg1) != 1 and x != 0 else 1) * int(arg2)) + "x"
        elif "x" not in arg1 and "x" in arg2:
            if arg1 == "1":
                return arg2
            if "^" in arg2:
                split2 = arg2.find("^")
                return str(int((arg2[:split2 - 1] if split2 != 1 else 1)) * arg1) + ("x^" + str(int(arg2[split2 + 1:])))
            else:
                x = arg2.find("x")
                return str(int(arg1) * (int(arg2[:x]) if len(arg2) != 1 and x != 0 else 1)) + "x"
        else:
            return str(int(arg1) * int(arg2))
    elif op == "/":
        if "x" in arg1 and "x" in arg2:
            if "^" in arg1 and "^" in arg2:
                split1 = arg1.find("^")
                split2 = arg2.find("^")
                return str(int(arg1[:split1 - 1]) / int(arg2[:split2 - 1])) + ("x^" + str(int(arg1[split1 + 1:]) - int(arg2[split2 + 1:])))
            elif "^" in arg1 and "^" not in arg2:
                split1 = arg1.find("^")
                split2 = arg2.find("x")
                return str(int(arg1[:split1 - 1]) / int(arg2[:split2])) + ("x" if int(arg1[split1 + 1:]) - 1 == 0 else "x^" + str(int(arg1[split1 + 1:]) - 1))
            elif "^" not in arg1 and "^" in arg2:
                split1 = arg1.find("x")
                split2 = arg2.find("^")
                return str(int(arg1[:split1]) / int(arg2[:split2 - 1])) + ("x" if int(arg2[split2 + 1:]) - 1 == 0 else "x^" + str(int(arg2[split2 + 1:]) - 1))
            else:
                return str(int(arg1) / int(arg2))
        elif "x" in arg1 and "x" not in arg2:
            if "^" in arg1:
                split1 = arg1.find("^")
                return str(int((arg1[:split1 - 1] if split1 != 1 else 1)) / arg2) + ("x^" + str(int(arg1[split1 + 1:])))
            elif "+" in arg1:
                split1 = arg1.find("+")
                return str(int(arg2) / (int(arg1[:split1 - 1]) if split1 != 1 else 1)) + "+" + str(int(arg2) / int(arg1[split1 + 1]))
            elif "-" in arg1:
                split1 = arg1.find("-")
                return str(int(arg2) / (int(arg1[:split1 - 1]) if split1 != 1 else 1)) + "-" + str(int(arg2) / int(arg1[split1 + 1]))
            else:
                x = arg1.find("x")
                return str((int(arg1[:x]) if len(arg1) != 1 and x != 0 else 1) / int(arg2)) + "x"
        elif "x" not in arg1 and "x" in arg2:
            if "^" in arg2:
                split2 = arg2.find("^")
                return str(int((arg2[:split2 - 1] if split2 != 1 else 1)) / arg1) + ("x^" + str(int(arg2[split2 + 1:])))
            else:
                op2, a, b = normalize_expr(arg2)
                return arg1 + op + "(" + op2 + " " + b + " " + a +")"
        else:
            return int(arg1) / int(arg2)
    elif op == "^":
        return arg1 + op + arg2
    
def normalize_expr(s):
    s = s.replace(" ", "")

    if s == "x":
        return "x"

    if re.fullmatch(r'[+-]?\d+', s):
        return s

    m = re.fullmatch(r'([+-]?\d+)x', s)
    if m:
        return ("*", m.group(1), "x")

    m = re.fullmatch(r'x\+([+-]?\d+)', s)
    if m:
        return ("+", "x", m.group(1))

    m = re.fullmatch(r'x-([+-]?\d+)', s)
    if m:
        return ("-", "x", m.group(1))

    m = re.fullmatch(r'x\^([+-]?\d+)', s)
    if m:
        return ("^", "x", m.group(1))

    return None
    
def func2(op, arg):
    
    if "(" in arg:
        fun = False
        for operator in operators:
            if arg[1:].startswith(operator):
                fun = True
                break
        if fun:
            arg = func2(arg[1:-1].split()[0], arg[1:-1].split()[1])
        else:
            op1, a, b = split_expr(arg[1:-1])
            arg = func3(op1, a, b)
            if len(arg) != 1:
                mono = normalize_expr(arg)
            else:
                mono = None
            if mono:
                op1, a, b = mono
                arg = f"({op1} {a} {b})"

    return op + "(" + arg + ")"

def diff(s):
    try:
        s = int(s)
        return "0"
    except:
        pass
    if s == "x":
        return "1"
    
    fun = False
    for operator in operators:
        if s[1:].startswith(operator):
            fun = True
            break
    if fun:
        split = s.find(" ")
        return derivative(func2(s[1:split], s[split + 1:-1]))
    else:
        op, a, b = split_expr(s[1:-1])
        return derivative(func3(op, a, b))