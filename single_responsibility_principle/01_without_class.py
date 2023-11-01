def provision_large(name):
  print("Provisioning a Large instance - Name: " + name )
  return 'i-Large-001'

def provision_medium(name):
  print("Provisioning a Medium instance - Name: " + name)
  return 'i-Medium-001'

def provision_small(name):
  print("Provisioning a Small instance - Name: " + name)
  return 'i-Small-001'

def get_status(id):
  return f"Ready ({id})"

# =======================================
# =======================================

print('--------------------------------------')
large_name = 'my-large-EC2'
large_id = provision_large(large_name)
print(f"{large_name} has been provisioned and it is {get_status(large_id)}")

print('--------------------------------------')
medium_name = 'my-medium-EC2'
medium_id = provision_medium(medium_name)
print(f"{medium_name} has been provisioned and it is {get_status(medium_id)}")

print('--------------------------------------')
small_name = 'my-small-EC2'
small_id = provision_small(small_name)
print(f"{small_name} has been provisioned and it is {get_status(small_id)}")
