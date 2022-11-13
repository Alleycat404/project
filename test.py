import torch
# from google import ScaleHyperprior

model = torch.load('checkpoint_best_loss.pth.tar')

for k, v in model['state_dict'].items():
  print(k)

# mod = ScaleHyperprior()
# mod.load_state_dict(model)
