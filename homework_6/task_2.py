
args = input("Введите выражение: ").split()
print(args)
def aka_evat (args):
    while len(args) !=1:
        while "*" in args or "/" in args:
            try:
                prod_index = args.index("*")
            except:
                prod_index = 100
            try:
                div_index = args.index("/")
            except:
                div_index = 100

            if prod_index < div_index:
                args[prod_index - 1] = int(args[prod_index - 1]) * int(args[prod_index + 1])
                args.pop(prod_index + 1)
                args.pop(prod_index)
            else:
                args[div_index - 1] = int(args[div_index - 1]) / int(args[div_index + 1])
                args.pop(div_index + 1)
                args.pop(div_index)

        while "+" in args or "-" in args:
            try:
                sum_index = args.index("+")
            except:
                sum_index = 100
            try:
                deg_index = args.index("-")
            except:
                deg_index = 100

            if sum_index < deg_index:
                args[sum_index - 1] = int(args[sum_index - 1]) + int(args[sum_index + 1])
                args.pop(sum_index + 1)
                args.pop(sum_index)
            else:
                args[deg_index - 1] = int(args[deg_index - 1]) - int(args[deg_index + 1])
                args.pop(deg_index + 1)
                args.pop(deg_index)
    return args[0]

if "(" in args:
    start_index = args.index("(")
    end_index = args.index(")") - 1
    new_args = args[start_index + 1 : end_index + 1]
    print(new_args)
    args.insert(start_index, aka_evat(new_args))
    
    while ")" in args:
        args.pop(start_index + 1)
    
    
aka_evat(args)
print(args[0])