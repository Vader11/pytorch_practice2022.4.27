import torch
from torch import nn
from torch.nn import functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)

        self.cf1 = nn.Linear(16 * 5 * 5, 120)
        self.cf2 = nn.Linear(120, 60)
        self.cf3 = nn.Linear(60, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))

        x = x.view(-1, self.num_flat_feature(x))

        x = F.relu(self.cf1(x))
        x = F.relu(self.cf2(x))
        x = F.relu(self.cf3(x))

        return x

    def num_flat_feature(self, x):
        size = x.size()[1:]
        num_feature = 1
        for s in size:
            num_feature *= s
        return num_feature


if __name__ == '__main__':
    net = Net()
    inputs = torch.randn((1, 1, 32, 32))
    outputs = net(inputs)
    print(net)
    print(outputs.shape, type(outputs.shape))
    print(outputs.size(), type(outputs.size()))
