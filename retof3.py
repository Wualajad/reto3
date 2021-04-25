#Preguntar cual programa se va a ejecutar 
sab1=input("Tiene una cantidad exacta de alumnos (Si/No) :")
sab2=input("Se tiene una cantidad determinada de notas por almunno (Si/No) :")
sab1=sab1.lower()
sab2=sab2.lower()
alumnos= {}
#Limitado alumnos y notas
if sab1 == "si"  and sab2 == "si":
    cantidades = int(input("Introduce la cantidad de alumnos que vamos a guradar:"))
    nnotas= int(input("Introduce la cantidad de notas por alumnos que vamos a guradar:"))
    for nu in range(cantidades):
        alumno= input("Nombre del alumno: ")
        while alumno in alumnos:
            print("Alumno ya existe")
            alumno= input("Nombre del alumno: ")
        notas=[]
        n=1
        while n<=nnotas:
            try:
                nota=int(input("Ingrese la nota : "))
            except:
                print("Ingrese un valor numerico valido para notas")
            if nota<= 20 and nota >=0:
                notas.append(nota)
                n=n+1
            else:
                print("Ingrese un valor valido para notas")
        alumnos[alumno] = notas.copy()
    for alumno, notas in alumnos.items():
        print("%s ha sacado de promedio %.2f" % (alumno,sum(notas)/len(notas)))
        print("Su menor calificacion es %i" % (min(notas)))
        print("Su mayor calificacion es %i" % (max(notas)))


#ilimitados alumnos , limitadas notas
elif sab1 == "no" and sab2 == "si":
    nnotas= int(input("Introduce la cantidad de notas por alumnos que vamos a guradar:"))
    nu=0
    while nu == 0:
        alumno= input("Nombre del alumno: ")
        while alumno in alumnos:
            print("Alumno ya existe")
            alumno= input("Nombre del alumno: ")
        notas=[]
        n=1
        while n<=nnotas:
            try:
                nota=int(input("Ingrese la nota : "))
            except:
                print("Ingrese un valor numerico valido para notas")
            if nota<= 20 and nota >=0:
                notas.append(nota)
                n=n+1
            else:
                print("Ingrese un valor valido para notas")   
        alumnos[alumno] = notas.copy()
        condi=input("Desea agregar a otro alumno (Si/No) :")
        if condi.lower() =="si":
            nu=nu
        else:
            nu=1

    for alumno, notas in alumnos.items():
        print("%s ha sacado de promedio %f" % (alumno,sum(notas)/len(notas)))
        print("Su menor calificacion es %i" % (min(notas)))
        print("Su mayor calificacion es %i " % (max(notas)))

# limado alumnos ,ilimitadas notas
elif sab1 == "si" and sab2 == "no":
    cantidades = int(input("Introduce la cantidad de alumnos que vamos a guradar:"))
    for num in range(cantidades):
        alumno = input("Nombre del alumno:")
        while alumno in alumnos:
            print("Alumno ya existe.")
            alumno = input("Nombre del alumno:")
        notas=[]
        lol=1
        while lol==1:
            try:
                nota = int(input("Dame una nota del alumno (negativo para terminar):"))
            except:
                print("Ingrese un valor numerico valido para notas")
            if nota<= 20 and nota >=0:
                notas.append(nota)
            elif nota<0:
                lol=lol+1
            else:
                print("Ingrese un valor valido para notas")
        alumnos[alumno] = notas.copy()
    for alumno, notas in alumnos.items():
        print("%s ha sacado de promedio %.2f" % (alumno,sum(notas)/len(notas)))
        print("Su menor calificacion es %i" % (min(notas)))
        print("Su mayor calificacion es %i" % (max(notas)))

#Ilimitados alumnos , ilimitadas notas
else:
    nu=0
    while nu == 0:
        alumno= input("Nombre del alumno: ")
        while alumno in alumnos:
            print("Alumno ya existe")
            alumno= input("Nombre del alumno: ")
        notas=[]
        lol=1
        while lol==1:
            try:
                nota = int(input("Dame una nota del alumno (negativo para terminar):"))
            except:
                print("Ingrese un valor numerico valido para notas")
            if nota<= 20 and nota >=0:
                notas.append(nota)
            elif nota<0:
                lol=lol+1
            else:
                print("Ingrese un valor valido para notas")
        alumnos[alumno] = notas.copy()
        condi=input("Desea agregar a otro alumno (Si/No) :")
        if condi.lower() =="si":
            nu=nu
        else:
            nu=1

    for alumno, notas in alumnos.items():
        print("%s ha sacado de promedio %f" % (alumno,sum(notas)/len(notas)))
        print("Su menor calificacion es %i" % (min(notas)))
        print("Su mayor calificacion es %i " % (max(notas)))

