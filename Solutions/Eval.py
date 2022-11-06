
def loop_eval():
    while True:
        line = input('> ')
        if line == 'done':
            break
        print(eval(line))
        
loop_eval()