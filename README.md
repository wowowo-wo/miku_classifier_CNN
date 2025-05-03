# miku_classifier_CNN

Miku Classifier is a simple CNN that tells you whether or not Hatsune Miku appears in an image. Built with PyTorch.

# Usage

Just run the command below to see whether the model thinks Miku is in your image — along with its confidence score.

```bash
git clone https://github.com/wowowo-wo/miku_classifier_CNN
cd miku_classifier_CNN
python3 cli.py (URL of image file)
```

## About Notebooks

The notebooks directory includes two ipynb files. They're mostly experiments and drafts, but you're welcome to play with them — they contain reusable functions and ideas.

### 1.miku_classifier_CNN_by_keras.ipynb

This notebook covers the following steps:

1.Scraping image data needed for training

2.Building and training a model using Keras

3.Evaluating the trained model

4.Using the model to check whether a given image via URL contains Miku or not.

#### Run on Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wowowo-wo/miku_classifier_CNN/blob/main/notebooks/miku_classifier_CNN_by_keras.ipynb)

### 2.miku_classifier_ResNet50

This notebook covers the following steps:
1.loading and preprocessing images
2.Transfer learning with ResNet50 using pytorch
3.save the trained model
4.Using the model to check whether a given image via URL contains Miku or not

#### Run on Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wowowo-wo/miku_classifier_CNN/blob/main/notebooks/miku_classifier_ResNet50.ipynb)


## Requirements


```bash
sudo apt install chafa
pip install -r requirements.txt
```

