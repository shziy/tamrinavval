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
        self.__having_volume='Yes'
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

class cylindre(threedimensionals):
    def __init__(self,height,radius):
        self.__name='cylindre'
        self.radius=radius
        self.height=height
        self.n_dimensions=3
        self.equal_sides:'no'
        
    def get_dimensions(self):
        super().dimensions()

          
    def area(self):
        
        
        return('it doesnt have area')
          
    def volume(self):
        self.volume=(2*math.pi)*((self.radius)**2)*self.height
        return("the volume is {} ".format(round(self.volume,2)))
          
    def total_area(self):
        self.total_area=(2*math.pi*self.radius)*(self.height)+((math.pi*(self.radius)**2))
        return('the total area of this sphere is {} '.format(round(self.total_area,2)))
          
    def sides(self):
        return('due to the fact that its a 3d shape we can not count any side for it')
  
class pyramid(threedimensionals):
    def __init__(self,height,length,width,side):
        self.height=height
        self.length=length
        self.width=width
        
        self.side=side
        #encapsolation
        self._name='pyramid'
        self.equal_sides='not always'
        self.n_diameter='nothing'
        
    def volume(self):
        self.volume=(1/3)*(self.width*self.height)*self.height
        return('the volume of this pyrami is {} '.format(round(self.volume,2)))
    
    def total_area(self):
        self.total_area=((((((self.width/2)**2+(self.side)*2)**0.5)*(self.side+self.length/2)**2+(self.side)*2)**0.5)*self.length)+(self.width*self.height)
        return('the total area of this pyramid is {} '.format(round(self.total_area,2)))
     
    def get_dimensions(self):
        super().dimensions()
        
    def area(self):
        return('it doesnt have an area')
    
    def sides(self):
        return('due to the fact that its a 3d shape we can not count any side for it')
 
class two_dimensionals(shapes) :
    def __init__(self,name):
        super().__init__()
        self.n_dimensions:3
        self.__having_angles:'it depends ..'
        self.__minimum_sides_a:3
        self.maximum_angles:'uncountable'
        self.minimum_angles:0
    def dimensions(self):        
        print('its a 2 dimensional shape')
        
    def area(self):
        pass
        
    def volume(self):
        print('two dimensional shapes doesnt have volume')
        
    def total_area(self):
        print('two dimensional shapes just have area')
        
    def sides(self):
        pass
    
    def angles(self):
        pass
    
    def perimeter(self):
        pass
class sin :
    def __init__(self,degree):
        self.degree=degree
        
    def sinus(self):
        return(abs(math.sin(self.degree)))    
    
class square(two_dimensionals):
    def __init__(self,length):
        self.length=length
        self.__name='square'
        self.__n_dimensions=2
        self.__equalsides:'yes'
        self.equal_angles:'yes'
        
        
        
    def sides(self):
        return('square has 4 sides')
    
    def angles(self):
        return('it has 4 angles')
    
    def get_total_area(self):
        super().total_area()
    
    def get_volume(self):
        super().volume()
        
    def area(self):
        self.area=self.lenght**2
        return('the area og this square is{} '.format(round(self.area,2)))
    
    def perimeter(self):
        self.perimeter=self.length*4
        return('the perimeter of this square is {} '.format(round(self.perimeter,2)))
        
    def diameter(self):
        self.diameter=(2*self.length**2)**0.5
        return('it has twi diameter and its lenght is {} '.format(round(self.diameter,2)))
    
    def get_dimensions(self):
        super().dimensions()

class rectangle(two_dimensionals):
    def __init__(self,width,length):
        self.length=length
        self.width=width
        self.__name='rectangle'
        self.__n_dimensions=2
        self.__tallest_side:length

    def sides(self):
        return('rectangle has 4 sides')
    
    def angles(self):
        return('it has 4 angles')
    
    def get_total_area(self):
        super().total_area()
    
    def get_volume(self):
        super().volume()
        
    def area(self):
        self.area=(self.width*self.length)
        return('the area of this rectangle is {} '.format(round(self.area,2)))
    
    def perimeter(self):
        self.perimeter=2*(self.width+self.length)
        return('the perimeter of thid rectangle is {} '.format(round(self.perimeter,2)))
    
    def diameter(self):
        self.diameter=(self.width**2+self.length**2)**0.5
        return('it has two equal diameter and its length is {} '.format(round(self.diameter,2)))
    
    def get_dimensions(self):
        super().dimensions()
        
class triangle(two_dimensionals):
    def __init__(self,ab,bc,ac,sin_degree):
        self.ab=ab
        self.bc=bc
        self.ac=ac
        self.__name='triangle'
        self.__n_dimensions=2
        self.sins=sin_degree.sinus()
        #aggregation
    def area(self):
        self.area=self.ab*self.bc*self.ac*self.sins*0.5
        return('the area is {} '.format(round(self.area,2)))
        
    def sides(self):
        return('it has 3 sides')
    
    def angles(self):
        return('it has 3 angles')
    
    def get_total_area(self):
        super().total_area()
    
    def get_volume(self):
        super().volume()
        
        
    def diameter(self):
        return('it doesnt have diameter!!!')
    
    def perimeter(self):
        self.perimeter=self.ab+self.bc+self.ac
        return('the perimeter of the triangle is {} '.format(round(self.perimeter,2)))
    
    def get_dimensions(self):
        super().dimensions()
        
class circle(two_dimensionals):
    def __init__(self,radius):
        self.__name='circle'
        self.__n_dimension=2
        self.radius=radius
        self.__diameter:self.radius*2
        self.n_diameter:'uncountable'
        
    def sides(self):
        return('it doesnt have sides')
    
    def angles(self):
        return('it doesnt have angles')
    
    def get_total_area(self):
        super().total_area()
    
    def get_volume(self):
        super().volume()
        
    def area(self):
        self.area=self.radius**2*2*math.pi
        return('the area of the circle is {} '.format(round(self.area,2)))
        
    def diameter(self):
        return('it have uncountable diameters')
    
    def perimeter(self):
        self.perimeter=2*math.pi*self.radius
        return('the perimeter is {} '.format(round(self.perimeter)))
    
    def get_dimensions(self):
        super().dimensions()
        

    
class diamond(two_dimensionals):
    def __init__(self,length,sin_biggest_degree):
        self.length=length
        self.sins=sin_biggest_degree.sinus()#aggregation
        self.__name='diamond'
        self.__n_dimensions=2
        self.n_diameter:2
        
    def sides(self):
        return('diamond has 4 sides')
    
    def angles(self):
        return('it has 4 angles')
    
    def get_total_area(self):
        super().total_area()
    
    def get_volume(self):
        super().volume()
        
    def area(self):
        self.area=(self.length**2)*(self.sins)
        return('the area of the diamond is {} '.format(round(self.area,2)))
    
    def perimeter(self):
        self.perimeter=self.length*4
        return('the perimeter of this diamond is {} '.format(self.perimeter))
        
    def diameter(self):
        self.diameter1=self.length*self.sins
        self.diameter2=((1-self.sins**2)**0.5)*self.length
        
        return('it has two diameter and their lenghts area  {} and {}  '.format(round(self.diameter1,2),round(self.diameter2,2)))
    
    def get_dimensions(self):
        super().dimensions()
        
        
        
        
        
        
        
        
        
        
