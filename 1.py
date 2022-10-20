def transfer(x,y):
    b=''
    num=x
    while num>0:
        b=str(num%y)+b
        num//=y
    return print("Число",x,"в системе счисления",y,"равно:",b)

def num():
    while True:
        s=int(input("Введите систему счисления(двоичная или восьмеричная), в которую хотите перевести введённое число: "))
        if s!=8 and s!=2:
            print("Вы ввели некорректную систему счисления! Пожалуйста, введите еще раз.(двоичная или восьмеричная)")
        if s==2 or s==8:
            break
    return s

num_1=int(input("Введите целое положительное число: "))
sys=num()
transfer(num_1,sys)
