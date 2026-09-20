<!--
  Visual-first README for GitHub.
  Inventory verified against the main branch.
-->

<div align="center">

# 🧠 Deep Learning Notebooks & Datasets

### A visual, hands-on deep learning laboratory — from the perceptron to CNNs, transfer learning, optimization, and applied neural networks.

<p>
  <a href="https://github.com/RITESH2127/Deep-learning-notebooks-and-datasets">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
  <img src="https://img.shields.io/badge/Notebooks-31-FF6F00?style=for-the-badge&logo=jupyter" alt="31 Jupyter notebooks">
  <img src="https://img.shields.io/badge/Datasets-8-2E7D32?style=for-the-badge&logo=databricks" alt="8 datasets">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/TensorFlow%20%2F%20Keras-Deep%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow and Keras">
  <img src="https://img.shields.io/badge/License-MIT-0A7BBB?style=for-the-badge" alt="MIT License">
</p>

<p>
  <strong>43 repository files</strong> · <strong>31 notebooks</strong> · <strong>8 datasets</strong> · <strong>2 image assets</strong>
</p>

<p>
  <a href="#-learning-architecture">Learning Architecture</a> ·
  <a href="#-notebook-atlas">Notebook Atlas</a> ·
  <a href="#-datasets">Datasets</a> ·
  <a href="#-run-it">Run It</a> ·
  <a href="#-repository-philosophy">Philosophy</a>
</p>

</div>

---

## ⚡ What is this repository?

This repository is a **hands-on deep learning laboratory** built around executable Jupyter notebooks and supporting datasets.

Instead of treating deep learning as a collection of black-box APIs, the notebooks explore the ideas that make neural networks work:

- 🧩 **Neural-network fundamentals**
- 📉 **Gradient descent and optimization**
- ⚙️ **Initialization and training dynamics**
- 🛡️ **Regularization and generalization**
- 🧠 **Multilayer perceptrons**
- 👁️ **Convolutional neural networks**
- 🖼️ **Image classification and augmentation**
- 🔄 **Transfer learning**
- 🏗️ **Functional neural-network architectures**
- 📊 **Applied machine-learning workflows**

> **Learning principle:** understand the mechanism → implement it → visualize its behavior → use it in a model.

---

## 📊 Repository at a glance

| Component | Current contents |
|:---|---:|
| 🧪 Jupyter notebooks | **31** |
| 🗂️ CSV datasets | **8** |
| 🖼️ Image assets | **2** |
| 📦 Total tracked files | **43** |
| 🧠 Core learning tracks | **6+** |
| 🛠️ Primary ecosystem | **Python + TensorFlow/Keras + NumPy** |

### The learning curve

**Foundations** → **Optimization** → **Training** → **Generalization** → **CNNs** → **Transfer Learning** → **Applied Deep Learning**

---

## 🗺️ Learning Architecture

~~~mermaid
flowchart LR
    A["🟦 Foundations<br/>Perceptron<br/>Neural Network<br/>Backpropagation"]
    B["🟨 Optimization<br/>Gradient Descent<br/>Optimizers<br/>EWMA"]
    C["🟩 Training Dynamics<br/>Scaling<br/>Xavier / He<br/>Batch Normalization"]
    D["🟪 Generalization<br/>Regularization<br/>Dropout<br/>Early Stopping"]
    E["🟥 Computer Vision<br/>CNN<br/>Pooling<br/>Padding<br/>LeNet-5"]
    F["🟧 Modern Vision<br/>Image Classification<br/>Augmentation<br/>VGG16<br/>ImageNet"]
    G["⬛ Applied Models<br/>MNIST<br/>Regression<br/>Customer Churn"]

    A --> B --> C --> D --> E --> F
    D --> G
    E --> G
    F --> G
~~~

---

## 🧭 The learning tracks

| Track | What you learn | Representative notebooks |
|:---|:---|:---|
| **01 · Foundations** | Perceptrons, neural networks, backpropagation | Perceptron, neural_network_scratch, backpropagation_* |
| **02 · Optimization** | Gradient descent, optimizers, EWMA, optimization geometry | Batch_vs_stochastic_GD, Optimizers, EWMA |
| **03 · Training** | Scaling, initialization, batch normalization, gradient behavior | feature_scaling, Xavier_and_He, batch_norm_example |
| **04 · Generalization** | Regularization, dropout, early stopping, hyperparameter tuning | regularizationNN, dropout_classification, early_stopping |
| **05 · Vision** | Convolution, pooling, padding, strides, CNN architectures | CNN_from_scratch, LENET5_CNN, ImageClassifierCNN |
| **06 · Transfer & Applied DL** | VGG16, ImageNet, MLP applications and functional APIs | transfer_learning_VGG16, pre_trained_imagenet_and_plots |

