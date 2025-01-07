# This Python file uses the following encoding: utf-8
# 模型训练  模型推理
import os
import shutil
import yaml
from abc import ABC, abstractmethod
import subprocess
from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW

from PySide6.QtCore import Signal, QObject

from utils.utils import get_timestamp


class MySignals(QObject):
    my_btn_clicked_signal = Signal(str, str)
    send_message_signal = Signal(str)


# 向界面开放的接口
class Model(ABC):

    @abstractmethod
    def train(self, train_cfg_pth):
        pass

    @abstractmethod
    def evaluate(self,
                 dataset_config_pth: str,  # 数据集配置文件
                 model_pth: str,
                 ):
        pass

    @abstractmethod
    def inference(self,
                  model_pth: str,
                  test_image_pth: str,
                  ):
        pass

    @abstractmethod
    def export(self,
               model_pth,
               ):
        pass


class YoloModel(Model):
    '''
    基于Ultralytics库
    '''

    def __init__(self,
                 tool_pth,  # yolo.exe 路径
                 pretrained_model_dir,  # 预训练模型文件夹
                 template_cfg_pth,  # 配置模板文件路径
                 work_dir,  # 训练工程路径
                 ):
        # 新建项目时，对应一个YoloModel
        assert os.path.isfile(tool_pth), "Error, Train tools not exists!!"
        self.tool_pth = tool_pth
        self.pretrained_model_dir = pretrained_model_dir
        self.template_cfg_pth = template_cfg_pth
        self.work_dir = os.path.abspath(work_dir)

        self.config_dict = {}
        self.curr_proj_dir = None
        self.use_config_pth = None
        self.process = None
        self.my_process_signal = MySignals()
        return

    def make_train_cfg(self,
                       mode: str,  # classify  detect  segment
                       dataset_config_pth: str,  # 数据集配置文件
                       pretrained_model_file_name: str,
                       epochs: int = 100,
                       batch: int = 8,
                       imgsz: int = 224,
                       learning_rate: float = 0.01,
                       ):
        with open(self.template_cfg_pth, "r") as fp:
            cfg = yaml.safe_load(fp)

        self.config_dict.update(cfg)
        self.config_dict["task"] = mode
        self.config_dict["mode"] = "train"
        self.config_dict["model"] = os.path.join(self.pretrained_model_dir, pretrained_model_file_name)
        self.config_dict["data"] = dataset_config_pth
        self.config_dict["epochs"] = epochs
        self.config_dict["batch"] = batch
        self.config_dict["imgsz"] = imgsz
        self.config_dict["lr0"] = learning_rate
        self.config_dict["device"] = None

        timestamp = get_timestamp()
        self.curr_proj_dir = os.path.join(self.work_dir, f"Proj_{timestamp}")
        if os.path.isdir(self.curr_proj_dir):
            shutil.rmtree(self.curr_proj_dir)
        os.makedirs(self.curr_proj_dir)
        self.config_dict["project"] = self.curr_proj_dir

        tmp_config_pth = os.path.join(self.curr_proj_dir, "tmp_config.yaml")
        with open(tmp_config_pth, "w") as fp:
            yaml.safe_dump(self.config_dict, fp)
        return tmp_config_pth

    def __run_cmd(self, command_):
        startup_info = STARTUPINFO()
        startup_info.dwFlags |= STARTF_USESHOWWINDOW
        startup_info.wShowWindow = 0
        self.process = subprocess.Popen(command_, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, startupinfo=startup_info)
        while self.process.poll() is None:
            line = self.process.stdout.readline()
            if type(line) == bytes:
                try:
                    line = line.decode(encoding="utf-8", errors="ignore")
                except Exception as e:
                    print(e)
            line = line.strip()
            if line:
                # print(line)
                self.my_process_signal.send_message_signal.emit(line)
        if self.process.returncode == 0:
            print("success")
        else:
            print("failed")
        return

    def shutdown(self):
        if self.process is not None:
            self.process.kill()
        return

    def __copy_base_model(self):
        src_pth = os.path.join(self.pretrained_model_dir, "yolo11n.pt")
        dst_pth = os.path.join("./", "yolo11n.pt")
        shutil.copy2(src_pth, dst_pth)
        return

    def check_env(self):
        command = f"{self.tool_pth} check"
        self.__run_cmd(command)
        return

    def train(self, train_cfg_pth):
        # 每次训练对应一个config
        self.__copy_base_model()
        # 复制一个 基础模型文件在工作目录下
        command = f"{self.tool_pth} cfg={train_cfg_pth}"
        self.__run_cmd(command)
        return command

    def evaluate(self,
                 dataset_config_pth: str,  # 数据集配置文件
                 model_pth: str,
                 ):

        assert (os.path.isfile(dataset_config_pth) or os.path.isdir(
            dataset_config_pth)), "Error, Dataset config yaml Not Found!"
        if self.curr_proj_dir is None:
            self.curr_proj_dir = os.path.split(model_pth)[0]

        command = f"{self.tool_pth} val project={self.curr_proj_dir} model={model_pth} data={dataset_config_pth}"
        self.__run_cmd(command)
        return command

    def inference(self,
                  model_pth: str,
                  test_image_pth: str,
                  ):
        assert os.path.isfile(test_image_pth), "Error, Test Image Not Found!"
        if self.curr_proj_dir is None:
            self.curr_proj_dir = os.path.split(model_pth)[0]

        command = f"{self.tool_pth} predict project={self.curr_proj_dir} model={model_pth} source={test_image_pth}"
        self.__run_cmd(command)  # 自己发起进程
        return command  # 交给调用方发起进程

    def export(self,
               model_pth,
               ):
        command = f"{self.tool_pth} export model={model_pth} format=onnx opset=13"
        self.__run_cmd(command)
        output_onnx_pth = model_pth.replace(".pt", ".onnx")
        if os.path.isfile(output_onnx_pth):
            print(f"Export Success, Model Save to [{output_onnx_pth}]")
            return output_onnx_pth
        else:
            print(f"Export Failed")
            return None

    def show_training_curve(self, port: int):
        tensorboard_pth = self.tool_pth.replace("yolo.exe", "tensorboard.exe")
        assert os.path.isfile(tensorboard_pth), "Error, Tensorboard is Not Found!!"
        command = f"{tensorboard_pth} --logdir={self.work_dir} --port={port}"
        self.__run_cmd(command)
        return command


