import sys 
import torch


print(torch.__version__)
print(sys.version)

a = torch.tensor([1, 2, 1])
b = torch.tensor([1, 2, 2])

total = a + b

print(total)