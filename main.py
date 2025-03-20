import os
import argparse

from ultralytics import YOLO
import cv2

def predict(args):
    model = YOLO(args.weights)
    cap = cv2.VideoCapture(args.video_path)
    if not cap.isOpened():
        raise IOError(f"Impossible d'ouvrir la vidéo : {args.video_path}")

    # Obtenir les propriétés de la vidéo
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Chemin de la vidéo de sortie
    output_path = os.path.join(args.output_dir, f"{args.name}_predictions.mp4")

    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame, imgsz=640, conf=0.5, verbose=False)
        annotated_frame = results[0].plot()
        out.write(annotated_frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Vidéo avec prédictions enregistrée dans : {output_path}")



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path',"-i", type=str, required=True, help='path to the video')
    parser.add_argument('--output_dir',"-o", type=str,default='output', help='path to the output directory')
    parser.add_argument('--weights',"-w", type=str, default='train_formula_yolo_l/weights/best.pt', help='path to the weights file')
    parser.add_argument('--conf', type=float, default=0.5, help='object confidence threshold')
    parser.add_argument('--name',"-n", type=str, default="model", help='name of the model')
    args = parser.parse_args()

    predict(args)
    
    

