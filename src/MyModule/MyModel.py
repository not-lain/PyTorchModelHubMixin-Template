from torch import nn
from huggingface_hub import PyTorchModelHubMixin


class MyModel(nn.Module, PyTorchModelHubMixin):
    """an AI model that inherits from PyTorchModelHubMixin"""

    def __init__(self, a=2, b=1):
        super().__init__()
        self.layer = nn.Linear(a, b, bias=False)

    def forward(self, input_ids):
        return self.layer(input_ids)
