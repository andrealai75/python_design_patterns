class Instance(object):
  id = ''
  
  def __init__(self, name):
    self.name = name
  
  def provision_large(self):
    print("Provisioning a Large instance - Name: " + self.name )
    return 'i-Large-001'

  def provision_medium(self):
    print("Provisioning a Medium instance - Name: " + self.name)
    return 'i-Medium-001'

  def provision_small(self):
    print("Provisioning a Small instance - Name: " + self.name)
    return 'i-Small-001'

  def get_status(self):
    return f"Ready ({self.id})"
  
  def __str__(self):
    return f"{self.name} has been provisioned and it is {self.get_status()}"

# =======================================
# =======================================

print('--------------------------------------')
large_instance = Instance('my-large-EC2')
large_instance.provision_large()
print(large_instance)

print('--------------------------------------')
medium_instance = Instance('my-medium-EC2')
medium_instance.provision_medium()
print(medium_instance)

print('--------------------------------------')
small_instance = Instance('my-small-EC2')
small_instance.provision_small()
print(small_instance)
