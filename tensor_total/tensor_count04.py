import torch

my_tensor_a = torch.rand(3, 4)
my_tensor_b = torch.rand(3, 4)

print(my_tensor_a == my_tensor_b)
print(my_tensor_a != my_tensor_b)
print(torch.eq(my_tensor_a, my_tensor_b))
print(torch.equal(my_tensor_a, my_tensor_b))

print(my_tensor_a > my_tensor_b)
print(torch.gt(my_tensor_a, my_tensor_b))
