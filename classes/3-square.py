class square:
  def __init__(self,size=0):
    self.size=size
    if  not isinstance(size,int):
      raise TypeError('the size must be an integer')
    if size < 0:
      raise ValueError('size must be >=0')
    
  def area(self):
    return self.size**2
try:
  size=5  
  square = square(size)
  print(f'square area {size}:{square.area()}')
except:
  print(0)


