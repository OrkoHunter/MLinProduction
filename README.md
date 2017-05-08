Machine Learning in Production
==============================

## About the project

In Python, currently we have libraries like Theano, TensorFlow and PyTorch where you can write low level code for Deep Learning, then there are libraries like Keras (built on top of Theano and Tensorflow) and Lasagne (built on top of Theano) which gives us more ease to create a production ready model.

We have tiny-dnn in C++ which has shown very promising speed up on CPU.

But any how the user has to write code in one of the language and it hinders a person's reach to Deep Learning model. When nearly every Deep Learning Paper has a graphical representation of the model, and nearly every Deep Learning library creates a graph of the model before training, why can't we just let the user create a graph and run the model?

But there is a compromise, the more high level abstraction you get to manipulating with the model becomes harder, but most of the deep learning model in production needs no manipulation as such.

We propose to create an interface such that the user would be able to create a graph without writing code and then easily train it. For it we would create an extension over Keras library and using flask we would create a web interface.

Why web interface?

Because not only this makes the app platform independent, but we would be able to host it on a server and give the user flexibility to create a graph from all the possible platforms, and even from a phone!

## About the application

We would create abstraction over every "layer" defined in the Keras library, and firstly would like to target the sequential model of Keras. (Note: Keras has two types of model, sequential and the functional model, We are targeting both the models but firstly the sequential model because it is easier to create a graph of sequential model)
This is a rough breakdown of few of the layers:
1. Input - User have to provide the dimension of the input specific to the data.
2. Dense - Number of Units, Non-linearity ...
3. Conv1D -
4. Conv2D
Similarly for others, see that we are providing enough flexibility to tweak with the layer parameters. We aim to cover every argument passed in the corresponding Keras API.

# Installation

Clone the repository, install the requirements using

```
pip install -r requirements.txt
```

And then run the app using

```
python run.py
```
