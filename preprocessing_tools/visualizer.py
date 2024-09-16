"""
Annotate the players and the ball from the description in the det.txt file
"""

import cv2
import os

def visualizePlayers_bounding_boxes(txt_file, image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(txt_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        frame_number = data[0]
        x = int(data[2])
        y = int(data[3])
        w = int(data[4])
        h = int(data[5])

        image_path = os.path.join(image_folder, f"{frame_number.zfill(5)}.jpg")
        image = cv2.imread(image_path)

        if image is None:
            print(f"Image for frame {frame_number} not found!")
            continue

        color = (0, 0, 255)

        top_left = (x, y)
        bottom_right = (x + w, y - h)
        cv2.rectangle(image, top_left, bottom_right, color, 2)

        output_path = os.path.join(output_folder, f"annotated_frame_{frame_number.zfill(5)}.jpg")
        cv2.imwrite(output_path, image)

def visualizeBall_bounding_boxes(txt_file, image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(txt_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        frame_number = data[0]
        x = int(data[2])
        y = int(data[3])
        w = int(data[4])
        h = int(data[5])

        image_path = os.path.join(image_folder, f"{frame_number.zfill(5)}.jpg")
        image = cv2.imread(image_path)

        if image is None:
            print(f"Image for frame {frame_number} not found!")
            continue

        color = (0, 255, 0)

        top_left = (x, y)
        bottom_right = (x + w, y - h)
        cv2.rectangle(image, top_left, bottom_right, color, 2)

        output_path = os.path.join(output_folder, f"annotated_frame_{frame_number.zfill(5)}.jpg")
        cv2.imwrite(output_path, image)

# Example usage
visualizePlayers_bounding_boxes('sample_data\SNMOT-060\det\det.txt', 'sample_data\SNMOT-060\img1', 'sample_data\SNMOT-060\Annotated')
visualizeBall_bounding_boxes('sample_data\SNMOT-060\gt\gt.txt', 'sample_data\SNMOT-060\Annotated', 'sample_data\SNMOT-060\FinalAnnotated')