# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1057, 584)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_8 = QWidget(self.centralwidget)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_4 = QGroupBox(self.widget_8)
        self.groupBox_4.setObjectName(u"groupBox_4")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 127))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush6 = QBrush(QColor(127, 127, 127, 127))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.groupBox_4.setPalette(palette)
        self.groupBox_4.setAutoFillBackground(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 8, 0, 4)
        self.widget_12 = QWidget(self.groupBox_4)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setAutoFillBackground(True)
        self.verticalLayout_5 = QVBoxLayout(self.widget_12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, -1, 0)
        self.rb_clas_prj = QRadioButton(self.widget_12)
        self.rb_clas_prj.setObjectName(u"rb_clas_prj")
        self.rb_clas_prj.setChecked(False)

        self.verticalLayout_5.addWidget(self.rb_clas_prj)

        self.rb_det_prj = QRadioButton(self.widget_12)
        self.rb_det_prj.setObjectName(u"rb_det_prj")
        self.rb_det_prj.setChecked(True)

        self.verticalLayout_5.addWidget(self.rb_det_prj)

        self.rb_seg_prj = QRadioButton(self.widget_12)
        self.rb_seg_prj.setObjectName(u"rb_seg_prj")
        self.rb_seg_prj.setEnabled(False)
        self.rb_seg_prj.setCheckable(True)

        self.verticalLayout_5.addWidget(self.rb_seg_prj)


        self.verticalLayout_11.addWidget(self.widget_12)


        self.horizontalLayout_7.addWidget(self.groupBox_4)

        self.tabWidget_2 = QTabWidget(self.widget_8)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setAutoFillBackground(False)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_6 = QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.le_orgimg_pth = QLineEdit(self.tab_3)
        self.le_orgimg_pth.setObjectName(u"le_orgimg_pth")

        self.gridLayout.addWidget(self.le_orgimg_pth, 2, 2, 1, 1)

        self.le_clas_names = QLineEdit(self.tab_3)
        self.le_clas_names.setObjectName(u"le_clas_names")

        self.gridLayout.addWidget(self.le_clas_names, 3, 2, 1, 1)

        self.le_labelme_pth = QLineEdit(self.tab_3)
        self.le_labelme_pth.setObjectName(u"le_labelme_pth")

        self.gridLayout.addWidget(self.le_labelme_pth, 1, 2, 1, 1)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.dsb_train_data_percent = QDoubleSpinBox(self.tab_3)
        self.dsb_train_data_percent.setObjectName(u"dsb_train_data_percent")
        self.dsb_train_data_percent.setDecimals(2)
        self.dsb_train_data_percent.setMaximum(1.000000000000000)
        self.dsb_train_data_percent.setSingleStep(0.100000000000000)
        self.dsb_train_data_percent.setValue(0.800000000000000)

        self.gridLayout.addWidget(self.dsb_train_data_percent, 4, 2, 1, 1)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 5, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.widget_2 = QWidget(self.tab_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_label = QPushButton(self.widget_2)
        self.btn_label.setObjectName(u"btn_label")

        self.horizontalLayout_6.addWidget(self.btn_label)

        self.btn_split = QPushButton(self.widget_2)
        self.btn_split.setObjectName(u"btn_split")

        self.horizontalLayout_6.addWidget(self.btn_split)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_8 = QVBoxLayout(self.tab_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_4 = QWidget(self.tab_4)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_2 = QGroupBox(self.widget_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 3, 0, 1, 1)

        self.le_temp_cfg_pth = QLineEdit(self.groupBox_2)
        self.le_temp_cfg_pth.setObjectName(u"le_temp_cfg_pth")

        self.gridLayout_4.addWidget(self.le_temp_cfg_pth, 3, 2, 1, 1)

        self.le_train_tool_pth = QLineEdit(self.groupBox_2)
        self.le_train_tool_pth.setObjectName(u"le_train_tool_pth")

        self.gridLayout_4.addWidget(self.le_train_tool_pth, 1, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.le_pretrained_dir = QLineEdit(self.groupBox_2)
        self.le_pretrained_dir.setObjectName(u"le_pretrained_dir")

        self.gridLayout_4.addWidget(self.le_pretrained_dir, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_4)

        self.widget_7 = QWidget(self.groupBox_2)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_10 = QVBoxLayout(self.widget_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btn_check_env = QPushButton(self.widget_7)
        self.btn_check_env.setObjectName(u"btn_check_env")

        self.verticalLayout_10.addWidget(self.btn_check_env)


        self.verticalLayout_2.addWidget(self.widget_7)


        self.horizontalLayout_8.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.widget_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 2, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.le_imgsz = QLineEdit(self.groupBox_3)
        self.le_imgsz.setObjectName(u"le_imgsz")

        self.gridLayout_2.addWidget(self.le_imgsz, 2, 3, 1, 1)

        self.cb_pretrained_model_file = QComboBox(self.groupBox_3)
        self.cb_pretrained_model_file.setObjectName(u"cb_pretrained_model_file")

        self.gridLayout_2.addWidget(self.cb_pretrained_model_file, 2, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 3, 2, 1, 1)

        self.le_dataset_cfg_pth = QLineEdit(self.groupBox_3)
        self.le_dataset_cfg_pth.setObjectName(u"le_dataset_cfg_pth")

        self.gridLayout_2.addWidget(self.le_dataset_cfg_pth, 1, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 1, 2, 1, 1)

        self.sb_epochs = QSpinBox(self.groupBox_3)
        self.sb_epochs.setObjectName(u"sb_epochs")
        self.sb_epochs.setMaximum(3000)
        self.sb_epochs.setValue(100)

        self.gridLayout_2.addWidget(self.sb_epochs, 3, 1, 1, 1)

        self.sb_batch_size = QSpinBox(self.groupBox_3)
        self.sb_batch_size.setObjectName(u"sb_batch_size")
        self.sb_batch_size.setMinimum(2)
        self.sb_batch_size.setMaximum(64)
        self.sb_batch_size.setValue(8)

        self.gridLayout_2.addWidget(self.sb_batch_size, 3, 3, 1, 1)

        self.le_learning_rate = QLineEdit(self.groupBox_3)
        self.le_learning_rate.setObjectName(u"le_learning_rate")

        self.gridLayout_2.addWidget(self.le_learning_rate, 1, 3, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.widget = QWidget(self.groupBox_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_save_cfg = QPushButton(self.widget)
        self.btn_save_cfg.setObjectName(u"btn_save_cfg")

        self.horizontalLayout_5.addWidget(self.btn_save_cfg)

        self.btn_open_cfg = QPushButton(self.widget)
        self.btn_open_cfg.setObjectName(u"btn_open_cfg")

        self.horizontalLayout_5.addWidget(self.btn_open_cfg)


        self.verticalLayout_4.addWidget(self.widget)


        self.horizontalLayout_8.addWidget(self.groupBox_3)


        self.verticalLayout_8.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.tab_4)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(33)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_train = QPushButton(self.widget_3)
        self.btn_train.setObjectName(u"btn_train")

        self.verticalLayout_3.addWidget(self.btn_train)

        self.btn_stop_train = QPushButton(self.widget_3)
        self.btn_stop_train.setObjectName(u"btn_stop_train")
        self.btn_stop_train.setEnabled(False)

        self.verticalLayout_3.addWidget(self.btn_stop_train)


        self.horizontalLayout_3.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_12 = QVBoxLayout(self.widget_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_show_train_info = QPushButton(self.widget_6)
        self.btn_show_train_info.setObjectName(u"btn_show_train_info")
        self.btn_show_train_info.setCheckable(False)

        self.verticalLayout_12.addWidget(self.btn_show_train_info)

        self.btn_stop_show_train = QPushButton(self.widget_6)
        self.btn_stop_show_train.setObjectName(u"btn_stop_show_train")
        self.btn_stop_show_train.setEnabled(False)
        self.btn_stop_show_train.setCheckable(False)

        self.verticalLayout_12.addWidget(self.btn_stop_show_train)


        self.horizontalLayout_3.addWidget(self.widget_6)


        self.verticalLayout_8.addWidget(self.widget_5)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_7 = QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.le_used_model_path = QLineEdit(self.tab_5)
        self.le_used_model_path.setObjectName(u"le_used_model_path")

        self.gridLayout_6.addWidget(self.le_used_model_path, 1, 2, 1, 1)

        self.label_25 = QLabel(self.tab_5)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_6.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_26 = QLabel(self.tab_5)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_6.addWidget(self.label_26, 1, 0, 1, 1)

        self.label_30 = QLabel(self.tab_5)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_6.addWidget(self.label_30, 0, 0, 1, 1)

        self.le_test_image_path = QLineEdit(self.tab_5)
        self.le_test_image_path.setObjectName(u"le_test_image_path")

        self.gridLayout_6.addWidget(self.le_test_image_path, 2, 2, 1, 1)

        self.le_test_tool_pth = QLineEdit(self.tab_5)
        self.le_test_tool_pth.setObjectName(u"le_test_tool_pth")

        self.gridLayout_6.addWidget(self.le_test_tool_pth, 0, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_6)

        self.widget_9 = QWidget(self.tab_5)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_9 = QVBoxLayout(self.widget_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_inference = QPushButton(self.widget_10)
        self.btn_inference.setObjectName(u"btn_inference")

        self.verticalLayout_9.addWidget(self.btn_inference)

        self.btn_check_result = QPushButton(self.widget_10)
        self.btn_check_result.setObjectName(u"btn_check_result")

        self.verticalLayout_9.addWidget(self.btn_check_result)


        self.horizontalLayout_4.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_16 = QVBoxLayout(self.widget_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.btn_export = QPushButton(self.widget_11)
        self.btn_export.setObjectName(u"btn_export")

        self.verticalLayout_16.addWidget(self.btn_export)

        self.btn_open_model_dir = QPushButton(self.widget_11)
        self.btn_open_model_dir.setObjectName(u"btn_open_model_dir")

        self.verticalLayout_16.addWidget(self.btn_open_model_dir)


        self.horizontalLayout_4.addWidget(self.widget_11)


        self.verticalLayout_7.addWidget(self.widget_9)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.horizontalLayout_7.addWidget(self.tabWidget_2)


        self.verticalLayout.addWidget(self.widget_8)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DLTrainer", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u7c7b\u578b\u9009\u62e9\uff1a", None))
        self.rb_clas_prj.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5206\u7c7b", None))
        self.rb_det_prj.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u68c0\u6d4b", None))
        self.rb_seg_prj.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5206\u5272", None))
        self.le_orgimg_pth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u56fe\u50cf\u7684\u6587\u4ef6\u5939\uff0c\u6807\u6ce8\u4ea7\u751f\u7684json\u6587\u4ef6\u4e5f\u4f1a\u4fdd\u5b58\u5728\u8be5\u8def\u5f84\u4e0b", None))
        self.le_clas_names.setPlaceholderText(QCoreApplication.translate("MainWindow", u"class1,class2,class3,... ...  \uff08\u6ce8\u610f\u4f7f\u7528\u82f1\u6587\u9017\u53f7\u5206\u9694\uff09", None))
        self.le_labelme_pth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"labelme.exe \u6587\u4ef6\u8def\u5f84", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u56fe\u50cf\u8def\u5f84\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u8c61\u7c7b\u522b\u540d\u79f0\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6807\u6ce8\u5de5\u5177\u8def\u5f84\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u96c6\u5360\u6bd4\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5c06\u5168\u90e8\u56fe\u7247\u5207\u5206\u4e3a\u8bad\u7ec3\u96c6\u548c\u6d4b\u8bd5\u96c6\uff0c\u8be5\u5360\u6bd4\u7528\u4e8e\u786e\u5b9a\u8bad\u7ec3\u56fe\u7247\u6570\u91cf\uff0c\u5982\u679c\u56fe\u7247\u5f88\u591a\u65f6\u53ef\u4ee5\u9002\u91cf\u964d\u4f4e\u8be5\u6bd4\u4f8b", None))
        self.btn_label.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u6807\u6ce8", None))
        self.btn_split.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5207\u5206", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5904\u7406", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u73af\u5883\u914d\u7f6e", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u6a21\u677f\u6587\u4ef6\uff1a", None))
        self.le_temp_cfg_pth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"config\u6a21\u677f\u6587\u4ef6\uff0c\u57fa\u4e8e\u6a21\u677f\u6587\u4ef6\u505a\u4fee\u6539", None))
        self.le_train_tool_pth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"yolo.exe \u6587\u4ef6\u8def\u5f84", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u9884\u8bad\u7ec3\u6a21\u578b\u6587\u4ef6\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u5de5\u5177\u8def\u5f84\uff1a", None))
        self.le_pretrained_dir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9884\u8bad\u7ec3\u6a21\u578b\u6587\u4ef6\u5939\u8def\u5f84\uff0c\u7528\u4e8e\u68c0\u7d22\u53ef\u4f7f\u7528\u7684\u6a21\u578b", None))
        self.btn_check_env.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c\u73af\u5883\u6d4b\u8bd5", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u8d85\u53c2\u6570\u914d\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8fed\u4ee3\u8f6e\u6b21\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u9884\u8bad\u7ec3\u6a21\u578b\u6587\u4ef6\uff1a", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5c3a\u5bf8\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6\u914d\u7f6e\u6587\u4ef6\uff1a", None))
        self.le_imgsz.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4:640 \u53ef\u6839\u636e\u9879\u76ee\u8c03\u6574\uff0c\u8981\u6c42\u76ee\u6807\u6e05\u6670\u53ef\u89c1", None))
        self.cb_pretrained_model_file.setPlaceholderText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u4e2a\u6570\uff1a", None))
        self.le_dataset_cfg_pth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u524d\u4e00\u6b65\u6570\u636e\u96c6\u5212\u5206\u540e\uff0c\u6240\u4ea7\u751f\u7684\u914d\u7f6e\u6587\u4ef6 yaml", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u4e60\u7387\uff1a", None))
        self.le_learning_rate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4:0.01 \u89c2\u5bdf\u8bad\u7ec3\u8fc7\u7a0b\uff0c\u82e5\u6570\u636e\u6ce2\u52a8\u5927\uff0c\u5219\u9002\u5f53\u964d\u4f4e\u5b66\u4e60\u7387", None))
        self.btn_save_cfg.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u914d\u7f6e\u6587\u4ef6", None))
        self.btn_open_cfg.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u63a5\u7f16\u8f91\u914d\u7f6e\u6587\u4ef6", None))
        self.btn_train.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c\u6a21\u578b\u8bad\u7ec3", None))
        self.btn_stop_train.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62\u6a21\u578b\u8bad\u7ec3", None))
        self.btn_show_train_info.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u8fc7\u7a0b\u53ef\u89c6\u5316", None))
        self.btn_stop_show_train.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62\u8bad\u7ec3\u8fc7\u7a0b\u53ef\u89c6\u5316", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u8bad\u7ec3", None))
        self.le_used_model_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u5f97\u5230\u7684\u6a21\u578b\u6587\u4ef6\u8def\u5f84\uff1abest.pt", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u56fe\u7247\u8def\u5f84\uff1a", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u5de5\u5177\u8def\u5f84\uff1a", None))
        self.le_test_image_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u56fe\u50cf\u7684\u8def\u5f84\uff0c\u53ef\u4ee5\u6307\u5b9a\u4e00\u5f20\u56fe\u7247\u6216\u8005\u4e00\u7ec4\u56fe\u7247\u7684\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.le_test_tool_pth.setText("")
        self.le_test_tool_pth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"yolo.exe \u6587\u4ef6\u8def\u5f84", None))
        self.btn_inference.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u7406\u6d4b\u8bd5", None))
        self.btn_check_result.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u63a8\u7406\u7ed3\u679c\u56fe\u7247", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa - ONNX", None))
        self.btn_open_model_dir.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6a21\u578b\u6587\u4ef6\u5939", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u6d4b\u8bd5\u4e0e\u5bfc\u51fa", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7\u4fe1\u606f", None))
    # retranslateUi

