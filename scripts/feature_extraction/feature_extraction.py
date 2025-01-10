from deepface import DeepFace
from mmpose.apis import init_model, inference_topdown
from crowdpose import dataset_info
import math

class IncorrectFaceAmountError(ValueError):
    pass

class IncorrectPeopleAmountError(ValueError):
    pass

# returns a 512 elements long list of face features extracted from image located
# under passed path, raises error when 0 or more than 1 face are found in image
def extract_face_features(image_path):
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

class PoseFeatureExtractionModel:
    def __init__(self):
        model_config = 'rtmo-l_16xb16-700e_body7-crowdpose-640x640.py'
        model_checkpoint = 'https://download.openmmlab.com/mmpose/v1/projects/rtmo/rtmo-l_16xb16-700e_body7-crowdpose-640x640-5bafdc11_20231219.pth'
        device = 'cpu'
        self.model = init_model(model_config, model_checkpoint, device=device)
        name_to_keypoint_id = {}
        for keypoint_info in dataset_info['keypoint_info'].values():
            keypoint_name = keypoint_info['name']
            keypoint_id = keypoint_info['id']
            name_to_keypoint_id[keypoint_name] = keypoint_id
        self.linked_keypoints_ids_list = []
        for link_info in dataset_info['skeleton_info'].values():
            link_by_names = link_info['link']
            link_end1_name, link_end2_name = link_by_names
            link_end1_id = name_to_keypoint_id[link_end1_name]
            link_end2_id = name_to_keypoint_id[link_end2_name]
            self.linked_keypoints_ids_list.append((link_end1_id, link_end2_id))

    def extract_features(self, img_path):
        model_results = inference_topdown(self.model, img_path)
        prediction_instances = model_results[0].pred_instances
        if len(prediction_instances) != 1:
            raise IncorrectPeopleAmountError(f"Found {len(prediction_instances)} "
            "people on image, should be 1")
        keypoints_coordinates = prediction_instances.keypoints[0]
        feature_list = []
        for point1_id, point2_id in self.linked_keypoints_ids_list:
            point1 = keypoints_coordinates[point1_id]
            point2 = keypoints_coordinates[point2_id]
            feature_list.append(math.dist(point1, point2))
        normalizing_distance = (feature_list[5] + feature_list[6]) / 2
        feature_list = [feature / normalizing_distance for feature in feature_list]
        return feature_list

# usage example
# if __name__ == "__main__":
#     face_embeddings = extract_face_features('image1.jpg')
#     model = PoseFeatureExtractionModel()
#     pose_embeddings = model.extract_features('image4.jpg')
#     print(face_embeddings)
#     print(pose_embeddings)
