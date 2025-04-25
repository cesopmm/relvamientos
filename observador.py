


class Subject:
    def __init__(self):
        self.observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        if obj in self.observadores:
            self.observadores.remove(obj)

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)
            print("Se ha efecutado una carga")
            
class Carga(Subject):
    def __init__(self):
        super().__init__()
        self.estado = None

    def set_estado(self, value):
        self.estado = value
        self.notificar(self.estado)

    def get_estado(self):
        return self.estado


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self,observed_obj):
        self.observado_a = observed_obj
        self.estado = None
        if hasattr(observed_obj, 'agregar'):
            observed_obj.agregar(self)
        

    def update(self, *args):
        print("Actualización dentro de ObservadorConcretoA")
        if args and len(args) > 0:
            self.estado = args [0]
        else:
            self.estado = self.observador_a.get_estado()
        print("Estado = ", self.estado)

#tema1 = Carga()
#observado_a = ConcreteObserverA(tema1)
#tema1.set_estado(1)

