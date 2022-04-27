import torch

x = torch.rand(3, 4)
y = torch.rand(3, 4)

z = x + y

print(x)
print(y)
print(z, z.shape)
