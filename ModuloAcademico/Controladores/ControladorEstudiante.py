from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Modelos.Estudiante import Estudiante
class ControladorEstudiante():
    def __init__(self):
        self.repositorioEstudiante = RepositorioEstudiante()
    def index(self):
        return self.repositorioEstudiante.findAll()
    def create(self,infoEstudiante):
        nuevoEstudiante=Estudiante(infoEstudiante)
        return self.repositorioEstudiante.save(nuevoEstudiante)
    def show(self,id):
        elEstudiante=Estudiante(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__
    def update(self,id,infoEstudiante):
        estudianteActual=Estudiante(self.repositorioEstudiante.findById(id))
        estudianteActual.cedula=infoEstudiante["cedula"]
        estudianteActual.nombre = infoEstudiante["nombre"]
        estudianteActual.apellido = infoEstudiante["apellido"]
        return self.repositorioEstudiante.save(estudianteActual)
    def delete(self,id):
        return self.repositorioEstudiante.delete(id)









#codigo pruebas del servidor inicial
"""
from Modelos.Estudiante import Estudiante
class ControladorEstudiante():
    def __init__(self):
        print("Creando ControladorEstudiante")
    def index(self):
        print("Listar todos los estudiantes")
        unEstudiante={
            "_id":"abc123",
            "cedula":"123",
            "nombre":"Juan",
            "apellido":"Perez"
        }
        return [unEstudiante]
    def create(self,infoEstudiante):
        print("Crear un estudiante")
        elEstudiante = Estudiante(infoEstudiante)
        return elEstudiante.__dict__
    def show(self,id):
        print("Mostrando un estudiante con id ",id)
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elEstudiante
    def update(self,id,infoEstudiante):
        print("Actualizando estudiante con id ",id)
        elEstudiante = Estudiante(infoEstudiante)
        return elEstudiante.__dict__
    def delete(self,id):
        print("Elimiando estudiante con id ",id)
        return {"deleted_count":1}"""