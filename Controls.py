# This Python file uses the following encoding: utf-8
import os
from PySide6.QtCore import QObject, Signal, Slot, QThread, QProcess
from PySide6.QtWidgets import QPushButton

from DataSetPy.dataset import UltrDetDataSet, UltrClasDataSet
from ModelPy.model import YoloModel, MySignals


class DataSetControl(QThread):
    def __init__(self, label_tool_path: str, org_image_dir: str, obj_classes: tuple):
        super().__init__()
        self.label_tool_path = label_tool_path
        self.org_image_dir = org_image_dir
        self.split_save_dir = os.path.join(os.getcwd(), "WorkDir")
        self.label_txt_path = os.path.join(self.split_save_dir, "labels.txt")
        with open(self.label_txt_path, "w", encoding="utf8") as fp:
            for clas in obj_classes:
                fp.write(f"{clas.strip()}\n")
        self.dataset_obj = None

        self.exit_code = 0
        self.exception = None
        return


class ClasDataLabelControl(DataSetControl):
    def __init__(self, label_tool_path, org_image_dir, obj_classes):
        super().__init__(label_tool_path, org_image_dir, obj_classes)
        self.dataset_obj = UltrClasDataSet(self.org_image_dir, self.split_save_dir, self.label_txt_path)
        return

    def run(self):
        try:
            self.dataset_obj.label_data()
        except Exception as e:
            self.exit_code = 1
            self.exception = e
        return


class ClasDataSplitControl(DataSetControl):
    def __init__(self, label_tool_path, org_image_dir, obj_classes, train_percent: float):
        super().__init__(label_tool_path, org_image_dir, obj_classes)
        self.dataset_obj = UltrClasDataSet(self.org_image_dir, self.split_save_dir, self.label_txt_path)
        self.train_data_percent = train_percent

    def run(self):
        try:
            self.dataset_obj.convert_and_split(self.train_data_percent)
        except Exception as e:
            self.exit_code = 1
            self.exception = e
        return


class DetDataLabelControl(DataSetControl):
    def __init__(self, label_tool_path, org_image_dir, obj_classes):
        super().__init__(label_tool_path, org_image_dir, obj_classes)
        self.dataset_obj = UltrDetDataSet(self.org_image_dir, self.split_save_dir, self.label_txt_path,
                                          self.label_tool_path)
        return

    def run(self):
        try:
            self.dataset_obj.label_data()
        except Exception as e:
            self.exit_code = 1
            self.exception = e
        return


class DetDataSplitControl(DataSetControl):
    def __init__(self, label_tool_path, org_image_dir, obj_classes, train_percent: float):
        super().__init__(label_tool_path, org_image_dir, obj_classes)
        self.dataset_obj = UltrDetDataSet(self.org_image_dir, self.split_save_dir, self.label_txt_path,
                                          self.label_tool_path)
        self.train_data_percent = train_percent

    def run(self):
        try:
            self.dataset_obj.convert_and_split(self.train_data_percent)
        except Exception as e:
            self.exit_code = 1
            self.exception = e
        return


class ModelControl(QThread):
    def __init__(self, train_tool_path: str, pretrained_model_path: str, template_cfg_path: str):
        super().__init__()
        self.train_tool_path = train_tool_path
        self.pretrained_model_path = pretrained_model_path
        self.template_cfg_path = template_cfg_path
        self.work_dir = os.path.join(os.getcwd(), "WorkDir")
        self.model = YoloModel(self.train_tool_path, self.pretrained_model_path, self.template_cfg_path, self.work_dir)
        return


class ModelCheckControl(ModelControl):
    def __init__(self, train_tool_path, pretrained_model_path, template_cfg_path):
        super().__init__(train_tool_path, pretrained_model_path, template_cfg_path)
        return

    def run(self):
        self.model.check_env()
        return


class ModelTrainControl(ModelControl):
    def __init__(self, train_tool_path, pretrained_model_path, template_cfg_path, train_cfg_path):
        super().__init__(train_tool_path, pretrained_model_path, template_cfg_path)
        self.train_cfg_path = train_cfg_path
        return

    def run(self):
        self.model.train(self.train_cfg_path)
        # self.run_task_by_process(command)
        return

    def shutdown(self):
        self.model.shutdown()
        return


class ModelShowTrainInfoControl(ModelControl):
    def __init__(self, train_tool_path, pretrained_model_path, template_cfg_path, server_port):
        super().__init__(train_tool_path, pretrained_model_path, template_cfg_path)
        self.server_port = server_port
        return

    def run(self):
        self.model.show_training_curve(self.server_port)
        return

    def shutdown(self):
        self.model.shutdown()
        return


class ModelEvaluateControl(ModelControl):
    def __init__(self, train_tool_path, pretrained_model_path, template_cfg_path, used_ptmodel_path: str,
                 dataset_cfg_path: str):
        super().__init__(train_tool_path, pretrained_model_path, template_cfg_path)
        self.used_ptmodel_path = used_ptmodel_path
        self.dataset_cfg_path = dataset_cfg_path
        return

    def run(self):
        self.model.evaluate(self.dataset_cfg_path, self.used_ptmodel_path)
        return


class ModelInferenceControl(ModelControl):
    def __init__(self, train_tool_path, pretrained_model_path, template_cfg_path, used_ptmodel_path: str,
                 test_image_path: str):
        super().__init__(train_tool_path, pretrained_model_path, template_cfg_path)
        self.used_ptmodel_path = used_ptmodel_path
        self.test_image_path = test_image_path
        return

    def run(self):
        self.model.inference(self.used_ptmodel_path, self.test_image_path)
        return


class ModelExportControl(ModelControl):
    def __init__(self, train_tool_path, pretrained_model_path, template_cfg_path, used_ptmodel_path: str):
        super().__init__(train_tool_path, pretrained_model_path, template_cfg_path)
        self.used_ptmodel_path = used_ptmodel_path
        return

    def run(self):
        self.model.export(self.used_ptmodel_path)
        return

# if __name__ == "__main__":
#     pass
