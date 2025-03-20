from ultralytics import YOLO



if __name__ == '__main__':
    path_to_config = "dataset/data.yaml"
    model = YOLO("yolo11n.pt")  
    results = model.train(data=path_to_config, epochs=100, imgsz=640)