with open(r"C:\Users\virgi\Downloads\logfile (2).txt") as inp, open('logfile.txt', 'w') as out:
    x = [line.split(',') for line in inp.read().split('\n')]
    print(x, file=out)