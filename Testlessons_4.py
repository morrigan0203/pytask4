# 1. 
def tr_matrix(matr):
    matr[:] = list(zip(*matr))
    return matr
    

print(tr_matrix([[1,2], [3,4], [5,6]]))


# 2.
def vocab(**kwargs) -> dict:
    voc = {}
    for key, value in kwargs.items():
        voc[value] = key
    return voc

print(vocab(Сидоров=34, Петров=44, Иванов=50))

# 3. 

ballance = 0
opCount = 0
count = 0
op = True
persentDecrease = 0.015
minDecrease = 30
maxDecrease = 600
multiplicity = 50
taxRichPersent = 10
increasePersent = 0.03
maxOperationCount = 3
maxRichBallance = 5000000
operations = []

def taxRich():
    global ballance
    if ballance > maxRichBallance:
        print(f"Балланс {round(ballance, 2)}. Вычитается налог на богатство : {ballance // taxRichPersent}")
        ballance -= ballance // taxRichPersent

def isCorrectSumm(summ):
    if summ % multiplicity != 0:
        print(f"Сумма {summ} должна быть кратна {multiplicity}")
        return False
    return True

def increaseBallance(summ):
    global ballance
    global operations
    print(f"Пополняем балланс {round(ballance, 2)} на сумму:{summ}")
    ballance += summ
    operations.append(f'Кладем на счет {summ}')

def decreaseBallance(summ):
    global ballance
    global operations
    persent = summ * persentDecrease
    if persent < minDecrease:
        persent = minDecrease
    if persent > maxDecrease:
        persent = maxDecrease
    debt = summ + persent
    print(f"Балланс {round(ballance, 2)}. Нужно снять {debt}")
    if ballance - debt < 0:
        print(f"Недостаточно средств на счете")
    else:
        print(f"Снимаем {debt} со счета")
        ballance -= debt
    operations.append(f'Снимаем со счета {summ}, снимается {debt}')

def increaseCountOperations():
    global opCount
    opCount = opCount + 1 if opCount < maxOperationCount else 1

def printBallance():
    global ballance
    print(f"--== Балланс {round(ballance, 2)} ==--")

while(op):
    operation = int(input("Выберите действие : \n1.Пополнить\n2.Снять\n3.Просмотреть операции со счетом\n4.Выйти\n:"))
    match operation:
        case 1: 
            countIn = int(input("Введите сумму пополнения : "))
            taxRich()
            if isCorrectSumm(countIn):
                increaseBallance(countIn)
                increaseCountOperations()
        case 2:
            countOut = int(input("Введите сумму снятия : "))
            taxRich()
            if isCorrectSumm(countOut):
                decreaseBallance(countOut)
                increaseCountOperations()
        case 3:
            op = "\n".join(operations)
            print(op)
        case 4: 
            printBallance()
            print("Пока.")
            break
    if opCount == maxOperationCount:
        persent = ballance * increasePersent
        print(f"Балланс {round(ballance, 2)}. Начисляются 3% процентов : {persent}")
        ballance += persent
    printBallance()


