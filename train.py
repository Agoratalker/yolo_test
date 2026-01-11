from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.info()  # 查看模型结构摘要
