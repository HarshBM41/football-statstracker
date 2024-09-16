"""
Base tracker consists of just configuring the dataset.yaml file, and passing it through the regular ultralytics model.train method

_________________________________________________________________________________________________________________________________________________________
NOTE: The complete dataset has not been included in the repository, since it is covered under a NDA. The training function below is just a template
assuming that sample_data is the complete dataset, which it really isn't.

However, while working with the actual dataset, the process is not all that different.
** Make sure to use the files in the <utils> folder, if you would need to also preprocess the labels in a similar format that I ended up following.
** Again, the normalize_labels and clean-labels together would be the best way to go about it, since the labels are not in the regular format of
        <id x_centre y_centre width height>

After converting the dataset into a format suitable for your model, just modify the dataset.yaml file and path argument here.

Also since the actual dataset is pretty huge, instead of compromising on quality of training, by using smaller datasets,
You could look into using a CSP like AWS for the whole process. Load data into S3 using AWS CLI, then importing it into SageMaker notebook for training.
Maybe even SageMaker Endpoints through the SageMaker studio for testing the model.
___________________________________________________________________________________________________________________________________________________________
"""

from ultralytics import YOLO
model = YOLO('yolovnas-s')
model.train(
    data="sample_yaml\dataset.yaml",
    epochs=11, # our sample dataset is smaller, modify later
    batch=32, # ''
    imgsz=640, # default value hai
#   device='0',
    verbose=False,
)