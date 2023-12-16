from hoses.abc_hose import Hose


class FiftyOneHose(Hose):
    
    def __init__(
        self,
        
    ):  
        super().__init__()
        self.diameter = 51
        self.pressure = 16
        self.resistance = 0.13
        self.throughput_rate = 11
        self.weight = 0.45
        self.status = None
        self.description = "OK"
        
class HoseFabric:
    
    @staticmethod
    def get_hose(diameter:str):
        
        if diameter == 51:
            return FiftyOneHose()
        elif diameter != 51:
            return None