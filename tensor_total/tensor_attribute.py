import torch

a = torch.randn((2, 3))
print(a.type())
print(type(a))

print(isinstance(a, torch.FloatTensor))
print(isinstance(a, torch.cuda.DoubleTensor))
a1 = a.cuda()
print(isinstance(a1, torch.cuda.FloatTensor))
print(a1)
