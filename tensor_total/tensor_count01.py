import torch

my_tensor_a = torch.rand(3, 4)
my_tensor_b = torch.rand(3, 4)
print(my_tensor_a, '\n', my_tensor_b)

my_tensor01 = my_tensor_a + my_tensor_b
print(my_tensor01)
# my_tensor01 - torch.add(my_tensor_a, my_tensor_b)
# print(my_tensor01)

my_tensor02 = my_tensor_a - my_tensor_b
print(my_tensor02)
# my_tensor02 = torch.sub(my_tensor_a ,my_tensor_b)
# print(my_tensor02)

my_tensor03 = my_tensor_a * my_tensor_b
print(my_tensor03)
# my_tensor03 = torch.mul(my_tensor_a, my_tensor_b)
# print(my_tensor03)

my_tensor04 = my_tensor_a / my_tensor_b
print(my_tensor04)
# my_tensor04 = torch.div(my_tensor_a, my_tensor_b)
# print(my_tensor04)

my_tensor05 = my_tensor_a ** 2
print(my_tensor05)
# my_tensor05=my_tensor_a.pow(2)
# print(my_tensor05)

my_tensor06 = my_tensor05.sqrt()
print(my_tensor06)

my_tensor07 = my_tensor_a.exp()
print(my_tensor07)

my_tensor08 = my_tensor07.log()
print(my_tensor08)
