# Object-Detection-Simplified-With-Tensorflow

## Introduction 
Nowadays accomplish a model of object detection is simplest, however still needs of some skills, thinking about that, developed a tool to easy the generation of a new model using the architectures what are of tensorflow (graph). For this approach all models will are save on format tflite, with this format is possible apply yours models in android (native) and ios (swift). 
All process of development are automated, below will be show all the steps of setup up until the applyied of model in a new image.

## Step by Step

### First (Setup of enviromment in python)

In this process the python used was 3.5.6, all setup of python was in the anaconda 4.7.12 (conda), as soon as you install the conda folowing the steps what if find this link (https://docs.anaconda.com/anaconda/install/) to the system what you is using.

```
conda create -n tensorflowlite python=3.5.6
```

In the next step is update the pip and setuptools,

```
python -m pip install --upgrade pip setuptools wheel
```

After of update o pip, you will go the clone, activate enviromment and install of all packages that if find in the file requeriments.txt,

```
git clone https://github.com/valteresj2/Object-Detection-Simplified-With-Tensorflow-Lite.git
cd Object-Detection-Simplified-With-Tensorflow-Lite
conda activate tensorflowlite
pip install requeriments.txt
```

Now

