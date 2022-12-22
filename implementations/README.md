I tried to implement various approaches. 

- Machine Learning Classifiers from the sci kit learn package(not the best results).


Deep Learning Approaches:

- One random approach by simpling adding Dense layers and relu activation functions.
- Based on the results of the previous model, I tried to improve the model by adding Dropout layers and Early Stop.
- Changed the activation functions and kernel initializers.

It's worth noted that after explaratory analysis three features where observed to be dummy features. Therefore, I droped those columns from the dataset and an increase in the accuracy metrics was observed.

The best model managed to acheive accuracy at 90%.

As a second phase of this project I am going to try and implement neural architecture search, to see if I can find a better classifier for the problem.

To be continued...
