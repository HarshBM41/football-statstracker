##  Overview: About The Model
This project is an effort towards a computer vision model, designed to comprehensively track the players and ball, even when out of frame. The model employs object detection and tracking algorithms to extract meaningful metrics such as team possession and ball-speed estimation.

Future Steps (open to suggestions -- WIP)
    (New functionality to incorporate offside detection, main hurdle being finding quality offside data)

## About the dataset
The dataset is provided by SoccerNet (cited).
The tracking dataset itself is quite huge (around 9GB) and is covered under a NDA/license.
They have been cited, but for the clarity and to better understand of the code, I shall be attaching a small sample of the dataset in sample_data.

SNMOT_60 or SoccerNetMulti-Object-Tracking_60 is one of the 110 folders in the training dataset, each containing the frames for a particular subsection of a match.

## Understanding Sample Dataset format
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
## Sample Annotated Results


## Citation

```bibtex
@inproceedings{cioppa2022soccernet,
  title={SoccerNet-Tracking: Multiple Object Tracking Dataset and Benchmark in Soccer Videos},
  author={Cioppa, Anthony and Giancola, Silvio and Deliege, Adrien and Kang, Le and Zhou, Xin and Cheng, Zhiyu and Ghanem, Bernard and Van Droogenbroeck, Marc},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={3491--3502},
  year={2022}
}
```

```bibtex
@inproceedings{Giancola_2022,
	doi = {10.1145/3552437.3558545},
	url = {https://doi.org/10.1145%2F3552437.3558545},
	year = 2022,
	month = {oct},
	publisher = {{ACM}},
	author = {Silvio Giancola and Anthony Cioppa and Adrien Deli{\`{e}}ge and Floriane Magera and Vladimir Somers and Le Kang and Xin Zhou and Olivier Barnich and Christophe De Vleeschouwer and Alexandre Alahi and Bernard Ghanem and Marc Van Droogenbroeck and Abdulrahman Darwish and Adrien Maglo and Albert Clap{\'{e}}s and Andreas Luyts and Andrei Boiarov and Artur Xarles and Astrid Orcesi and Avijit Shah and Baoyu Fan and Bharath Comandur and Chen Chen and Chen Zhang and Chen Zhao and Chengzhi Lin and Cheuk-Yiu Chan and Chun Chuen Hui and Dengjie Li and Fan Yang and Fan Liang and Fang Da and Feng Yan and Fufu Yu and Guanshuo Wang and H. Anthony Chan and He Zhu and Hongwei Kan and Jiaming Chu and Jianming Hu and Jianyang Gu and Jin Chen and Jo{\~{a}}o V. B. Soares and Jonas Theiner and Jorge De Corte and Jos{\'{e}} Henrique Brito and Jun Zhang and Junjie Li and Junwei Liang and Leqi Shen and Lin Ma and Lingchi Chen and Miguel Santos Marques and Mike Azatov and Nikita Kasatkin and Ning Wang and Qiong Jia and Quoc Cuong Pham and Ralph Ewerth and Ran Song and Rengang Li and Rikke Gade and Ruben Debien and Runze Zhang and Sangrok Lee and Sergio Escalera and Shan Jiang and Shigeyuki Odashima and Shimin Chen and Shoichi Masui and Shouhong Ding and Sin-wai Chan and Siyu Chen and Tallal El-Shabrawy and Tao He and Thomas B. Moeslund and Wan-Chi Siu and Wei Zhang and Wei Li and Xiangwei Wang and Xiao Tan and Xiaochuan Li and Xiaolin Wei and Xiaoqing Ye and Xing Liu and Xinying Wang and Yandong Guo and Yaqian Zhao and Yi Yu and Yingying Li and Yue He and Yujie Zhong and Zhenhua Guo and Zhiheng Li},
	title = {{SoccerNet} 2022 Challenges Results},
	booktitle = {Proceedings of the 5th International {ACM} Workshop on Multimedia Content Analysis in Sports}
}
```

## Sample Model Inference Footage
