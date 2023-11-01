import abc

class Instance(object):
  id = ''
  
  def __init__(self, name):
    self.name = name

  def get_status(self):
    return f"Ready ({self.id})"
  
  def __str__(self):
    return f"{self.name} has been provisioned and it is {self.get_status()}"
  
class AbcProvisioner(abc.ABC):
  @abc.abstractmethod
  def provision(self, instance):
    pass
  
class ProvisionerLarge(AbcProvisioner):
  def provision(self, instance):
    print("Provisioning a Large instance - Name: " + instance.name )
    return 'i-Large-001'

class ProvisionerMedium(AbcProvisioner):
  def provision(self, instance):
    print("Provisioning a Medium instance - Name: " + instance.name)
    return 'i-Medium-001'

class ProvisionerSmall(AbcProvisioner):
  def provision(self, instance):
    print("Provisioning a Small instance - Name: " + instance.name)
    return 'i-Small-001'

# =======================================
# =======================================

print('--------------------------------------')
large_instance = Instance('my-large-EC2')
large_instance.id = ProvisionerLarge().provision(large_instance)
print(large_instance)

print('--------------------------------------')
medium_instance = Instance('my-medium-EC2')
medium_instance.id = ProvisionerMedium().provision(medium_instance)
print(medium_instance)

print('--------------------------------------')
small_instance = Instance('my-small-EC2')
small_instance.id = ProvisionerSmall().provision(small_instance)
print(small_instance)
