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
        
class cube(threedimensionals):
   
    def __init__(self,length,width,height):
        
        self.cube_sides=12
        self.__shape_name='cube'
        self.__having_volume='yes'
        self.length=length
        self.equal_sides='equal'
        self.width=width
        self.height=height
    
    def volume(self):
        self.volume=self.length*self.height*self.width
        return('the volume of cube is {}'.format(self.volume))
        
    def total_area(self):
        self.total_area_cube=self.length**2*6
        return('the total area of the cube is {} '.format(self.total_area_cube))
    
    def area(self):
        return('it just has total area not area')
    
    def get_dimensions(self):
        
        super().dimensions()
        
    def shape_kind(self):
        self.cube_shape='square'
        return('the shape is square')
        
    def get__sides(self):
        
        return("the cube has 12 sides")
        
    def get_equal_sides(self):
       
        return('so all sides are {} '.format(self.equal_sides))
#inja baraye inke  mokaab mostatil az khanevade mokaab hastaz cube ers bari karde ast      
class rectangular_cube(cube):
    def __init__(self,length,width,height):
        super().__init__(length,width,height)
        self.rec_cube_sides=self.cube_sides
    #composiosion                      
    def volume(self):
        rectangularcube=cube(self.length,self.width,self.height)
        return('the volume of the rectangular cube is {} '.format(rectangularcube.volume()))
        
    def total_area(self):
        self.total_area=2*((self.width*self.height)+(self.width*self.length)+self.length*self.height)
        return ('the totall area of the rectangular cube is {} '.format(self.total_area))        
        
    def shape_kind(self):
        self.rectangular_cube_shape_kind='square and rectangle'
        return ('the shap of the rectangular cube is {} '.format(self.rectangular_cube_shape_kind))
         
    def get__sides(self):

        return('rectangular cube has 12 sides ')
        
    def get_dimensions(self):
        super().dimensions()
#tarif moteghayer ha        
class cone(threedimensionals):
    def __init__(self,radius, height, slope_length):
        self.radius=radius
        self.height=height
        self.slope_length=slope_length
        self.__having_volume='yes'
        self.__shape_name='cone'
        self.n_dimensions=3
        
    def volume(self):
        self.volume=((math.pi/3)*self.height*(self.radius)**2)
        return('the volume is {} '.format(round(self.volume,2)))
    #polymorphysm hamin tor ke maloome chnd tabe yksan dr klas ha dirim ke kar yksan vli rvesh haye motefaveti anjam midhnd
    def total_area(self):
        self.total_area=(math.pi*self.radius*self.slope_length)+(math.pi*((self.radius)**2)*self.height)
                                                                 
        return('total area of cone is {} '.format(round(self.total_area,2)))
    
    def shape_kind(self):
        
        
        return('cross and circle')
    
    def  get__sides(self):
        return('cos its based on a circle and a cross it doesnt have any unique side')
    
    def get_dimensions(self):
        super().dimensions()
    
    def side_area(self):
        self.side_area=((math.pi)*self.radius)*(self.slope_length)
        return('the side area is {} '.format(round(self.side_area,2)))
    
class sphere(threedimensionals):
    def __init__(self,radius):
        self.radius=radius
        self.__having_volume='yes'
        self.__shape_name='sphere'
        self.__diameter=self.radius*2
        self.n_dimensions=3
        
    def get_dimensions(self):
        super().dimensions()
         
         
    def area(self):
         return('it doesnt have area just total area')
         
    def volume(self):
         self.volume=(4*math.pi/3)*(self.radius)**3
         return('the volume is {} '.format(round(self.volume,2)))     
         
    def total_area(self):
         self.total_area=4*math.pi*(self.radius**2)
         return('the total area is {} '.format(round(self.total_area,2)))
         
    def sides(self):
         return('it doesnt have any sepecial sides')
 #dr kol klas haye sebodi az class threedimensionals ers bari mikonnd       
