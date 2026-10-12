class EmpleadoDTO:
    def __init__(self, nombre, apellido, direccion, NumeroTelefono, correo, password, codEmpleado=None, inicioContrato=None, Salario=None, turno=None, cod_departamento=None, id_empleado=None):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.NumeroTelefono = NumeroTelefono
        self.correo = correo
        self.password = password
        self.codEmpleado = codEmpleado
        self.cod_empleado = codEmpleado
        self.inicioContrato = inicioContrato
        self.Salario = Salario
        self.turno = turno
        self.cod_departamento = cod_departamento

    def __str__(self):
        return (
            f"ID: {self.id_empleado}\n"
            f"Empleado: {self.nombre} {self.apellido}\n"
            f"Dirección: {self.direccion}\n"
            f"Teléfono: {self.NumeroTelefono}\n"
            f"Correo: {self.correo}\n"
            f"Código: {self.codEmpleado}\n"
            f"Inicio de Contrato: {self.inicioContrato}\n"
            f"Salario: {self.Salario}"
        )