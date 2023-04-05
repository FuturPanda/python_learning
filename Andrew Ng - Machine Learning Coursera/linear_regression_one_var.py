import numpy as np
import matplotlib.pyplot as plt
# plt.style.use("./deeplearning.mplstyle")

# x_train is the input variable (size in 1000 square feet)
# y_train is the target (price in 1000s of dollars)
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

# m is the number of training examples
m = x_train.shape
print(m)

i = 1 # Change this to 1 to see (x^1, y^1)

x_i = x_train[i]
y_i = y_train[i]

# plt.scatter(x_train, y_train, marker='x', c='r')
# # Set the title
# plt.title("Housing Prices")
# # Set the y-axis label
# plt.ylabel('Price (in 1000s of dollars)')
# # Set the x-axis label
# plt.xlabel('Size (1000 sqft)')
# plt.show()

w = 200
b = 100

def compute_model_output(x, w, b):
    """
    Computes the prediction of a linear model
    Args:
      x (ndarray (m,)): Data, m examples 
      w,b (scalar)    : model parameters  
    Returns
      y (ndarray (m,)): target values
    """
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
        
    return f_wb

tmp_f_wb = compute_model_output(x_train, w, b,)
print(tmp_f_wb)

# Plot our model prediction
# plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction')

# # Plot the data points
# plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')

# # Set the title
# plt.title("Housing Prices")
# # Set the y-axis label
# plt.ylabel('Price (in 1000s of dollars)')
# # Set the x-axis label
# plt.xlabel('Size (1000 sqft)')
# plt.legend()
# plt.show()

ex_points1 = np.array([1, 2] )
ex_points2 = np.array([4, 9] )
ex_points3 = np.array([21, 47] )
plt.plot(ex_points1, ex_points2, ex_points3, c="r", marker='x', label="Ex")
plt.show()

