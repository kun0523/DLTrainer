import os
import json
import shutil
import random

CLASSES = ["dent", ]


def createDir(target_dir, is_rm=0):
    if is_rm and os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    return target_dir


def lb2obb(fname):
    label_info = ""
    with open(fname, 'r') as fp:
        content = json.load(fp)

    img_h = content["imageHeight"]
    img_w = content["imageWidth"]
    objects = content["shapes"]
    for obj in objects:
        cls_idx = CLASSES.index(obj['label'])
        label_info += f"{cls_idx} "
        x1, y1 = obj["points"][0]
        x2, y2 = obj["points"][1]
        center_x = (x1+x2)/2
        center_y = (y1+y2)/2
        w = abs(x2-x1)
        h = abs(y2-y1)
        label_info += f"{center_x/img_w:.6f} {center_y/img_h:.6f} {w/img_w:.6f} {h/img_h:.6f}"
        label_info += "\n"

    return label_info


if __name__ == "__main__":
    src_dir = r"E:\ultralytics\datasets\impressions\cut_cell"
    dst_img_dir = r"E:\ultralytics\datasets\impressions\yolo\images"
    dst_lbl_dir = r"E:\ultralytics\datasets\impressions\yolo\labels"
    createDir(dst_img_dir, is_rm=1)
    createDir(dst_lbl_dir, is_rm=1)

    label_lst = [f for f in os.listdir(src_dir) if f.endswith(".json")]
    random.shuffle(label_lst)
    val_num = 0.2 * len(label_lst)
    # test_num = 0.1 * len(label_lst)

    counter = 0
    for f in os.listdir(src_dir):
        if not f.endswith(".json"): continue
        counter += 1
        src_file = os.path.join(src_dir, f)
        obb_label = lb2obb(src_file)

        # if counter < test_num:
        #     tmp_dst_img_dir = createDir(os.path.join(dst_img_dir, "test"))
        #     tmp_dst_lbl_dir = createDir(os.path.join(dst_lbl_dir, "test"))
        if counter < val_num:
            tmp_dst_img_dir = createDir(os.path.join(dst_img_dir, "val"))
            tmp_dst_lbl_dir = createDir(os.path.join(dst_lbl_dir, "val"))
        else:
            tmp_dst_img_dir = createDir(os.path.join(dst_img_dir, "train"))
            tmp_dst_lbl_dir = createDir(os.path.join(dst_lbl_dir, "train"))

        dst_file = os.path.join(tmp_dst_lbl_dir, f.replace(".json", ".txt"))
        with open(dst_file, 'w') as fp:
            fp.write(obb_label)

        src_pth = os.path.join(src_dir, f.replace(".json", ".jpg"))
        dst_pth = os.path.join(tmp_dst_img_dir, f.replace(".json", ".jpg"))
        shutil.copy(src_pth, dst_pth)

    print()

