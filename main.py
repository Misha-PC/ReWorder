'''
Изменение порядка букв в словах
'''
from random import randint
import sys
#Const:
symbol = [' ', ',', '.', ':', '!', '?', "\n", "'", '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ';', '<', '=', '>', '@', '«', '»']


def mixer(inStr):            #    перемешивает буквы в отдельных словах
    outStr = inStr
    iter = 0
    while inStr == outStr and iter < 10:
        iter += 1
        outStr = inStr[0]
        mass2 = []
        index_ = []
        mass = inStr[1:len(inStr)-1]

        for i in range(len(mass)):
            index_.append(i)

        while index_:
            j = randint(0,len(mass)-1)
            if j in index_:
                index_.remove(j)
                mass2.append(mass[j])

        for x in mass2:
            outStr += x
        outStr += inStr[len(inStr)-1]

    return(outStr)


def findSymbol(inChar):      #    проверяет входит ли символ в массив symbol
    for i in symbol:
        if i == inChar:
            return(1)
    return(0)


def disassembler(inStr):     #    Делит строку на массив из слов и символов
    outArr = []
    currentWord = ''
    for currentSymbol in inStr:
        if findSymbol(currentSymbol):
            if currentWord:
                outArr.append(currentWord)
                currentWord = ''
            outArr.append(currentSymbol)
        else:
            currentWord += currentSymbol
    return(outArr)


def mixText(inStr):          #   основная функция, перемешивает все слова в массиве выдоном предидущей функцией
    inArr = disassembler(inStr)
    #print(inArr)
    outStr = ''
    for currentWord in inArr:
        #print(currentWord)
        if len(currentWord) > 3:
            outStr += mixer(currentWord)
        else:
            outStr += currentWord
        #print(outStr)
    return (outStr)


def readFile(fileName):      #  читает файл и возвращает содержимое строкой
    f = open(fileName, 'r')
    txt = f.read()
    f.close()
    return(txt)


def main(argv):              #  главная функция, парсит аргументы, решает что с этим говном делать
    if len(argv) >= 2:
        if argv[1] == '-f':
            if len(argv) >= 3:
                print(mixText(readFile(argv[2])))
            else:
                print('Введите путь к файлу: ', end='')
                print(mixText(readFile(input())))
        elif argv[1] == '-c':
            print('Введите ваш текст: \n')
            print(mixText(input()))
    else:
        print("Используйте аргумент -f [+ название файла] для чтения файла, или -с для ввода текста вручную")

if __name__ == '__main__':
    main(sys.argv)
