import torch
from torch.autograd import Variable

my_tensor = torch.ones(2, 2)
x = Variable(my_tensor, requires_grad=True)
print(x)

y = x + 2
print(y)

z = y * y * 3
print(z)

out = z.mean()
print(out)

out.backward()
print(x.grad)
