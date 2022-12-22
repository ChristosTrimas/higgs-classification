To implement the NAS for my model I used a Multi Layer Perceptron Neural Architecture Search by codeaway23 and his repo MLPNAS.

Note: if two consecutive layers are dropout layers, then the program crashes because both layers have the same name 'dropout'. Solution add an if statement to prevent that from happening. 
