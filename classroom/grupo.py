from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, listadoAlumnos=None):
        self._grupo = grupo
        if asignaturas is None:
            self._asignaturas=[]
        else:
            self._asignaturas = asignaturas
        if listadoAlumnos is None:
            self.listadoAlumnos=[]
        else:
            self.listadoAlumnos = listadoAlumnos
        self.grado="Grado 12"

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista=[]
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        return "Grupo de estudiantes: "+self._grupo
    

   

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

   
