# Object-Detection-Simplified-With-Tensorflow-Lite

## Introduction 
Nowadays accomplish a model of object detection is simplest, however still needs of some skills, thinking about that, developed a tool to easy the generation of a new model using the architectures what are of tensorflow (graph). For this approach all models will are save on format tflite, with this format is possible apply yours models in android (native) and ios (swift). 
All process of development are automated, below will be show all the steps of setup up until the applyied of model in a new image.

## Step by Step

### First (Setup of enviromment in python)

In this process the python used was 3.5.6, all setup of python was in the anaconda 4.7.12 (conda), as soon as you install the conda folowing the steps what if find this link (https://docs.anaconda.com/anaconda/install/) to the system what you is using.

```
conda create -n tensorflowlite python=3.5.6
conda activate tensorflowlite
```

In the next step is update the pip and setuptools,

```
python -m pip install --upgrade pip setuptools wheel
```

After of update o pip, you will go the clone, activate enviromment and install of all packages that if find in the file requeriments.txt,

```
git clone https://github.com/valteresj2/Object-Detection-Simplified-With-Tensorflow-Lite.git
cd Object-Detection-Simplified-With-Tensorflow-Lite
pip install requeriments.txt
```

Now you can clone the api model of tensorflow:
```
git clone https://github.com/tensorflow/models.git
```

Done the clone of api do tensorflow is necessary compile protobufs and run setup.py that if find in the paste model:
```
cd model/research
protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto .\object_detection\protos\calibration.proto .\object_detection\protos\flexible_grid_anchor_generator.proto

python setup.py build
python setup.py install
```

Done all process of setup of api model tensorflow, you can add yours pictures of training and testing in the paste that if find on directory root (train, test), to this example i caught the pictures of example  of github of EdjeElectronics (https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10), where also i used some of steps of setup his, thank you EdjeElectronics!

Added the pictures, you can seleceted the model that wish this is link (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md), to transform you model in tflite is necessary that you download the models with the initials SSD (Single Shot MultiBox Detector), to this project will be used the model inception-v2 coco. If you to add a new model is necessary follow some steps:

1. Replace all files of paste "fine_tunning_model" new model hair you downloaded.
2. Open the file "labelmap.pbtxt" that if find of paste conf_model and add the labels of classification, equal the example. 
3. Open the file "model_conf.config" and open o file .config of you new model and replace in the on "model_conf.config" and after save.

After realized all steps above, now is run the command:
```
./process_model.sh
```

When finished the model is necessary run the next command to save the model in the format .tflite.
```
./save_model.sh
```

Command finished, you model it's in the paste "tflite"

Now can you run the query of example, add the picture desired equal the line "image=CWD_PATH+'/test/cam_image45.jpg'" of code "example_predict_image_tflite.ipynb"

If you want to test without having to run a new model, download model weights from this link (https://drive.google.com/file/d/1OYzxCeyiti2vBhTNhCvtdi8cq6U3dbRz/view?usp=sharing), create a paste with name "tflite" and add the file to this folder.

Obs.: For run the example is necessary create a new enviromment in python with the tensorflow==1.15






