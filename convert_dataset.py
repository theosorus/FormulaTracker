import os
import shutil

RAW_DATASET = "data/raw_dataset"
NEW_DATASET = "dataset"
SPLIT = 0.8

def copy_files(src_list, dst_sub):
    for f in src_list:
        shutil.copy(os.path.join(RAW_DATASET, "images", f),
                    os.path.join(NEW_DATASET, dst_sub, "images", f))
    for f in src_list:
        shutil.copy(os.path.join(RAW_DATASET, "labels", f),
                    os.path.join(NEW_DATASET, dst_sub, "labels", f))
        
if __name__ == "__main__":

    images = os.listdir(os.path.join(RAW_DATASET, "images"))
    labels = os.listdir(os.path.join(RAW_DATASET, "labels"))
    assert len(images) == len(labels), "Mismatch in image/label counts"

    split_index = int(SPLIT * len(images))
    train_images, val_images = images[:split_index], images[split_index:]
    train_labels, val_labels = labels[:split_index], labels[split_index:]

    for sub in ["train", "val"]:
        for t in ["images", "labels"]:
            os.makedirs(os.path.join(NEW_DATASET, sub, t), exist_ok=True)


    copy_files(train_images, "train")
    copy_files(val_images, "val")
    shutil.copy(os.path.join(RAW_DATASET, "classes.txt"),
                os.path.join(NEW_DATASET, "classes.txt"))