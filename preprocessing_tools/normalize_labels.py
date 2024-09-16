"""
The dataset is provided by SoccerNet
The tracking dataset itself is quite huge (around 9GB) and is covered under a NDA/license.
They have been cited, but for the clarity and to better understand of the code, I shall be attaching a small sample of the dataset in sample_data

SNMOT_60 or SoccerNetMulti-Object-Tracking_60 is one of the 110 folders in the training dataset, each containing the frames for a particular subsection of a match.

Summary of data:
Each folder has 3 main parts: 
    1) an image-file folder, containing around 750 images/frames from footage of the game(s)
    Instead of each image being already (visually) annotated with bounding boxes around the players/ referee and the ball,
    the labels/boxes for the players on the field and the ball are contained in separate files

    2) a gt.txt, which contains the ground truth or the coordinates of the bounding box around the ball in each frame
        # example: 3,1,901,855,79,172,1,-1,-1,-1
        # 3: frame number
        # 1: tracking ID for the ball (there is only 1 ball, so always 1 for the ball)
        # 901: x-coordinate of the top-left corner of the bounding box
        # 855: y-coordinate of the top-left corner of the bounding box
        # 79: width of the bounding box
        # 172: height of the bounding box
        # 1: Confidence score (always 1 since ground truth)
        # other coordinates are not of much use for the initial case of tracking.
    3) a det.txt, which contains the same descriptions but for the ball as well as the players
        # Key difference: the 2nd value or the tracking ID, each player has its own tracking ID throughout the whole frame(s)
        # Helps with associating teams and to not lose track of players in subsequent frames
"""

import os

def centralizedBoxes(txt_file, output_folder, img_width, img_height):
    """
    Processes the det.txt file
    Returns centralized bounding boxes in YOLO format for each frame in folder <output_folder>
    """
    with open(txt_file, 'r') as file:
        lines = file.readlines()
    counter = 0

    for line in lines:
        counter += 1
        data = line.strip().split(',')
        # Official Reference: https://github.com/SoccerNet/sn-tracking
        frame_number = data[0]
        _ = data[1]
        x = int(data[2])
        y = int(data[3])
        w = int(data[4])
        h = int(data[5])
        conf = int(data[6])
        _ = data[7:]

        center_x = (x + w / 2) / w
        center_y = (y - h / 2) / h
        width_normal = w
        height_normal = h

        # if counter<100:
        #     print(center_x, center_y, width_normal, height_normal)
        label_file = os.path.join(output_folder, f"frame_{frame_number}.txt")

        with open(label_file, 'a+') as f:
            f.write(f"{1} {center_x} {center_y} {width_normal} {height_normal}\n")

centralizedBoxes('sample_data\SNMOT-060\det\det.txt', 'sample_data\SNMOT-060\labels\sample_public', 1920, 1080)

"""
update: The above code takes ages to run, taking around 150 seconds to process the 750 frames in the sample dataaset.
Below is some possible imporvements if you are reading this, and wondering the same.

logs:   [Running] python -u "c:\Users\harsh\Desktop\GitLocal\SoccerAnalytics\utils\normalize_labels.py"

        [Done] exited with code=0 in 151.594 seconds


Lines 36-56 can be simplified by importing and using the pybboxes library.
Credit: from stack overflow replies of simpler code snippets, https://stackoverflow.com/questions/56115874/how-to-convert-bounding-box-x1-y1-x2-y2-to-yolo-style-x-y-w-h
# pip install pybboxes
import pybboxes as pbx

voc_bbox = (100, 100, 200, 200)
W, H = 1000, 1000  # WxH of the image
pbx.convert_bbox(voc_bbox, from_type="voc", to_type="yolo", image_size=(W,H))
>>> (0.15, 0.15, 0.1, 0.1)
"""