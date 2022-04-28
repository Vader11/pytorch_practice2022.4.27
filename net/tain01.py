import torch
from torch import optim
from torch.autograd import Variable

from moudle import Net

net = Net()
# params = list(net.parameters())
# params_size = [param.size() for param in params]
# print(len(params))
# for p in params_size:
#     print(p)

inputs = Variable(torch.randn(1, 1, 32, 32))

# print(inputs)
# print(out)
#
# net.zero_grad()
# out.backward(torch.randn(1, 10))

target = Variable(torch.randn(1, 10))
loss_func = torch.nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.1)
epoch = 10
for i in range(1, epoch + 1):
    print(f"star train{i}")
    out = net(inputs)
    loss = loss_func(out, target)
    loss.backward()
    optimizer.step()
print('train over')
