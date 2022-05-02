import numpy as np
import torch

tensor00 = torch.tensor([[1, 2, 3], [3, 2, 4]])
print(tensor00)

tensor01 = torch.ones(2, 3)
print(tensor01)

tensor02 = torch.rand(2, 3)
print(tensor02)

tensor03 = torch.randn((2, 3))
print(tensor03)

tensor0304 = torch.from_numpy(np.array([1, 2, 3]))
print(tensor0304)