class PaddleModel:
    '''
    基于Paddle库
    '''

    def __init__(self):
        return


def run_ultra_clas_process():
    model = YoloModel(r"D:\envs\ultr_py11\Scripts\yolo.exe",
                      r"E:\Pretrained_models\YOLOv11-cls",
                      r"D:\share_dir\DLTrainer\default_configs\ultral_config_template.yaml",
                      r".\DLTmp",
                      )

    config_pth = model.make_train_cfg("classify",
                                      r"D:\share_dir\DLTrainer\DataSetPy\DLTmp\dataset_20250106101803",
                                      "yolo11n-cls.pt"
                                      )
    model.train(config_pth)

    # model.evaluate(r"D:\share_dir\DLTrainer\DataSetPy\DLTmp\dataset_20250106101803",
    #                r"D:\share_dir\DLTrainer\ModelPy\DLTmp\Proj_20250106124431\train\weights\best.pt",
    #                )

    # model.inference(r"D:\share_dir\DLTrainer\ModelPy\DLTmp\Proj_20250106124431\train\weights\best.pt",
    #                 r"D:\share_dir\DLTrainer\ModelPy\DLTmp\Proj_20250106124431\train\weights\2024-01-04_test.jpg"
    #                 )

    # model.export(r"D:\share_dir\DLTrainer\ModelPy\DLTmp\Proj_20250106124431\train\weights\best.pt", )

    # model.show_training_curve()

    # model.check_env()

    return


def run_ultra_det_process():
    model = YoloModel(r"D:\envs\ultr_py11\Scripts\yolo.exe",
                      r"E:\Pretrained_models\YOLOv11",
                      r"D:\share_dir\DLTrainer\default_configs\ultral_config_template.yaml",
                      r"../DLTmp",
                      )

    # config_pth = model.make_train_cfg("detect",
    #                                   r"D:\share_dir\DLTrainer\WorkDir\dataset_20241230171728\dataset_20241230171730.yaml",
    #                                   "yolo11n.pt"
    #                                   )

    model.evaluate(r"D:\share_dir\DLTrainer\WorkDir\dataset_20241230171728\dataset_20241230171730.yaml",
                   r"D:\share_dir\DLTrainer\WorkDir\Proj_20241230171627\train\weights\best.pt",
                   )

    model.inference(r"D:\share_dir\DLTrainer\WorkDir\Proj_20241230171627\train\weights\best.pt",
                    r"D:\share_dir\DLTrainer\WorkDir\dataset_20241230171728\images\train\5_5428.jpg"
                    )

    model.export(r"D:\share_dir\DLTrainer\WorkDir\Proj_20241230171627\train\weights\best.pt", )

    # model.show_training_curve()

    # model.check_env()
    return


if __name__ == "__main__":
    # TODO: 测试模型训练  导出  推理

    run_ultra_clas_process()

    # run_ultra_det_process()
