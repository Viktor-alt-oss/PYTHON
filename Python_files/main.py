with open(r"C:\Users\virgi\Downloads\logfile (6).txt", encoding='utf-8') as inp, open('logfile.txt', 'w', encoding='utf-8') as out:
    for line in inp:
        name, data, time = line.strip().split(', ')
        if (int(time[:2]) * 60 + int(time[3:])) - (int(data[:2]) * 60 + int(data[3:])) >= 60:
            out.write(name + '\n')

    
