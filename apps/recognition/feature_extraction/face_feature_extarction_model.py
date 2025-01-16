from core.utils.singleton import singleton
from deepface import DeepFace
from mmpose.apis import init_model, inference_topdown


@singleton
class FaceFeatureExtractionModel:
    def __init__(self, image_path: str = ''):
        self.image_path = image_path

    def extract_features(self):
        if self.image_path == '':
            raise ValueError('Image path cannot be empty')

        embeddings = DeepFace.represent(
            img_path = self.image_path,
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