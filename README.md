                                                 **Real-Time Object Detection and Tracking Using YOLOv6**
        
**Introduction**
The project involves real-time object detection and tracking using a custom-trained YOLOv6 model. 
The primary objective is to detect and track a wristwatch in video feeds, utilizing a custom dataset consisting of images and corresponding labels. This report details the entire process
from dataset preparation to the deployment of the model in a real-time application.

**2. Dataset Preparation**
The dataset consists of 100 images in total, with 80 images used for training and 20 images for validation. Each image has a corresponding label file in YOLO format, which contains the 
bounding box coordinates for the wristwatch in the image.

**Training Dataset:**

80 images
Corresponding label files
data.yml file specifying the paths for images and labels
Validation Dataset:

20 images
Corresponding label files
data.yml file specifying the paths for images and labels
The data.yml file is crucial as it configures the paths for images and labels, ensuring the model correctly identifies the data sources during training.

**3. Model Training**
The YOLOv6 model was used for training the dataset. The following key aspects were considered during the training process:

Model Weights:

Initial Weights: YOLOv6 pre-trained weights were used to initialize the model.
Best Weights: The best-performing model checkpoint during training, saved as watch2.pt.
Last Weights: The last model checkpoint saved after training completion.

Training Process:
The model was trained on the 80-image dataset, using the provided data.yml file to load images and labels.
The training process included multiple epochs, with the model adjusting weights based on the loss function to improve detection accuracy.

**4. Model Evaluation**
The model's performance was evaluated using various metrics, with outputs provided as graphical and tabular data:

Precision-Recall (PR) Curve: Demonstrates the trade-off between precision and recall for different threshold values.

F1-Score Curve: Shows the harmonic mean of precision and recall, highlighting the model's balance between the two.

Precision Curve: Indicates the accuracy of the positive predictions.

Recall Curve: Reflects the ability of the model to identify all relevant instances of the object.

**Results:**

Results.png: A visual representation of the model’s performance.
Results.csv: A tabular representation of evaluation metrics.
Label Correlogram: A graphical representation of label correlation, showing how different classes interact and overlap during predictions.

These evaluation metrics are essential for understanding the model's strengths and weaknesses, enabling further refinement if necessary.

**5. Real-Time Object Detection and Tracking Implementation**
The project implemented real-time object detection and tracking using OpenCV and the trained YOLOv6 model. The key steps involved in the implementation are:

Loading the YOLOv6 Model:

The model is loaded using the ultralytics library, with the watch2.pt weight file.
Video Capture:

The webcam feed is captured using OpenCV’s VideoCapture function.
Object Detection:

The model processes each frame to detect objects (wristwatches) with a confidence threshold of 0.9.
Tracking:

The detected objects are tracked using a custom AtlasTracker class, which leverages OpenCV’s CSRT tracker.
Bounding Boxes:

Bounding boxes are drawn around detected objects, with color coding to indicate whether the watch is detected.
Visualization:

The results are visualized in real-time, showing both the detection and tracking outcomes.
**6. Conclusion**
The project successfully demonstrates the use of a custom-trained YOLOv6 model for real-time wristwatch detection and tracking. The implementation leverages various tools, including OpenCV for video processing and the YOLOv6 framework for object detection. The model's performance was thoroughly evaluated using industry-standard metrics, ensuring its reliability for deployment in practical applications.

The provided weights, evaluation metrics, and implementation code offer a comprehensive toolkit for extending this project to other object detection tasks, highlighting the flexibility and power of the YOLOv6 model.
