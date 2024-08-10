import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model_path = 'D:/aitec/AbubakkarDataset/watch2.pt'
model = YOLO(model_path)

# Open the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Make predictions
    results = model(frame)
    
    # Check if results are valid and contain bounding boxes
    if results and len(results) > 0:
        # Visualize the results
        annotated_frame = results[0].plot()
        
        # Display the frame with bounding boxes
        cv2.imshow('YOLOv8 Detection', annotated_frame)
    else:
        # Display the original frame if no detections
        cv2.imshow('YOLOv8 Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
