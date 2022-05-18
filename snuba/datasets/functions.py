from snuba.datasets.dataset import Dataset
from snuba.datasets.entities import EntityKey


class FunctionssDataset(Dataset):
    def __init__(self) -> None:
        super().__init__(default_entity=EntityKey.FUNCTIONS)
