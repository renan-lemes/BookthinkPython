
def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print(linecount('C:\\Users\\RenanLemes\\Desktop\\Projeto_\\BookThinkPython\\Solutions\\wc.py'))