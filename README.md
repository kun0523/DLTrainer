# DLTrainer

## 路径管理
- 在软件目录下，创建一个`WorkDir`文件夹
- 切分的数据保存在 `dataset_timestamp` 文件夹下
- 训练过程文件保存在 `train_timestamp` 文件夹下

## 数据处理
- labelme: `D:\envs\ultr_py11\Scripts\labelme.exe`
- org_image_pth: `E:\DataSets\dents_det\org_D1\gold_scf\cutPatches640\NG`
- classes_names: `dent,`

## 模型训练
- yolo: `D:\envs\ultr_py11\Scripts\yolo.exe`
- 预训练模型文件夹：`E:\Pretrained_models\YOLOv11`
- 配置模板文件: `D:\share_dir\DLTrainer\default_configs\ultral_config_template.yaml`
- 数据集配置文件：`E:\DLTmp\dataset_20241227151050\dataset_20241227151050.yaml`

- 测试模型文件：`D:\share_dir\impression_detect\workdir\yolov11\det_dent_gold_scf\yolo11n_sgd\weights\last.pt`
- 测试图片文件：`E:\DataSets\dents_det\org_D1\gold_scf\cutPatches640\NG\4_5398.jpg`

## 模型测试和导出

## 软件打包命令
- `pyside6-deploy mainwindow.py --init`
  - 产生config文件
  - mainwindow.py 文件中包含整个APP的入口函数

- `pyside6-deploy -c pysidedeploy.spec`
  - 根据config文件进行打包
  - 可以修改的项目：
    - 修改app名称
    - 关闭console窗口

## TODO:
1. 在原图上标注后，根据标注信息，统计目标占原图的比例
2. 如果占比过低，则程序中自行切割图像，使得目标面积占比增大
3. 针对切割与旋转后的图像，对标注信息进行自动匹配