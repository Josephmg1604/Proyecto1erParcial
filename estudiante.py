from persona1 import Persona


class Estudiante(Persona):
    _contador_estudiante = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera, idES=int,
                 nivel=int):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self.idES = idES
        self.nivel = nivel
        Estudiante._contador_estudiante += 1

    @property
    def idES(self):
        return self._idES

    @idES.setter
    def idES(self, idES):
        self._idES = idES

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @property
    def contador_estudiante(self):
        return Estudiante._contador_estudiante

    def pedir_libro(self):
        self._contador_estudiante += 1
        return True

    def devolver_libro(self):
        if self._contador_estudiante > 0:
            self._contador_estudiante -= 1
            return True
        else:
            return False

    def __str__(self):
        return f"Estudiante(cedula={self.cedula}, nombre={self.nombre}, apellido={self.apellido}, email={self.email}, telefono={self.telefono}, direccion={self.direccion}, numero_libros={self.numero_libros}, activo={self.activo}, carrera={self.carrera}, idES={self.idES}, nivel={self.nivel}, contador_estudiantes={self._contador_estudiante})"

def main():
    estudiante1 = Estudiante(cedula="0957752322", nombre="0957752322", apellido="Iza", email="sweet_eli97@outlook.es", telefono="0979482643", direccion="28 y maldonado", numero_libros=1, activo=True, carrera="Gestión de la información gerencial", idES=101, nivel=3)
    print(estudiante1)
    estudiante2 = Estudiante(cedula="0943308221", nombre="Daniela", apellido="Ochoa", email="daniela.ochoa@ug.edu.ec", telefono="0939179295", direccion="46 y Nicolás Agusto González",numero_libros=3, activo=True, carrera="Gestión de la información gerencial", idES=202, nivel=3)
    print(estudiante2)
    estudiante3 = Estudiante(cedula="0927597021", nombre="Josehpt", apellido="Montenegro", email="josephmgbsc@gmail.com",telefono="0985381771", direccion="Fco. seguro entre la 37 y 38", numero_libros=3, activo=True, carrera="Gestión de la información gerencial", idES=202, nivel=3)
    print(estudiante3)
if __name__ == "__main__":
    main()