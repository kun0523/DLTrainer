# This Python file uses the following encoding: utf-8
# 数据校验  输入是labelme标注格式，输出yolo标注格式
from abc import ABC, abstractmethod
import os
import shutil
import json
import random
import subprocess
from PIL import Image

from utils.utils import create_dir, get_timestamp, copy_files


# 向界面开放的接口
class DataSet(ABC):
    def __init__(self, src_dir: str, save_dir: str, label_txt_pth: str):
        assert os.path.isdir(src_dir), f"Error, dir:[{src_dir}] Not Found!"
        self.src_dir = src_dir

        save_dir = os.path.join(save_dir, f"dataset_{get_timestamp()}")
        self.save_dir = save_dir

        assert os.path.isfile(label_txt_pth), f"Error, file:[{label_txt_pth}] Not Found!"
        self.label_txt_pth = label_txt_pth

        self.CLASSES = []
        with open(label_txt_pth, "r") as fp:
            self.CLASSES = [line.strip() for line in fp.readlines() if line not in ["__ignore__", "_background_"]]
        return

    @abstractmethod
    def label_data(self):
        # cls: 打开文件夹，新建各个类别的子文件夹，让用户自己分；  det：打开labelme，用户自己标注
        pass

    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def convert_and_split(self, train_percent: float):
        pass


class UltrClasDataSet(DataSet):
    def __init__(self):
        super().__init__()
        return



class UltrDetDataSet(DataSet):
    def __init__(self, src_dir, save_dir, label_txt_pth, tool_pth: str):
        super().__init__(src_dir, save_dir, label_txt_pth)
        self.tool_pth = tool_pth
        return

    @staticmethod
    def __run_cmd(command_):
        process = subprocess.Popen(command_, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while process.poll() is None:
            line = process.stdout.readline()
            if type(line) == bytes:
                line = line.decode()
            line = line.strip()
            if line:
                print(line)
        if process.returncode == 0:
            print("success")
        else:
            print("failed")
        return

    def __parse_json2yolo_txt(self, image_pth, json_pth, save_txt_pth):
        img = Image.open(image_pth)
        imgw, imgh = img.size
        with open(json_pth, "r") as j:
            json_info = json.load(j)

        with open(save_txt_pth, "w") as t:
            label_str = ""
            for obj in json_info["shapes"]:
                if obj["label"] not in self.CLASSES: continue
                label_str += f"{self.CLASSES.index(obj['label'])} "
                box = obj["points"]
                cx = (box[0][0] + box[1][0]) / 2
                cy = (box[0][1] + box[1][1]) / 2
                w = abs(box[0][0] - box[1][0])
                h = abs(box[0][1] - box[1][1])
                label_str += f"{cx / imgw:.6f} {cy / imgh:.6f} {w / imgw:.6f} {h / imgh:.6f}"
                label_str += "\n"
            t.write(label_str)

        return

    def label_data(self):
        command = f"{self.tool_pth} {self.src_dir} --labels {self.label_txt_pth} --nodata --autosave"
        self.__run_cmd(command)
        return

    def check(self):
        # 统计 bbox长宽与图像长宽的比值
        return

    def __create_dataset_dir(self):
        # dataset_root/(images|labels)/(train|val)
        ret = dict()
        ret["train_img_dir"] = create_dir(os.path.join(self.save_dir, "images", "train"))
        ret["val_img_dir"] = create_dir(os.path.join(self.save_dir, "images", "val"))
        ret["train_lbl_dir"] = create_dir(os.path.join(self.save_dir, "labels", "train"))
        ret["val_lbl_dir"] = create_dir(os.path.join(self.save_dir, "labels", "val"))
        return ret

    def __get_image_name_base_json(self, json_file):
        # 根据json文件找图片
        IMAGE_FORMAT = ["bmp", "jpeg", "png", "jpg", ]
        for suffix in IMAGE_FORMAT:
            target_file = json_file.replace("json", suffix)
            target_file_pth = os.path.join(self.src_dir, target_file)
            if os.path.isfile(target_file_pth):
                return target_file
        return None

    def convert_and_split(self, train_percent: float):
        # labelme 标注格式转为yolo标注格式
        # 对有标注的样本 切分 train val 保存
        # 并生成 数据集配置文件

        # 创建文件夹结构
        dir_struct = self.__create_dataset_dir()

        # 获取标注文件
        json_files = [f for f in os.listdir(self.src_dir) if f.endswith(".json")]
        assert len(json_files) > 10, "Error, Need to Label More Data..."
        random.shuffle(json_files)
        total_file_num = len(json_files)
        train_file_num = int(total_file_num * train_percent)
        print(
            f"Total Data Num: {total_file_num}, Train Data Num: {train_file_num}, Val Data Num: {total_file_num - train_file_num}")

        # 随机切分训练集 验证集
        train_json_files = json_files[:train_file_num]
        for json_file in train_json_files:
            image_pth = self.__get_image_name_base_json(json_file)
            # 迁移图片
            copy_files(self.src_dir, dir_struct["train_img_dir"], [image_pth, ])
            # 生成标注文件
            lbl_txt_pth = os.path.join(dir_struct["train_lbl_dir"], json_file.replace(".json", ".txt"))
            self.__parse_json2yolo_txt(os.path.join(self.src_dir, image_pth), os.path.join(self.src_dir, json_file),
                                       lbl_txt_pth)

        val_json_files = json_files[train_file_num:]
        for json_file in val_json_files:
            image_pth = self.__get_image_name_base_json(json_file)
            # 迁移图片
            copy_files(self.src_dir, dir_struct["val_img_dir"], [image_pth, ])
            # 生成标注文件
            lbl_txt_pth = os.path.join(dir_struct["val_lbl_dir"], json_file.replace(".json", ".txt"))
            self.__parse_json2yolo_txt(os.path.join(self.src_dir, image_pth), os.path.join(self.src_dir, json_file),
                                       lbl_txt_pth)

        # 生成数据集配置文件
        timestamp = get_timestamp()
        dataset_config_pth = os.path.join(self.save_dir, f"dataset_{timestamp}.yaml")
        with open(dataset_config_pth, "w") as fp:
            fp.write(f"path: {os.path.abspath(self.save_dir)}\n")
            fp.write(f"train: images/train\n")
            fp.write(f"val: images/val\n")
            fp.write(f"names:\n")
            for i, cls in enumerate(self.CLASSES):
                fp.write(f"  {i}: {cls}")

        print(f"DataSet Split Complete. {os.path.abspath(dataset_config_pth)}")
        return


if __name__ == "__main__":
    # TODO: 测试 数据集格式  导出训练集测试集  在数据集路径下生成配置文件
    dataset = UltrDetDataSet(r"E:\DataSets\dents_det\org_D1\gold_scf\cutPatches640\NG",
                              r"/DLTmp",
                              r"D:\share_dir\DLTrainer\labels.txt",
                              r"D:\envs\ultr_py11\Scripts\labelme.exe")
    # dataset.label_data()
    # dataset.check()
    dataset.convert_and_split(0.8)

    print("Done")
