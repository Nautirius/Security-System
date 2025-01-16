from apps.recognition.feature_extraction.feature_extraction_model import FeatureExtractionModel
from core.utils.singleton import singleton
from deepface import DeepFace
from mmpose.apis import init_model, inference_topdown


@singleton
class FaceFeatureExtractionModel(FeatureExtractionModel):
    def __init__(self):
        pass

    def extract_features(self, image_path: str = ''):
        if image_path == '':
            raise ValueError('Image path cannot be empty')

        embeddings = DeepFace.represent(
            img_path = image_path,
            model_name = "GhostFaceNet",
            detector_backend = 'mtcnn',
            align = True,
        )
        if len(embeddings) != 1:
            raise IncorrectFaceAmountError(f"Found {len(embeddings)} faces on image, "
                                           "should be 1")
        return embeddings[0]['embedding']


class IncorrectFaceAmountError(ValueError):
    pass