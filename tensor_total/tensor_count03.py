import torch

my_tensor = torch.rand(3, 4)
print(my_tensor)

print(my_tensor.sum())
print(my_tensor.mean())
print(my_tensor.prod())

print(my_tensor.max())
print(my_tensor.min())

print(my_tensor.max(dim=1))
print(my_tensor.min(dim=1))

print(my_tensor.argmin())
print(my_tensor.argmax())

print(my_tensor.argmin(dim=1))
print(my_tensor.argmax(dim=1))

print('***************************')

