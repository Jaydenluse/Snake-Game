class Variables(object):
  framerate: int
  multiplier: int
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Variables, cls).__new__(cls)
    return cls.instance
   
singleton = Variables()
new_singleton = Variables()
 
print(singleton is new_singleton)
 
singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)