"""
Methodology followed: 
    Get the center pixel around each player (ignore the ball's label)
    Capture the colour of pixels around it of an **arbitrary size **(Update size when finalized)
    -? Use a clustering algorithm to group the players with "similar jersey" colours together. 
    (outlier assigned as referee, ALWAYS YELLOW IN SAMPLE_DATA
        more specifically, referee usually has the HEX code #bbd245 and RGB (187,210,69)
"""
import os
import cv2
import numpy as np

def process_images_and_labels(image_folder, label_folder, output_label_folder):
    
    for image_file in os.listdir(image_folder):
        if image_file.endswith('.jpg') or image_file.endswith('.png'):
            image_path = os.path.join(image_folder, image_file)
            label_path = os.path.join(label_folder, image_file.replace('.jpg', '.txt').replace('.png', '.txt'))

            image = cv2.imread(image_path)
            height, width = 1920, 1080

            with open(label_path, 'r') as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                data = line.strip().split()
                class_id = int(data[0])
                x_center = float(data[1]) * width
                y_center = float(data[2]) * height
                box_width = float(data[3]) * width
                box_height = float(data[4]) * height

                center_x = int(x_center)
                center_y = int(y_center)
                pixel_region = image[max(center_y - 5, 0):min(center_y + 5, height), 
                                     max(center_x - 5, 0):min(center_x + 5, width)]

                mean_color = np.mean(pixel_region, axis=(0, 1))

                if mean_color[2] > 150:
                    team_id = 0
                elif mean_color[0] > 150:
                    team_id = 1
                else:
                    team_id = 2

                new_line = f"{class_id} {data[1]} {data[2]} {data[3]} {data[4]} {team_id}\n"
                new_lines.append(new_line)

            output_label_path = os.path.join(output_label_folder, image_file.replace('.jpg', '.txt').replace('.png', '.txt'))
            with open(output_label_path, 'w') as f:
                f.writelines(new_lines)

image_folder = 'path_to_images_folder'
label_folder = 'path_to_labels_folder'
output_label_folder = 'path_to_output_labels_folder'

process_images_and_labels('sample_data\SNMOT-060\img1', 'sample_data\SNMOT-060\labels\sample_public', 'sample_data\SNMOT-060\labels\metric_labels_final')