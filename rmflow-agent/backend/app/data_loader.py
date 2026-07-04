from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any


class MockDataLoader:
    def __init__(self) -> None:
        self.project_root = Path(__file__).resolve().parents[2]
        self.data_dir = self.project_root / "data"

    def load_json(self, filename: str) -> list[dict[str, Any]]:
        file_path = self.data_dir / filename
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def customers(self) -> list[dict[str, Any]]:
        return self.load_json("customers.json")

    def interactions(self) -> list[dict[str, Any]]:
        return self.load_json("interactions.json")

    def opportunities(self) -> list[dict[str, Any]]:
        return self.load_json("opportunities.json")

    def campaigns(self) -> list[dict[str, Any]]:
        return self.load_json("campaigns.json")

    def products(self) -> list[dict[str, Any]]:
        return self.load_json("products.json")

    def email_templates(self) -> list[dict[str, Any]]:
        return self.load_json("email_templates.json")

    def call_scripts(self) -> list[dict[str, Any]]:
        return self.load_json("call_scripts.json")


@lru_cache(maxsize=1)
def get_data_loader() -> MockDataLoader:
    return MockDataLoader()
