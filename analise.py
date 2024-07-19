from ultralytics import YOLO

modelo = YOLO('yolov8m.pt')

modelo.predict(source='0', show=True)