---

# 📚 Notebook Atlas

> **Tip:** Every notebook can be opened directly from the tables below. The **Colab** links use the repository's current main branch.

## 01 · Neural Network Foundations

| Notebook | What it explores | Launch |
|:---|:---|:---:|
| [Perceptron.ipynb](./Perceptron.ipynb) | Single-neuron classification and perceptron learning | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/Perceptron.ipynb) |
| [Problem_with_perceptron.ipynb](./Problem_with_perceptron.ipynb) | Where a single perceptron breaks down | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/Problem_with_perceptron.ipynb) |
| [neural_network_scratch.ipynb](./neural_network_scratch.ipynb) | Neural-network mechanics without hiding the fundamentals | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/neural_network_scratch.ipynb) |
| [backpropagation_classification.ipynb](./backpropagation_classification.ipynb) | Backpropagation for classification | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/backpropagation_classification.ipynb) |
| [backpropagation_regression.ipynb](./backpropagation_regression.ipynb) | Backpropagation for regression | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/backpropagation_regression.ipynb) |

---

## 02 · Optimization & Gradient Descent

| Notebook | What it explores | Launch |
|:---|:---|:---:|
| [Batch_vs_stochastic_GD.ipynb](./Batch_vs_stochastic_GD.ipynb) | Batch vs. stochastic gradient descent | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/Batch_vs_stochastic_GD.ipynb) |
| [Optimizers.ipynb](./Optimizers.ipynb) | Optimization strategies used during neural-network training | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/Optimizers.ipynb) |
| [EWMA.ipynb](./EWMA.ipynb) | Exponentially weighted moving averages | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/EWMA.ipynb) |
| [elongated_bowl_problem.ipynb](./elongated_bowl_problem.ipynb) | Intuition for optimization landscapes and gradient-based movement | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/elongated_bowl_problem.ipynb) |

---

## 03 · Training Dynamics

| Notebook | What it explores | Launch |
|:---|:---|:---:|
| [feature_scaling.ipynb](./feature_scaling.ipynb) | Why input scaling matters during training | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/feature_scaling.ipynb) |
| [Xavier_and_He.ipynb](./Xavier_and_He.ipynb) | Xavier and He weight initialization | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/Xavier_and_He.ipynb) |
| [batch_norm_example.ipynb](./batch_norm_example.ipynb) | Batch normalization in neural networks | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/batch_norm_example.ipynb) |
| [vanishing_gradient.ipynb](./vanishing_gradient.ipynb) | Vanishing-gradient behavior | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/vanishing_gradient.ipynb) |
| [zero_initialization_sigmoid.ipynb](./zero_initialization_sigmoid.ipynb) | Zero initialization and sigmoid-based training behavior | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/zero_initialization_sigmoid.ipynb) |

---

## 04 · Regularization & Model Design

| Notebook | What it explores | Launch |
|:---|:---|:---:|
| [regularizationNN.ipynb](./regularizationNN.ipynb) | Regularization techniques for neural networks | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/regularizationNN.ipynb) |
| [dropout_classification.ipynb](./dropout_classification.ipynb) | Dropout for classification | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/dropout_classification.ipynb) |
| [early_stopping.ipynb](./early_stopping.ipynb) | Early stopping as a training-control technique | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/early_stopping.ipynb) |
| [HyperParamterTuning.ipynb](./HyperParamterTuning.ipynb) | Hyperparameter experimentation and model tuning | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/HyperParamterTuning.ipynb) |
| [functional_api_demo.ipynb](./functional_api_demo.ipynb) | Keras Functional API | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/functional_api_demo.ipynb) |
| [non_sequential_model_functionalAPI.ipynb](./non_sequential_model_functionalAPI.ipynb) | Non-sequential model construction | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/non_sequential_model_functionalAPI.ipynb) |

---

## 05 · Convolutional Neural Networks

| Notebook | What it explores | Launch |
|:---|:---|:---:|
| [CNN_from_scratch.ipynb](./CNN_from_scratch.ipynb) | CNN mechanics implemented from the ground up | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/CNN_from_scratch.ipynb) |
| [padding_and_strides_CNN.ipynb](./padding_and_strides_CNN.ipynb) | Padding and stride behavior | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/padding_and_strides_CNN.ipynb) |
| [pooling_CNN.ipynb](./pooling_CNN.ipynb) | Pooling operations | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/pooling_CNN.ipynb) |
| [LENET5_CNN.ipynb](./LENET5_CNN.ipynb) | LeNet-5 architecture | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/LENET5_CNN.ipynb) |
| [ImageClassifierCNN.ipynb](./ImageClassifierCNN.ipynb) | CNN-based image classification workflow | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/ImageClassifierCNN.ipynb) |
| [ImageDataGenerator.ipynb](./ImageDataGenerator.ipynb) | Image data generation and augmentation | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/ImageDataGenerator.ipynb) |

