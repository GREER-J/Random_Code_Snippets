class test():
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname

names = []

for i in range(0,10):
  name = "object" + str(i)
  names.append(name)
  name = test("Jake", "Miles")

print("Done!")

for name in names:
  print(vars(name))
  
