import inspect
import doctest
import re
import math

# Define the class 'Circle' and its methods with proper doctests:
class Circle:
    
    def __init__(self, radius):
        # Define doctests for __init__ method:
        """
        """
        self.radius = radius
        
    def area(self):
        # Define doctests for area method:
        """
        """
        # Define area functionality:
        
        
        
    def circumference(self):
        # Define doctests for circumference method:
        """
        """
        # Define circumference functionality:
        
if __name__ == '__main__':
    doctest.testmod()
    
    c2 = Circle(2.5)
    doc1 = inspect.getdoc(c2.__init__)
    doc2 = inspect.getdoc(c2.area)
    doc3 = inspect.getdoc(c2.circumference)
    
    class_count = len(re.findall(r'Circle', doc1))
    func1_count = len(re.findall(r'c1.radius', doc1))
    func1_val = len(re.findall(r'2.5', doc1))
    
    print(str(class_count), str(func1_count), str(func1_val))
    
    class_count = len(re.findall(r'Circle', doc2))
    func1_count = len(re.findall(r'c1.area', doc2))
    func1_val = len(re.findall(r'19.63', doc2)) 
                      
    print(str(class_count), str(func1_count), str(func1_val))
                      
    class_count = len(re.findall(r'Circle', doc3))
    func1_count = len(re.findall(r'c1.circumference', doc3))
    func1_val = len(re.findall(r'15.71', doc3)) 
                      
    print(str(class_count), str(func1_count), str(func1_val))