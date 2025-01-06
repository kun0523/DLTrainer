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
        self.IMAGE_FORMAT = (".jpeg", ".jpg", ".bmp", ".png")
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
    def convert_and_split(self, train_percent: float):
        pass


class UltrClasDataSet(DataSet):
    def __init__(self, src_dir: str, save_dir: str, label_txt_pth: str):
        """
        如果 src_dir 下全是文件夹，则认为已经标注完成，直接复制到目标路径下
        如果 src_dir 下全是图片，则认为没有标注，创建文件目录结构，由用户将图片归类
        """
        super().__init__(src_dir, save_dir, label_txt_pth)
        return

    def __is_image(self, tmp_path: str):
        # 判断指定的文件是否是图片
        if not os.path.isfile(tmp_path):
            return False

        for ends in self.IMAGE_FORMAT:
            if tmp_path.lower().endswith(ends):
                return True

        return False

    def __check_dataset(self, check_path):
        """
        要求：
        1. check_path 是一个有效文件夹；
        2. check_path 下只有文件夹；
        3. 文件夹名称要与 self.CLASSES 内的类别名称对应
        4. check_path 下的文件夹，每个文件夹中只包含图片
        """
        if not os.path.isdir(check_path):
            return 1, f"Not a Valid Directory: {check_path}"

        path_list = os.listdir(check_path)
        for p in path_list:
            tmp_dir = os.path.join(check_path, p)
            if not os.path.isdir(tmp_dir):
                return 1, f"Not a Valid Directory: {tmp_dir}"

        if len(self.CLASSES) != len(path_list):
            return 1, f"CLASSES Num:{len(self.CLASSES)} != Dir Num:{len(path_list)}"

        sorted_path_list = sorted(path_list)
        sorted_classes = sorted(self.CLASSES)
        for clas_name, dir_name in zip(sorted_classes, sorted_path_list):
            if clas_name != dir_name:
                return 1, f"Dir Name:{dir_name} != Class Name:{clas_name}"

        for dirpath, dirname, files in os.walk(check_path):
            for file in files:
                image_path = os.path.join(dirpath, file)
                if not self.__is_image(image_path):
                    return 1, f"Not a Valid Image: {image_path}"

        return 0, "DataSet Structure Correct"

    def __create_dataset_dir(self):
        # dataset_root/(train|val)/(clas1|clas2|clas3)
        ret = dict()
        ret["train_img_dir"] = create_dir(os.path.join(self.save_dir, "train"))
        ret["val_img_dir"] = create_dir(os.path.join(self.save_dir, "val"))
        for k, d in ret.items():
            for clas in self.CLASSES:
                create_dir(os.path.join(d, clas))
        return ret

    def label_data(self):
        status, message = self.__check_dataset(self.src_dir)
        assert status == 0, message
        return

    def convert_and_split(self, train_percent: float):
        # 图片区分文件夹保存
        # 创建文件夹结构
        save_dir_structure = self.__create_dataset_dir()

        # 按比例切分图片数据
        for clas in self.CLASSES:
            image_dir = os.path.join(self.src_dir, clas)
            train_save_dir = os.path.join(save_dir_structure["train_img_dir"], clas)
            val_save_dir = os.path.join(save_dir_structure["val_img_dir"], clas)

            image_lst = os.listdir(image_dir)
            random.shuffle(image_lst)
            train_image_num = int(len(image_lst) * train_percent)
            train_image_lst = image_lst[:train_image_num]
            val_image_lst = image_lst[train_image_num:]
            copy_files(image_dir, train_save_dir, train_image_lst)
            copy_files(image_dir, val_save_dir, val_image_lst)
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


# 分类图片
# TODO: 分类数据集创建与管理
# TODO: 目标检查数据集，基于标注框切割图片

if __name__ == "__main__":
    # TODO: 测试分类数据集
    # 传入数据集路径
    dataset = UltrClasDataSet(r"E:\DataSets\vacuum_package\tmp_dataset",
                              r"./DLTmp",
                              r"E:\DataSets\vacuum_package\labels.txt", )

    # TODO: 测试 数据集格式  导出训练集测试集  在数据集路径下生成配置文件
    # dataset = UltrDetDataSet(r"E:\DataSets\dents_det\org_D1\gold_scf\cutPatches640\NG",
    #                          r"/DLTmp",
    #                          r"D:\share_dir\DLTrainer\labels.txt",
    #                          r"D:\envs\ultr_py11\Scripts\labelme.exe")

    dataset.label_data()
    dataset.convert_and_split(0.8)

    print("Done")
