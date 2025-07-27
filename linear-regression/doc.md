Steps:
Prepare Data: We'll create a dataset with features such as area (square feet), number of rooms, and other relevant features.

Train Model: We'll use LinearRegression to train the model.

Predict Prices: Once the model is trained, we can make predictions on new data.


Explanation:
Data Creation:

We create a small dataset with columns for Area, Num_Rooms, and Price (representing house price). This is just a simulation; in a real-world scenario, you would use actual housing data.

Feature and Target Variables:

X contains the input features, like the Area and Num_Rooms, while y contains the target variable, which is the Price we are trying to predict.

Train-Test Split:

We split the dataset into training and testing sets using train_test_split from scikit-learn. This is done to ensure that the model is trained on a portion of the data and tested on another portion to evaluate its performance.

Linear Regression:

We use LinearRegression() from scikit-learn to train the model using the training data. After training, the model can predict house prices based on the input features.

Model Evaluation:

We use Mean Squared Error (MSE) to evaluate how well the model performs. A lower MSE indicates a better model.

Visualization:

We use matplotlib to plot the predicted prices vs. the actual prices, showing how well the model fits the data.