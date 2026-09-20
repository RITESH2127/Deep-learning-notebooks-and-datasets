# Learning Path

This guide turns the repository into a deliberate deep-learning curriculum.

## Stage 1 — Foundations

**Goal:** understand what a neural network computes before relying on high-level APIs.

Study:

1. Perceptron
2. Perceptron limitations
3. Neural network from scratch
4. Backpropagation for classification
5. Backpropagation for regression

**Checkpoint:** explain a forward pass, loss, gradient, and parameter update in your own words.

## Stage 2 — Optimization

**Goal:** understand how parameters actually move toward useful values.

Study:

1. Batch vs stochastic gradient descent
2. Optimizers
3. EWMA
4. Elongated-bowl optimization geometry

**Checkpoint:** explain why learning rate and optimizer choice can change convergence behavior.

## Stage 3 — Training Dynamics

**Goal:** understand why the same architecture can train very differently under different numerical conditions.

Study:

1. Feature scaling
2. Xavier initialization
3. He initialization
4. Batch normalization
5. Vanishing gradients
6. Zero initialization with sigmoid

**Checkpoint:** explain why initialization, scale, and gradient flow matter.

## Stage 4 — Generalization and Model Design

**Goal:** learn how to build models that generalize instead of simply fitting training data.

Study:

1. Regularization
2. Dropout
3. Early stopping
4. Hyperparameter tuning
5. Functional API
6. Non-sequential model design

**Checkpoint:** distinguish underfitting, good fit, and overfitting using training and validation behavior.

## Stage 5 — Computer Vision

**Goal:** understand the building blocks of convolutional neural networks.

Study:

1. Convolution from scratch
2. Padding and stride
3. Pooling
4. LeNet-5
5. Image classification
6. Image data generation

**Checkpoint:** explain how convolution, receptive fields, pooling, and augmentation contribute to visual learning.

## Stage 6 — Transfer Learning

**Goal:** understand how pretrained representations can reduce the amount of task-specific learning required.

Study:

1. VGG16 transfer learning
2. ImageNet pretrained models
3. Pretrained-model visualization

**Checkpoint:** explain the difference between using a pretrained model as a fixed feature extractor and fine-tuning it.

## Stage 7 — Applied Neural Networks

**Goal:** connect concepts to recognizable machine-learning tasks.

Study:

1. MNIST digit classification
2. Regression with an MLP
3. Customer churn prediction

**Checkpoint:** build a complete workflow from dataset inspection through preprocessing, training, evaluation, and interpretation.

## How to study each notebook

For every experiment:

1. Read the objective before executing code.
2. Predict what should happen.
3. Run the notebook top-to-bottom.
4. Inspect every visualization instead of skipping it.
5. Change one meaningful parameter.
6. Run the experiment again.
7. Compare the outputs.
8. Write down the reason for the observed difference.

That final step is where passive notebook execution becomes actual understanding.
