registro = input(f'¿Ingresará registro de "alumno" o "docente"?\n')

if registro=="alumno":
    while True:
        try:
            nombre_alumno = input(f'Ingrese el nombre del Alumno\n')
            if nombre_alumno.isalpha():
                break
            else:
                print('Ingrese caracteres válidos\n')    
            break
        except ValueError as e:
            print('Por favor, ingrese nombre del alumno')

    nota1 = int(input('Ingrese Nota 1  del alumno\n'))
    nota2 = int(input('Ingrese Nota 2  del alumno\n'))
    nota3 = int(input('Ingrese Nota 3  del alumno\n'))
    nota4 = int(input('Ingrese Nota 4  del alumno\n'))
    listanotas = [nota1, nota2, nota3, nota4]

    notamayor = max(listanotas)
    notamenor = min(listanotas)
    sumanotas = sum(listanotas)
    numeronotas = len(listanotas)
    notapromedio = sumanotas/numeronotas
    listaestadisticas = [notamayor, notamenor, notapromedio]

    class alumno:
        def __init__(self, nombre,notas, estadisticas):
            self.nombre = nombre
            self.notas = notas
            self.estadisticas = estadisticas

    class archivo:
        def __init__(self, nombre_archivo):
            self.nombre_archivo = nombre_archivo

        def mostrar_alumnos(self):
            try:
                file=open(self.nombre_archivo, 'r')
                for linea in file.readlines():
                    print(linea)
            except Exception as e:
                print(f'error: {e}')
            finally:
                if file:
                    file.close()

        def agregar_alumnos(self,alumno):
            try:
                file=open(self.nombre_archivo, 'a', encoding= 'utf-8')
                #texto_alumnos = f'{alumno.nombre}, {alumno.notas}, {alumno.estadisticas}\n'
                file.write(f'Alumno: {alumno.nombre}, Notas: {alumno.notas}, Máxima Nota: {alumno.estadisticas[0]}, Mínima Nota: {alumno.estadisticas[1]}, Promedio: {alumno.estadisticas[2]}\n')
                # file.write(texto_alumnos)
            except Exception as e:
                print(f'error: {e}')
            finally:
                if file:
                    file.close()

    alumno_1 = alumno(nombre_alumno, listanotas, listaestadisticas)
    archivo1 = archivo('alumnos.txt')
    archivo1.agregar_alumnos(alumno_1)
    archivo1.mostrar_alumnos()

elif registro=="docente":
    while True:
        try:
            nombre_docente = input(f'Ingrese el nombre del docente\n')
            if nombre_docente.isalpha():
                break
            else:
                print('Ingrese caracteres válidos\n')
            break
        except ValueError as e:
            print('Por favor, ingrese nombre del alumno')

    while True:
        try:
            edad_docente = int(input(f'Ingrese la edad del docente\n'))
            break
        except ValueError as e:
            print('Por favor, ingrese la edad del docente')

    while True:
        try:
            dni_docente = int(input(f'Ingrese el DNI del docente\n'))
            #if len(str(dni_docente))==8:
            #    break
            #else:
            #    print('Por favor, ingrese DNI de 8 digitos')
            break
        except ValueError as e:
            print('Por favor, ingrese el numero del DNI del docente')
            
    class docente:
        def __init__(self, nombre,edad, dni):
            self.nombre = nombre
            self.edad = edad
            self.dni = dni

    class archivo:
        def __init__(self, nombre_archivo):
            self.nombre_archivo = nombre_archivo

        def mostrar_docentes(self):
            try:
                file=open(self.nombre_archivo, 'r')
                for linea in file.readlines():
                    print(linea)
            except Exception as e:
                print(f'error: {e}')
            finally:
                if file:
                    file.close()

        def agregar_docentes(self,docente):
            try:
                file=open(self.nombre_archivo, 'a', encoding= 'utf-8')
                #texto_docentes = f'{docente.nombre}, {docente.edad}, {docente.dni}\n'
                file.write(f'Docente: {docente.nombre}, Edad: {docente.edad}, DNI: {docente.dni}\n')
                #file.write(texto_docentes)
            except Exception as e:
                print(f'error: {e}')
            finally:
                if file:
                    file.close()

    docente_1 = docente(nombre_docente, edad_docente, dni_docente)
    archivo1 = archivo('docentes.txt')
    archivo1.agregar_docentes(docente_1)
    archivo1.mostrar_docentes()

else:
    print('No se registra alumno o docente')