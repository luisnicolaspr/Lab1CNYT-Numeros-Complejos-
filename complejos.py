#SUMA COMPLEJOS
import math
def SumaComplejos (c1,c2):
     real = c1[0] + c2[0]
     imaginaria = c1[1] + c2[1]
    
     return ((real,imaginaria))

def PrettyPrinting (c):
    if c[1]>0:
        print("{} + {}i".format(c[0],c[1]))
    else:
        print("{} {}i".format(c[0],c[1]))

#RESTA COMPLEJOS

def RestaComplejos (c1,c2):
     real = c1[0] - c2[0]
     imaginaria = c1[1] - c2[1]
    
     return ((real,imaginaria))


#MULTIPLICACION COMPLEJOS

def MultiplicacionComplejos (c1,c2):

    real = ((c1[0]*c2[0]) - (c1[1]*c2[1]))
    imaginaria = ((c2[0]*c1[1]) + (c1[0]*c2[1]))

    return ((real,imaginaria))

#DIVISIÓ COMPLEJOS

def DivisionComplejos(c1, c2):
    conjugado = (c2[0], -c2[1])
    numerator = MultiplicacionComplejos(c1, conjugado)
    denominator = MultiplicacionComplejos(c2, conjugado)[0] + MultiplicacionComplejos(c2, conjugado)[1]**2
    real = numerator[0] / denominator
    imag = numerator[1] / denominator
    return (real, imag)



#MODULO

def ModuloComplejos (c):

    modulo = math.sqrt(c[0]**2+c[1]**2)

    return(modulo)

#CONJUDAGO 

def ConjugadoComplejos (c):
    return (c[0],-c[1])

#FASE 

def FaseComplejos(c):
    
    x, y = c[0], c[1]
    return math.atan2(y, x)

    