# How to start

## Create env:
```
python3 -m venv myvenv
```

## Activate virtual env
``` 
source myvenv/bin/activate
```


## Install libraries
``` 
pip3 install tensorboard install -q supervision
pip3 install huggingface_hub
```



## Download yolo models weights
``` 
mkdir -p weights
wget -P ./weights -q https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt
wget -P ./weights -q https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10s.pt
wget -P ./weights -q https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10m.pt
wget -P ./weights -q https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10b.pt
wget -P ./weights -q https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10x.pt
wget -P ./weights -q https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10l.pt
ls -lh ./weights
```

## Prepare the data

## Create a folder for the dataset
``` 
mkdir -p datasets
```


## Create a folder for the each type of data
```
mkdir -p datasets/train/images
mkdir -p datasets/train/labels

mkdir -p datasets/valid/images
mkdir -p datasets/valid/labels

mkdir -p datasets/test/images
mkdir -p datasets/test/labels
```

Put images inside the images folders
Put the relative labels in the labels folders  (inside datasets/train/labels you should put the labels relative to datasets/train/images and so on)


Edit the file data.yaml

replace the string:
```
path: /tmp/miniexample_mio/datasets
```

with the absolute path where you put the datasets




## Train the model

```
python simple_yolo_train.py
```

After few minutes you should see something like this:



```
optimizer: AdamW(lr=0.002, momentum=0.9) with parameter groups 99 weight(decay=0.0), 112 weight(decay=0.0005), 111 bias(decay=0.0)
TensorBoard: model graph visualization added ✅
Image sizes 640 train, 640 val
Using 8 dataloader workers
Logging results to runs/detect/train6
Starting training for 100 epochs...

      Epoch    GPU_mem     box_om     cls_om     dfl_om     box_oo     cls_oo     dfl_oo  Instances       Size
      1/100      5.43G      1.025      2.798      1.568     0.9787      12.08      1.547         30        640: 10
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00
                   all         38         38       0.44      0.684      0.535      0.389

      Epoch    GPU_mem     box_om     cls_om     dfl_om     box_oo     cls_oo     dfl_oo  Instances       Size
      2/100       5.8G     0.9356      1.596      1.462     0.9204      7.466      1.423         16        640: 10
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00
                   all         38         38      0.885      0.813      0.833      0.579

      Epoch    GPU_mem     box_om     cls_om     dfl_om     box_oo     cls_oo     dfl_oo  Instances       Size
      3/100      5.82G     0.8888      1.113      1.391      0.902      3.722      1.395         21        640: 10
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00
                   all         38         38    0.00376      0.632    0.00328    0.00153

      Epoch    GPU_mem     box_om     cls_om     dfl_om     box_oo     cls_oo     dfl_oo  Instances       Size
      4/100      5.53G      1.011      1.063      1.461      1.075      2.308      1.472         18        640: 10
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 2/2 [00
                   all         38         38    0.00123      0.368   0.000963    0.00048


```

See :
https://colab.research.google.com/drive/1Sv3_0S4zhZT763bBMjYxf0HhTit4Bvh6?usp=sharing#scrollTo=LyopYpK1TQrB
