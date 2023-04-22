from controllers.controllerHTTP.controllerKamino import ControllerKamino
from entities.entityTransfers import Transfer

class LoadTransfers:
    def __init__(self):
        self.controller = ControllerKamino()

    def loadTransfers(self) -> list[Transfer]:
        return self.controller.getTransfers()