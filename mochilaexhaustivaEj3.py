class Objeto():
    def __init__(self,gramos,valor):
        self.gramos=gramos
        self.valor=valor
    def getGramos(self):
        return self.gramos
    def getValor(self):
        return self.valor
#armar la lista con los objetos
objetos=[]
objetos.extend([Objeto(1800,72)])
objetos.extend([Objeto(600,36)])
objetos.extend([Objeto(1200,60)])


#hacer un arrar de 8 posiciones, lo inicializo con 0
combinaciones =  [0 for columna in range(0,8)] 

#  0 significa que ese objeto no va en la mochila y 1 significa que ese objeto si va en la mochila
datos=['1','0']
# combinaciones son en total 3 elementos posibles
cont=0
for a in range (len(datos)):
    for b in range(len(datos)):
        for c in range(len(datos)):
            combinaciones[cont]=datos[a]+datos[b]+datos[c]
            cont=cont + 1
#imprimo todas las combinaciones y el contador para verificar
#for x in range(len(combinaciones)):
    #print(combinaciones[x])
    #print('\n')
#print(cont)


mejorCombinacionMochila=0
mejorValorMochila=0
gramos_max=3000
#comparo cada combinacion de mochila
for x in range(len(combinaciones)):
    gramosTotal=0
    valorTotal=0
    for j in range(len(combinaciones[x])):
        #calculo el peso total y valor total de la mochila
        if(combinaciones[x][j]=='1'):
            gramosTotal=gramosTotal+objetos[j].gramos
            #print(volumenTotal)
            valorTotal=valorTotal+objetos[j].valor
            #print(valorTotal)
            #print(volumenTotal)
       
        #me fijo si el peso de esa mochila supera el maximo
        #si no supera calculo la funcion y busco el maximo 

        #hago la validacion que volumenTotal != 0 ya que la combinacion [0,0,0,0,0,0,0,0,0,0] 
        # me da volumen y valor =0 y no se puede dividir por 0
        
    if(gramosTotal<=gramos_max):
        #print(volumenTotal)
        comb=combinaciones[x]
        #print(comb)
        
        #print(totalvalor)
        #print(funcion)
        if(valorTotal>=mejorValorMochila):
            mejorValorMochila=valorTotal
            mejorCombinacionMochila=combinaciones[x]

mejorCombinacionMochila=str(mejorCombinacionMochila)
mejor_combinacion = [int(i) for i in list(mejorCombinacionMochila)]

print(mejor_combinacion) #en 0 y 1
print("Valores de la mochila:")
for i in range (len(mejor_combinacion)):
    if(mejor_combinacion[i]==1):
        print(objetos[i].valor,end=" ")
print("\nGramos de la mochila:")
for i in range (len(mejor_combinacion)):
    if(mejor_combinacion[i]==1):
        print(objetos[i].gramos,end=" ")
sumaMochila =0
for i in range(len(mejor_combinacion)):
    if(mejor_combinacion[i]==1):
        sumaMochila = sumaMochila + objetos[i].gramos
        #print(objeto[i].volumen)

print()
print("\nTotal Gramos: ", sumaMochila)
print("\nValor de la Mochila:$", valorMochila)
