from abc import ABC,abstractmethod

class Bike(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Hunter(Bike):

    def start(self):
        print("hunter start method")
    def accelerate(self):
        print("Hunter accelerate method")
    def stop(self):
        print("hunter stops")

hunter_inst=Hunter()
hunter_inst.start()
hunter_inst.accelerate()
hunter_inst.stop()

