import torch

tensor01 = torch.rand(2, 3, 4, 5)
index01 = tensor01[0]
index02 = tensor01[0, 1]
index03 = tensor01[0, 1, 1]
index04 = tensor01[0, 1, 1, 0]
print(tensor01.shape)
print(index01.shape, index02.shape, index03.shape, index04)
