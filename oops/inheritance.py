#inheritance

class BaseClass():
  def __init__(self):
    self.name=""
class DerivedCLass(BaseClass):
  def display(self):
    print(self.name)

person = BaseClass()
person.name="yogesh"
