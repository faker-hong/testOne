import numpy as np
import torch
import helper
import matplotlib.pyplot as plt
from torchvision import datasets, transforms
from torch import nn
import torch.nn.functional as F

# Define a transform to normalize the data
# transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)), ])
transform = transforms.Compose([
     transforms.ToTensor(),
     transforms.Lambda(lambda x: x.repeat(3, 1, 1)),
     transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
 ])
# Download and load the training data
train_set = datasets.MNIST('MNIST_data/', download=True, train=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)

# Download and load the test data
test_set = datasets.MNIST('MNIST_data/', download=True, train=False, transform=transform)
train_loader = torch.utils.data.DataLoader(test_set, batch_size=64, shuffle=True)

dataiter = iter(train_loader)
images, labels = dataiter.next()
# squeeze() 去除单维度条目
plt.imshow(images[1][1].numpy().reshape(28, 28).squeeze(), cmap='Greys_r')
plt.show()