# Deep Learning Notebooks & Datasets

A practical deep learning learning lab containing notebooks, experiments, and datasets covering neural networks, optimization, regularization, CNNs, transfer learning, and applied ML workflows.

> Built as a hands-on reference for understanding deep learning concepts by implementing and experimenting with them in Python.

## What you'll find here

This repository moves from neural-network fundamentals to computer vision and applied deep learning:

| Area | Topics |
|---|---|
| Neural Network Fundamentals | Perceptrons, neural networks from scratch, backpropagation |
| Optimization | Batch vs. stochastic gradient descent, optimizers, EWMA |
| Training Techniques | Feature scaling, Xavier/He initialization, batch normalization |
| Generalization | Regularization, dropout, early stopping |
| CNNs | Convolution, pooling, padding, strides, CNN from scratch |
| Computer Vision | Image classification, image data generation, LeNet-5 |
| Transfer Learning | VGG16 and pretrained ImageNet workflows |
| Applied Deep Learning | Customer churn prediction with an MLP |
| Supporting Data | Tabular and image datasets used by the notebooks |

## Repository roadmap

### 01 · Foundations

| Notebook | Focus |
|---|---|
| [Perceptron.ipynb](./Perceptron.ipynb) | Perceptron fundamentals |
| [Problem_with_perceptron.ipynb](./Problem_with_perceptron.ipynb) | Limitations of a single perceptron |
| [neural_network_scratch.ipynb](./neural_network_scratch.ipynb) | Neural network implementation from scratch |
| [backpropagation_classification.ipynb](./backpropagation_classification.ipynb) | Backpropagation for classification |
| [backpropagation_regression.ipynb](./backpropagation_regression.ipynb) | Backpropagation for regression |

### 02 · Optimization & Training

| Notebook | Focus |
|---|---|
| [Batch_vs_stochastic_GD.ipynb](./Batch_vs_stochastic_GD.ipynb) | Batch, stochastic, and gradient-descent behavior |
| [Optimizers.ipynb](./Optimizers.ipynb) | Neural-network optimization methods |
| [EWMA.ipynb](./EWMA.ipynb) | Exponentially weighted moving average |
| [feature_scaling.ipynb](./feature_scaling.ipynb) | Input feature normalization/scaling |
| [Xavier_and_He.ipynb](./Xavier_and_He.ipynb) | Weight initialization strategies |
| [batch_norm_example.ipynb](./batch_norm_example.ipynb) | Batch normalization |
| [vanishing_gradient.ipynb](./vanishing_gradient.ipynb) | Vanishing-gradient behavior |
| [zero_initialization_sigmoid.ipynb](./zero_initialization_sigmoid.ipynb) | Zero initialization and sigmoid activation |
| [elongated_bowl_problem.ipynb](./elongated_bowl_problem.ipynb) | Optimization geometry and gradient descent |

### 03 · Regularization & Model Design

| Notebook | Focus |
|---|---|
| [regularizationNN.ipynb](./regularizationNN.ipynb) | Neural-network regularization |
| [dropout_classification.ipynb](./dropout_classification.ipynb) | Dropout for classification |
| [early_stopping.ipynb](./early_stopping.ipynb) | Early stopping |
| [HyperParamterTuning.ipynb](./HyperParamterTuning.ipynb) | Hyperparameter tuning |
| [functional_api_demo.ipynb](./functional_api_demo.ipynb) | Keras Functional API |
| [non_sequential_model_functionalAPI.ipynb](./non_sequential_model_functionalAPI.ipynb) | Non-sequential model architectures |

### 04 · Convolutional Neural Networks

| Notebook | Focus |
|---|---|
| [CNN_from_scratch.ipynb](./CNN_from_scratch.ipynb) | CNN mechanics from scratch |
| [padding_and_strides_CNN.ipynb](./padding_and_strides_CNN.ipynb) | Padding and stride behavior |
| [pooling_CNN.ipynb](./pooling_CNN.ipynb) | Pooling operations |
| [LENET5_CNN.ipynb](./LENET5_CNN.ipynb) | LeNet-5 architecture |
| [ImageClassifierCNN.ipynb](./ImageClassifierCNN.ipynb) | CNN-based image classification |
| [ImageDataGenerator.ipynb](./ImageDataGenerator.ipynb) | Image augmentation/data generation |

### 05 · Transfer Learning & Pretrained Models

| Notebook | Focus |
|---|---|
| [transfer_learning_VGG16.ipynb](./transfer_learning_VGG16.ipynb) | Transfer learning with VGG16 |
| [pre_trained_imagenet_and_plots.ipynb](./pre_trained_imagenet_and_plots.ipynb) | Pretrained ImageNet models and visualization |

### 06 · Applied Neural Networks

| Notebook | Focus |
|---|---|
| [MNIST_digits_MLP.ipynb](./MNIST_digits_MLP.ipynb) | MLP for handwritten-digit classification |
| [Regression_MLP.ipynb](./Regression_MLP.ipynb) | Multilayer perceptron for regression |
| [CustomerChurnPredictionMLP.ipynb](./CustomerChurnPredictionMLP.ipynb) | Customer churn prediction using an MLP |

## Datasets

The repository includes small datasets used for demonstrations and experiments:

- `Admission_Predict_Ver1.1.csv`
- `Churn_Modelling.csv`
- `DailyDelhiClimate.csv`
- `Social_Network_Ads.csv`
- `car_prices.csv`
- `concertriccir2.csv`
- `diabetes.csv`
- `ushape.csv`

Image assets are also included for selected computer-vision notebooks.

## Suggested learning path

`Perceptron → Neural Network from Scratch → Backpropagation → Gradient Descent → Optimizers → Initialization → Batch Normalization → Regularization → Dropout → CNN Basics → CNN from Scratch → Image Classification → Transfer Learning`

This order builds intuition first and introduces higher-level deep learning workflows afterward.

## Tech stack

**Python** · **NumPy** · **Pandas** · **Matplotlib** · **TensorFlow / Keras** · **Jupyter / Google Colab**

## Running the notebooks

Most notebooks are designed for Jupyter Notebook or Google Colab.

```bash
git clone https://github.com/RITESH2127/Deep-learning-notebooks-and-datasets.git
cd Deep-learning-notebooks-and-datasets
```

Then open the desired `.ipynb` file in Jupyter or upload it to Google Colab.

Some notebooks may download standard datasets or pretrained models at runtime, so an internet connection can be required.

## Repository structure

```text
Deep-learning-notebooks-and-datasets/
├── Neural network & optimization notebooks
├── CNN & computer-vision notebooks
├── Transfer-learning notebooks
├── Applied deep-learning notebooks
├── CSV datasets
├── Image assets
└── LICENSE
```

## Why this repository exists

The goal is not just to call a library and train a model. The notebooks focus on understanding **why** deep learning components work, how training behaves, and how individual building blocks fit together into complete models.

## Author

**Ritesh Kumar**  
Computer Science Engineering  
GitHub: [@RITESH2127](https://github.com/RITESH2127)

## License

Distributed under the repository's existing [LICENSE](./LICENSE).
