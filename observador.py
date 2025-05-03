import datetime


class Subject:
    def __init__(self):
        self.observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        if obj in self.observadores:
            self.observadores.remove(obj)

    def notificar(self, *args):
        with open("registo de apertura.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} - Acción: {args[0]}\n")

        for observador in self.observadores:
            observador.update(args)
            
            
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
        
        if args and len(args) > 0:
            self.estado = args [0]
        else:
            self.estado = self.observador_a.get_estado()
        


