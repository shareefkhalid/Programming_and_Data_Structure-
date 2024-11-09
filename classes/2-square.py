class square:
  def __init__(self,size):
    self.size=size
    if  not isinstance(size,int):
      raise TypeError('the size must be an integer')
    if size < 0:
      raise ValueError('size must be >=0')

