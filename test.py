import torch
from compressai.models.google import ScaleHyperprior

# model = torch.load('checkpoint_best_loss.pth.tar')

# for k, v in model['state_dict'].items():
#   print(k)

mod = ScaleHyperprior()
print(mod)
