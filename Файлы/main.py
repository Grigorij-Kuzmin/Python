# open('путь') - открывает файл для работы с ним
f = open('input1.txt')

# Если файл очень большой, то есть смысл читать его построчно
for line in f:
    print(line.strip())

# readline() - читает одноу строку из файла
#f.readline()

f.close()