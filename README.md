# 🏎️ FormulaTracker — Detect F1 cars by team with YOLO

> The goal of this project is to train a **YOLO model** on a **custom dataset** to detect Formula 1 cars and classify them by team in video footage.

<div align="center">
  <img src="assets/f1_gif_1.gif" alt="FormulaTracker demo gif" width="700"/>
</div>

<p align="center">
  <a href="https://www.kaggle.com/datasets/gazeux330000/formula1-box">Dataset on Kaggle</a> •
  <a href="https://docs.ultralytics.com/">Ultralytics YOLO docs</a> •
</p>

---


## Dataset

- **Source:** curated from a full Grand Prix broadcast. Non-relevant segments were trimmed out.
- **Annotation tool:** [labelImg](https://github.com/HumanSignal/labelImg)
- **Split:** `train = 442` images, `val = 111` images
- **Classes (10):**
  
1. Alfa Romeo Racing
2. Ferrari
3. Haas
4. McLaren
5. Mercedes
6. Racing Point
7. RedBull
8. Renault
9. Toro Rosso
10. Williams




# Train the model

| Hyperparameters | value      |
|-----------------|------------|
| task            | detect     |
| mode            | train      |
| model           | yolo11l.pt |
| epochs          | 200        |
| batch           | 16         |
| imgsz           | 640        |

### Results

  <img src="assets/results.png" alt="" width="600"/>


### Confusion matrix


  <img src="assets/confusion_matrix_normalized.png" alt="" width="600"/>


### Sample Predictions (validation batch)


  <img src="assets/val_batch2_pred.jpg" alt="" width="600"/>

# Roadmap / Future ideas
- 🚥 Real-time speed estimation: approximate car speeds using multi-frame tracking + homography.
- 📺 On-screen overlay: draw team labels on live or recorded video streams.
- 🧩 Tracking: integrate ByteTrack/BoT-SORT for consistent track IDs across frames.
- 🏁 More seasons: expand dataset with multiple races and lighting/weather conditions.








