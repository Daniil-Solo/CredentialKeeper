from dataclasses import dataclass
from src.domains_layer.shared import UniqueId


@dataclass
class BaseDomainEntity:
    id: UniqueId or None