---

## 06 · Transfer Learning & Pretrained Models

| Notebook | What it explores | Launch |
|:---|:---|:---:|
| [transfer_learning_VGG16.ipynb](./transfer_learning_VGG16.ipynb) | Transfer learning with VGG16 | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/transfer_learning_VGG16.ipynb) |
| [pre_trained_imagenet_and_plots.ipynb](./pre_trained_imagenet_and_plots.ipynb) | Pretrained ImageNet models and visual analysis | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/pre_trained_imagenet_and_plots.ipynb) |

---

## 07 · Applied Neural Networks

| Notebook | What it explores | Launch |
|:---|:---|:---:|
| [MNIST_digits_MLP.ipynb](./MNIST_digits_MLP.ipynb) | MLP-based handwritten-digit classification | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/MNIST_digits_MLP.ipynb) |
| [Regression_MLP.ipynb](./Regression_MLP.ipynb) | MLP for regression | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/Regression_MLP.ipynb) |
| [CustomerChurnPredictionMLP.ipynb](./CustomerChurnPredictionMLP.ipynb) | Customer churn prediction using an MLP | [▶ Colab](https://colab.research.google.com/github/RITESH2127/Deep-learning-notebooks-and-datasets/blob/main/CustomerChurnPredictionMLP.ipynb) |

---

## 🧪 Dataset Lab

The repository currently contains **8 CSV datasets** used across experiments.

| Dataset | Format | Learning context |
|:---|:---:|:---|
| [Admission_Predict_Ver1.1.csv](./Admission_Predict_Ver1.1.csv) | CSV | Regression / prediction |
| [Churn_Modelling.csv](./Churn_Modelling.csv) | CSV | Customer churn classification |
| [DailyDelhiClimate.csv](./DailyDelhiClimate.csv) | CSV | Time-series / climate experiments |
| [Social_Network_Ads.csv](./Social_Network_Ads.csv) | CSV | Binary classification |
| [car_prices.csv](./car_prices.csv) | CSV | Regression / tabular ML |
| [concertriccir2.csv](./concertriccir2.csv) | CSV | Non-linear classification |
| [diabetes.csv](./diabetes.csv) | CSV | Binary classification |
| [ushape.csv](./ushape.csv) | CSV | Non-linear classification |

> Dataset descriptions indicate the learning context suggested by the repository's notebook and dataset naming. They are not formal provenance statements.

---

## 🖼️ Visual Assets

The repository also contains two image assets used by selected notebooks:

- [doggo.jpg](./doggo.jpg)
- [kitty-cat-kitten-pet-45201.jpeg](./kitty-cat-kitten-pet-45201.jpeg)

---

# 🧠 Concept Map

~~~mermaid
mindmap
  root((Deep Learning Lab))
    Foundations
      Perceptron
      Neural Network
      Backpropagation
    Optimization
      Gradient Descent
      Optimizers
      EWMA
      Optimization Geometry
    Training
      Feature Scaling
      Xavier Initialization
      He Initialization
      Batch Normalization
      Vanishing Gradients
    Generalization
      Regularization
      Dropout
      Early Stopping
      Hyperparameter Tuning
    Architectures
      Sequential
      Functional API
      Non-Sequential Models
    Computer Vision
      Convolution
      Pooling
      Padding
      Strides
      LeNet-5
      Image Classification
      Data Generation
    Transfer Learning
      VGG16
      ImageNet
    Applications
      MNIST
      Regression
      Customer Churn
~~~

---

# 🔬 From intuition to implementation

A major theme of the repository is moving from **concept → experiment → model**.

~~~text
             ┌─────────────────────┐
             │  Mathematical idea  │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │  Small experiment   │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │ Visualize behavior  │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │ Build neural model  │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │ Apply to real data  │
             └─────────────────────┘
~~~

This makes the collection useful not only as a code archive, but also as a **study and revision system**.

---

# 🚀 Run It

## Option A — Google Colab

Choose a notebook above and click its **▶ Colab** link.

No local environment is required for the basic notebook workflow.

## Option B — Run locally

### 1. Clone

~~~bash
git clone https://github.com/RITESH2127/Deep-learning-notebooks-and-datasets.git
cd Deep-learning-notebooks-and-datasets
~~~

### 2. Create an environment

~~~bash
python -m venv .venv
~~~

Activate it:

**Windows**

~~~powershell
.venv\Scripts\activate
~~~

**macOS / Linux**

~~~bash
source .venv/bin/activate
~~~

### 3. Install the common notebook stack

~~~bash
python -m pip install --upgrade pip
pip install jupyter numpy pandas matplotlib scikit-learn tensorflow
~~~

> Individual notebooks can require additional packages or external model/data downloads. If a notebook reports a missing dependency, install the package required by that notebook.

### 4. Start Jupyter

~~~bash
jupyter notebook
~~~

Then open the notebook you want to explore.

---

# 🧰 Technology Stack

| Layer | Technologies |
|:---|:---|
| **Language** | Python |
| **Notebook** | Jupyter Notebook / Google Colab |
| **Numerical Computing** | NumPy |
| **Data Handling** | Pandas |
| **Visualization** | Matplotlib |
| **Machine Learning** | Scikit-learn |
| **Deep Learning** | TensorFlow / Keras |
| **Version Control** | Git / GitHub |

---

# 🎯 Recommended Learning Route

If you are learning deep learning from the beginning, follow this progression rather than jumping randomly.

### Phase 1 — Understand the neuron

**Perceptron**  
↓  
**Problem with perceptron**  
↓  
**Neural network from scratch**

### Phase 2 — Learn how models learn

**Backpropagation**  
↓  
**Gradient descent**  
↓  
**Optimizers**

### Phase 3 — Understand training behavior

**Feature scaling**  
↓  
**Xavier / He initialization**  
↓  
**Batch normalization**  
↓  
**Vanishing gradients**

### Phase 4 — Control overfitting

**Regularization**  
↓  
**Dropout**  
↓  
**Early stopping**  
↓  
**Hyperparameter tuning**

### Phase 5 — Enter computer vision

**Padding & strides**  
↓  
**Pooling**  
↓  
**CNN from scratch**  
↓  
**LeNet-5**  
↓  
**Image classification**  
↓  
**Image data generation**

### Phase 6 — Use pretrained representations

**VGG16 transfer learning**  
↓  
**ImageNet pretrained models**

### Phase 7 — Build applied models

**MNIST** · **Regression** · **Customer Churn**

---

# 📈 What you can learn

By working through the collection, you can build practical understanding of:

- How a perceptron makes a decision
- Why a single perceptron has limitations
- How multiple layers form a neural network
- How forward propagation and backpropagation work
- How gradients drive parameter updates
- Why batch and stochastic optimization behave differently
- How optimizer choices affect training
- Why feature scaling matters
- Why initialization can make or break training
- What causes vanishing gradients
- How batch normalization changes training behavior
- How regularization reduces overfitting
- How dropout works
- Why early stopping is useful
- How hyperparameters influence model behavior
- How convolution extracts spatial patterns
- How padding and stride change feature-map dimensions
- How pooling reduces spatial dimensions
- How CNN architectures are assembled
- How image augmentation expands training variation
- How transfer learning reuses pretrained representations
- How pretrained ImageNet models can be used in computer vision
- How neural networks can be applied to tabular classification and regression

---

# 🧩 Repository Design

~~~mermaid
flowchart TB
    R["📦 Repository"]

    R --> N["📓 31 Notebooks"]
    R --> D["📊 8 CSV Datasets"]
    R --> I["🖼️ 2 Image Assets"]

    N --> F["Foundations"]
    N --> O["Optimization"]
    N --> T["Training Dynamics"]
    N --> G["Generalization"]
    N --> C["CNN / Vision"]
    N --> P["Pretrained Models"]
    N --> A["Applied Models"]

    F --> O
    O --> T
    T --> G
    G --> C
    C --> P
    C --> A
    P --> A
~~~

---

# 🏗️ Repository Structure

~~~text
Deep-learning-notebooks-and-datasets/
│
├── 🧠 Foundations
│   ├── Perceptron.ipynb
│   ├── Problem_with_perceptron.ipynb
│   ├── neural_network_scratch.ipynb
│   └── backpropagation_*.ipynb
│
├── 📉 Optimization & Training
│   ├── Batch_vs_stochastic_GD.ipynb
│   ├── Optimizers.ipynb
│   ├── EWMA.ipynb
│   ├── feature_scaling.ipynb
│   ├── Xavier_and_He.ipynb
│   ├── batch_norm_example.ipynb
│   └── vanishing_gradient.ipynb
│
├── 🛡️ Generalization & Architecture
│   ├── regularizationNN.ipynb
│   ├── dropout_classification.ipynb
│   ├── early_stopping.ipynb
│   ├── HyperParamterTuning.ipynb
│   └── Functional API notebooks
│
├── 👁️ CNN & Computer Vision
│   ├── CNN_from_scratch.ipynb
│   ├── pooling_CNN.ipynb
│   ├── padding_and_strides_CNN.ipynb
│   ├── LENET5_CNN.ipynb
│   ├── ImageClassifierCNN.ipynb
│   └── ImageDataGenerator.ipynb
│
├── 🔄 Transfer Learning
│   ├── transfer_learning_VGG16.ipynb
│   └── pre_trained_imagenet_and_plots.ipynb
│
├── 📊 Applied Deep Learning
│   ├── MNIST_digits_MLP.ipynb
│   ├── Regression_MLP.ipynb
│   └── CustomerChurnPredictionMLP.ipynb
│
├── 📁 Datasets
│   └── 8 CSV files
│
├── 🖼️ Image Assets
│   └── 2 image files
│
├── LICENSE
└── README.md
~~~

---

# 💡 Repository Philosophy

> **Don't just learn how to use a model. Learn what the model is doing.**

The notebooks cover both **low-level intuition** and **higher-level frameworks**.

That makes the repository useful for:

- 🎓 Students learning deep learning
- 🧑‍💻 Developers building ML foundations
- 🧪 Experimentation and rapid prototyping
- 📚 Exam and interview revision
- 🔬 Understanding neural-network internals
- 🧠 Revisiting important deep-learning concepts

---

# 🔎 Quick Navigation

| I want to learn... | Start here |
|:---|:---|
| Perceptrons | [Perceptron.ipynb](./Perceptron.ipynb) |
| Neural networks from scratch | [neural_network_scratch.ipynb](./neural_network_scratch.ipynb) |
| Backpropagation | [backpropagation_classification.ipynb](./backpropagation_classification.ipynb) |
| Gradient descent | [Batch_vs_stochastic_GD.ipynb](./Batch_vs_stochastic_GD.ipynb) |
| Optimizers | [Optimizers.ipynb](./Optimizers.ipynb) |
| Weight initialization | [Xavier_and_He.ipynb](./Xavier_and_He.ipynb) |
| Batch normalization | [batch_norm_example.ipynb](./batch_norm_example.ipynb) |
| Overfitting / regularization | [regularizationNN.ipynb](./regularizationNN.ipynb) |
| Dropout | [dropout_classification.ipynb](./dropout_classification.ipynb) |
| CNN fundamentals | [CNN_from_scratch.ipynb](./CNN_from_scratch.ipynb) |
| Pooling | [pooling_CNN.ipynb](./pooling_CNN.ipynb) |
| LeNet-5 | [LENET5_CNN.ipynb](./LENET5_CNN.ipynb) |
| Image classification | [ImageClassifierCNN.ipynb](./ImageClassifierCNN.ipynb) |
| Image augmentation | [ImageDataGenerator.ipynb](./ImageDataGenerator.ipynb) |
| VGG16 transfer learning | [transfer_learning_VGG16.ipynb](./transfer_learning_VGG16.ipynb) |
| ImageNet | [pre_trained_imagenet_and_plots.ipynb](./pre_trained_imagenet_and_plots.ipynb) |
| MNIST | [MNIST_digits_MLP.ipynb](./MNIST_digits_MLP.ipynb) |
| Regression with an MLP | [Regression_MLP.ipynb](./Regression_MLP.ipynb) |
| Customer churn | [CustomerChurnPredictionMLP.ipynb](./CustomerChurnPredictionMLP.ipynb) |

---

# 🤝 Contributions

This repository is primarily a personal learning laboratory, but improvements are welcome.

If you find:

- a broken notebook,
- an incorrect explanation,
- a reproducibility issue,
- a dependency problem,
- or an opportunity to improve an experiment,

feel free to open an issue or submit a pull request.

---

# 👤 Author

<div align="center">

### Ritesh Kumar

**Computer Science Engineering · Machine Learning · AI · Data Science**

<a href="https://github.com/RITESH2127">
  <img src="https://img.shields.io/badge/GitHub-RITESH2127-181717?style=for-the-badge&logo=github" alt="Ritesh Kumar on GitHub">
</a>

</div>

---

<div align="center">

### ⭐ If this repository helps you understand deep learning, consider starring it.

**Learn → Experiment → Visualize → Build → Repeat**

</div>

---

<sub>Repository inventory verified against the current main branch on September 20, 2026.</sub>
