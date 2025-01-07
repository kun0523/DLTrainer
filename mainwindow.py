# This Python file uses the following encoding: utf-8
import subprocess
import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon, QColor, QPalette

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ModelPy.model import YoloModel
from Controls import MySignals, ModelTrainControl, ModelEvaluateControl, \
    ModelInferenceControl, ModelCheckControl, ModelShowTrainInfoControl, ModelExportControl, \
    ClasDataLabelControl, ClasDataSplitControl, DetDataLabelControl, DetDataSplitControl

from utils.utils import get_timenow

TASK_TYPE = 0 # 0 img_clas  1 obj_det  2 obj_seg

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.DataLabelControl = None
        self.DataSplitControl = None
        self.check_task_type()

        # 判断任务类型
        self.ui.rb_clas_prj.clicked.connect(self.check_task_type)
        self.ui.rb_det_prj.clicked.connect(self.check_task_type)
        self.ui.rb_seg_prj.clicked.connect(self.check_task_type)

        # 标识运行状态
        self.status_label = QLabel("~空闲~")
        self.status_label.setStyleSheet("background-color: darkseagreen; color: white;")
        self.status_label.setMargin(5)
        self.ui.statusbar.addWidget(self.status_label)

        # 标识软件版本
        version_label = QLabel("Version 0.8")
        self.ui.statusbar.addPermanentWidget(version_label)

        # 用于测试软件是否卡顿
        clock_label = QLabel("xx:xx:xx")
        clock_label.setMargin(5)
        self.ui.statusbar.addWidget(clock_label)
        self.workdir = os.path.join(os.getcwd(), "WorkDir")
        if not os.path.isdir(self.workdir):
            os.makedirs(self.workdir)

        # 目标检测 --- 数据处理页面
        self.ui.btn_label.clicked.connect(self.on_btn_label_clicked)
        self.ui.btn_split.clicked.connect(self.on_btn_split_clicked)

        # 目标检测 --- 模型训练页面
        self.train_config_pth = None
        self.ui.btn_check_env.clicked.connect(self.on_btn_check_env_clicked)
        self.ui.btn_save_cfg.clicked.connect(self.on_btn_save_cfg_clicked)
        self.ui.btn_open_cfg.clicked.connect(self.on_btn_open_cfg_clicked)
        self.ui.btn_train.clicked.connect(self.on_btn_train_clicked)
        self.ui.btn_show_train_info.clicked.connect(self.on_btn_show_train_info_clicked)
        self.ui.le_train_tool_pth.textChanged.connect(
            lambda: self.ui.le_test_tool_pth.setText(self.ui.le_train_tool_pth.text()))

        # 目标检测 --- 模型推理与导出页面
        self.ui.btn_inference.clicked.connect(self.on_btn_inference_clicked)
        self.ui.btn_export.clicked.connect(self.on_btn_export_clicked)
        self.ui.btn_open_model_dir.clicked.connect(self.on_btn_open_model_dir_clicked)
        self.ui.btn_check_result.clicked.connect(self.on_btn_open_model_dir_clicked)

        # 记录log相关信号
        self.my_signal = MySignals()
        self.my_signal.my_btn_clicked_signal.connect(self.write_system_log)

        # 界面刷新
        def update_time():
            clock_label.setText(get_timenow())
            if self.ui.pte_log_info.toPlainText().count("\n") > 1000:
                self.ui.pte_log_info.clear()
            return

        timer = QTimer(self)
        timer.setInterval(100)
        timer.timeout.connect(update_time)
        timer.start()

        # 用于提示报错信息
        self.msg_box = QMessageBox(self)
        self.msg_box.setWindowTitle("ErrorMessage")
        self.msg_box.setIcon(QMessageBox.Icon.Critical)
        return

    def check_task_type(self):
        global TASK_TYPE
        if self.ui.rb_clas_prj.isChecked():
            TASK_TYPE = 0
            self.DataLabelControl = ClasDataLabelControl
            self.DataSplitControl = ClasDataSplitControl
            self.ui.lb_dataset.setText("数据集路径:")
            self.ui.le_labelme_pth.setDisabled(True)
            self.write_system_log("INFO", "Use Classify Task Mode")
        elif self.ui.rb_det_prj.isChecked():
            TASK_TYPE = 1
            self.DataLabelControl = DetDataLabelControl
            self.DataSplitControl = DetDataSplitControl
            self.ui.le_labelme_pth.setDisabled(False)
            self.ui.lb_dataset.setText("数据集配置文件:")
            self.write_system_log("INFO", "Use Detection Task Mode")
        elif self.ui.rb_seg_prj.isChecked():
            TASK_TYPE = 2
            self.ui.tabWidget_2.setPalette(QPalette(QColor(0,0,255)))
            self.ui.le_labelme_pth.setDisabled(False)
            self.write_system_log("INFO", "Use Segmentation Task Mode")
        else:
            self.write_system_log("Error", "Use Wrong Task Mode")
            raise RuntimeError("Error, Wrong TASK TYPE")

    def write_system_log(self, level, content):
        self.ui.pte_log_info.appendPlainText(f"[{get_timenow()}] [{level}] {content}")
        return

    def write_model_log(self, message):
        self.ui.pte_log_info.appendPlainText(message)
        return

    def status_label_busy(self):
        self.status_label.setText("HardWorking...")
        self.status_label.setStyleSheet("background-color: red; color: white;")
        return

    def status_label_idle(self):
        self.status_label.setText("~空闲~")
        self.status_label.setStyleSheet("background-color: darkseagreen; color: white;")
        return

    @staticmethod
    def button_status_invert(button_obj: QPushButton):
        if button_obj.isEnabled():
            button_obj.setDisabled(True)
        else:
            button_obj.setDisabled(False)

    def on_btn_label_clicked(self):
        self.my_signal.my_btn_clicked_signal.emit("INFO", "DataSet Labelling Start...")
        self.button_status_invert(self.ui.btn_label)
        self.button_status_invert(self.ui.btn_split)

        tool_path = self.ui.le_labelme_pth.text().strip()
        org_img_dir = self.ui.le_orgimg_pth.text().strip()
        obj_classes_str = self.ui.le_clas_names.text().strip()
        obj_classes = tuple(obj_classes_str.split(","))

        try:
            global worker
            worker = self.DataLabelControl(tool_path, org_img_dir, obj_classes)
            worker.finished.connect(lambda: self.button_status_invert(self.ui.btn_label))
            worker.finished.connect(lambda: self.button_status_invert(self.ui.btn_split))
            worker.finished.connect(lambda: self.write_system_log("INFO", "DataSet Label Complete."))
            worker.start()

            if worker.wait() and worker.exit_code==1:
                raise worker.exception

        except Exception as ex:
            self.msg_box.setText(str(ex))
            self.msg_box.exec()
        return

    def on_btn_split_clicked(self):
        self.my_signal.my_btn_clicked_signal.emit("INFO", "DataSet Splitting Start...")

        self.button_status_invert(self.ui.btn_label)
        self.button_status_invert(self.ui.btn_split)

        tool_path = self.ui.le_labelme_pth.text().strip()
        org_img_dir = self.ui.le_orgimg_pth.text().strip()
        obj_classes_str = self.ui.le_clas_names.text().strip()
        obj_classes = tuple(obj_classes_str.split(","))
        train_data_percent = float(self.ui.dsb_train_data_percent.text())

        try:
            assert train_data_percent > 0.0, f"Error, Set train precent:{train_data_percent} too small"

            global worker
            worker = self.DataSplitControl(tool_path, org_img_dir, obj_classes, train_data_percent)
            worker.finished.connect(lambda: self.button_status_invert(self.ui.btn_label))
            worker.finished.connect(lambda: self.button_status_invert(self.ui.btn_split))
            worker.finished.connect(lambda: self.write_system_log("INFO", "DataSet Split Complete."))
            worker.start()

            if worker.wait() and worker.exit_code==1:
                raise worker.exception

        except Exception as ex:
            self.msg_box.setText(str(ex))
            self.msg_box.exec()
        return

    def on_btn_check_env_clicked(self):
        self.my_signal.my_btn_clicked_signal.emit("INFO", "Env Check Start...")
        self.button_status_invert(self.ui.btn_check_env)

        tool_path = self.ui.le_train_tool_pth.text().strip()
        pretrained_model_dir = self.ui.le_pretrained_dir.text().strip()
        temp_cfg_path = self.ui.le_temp_cfg_pth.text().strip()
        self.ui.cb_pretrained_model_file.clear()
        try:
            pt_file_lst = [(f, os.path.getsize(os.path.join(pretrained_model_dir, f))) for f in
                           os.listdir(pretrained_model_dir) if f.endswith(".pt")]
            pt_file_lst = sorted(pt_file_lst, key=lambda t: t[1])
            self.ui.cb_pretrained_model_file.addItems([i[0] for i in pt_file_lst])

            global model_worker
            model_worker = ModelCheckControl(tool_path, pretrained_model_dir, temp_cfg_path)
            model_worker.finished.connect(lambda: self.button_status_invert(self.ui.btn_check_env))
            model_worker.model.my_process_signal.send_message_signal.connect(self.write_model_log)
            model_worker.start()
        except Exception as ex:
            self.msg_box.setText(str(ex))
            self.msg_box.exec()

            self.button_status_invert(self.ui.btn_check_env)
        return

    def on_btn_save_cfg_clicked(self):
        self.my_signal.my_btn_clicked_signal.emit("INFO", "Save Train Config Info...")

        try:
            tool_path = self.ui.le_train_tool_pth.text().strip()
            temp_cfg_path = self.ui.le_temp_cfg_pth.text().strip()
            dataset_cfg_pth = self.ui.le_dataset_cfg_pth.text().strip()
            pretrained_model_dir = self.ui.le_pretrained_dir.text().strip()
            pretrained_model_name = self.ui.cb_pretrained_model_file.currentText().strip()
            learning_rate = float(self.ui.le_learning_rate.text().strip())
            imgsz = int(self.ui.le_imgsz.text().strip())
            epochs = int(self.ui.sb_epochs.text().strip())
            batchsz = int(self.ui.sb_batch_size.text().strip())

            assert os.path.isfile(temp_cfg_path), f"Error, template config file:[{temp_cfg_path}] Not Found"
            assert (os.path.isdir(dataset_cfg_pth) or os.path.isfile(dataset_cfg_pth)), f"Error, dataset: [{dataset_cfg_pth}] Not Found"
            used_pretrained_model_pth = os.path.join(pretrained_model_dir, pretrained_model_name)
            assert os.path.isfile(
                used_pretrained_model_pth), f"Error, pretrained model file:[{used_pretrained_model_pth}] Not Found"

            model = YoloModel(tool_path, pretrained_model_dir, temp_cfg_path, self.workdir)
            if TASK_TYPE == 0:
                task_mode = "classify"
            elif TASK_TYPE == 1:
                task_mode = "detect"
            elif TASK_TYPE == 2:
                task_mode = "segment"
            else:
                task_mode = ""
            self.train_config_pth = model.make_train_cfg(task_mode, dataset_cfg_pth, used_pretrained_model_pth, epochs,
                                                         batchsz, imgsz, learning_rate)
            if os.path.isfile(self.train_config_pth):
                self.my_signal.my_btn_clicked_signal.emit("INFO",
                                                          f"Train Config: [{self.train_config_pth}] Save Success")
            else:
                self.my_signal.my_btn_clicked_signal.emit("Warning", "Failed to Save Config File...")
        except Exception as ex:
            self.msg_box.setText(str(ex))
            self.msg_box.exec()

        return

    def on_btn_open_cfg_clicked(self):
        if self.train_config_pth is None:
            self.msg_box.setText("Need to Save Config Info First!")
            self.msg_box.exec()
            return

        subprocess.Popen(f"notepad {self.train_config_pth}")
        return

    def on_btn_train_clicked(self):
        if self.train_config_pth is None:
            self.msg_box.setText("Need to Save Config Info First!")
            self.msg_box.exec()
            return

        self.my_signal.my_btn_clicked_signal.emit("INFO", "Start Train Process...")
        self.button_status_invert(self.ui.btn_train)
        self.button_status_invert(self.ui.btn_stop_train)
        try:
            tool_path = self.ui.le_train_tool_pth.text().strip()
            pretrained_model_dir = self.ui.le_pretrained_dir.text().strip()
            temp_cfg_path = self.ui.le_temp_cfg_pth.text().strip()

            global train_worker
            train_worker = ModelTrainControl(tool_path, pretrained_model_dir, temp_cfg_path, self.train_config_pth)
            train_worker.started.connect(self.status_label_busy)
            train_worker.finished.connect(self.status_label_idle)
            train_worker.finished.connect(lambda: self.button_status_invert(self.ui.btn_train))
            train_worker.finished.connect(lambda: self.button_status_invert(self.ui.btn_stop_train))
            train_worker.model.my_process_signal.send_message_signal.connect(self.write_model_log)
            self.ui.btn_stop_train.clicked.connect(train_worker.shutdown)
            train_worker.start()
        except Exception as ex:
            self.msg_box.setText(str(ex))
            self.msg_box.exec()

            self.button_status_invert(self.ui.btn_train)
            self.button_status_invert(self.ui.btn_stop_train)
        return

    def on_btn_show_train_info_clicked(self):

        self.button_status_invert(self.ui.btn_show_train_info)
        self.button_status_invert(self.ui.btn_stop_show_train)
        try:
            tool_path = self.ui.le_train_tool_pth.text().strip()
            temp_cfg_path = self.ui.le_temp_cfg_pth.text().strip()
            pretrained_model_dir = self.ui.le_pretrained_dir.text().strip()
            global show_worker
            show_worker = ModelShowTrainInfoControl(tool_path, pretrained_model_dir, temp_cfg_path, 8899)
            show_worker.finished.connect(lambda: self.button_status_invert(self.ui.btn_show_train_info))
            show_worker.finished.connect(lambda: self.button_status_invert(self.ui.btn_stop_show_train))
            show_worker.model.my_process_signal.send_message_signal.connect(self.write_model_log)
            self.ui.btn_stop_show_train.clicked.connect(show_worker.shutdown)
            show_worker.start()
        except Exception as ex:
            self.msg_box.setText(str(ex))
            self.msg_box.exec()

            self.button_status_invert(self.ui.btn_show_train_info)
            self.button_status_invert(self.ui.btn_stop_show_train)
        return

    def on_btn_inference_clicked(self):
        self.my_signal.my_btn_clicked_signal.emit("INFO", "Start Test Process...")

        self.button_status_invert(self.ui.btn_inference)
        try:
            test_tool_path = self.ui.le_test_tool_pth.text().strip()
            assert os.path.isfile(test_tool_path), f"Error, Test Tool:{test_tool_path} Not Found!"
            used_model_path = self.ui.le_used_model_path.text().strip()
            assert os.path.isfile(used_model_path), f"Error, Model File:{used_model_path} Not Found!"
            test_image_path = self.ui.le_test_image_path.text().strip()
            assert os.path.isdir(test_image_path) or os.path.isfile(
                test_image_path), f"Error, Test Image File:{test_image_path} Not Found!"

            global inference_worker
            inference_worker = ModelInferenceControl(test_tool_path, "", "", used_model_path, test_image_path)
            inference_worker.started.connect(self.status_label_busy)
            inference_worker.finished.connect(self.status_label_idle)
            inference_worker.finished.connect(lambda: self.button_status_invert(self.ui.btn_inference))
            inference_worker.model.my_process_signal.send_message_signal.connect(self.write_model_log)
            inference_worker.start()
        except Exception as ex:
            self.msg_box.setText(str(ex))
            self.msg_box.exec()
            self.button_status_invert(self.ui.btn_inference)
        return

    def on_btn_export_clicked(self):
        self.button_status_invert(self.ui.btn_export)
        try:
            test_tool_path = self.ui.le_test_tool_pth.text().strip()
            assert os.path.isfile(test_tool_path), f"Error, Test Tool:{test_tool_path} Not Found!"
            used_model_path = self.ui.le_used_model_path.text().strip()
            assert os.path.isfile(used_model_path), f"Error, Model File:{used_model_path} Not Found!"

            global export_worker
            export_worker = ModelExportControl(test_tool_path, "", "", used_model_path)
            export_worker.finished.connect(lambda: self.button_status_invert(self.ui.btn_export))
            export_worker.model.my_process_signal.send_message_signal.connect(self.write_model_log)
            export_worker.start()
        except Exception as ex:
            self.msg_box.setText(str(ex))
            self.msg_box.exec()
            self.button_status_invert(self.ui.btn_export)
        return

    def on_btn_open_model_dir_clicked(self):
        try:
            used_model_path = self.ui.le_used_model_path.text().strip()
            assert os.path.isfile(used_model_path), f"Error, Model File:{used_model_path} Not Found!"
            model_dir = os.path.split(used_model_path)[0]
            subprocess.Popen(f"start explorer {model_dir}", shell=True)
        except Exception as ex:
            self.msg_box.setText(str(ex))
            self.msg_box.exec()
        return


# Done： 完成整体流程  数据处理+模型训练+模型推理
# TODO: 在不同电脑上做测试。。。
# TODO: 当同时发生多个任务时，某一个任务进行完成就会把状态改成空闲。。待改正
# TODO: 当一个任务进行过程中，切换到另一个任务怎么办？
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
