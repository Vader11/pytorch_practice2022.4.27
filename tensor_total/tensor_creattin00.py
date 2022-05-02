import torch

my_tensor_calar = torch.tensor(2.)
print(my_tensor_calar)
print(my_tensor_calar.type(), type(my_tensor_calar), len(my_tensor_calar.shape))

my_tensor_arry = torch.tensor(1.3)
print(my_tensor_arry)
print(my_tensor_arry.type(), type(my_tensor_arry), len(my_tensor_arry.shape))

my_tensor_arry01 = torch.tensor([1.0])
print(my_tensor_arry01, '\n', my_tensor_arry01.type(), type(my_tensor_arry01), len(my_tensor_arry01.shape))

my_tensor_arry02 = torch.ones(2)
print(my_tensor_arry02, '\n', my_tensor_arry02.type(), type(my_tensor_arry02), len(my_tensor_arry02.shape))

my_tensor_arry03 = torch.rand(2, 3)
print(my_tensor_arry03)
print(my_tensor_arry03.shape, my_tensor_arry03.size(), my_tensor_arry03.size(0), my_tensor_arry03.size(1))

my_tensor_arry04 = torch.randn(1, 2, 3)
print(my_tensor_arry04)
print(my_tensor_arry04.shape, my_tensor_arry04.size(), my_tensor_arry04.size(0), my_tensor_arry04.size(1))
print(type(my_tensor_arry04.shape), list(my_tensor_arry04.shape))

my_tensor_arry05 = torch.rand(1, 2, 3, 4)
print(my_tensor_arry05)
print(my_tensor_arry05.shape)
print(my_tensor_arry05.dim(),my_tensor_arry05.numel())
