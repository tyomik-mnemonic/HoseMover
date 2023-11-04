from abc import ABCMeta, abstractmethod
from collections import namedtuple
import uuid

class AbcHose(metaclass=ABCMeta):
    @property
    def pk():
        pass
    
    @property
    def number():
        pass
    
    
    @property
    def lenght():
        pass
        
    @abstractmethod
    def pk()->str:
        raise NotImplementedError
    
    @abstractmethod
    def number()->str:
        raise NotImplementedError
    
    @abstractmethod
    def lenght()->int:
        raise NotImplementedError
    
    @abstractmethod
    def diameter()->int:
        raise NotImplementedError
    
    @abstractmethod
    def throughput_rate()->int or float:
        raise NotImplementedError
    
    @abstractmethod
    def resistance()->int or float:
        raise NotImplementedError
    
    @abstractmethod
    def pressure()->int or float:
        raise NotImplementedError
    
    @abstractmethod
    def weight()->int or float:
        raise NotImplementedError
    
    @abstractmethod
    def status()->str:
        raise NotImplementedError
    
    @abstractmethod
    def description()->str:
        raise NotImplementedError
    
class Hose(AbcHose):
    
    def __init__(self):
        self.pk = str(uuid.uuid4())
        self.number = 0
        self.lenght = 20
        self.diameter = None
        self.pressure = None
        self.resistance = None
        self.throughput_rate = None
        self.weight = None
        self.status = None
        self.discription = None
        super()
        
    
    @property
    def pk(self):
        """
        уникальный uuid рукава
        (сурогатный ключ для id и qr code)
        """
        self._pk
    
    @pk.setter
    def pk(self, pk):
        self._pk = pk
    
    @pk.getter
    def pk(self):
        return self._pk
    
    
    @property
    def number(self):
        """
        бизнес ключ рукава
        """
        self._number
        
    @number.setter
    def number(self, number):
        self._number = number
    
    @number.getter
    def number(self):
        return self._number
    
    
    @property
    def lenght(self):
        """
        длина рукава
        (может меняться после ремонта)
        """
        self._lenght

    @lenght.setter
    def lenght(self, lenght):
        self._lenght = lenght
    
    @lenght.getter
    def lenght(self):
        return self._lenght
    
    
    @property
    def diameter(self):
        """
        диаметр рукава
        """
        self._diameter

    @diameter.setter
    def diameter(self, diameter):
        self._diameter = diameter
    
    @diameter.getter
    def diameter(self):
        return self._diameter
    
    
    @property
    def pressure(self):
        """
        давление рукава
        """
        self._pressure

    @pressure.setter
    def pressure(self, pressure):
        self._pressure = pressure
    
    @pressure.getter
    def pressure(self):
        return self._pressure


    @property
    def throughput_rate(self):
        """
        пропусктная способность рукава, л/сек
        """
        self._throughput_rate

    @throughput_rate.setter
    def throughput_rate(self, throughput_rate):
        self._throughput_rate = throughput_rate
    
    @throughput_rate.getter
    def throughput_rate(self):
        return self._throughput_rate
  
  
    @property
    def resistance(self):
        """
        сопротивление рукава
        """
        self._resistance

    @resistance.setter
    def resistance(self, resistance):
        self._resistance = resistance
    
    @resistance.getter
    def resistance(self):
        return self._resistance
    
    
    @property
    def weight(self):
        """
        вес рукава
        """
        self._weighrt
        
    @weight.setter
    def weight(self, weight):
        self._weight = weight
    
    @weight.getter
    def weight(self):
        return self._weight
    
    
    @property
    def status(self):
        """
        статус рукава (в ремонте, в резерве и тд)
        """
        self._status
      
    @status.setter
    def status(self, status):
        self._status = status
        
    @status.getter
    def status(self):
        return self._status
    
    @property
    def description(self):
        """
        описание рукава (состояние, повреждения и др.)
        """
        self._description
        
    @description.setter
    def description(self, description):
        self._description = description
        
    @description.getter
    def description(self):
        return self._description
    
fiftyone = Hose()
fiftyone.number, fiftyone.lenght, fiftyone.pressure, fiftyone.resistance, fiftyone.throughput_rate, fiftyone.weight \
    = 34, 15, 16, 0.013, 11, 0.43

pass