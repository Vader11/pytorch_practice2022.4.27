import torch

my_tensor_a = torch.tensor(3.94)
my_tensor_b = torch.tensor(3.14)
my_tensor_c = torch.rand(3, 4)
print(my_tensor_a)
print(my_tensor_b)

my_tensor01 = my_tensor_a.floor()
print(my_tensor01)
my_tensor02 = my_tensor_b.floor()
print(my_tensor02)

my_tensor01 = my_tensor_a.ceil()
print(my_tensor01)
my_tensor02 = my_tensor_b.ceil()
print(my_tensor02)

my_tensor01 = my_tensor_a.round()
print(my_tensor01)
my_tensor02 = my_tensor_b.round()
print(my_tensor02)

my_tensor01 = my_tensor_a.trunc()
my_tensor02 = my_tensor_a.frac()
print(my_tensor01, '\n', my_tensor02)

print(my_tensor_c)
my_tensor03 = my_tensor_c.clamp(0.4, 0.5)
print(my_tensor03)
