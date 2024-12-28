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
