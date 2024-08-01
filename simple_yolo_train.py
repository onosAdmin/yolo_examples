import cv2
import supervision as sv
from ultralytics import YOLOv10
import os

import gc
import torch
torch.cuda.empty_cache()
gc.collect()

os.environ["PYTORCH_USE_CUDA_DSA"] = "1"
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"
model = YOLOv10(f'weights/yolov10s.pt')
results = model.train(data="data.yaml",epochs=100)

#yolo task=detect mode=train epochs=2 batch=8 plots=True model=weights/yolov10n.pt data=config.yaml
