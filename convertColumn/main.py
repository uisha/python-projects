from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV

# Define the hyperparameter space to search over
param_grid = {
    'hidden_layer_sizes': [(10,), (20,), (30,), (40,), (50,)],
    'activation': ['logistic', 'tanh', 'relu'],
    'learning_rate_init': [0.001, 0.01, 0.1]
}

# Create an MLP classifier object
mlp = MLPClassifier(max_iter=100)

# Create a GridSearchCV object with 5-fold cross-validation
grid_search = GridSearchCV(mlp, param_grid=param_grid, cv=5, scoring='neg_log_loss')

# Fit the GridSearchCV object to the training data
grid_search.fit(X_train, y_train)

# Get the best hyperparameters and the corresponding validation loss
best_params = grid_search.best_params_
best_val_loss = -grid_search.best_score_

# Train a new model with the best hyperparameters on the combined training and validation sets
best_mlp = MLPClassifier(max_iter=100, **best_params)
best_mlp.fit(X_train_val, y_train_val)

# Evaluate the final model on the test set
test_loss = log_loss(y_test, best_mlp.predict_proba(X_test))
