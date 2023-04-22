from controllers.controllerHTTP.controllerKamino import ControllerKamino

class PostTransaction:
        
    def postTransaction(self, listObj: list):
        c = 0    
        for obj in listObj:
            c += 1
            if c > 2:
                break
            ControllerKamino().postTransfer(obj=obj)   