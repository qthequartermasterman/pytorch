from typing import Union

import numpy as np

import torch

def make_np(x:Union[np.ndarray, str,torch.Tensor]) -> np.ndarray: ...
