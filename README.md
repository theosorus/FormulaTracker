

# FormulaTracker

The goal og this project is to train a Yolo model with my own dataset capable of detecting formula1 depends to their team on a given video.

Dataset link : https://www.kaggle.com/datasets/gazeux330000/formula1-box

Yolo link : https://docs.ultralytics.com/fr/

<br>



<div align="center">
<img src="assets/f1_gif_1.gif" alt="Demo du projet" width="600"/>
</div>


# Build the dataset

Pour creer le [dataset](https://www.kaggle.com/datasets/gazeux330000/formula1-box). Je me suis procuré la video entiere d'un grand prix de forule 1. J'ai ensuite enlevé tous les moments qui n'etaient pas pertinents.
J'ai ensuite utilise l'outil [labelImg](https://github.com/HumanSignal/labelImg) pour labeliser les images une a une.

Le dataset contient 10 classes : 
1.Alfa Romeo Racing
2. Ferrari
3.Haas
4.McLaren
5.Mercedes
6.Racing Point
7.RedBull
8.Renault
9.Toro Rosso
10.Williams

train set : 442 images
valid set : 111 images


# Train the model

task: detect
mode: train
model: yolo11l.pt
epochs: 200
time: null
batch: 16
imgsz: 640

## Results




