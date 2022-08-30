def sum(number):
    val=0
    contador = 0
    for i in range(1,number):
        val += i
        contador +=1
    print(val, "Suma total")
    print(contador,"Conteo de acciones")




if __name__ == '__main__':
    sum(5)

