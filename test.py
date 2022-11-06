import torch
from google import ScaleHyperprior

model = torch.load('checkpoint_best_loss.pth.tar')
print(model)

mod = ScaleHyperprior()
mod.load_state_dict(model)
