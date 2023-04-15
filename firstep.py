from abc import ABC, abstractmethod
import math

#inja az abstact method estefade kardim va ba estefade az tabe init moteghayer hara zakhire kardim
class shapes(ABC):
    def __init__(self,name):
        self.name=name
        self.__n_angles=None
        self.__equal_sides='it depends'
        self.__n_diameter='it depends'
        self.__edges=None
        
    def __str__(self):
        return('the name is {} '.format(self.name))
    
    @abstractmethod
    def dimensions(self):        
        pass
    
    def area(self):
        pass
    
    def volume(self):
        pass
    
    def total_area(self):
        pass
    
    def sides(self):
        pass
#inja class threedimensionals az class shapes ers bari mikonad
va method haye abstract ham bayad nveshte shavand
class threedimensionals(shapes):
    def __init__(self,length,width,height,radius):      
        
        
        self.length=length
        self.width=width
        self.height=height
        self.radius=radius
        self.n_dimensions:3
        
    
    def dimensions(self):
        print('it has 3 dimensions')
        
        
    def area(self):
        pass
        
    def volume(self):
        pass
        
    def total_area(self):
        pass
        
    def sides(self):
        pass
