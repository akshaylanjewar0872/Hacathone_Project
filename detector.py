# detector.py
import os
import urllib.request
from ultralytics import YOLO
import cv2

class PlasticBottleDetector:
    def __init__(self, model_path):
        self.model_path = model_path
        self._ensure_model_exists()
        self.model = YOLO(self.model_path)

    def _ensure_model_exists(self):
        """Check if YOLO model exists; if not, download it automatically."""
        model_dir = os.path.dirname(self.model_path)
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)

        if not os.path.exists(self.model_path):
            print("🔽 Model file not found. Downloading pretrained YOLO model...")
            url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt"
            try:
                urllib.request.urlretrieve(url, self.model_path)
                print("✅ YOLO model downloaded successfully!")
            except Exception as e:
                print("❌ Failed to download YOLO model:", e)
                raise FileNotFoundError("Could not download the YOLO model automatically.")

    def detect(self, frame):
        """Detect plastic bottles in the given frame using YOLO model."""
        results = self.model.predict(source=frame, conf=0.5, verbose=False)
        count = 0
        for r in results:
            boxes = r.boxes.xyxy
            labels = r.boxes.cls
            names = self.model.names
            for box, cls in zip(boxes, labels):
                label = names[int(cls)]
                if "bottle" in label.lower():
                    count += 1
                    x1, y1, x2, y2 = map(int, box)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{label}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        return frame, count
