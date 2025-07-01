#ingrese las  notas 
n1=float(input("ingrese nota 1: "))
n2=float(input("ingrese nota 2: "))
n3=float(input("ingrese nota 3: "))
n4=float(input("ingrese nota 4: "))
promedio=n1*0.3+n2*0.4+n3*0.3+n4*0.3
promedio=round(promedio, 1)
print("el promedio de presentacion final es: ",promedio)
nfinal=float(input("ingrese la nota final: "))
promedio_final=promedio*0.6+nfinal*0.4
promedio_final=round(promedio_final, 1)
print("El promedio Final es : ",promedio_final)