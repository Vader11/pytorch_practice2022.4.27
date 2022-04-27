import torch

my_tensor = torch.rand(3, 4)
print(my_tensor)

if torch.cuda.is_available():
    my_tensor01 = my_tensor.cuda()
    print(my_tensor01)
