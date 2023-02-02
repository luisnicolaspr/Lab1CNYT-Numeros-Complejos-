import complejos as clpx



print("-----------PRUEBAS--------------")

print("-----------SUMAS--------------")
clpx.PrettyPrinting(clpx.SumaComplejos((3,-8),(4,6)))
clpx.PrettyPrinting(clpx.SumaComplejos((7,8),(3,6)))
print("-----------MULTIPLICACIONES--------------")
clpx.PrettyPrinting(clpx.MultiplicacionComplejos((2,-3),(-1,1)))
clpx.PrettyPrinting(clpx.MultiplicacionComplejos((5,-7),(2,9)))
print("-----------MODULOS--------------")
print(clpx.ModuloComplejos((3,-8)))
print(clpx.ModuloComplejos((-2,-3)))
print("-----------CONJUGADOS--------------")
clpx.PrettyPrinting(clpx.ConjugadoComplejos((2,-6)))
clpx.PrettyPrinting(clpx.ConjugadoComplejos((8,2)))
clpx.PrettyPrinting(clpx.ConjugadoComplejos((4,-7)))
print("-----------RESTAS--------------")
clpx.PrettyPrinting(clpx.RestaComplejos((7,-8),(2,6)))
clpx.PrettyPrinting(clpx.RestaComplejos((4,1),(-9,3)))
print("-----------DIVISIONES--------------")
clpx.PrettyPrinting(clpx.DivisionComplejos((3,-7),(3,2)))
clpx.PrettyPrinting(clpx.DivisionComplejos((4,-2),(1,-7)))
print("-----------FASES--------------")
print(clpx.FaseComplejos((3,4)))
print(clpx.FaseComplejos((-2,-3)))