
import numpy as np
import matplotlib.pyplot as plt
K = int(input('Введите число K: '))
N = int(input('Введите число N от 3 до 100: '))
while True:
    if N<100 and N>2: break
    else: N=int(input('Введите число N от 3 до 100: '))
choice=input('Выберите, каким способом вы хотите заполнить массив:\n1-из файла 2-случайными числами\n')
while True:
    if choice.isnumeric():
        if choice == '1':
            A = np.loadtxt('1.txt',dtype=int, skiprows=0,usecols=list(range(0, N)), max_rows=N)
            break
        elif choice == '2':
            A = np.random.randint(-10,10,(N,N))
            break
        else: choice = input('Введите целое число:\n 1-из файла 2-случайными числами\n')
F=np.copy(A)
print(f'Первоначальная матрица А:\n{A}')
print(f'Первоначальная матрица F:\n{F}')
if N%2==0: ch, nch = 1,0
else: ch, nch = 0,1
summa=0
for x in range(N//2-ch):
    for y in range(N//2+nch,N):
        if (y+1)%2!=0 and F[x][y]>K: summa+=F[x][y]
prper=1
for y in F[0]: prper*=y
for y in F[N-1]: prper*=y
for x in range(1,N-1): prper*=F[x][0]*F[x][N-1]
if summa>prper:
    for x in range(N//2+nch, N):
        for y in range(N//2):
            F[x][y],F[x-N//2-nch][N-y-1]=F[x-N//2-nch][N-y-1],F[x][y]
    print('Матрицы C и Е были поменяны симметрично')
else:
    for x in range(N//2):
        for y in range(N//2):
            F[x][y],F[N//2+nch+x][y]=F[N//2+nch+x][y],F[x][y]
    print('Матрицы В и С были поменяны несимметрично') 
print(f'Измененная матрица F:\n{F}')
opred = np.linalg.det(A)
sumdiag = np.diagonal(F).sum() + np.diagonal(np.fliplr(F)).sum()
plt.figure(figsize=(8, 6))
plt.plot(np.diag(F), marker='o', linestyle='-')
plt.title('Линейный график диагональных элементов матрицы F')
plt.xlabel('Номер строки/столбца')
plt.ylabel('Значение элемента')
plt.figure(figsize=(8, 6))
for i in range(len(F)):
    plt.hist(F[i, :], bins=10, label=f'Строка {i+1}')
plt.title('Гистограммы элементов по строкам')
plt.legend()
plt.figure(figsize=(8, 6))
for i in range(len(F)):
    plt.hist(F[:, i], bins=10, label=f'Столбец {i}')
plt.title('Гистограммы элементов по столбцам')
plt.legend()
if opred > sumdiag:
    Aobr=np.linalg.inv(A)
    print(f'Обратная матрица А:\n{Aobr}')
    Aobr=Aobr*A
    print(f'Обратная матрица А, умноженная на матрицу А:\n{Aobr}')
    F=np.linalg.inv(F)*K
    print(f'Обратная матрица F, умноженная на {K}:\n{F}')
    result = Aobr-F
else:
    At=np.transpose(A)
    print(f'Транспортированная матрица А:\n{At}')
    G = np.tril(A)
    print(f'Нижняя треугольная матрица G:\n{G}')
    Ft=np.transpose(F)
    print(f'Транспортированная матрица F:\n{Ft}')
    result = (At+G-Ft)*K
print(f'Результат операций:\n{result}')
plt.show()  