## 5A_IA_-face_mask_detection
L’objectif de ce projet est de permettre aux étudiants de voir l’ensemble de la chaine permettant de concevoir une application à base de Machine Learning (incluant les méthodes de Deep-Learning présentées lors des cours). Le projet porte donc sur les 3 axes principaux suivants : 1. Conception d’une base d’images annotées destinée à l’entrainement des modèles/algorithmes de Machine Learning. 2. Sélection et entrainement d’un modèle adapté à l’application choisie. 3. Mise en œuvre temps réel de ce modèle pour présentation des résultats obtenus.

## Quelques commandes :

Tous les résultats des entrainements ou des traitements sont dans le repertoire "yolov5/runs".

# Installation :
```
git clone https://github.com/HugoBlain/5A_IA_-face_mask_detection
cd yolov5
pip install -r requirements.txt
```

# Entrainement de 0 :
```
python train.py --data data.yaml --cfg yolov5s.yaml --weights '' --epoch 15
```

# Entrainement à partir de poids déjà entrainés :
```
python train.py --data data.yaml --weights yolov5s.pt --epochs 15
```

# Lancer les traitements sur des images :
```
python detect.py --weights best.pt --source ..\DataSets_RoboFlow\valid\images
```

# Lancer les traitements sur le flux de la webcam :
```
python detect.py --weights best.pt --source 0
```




