from abc import ABC, abstractmethod
from typing import Any


class FeatureExtractionModel(ABC):
    @abstractmethod
    def extract_features(self, image_path: str) -> Any:
        """
        Extract features from the provided image path.

        Args:
            image_path (str): Path to the image.

        Returns:
            Any: Extracted features.

        Raises:
            ValueError: If the image path is empty.
        """
        pass
