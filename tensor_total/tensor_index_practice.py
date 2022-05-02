import torch

my_tensor = torch.randn(3, 3)
print(my_tensor, my_tensor.shape)

my_mask = my_tensor > 0
print(my_mask, my_mask.shape)

my_value = torch.masked_select(my_tensor, my_mask)
print(my_value)
