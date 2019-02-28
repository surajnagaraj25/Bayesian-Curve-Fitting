Suraj Nagaraja (RUID:189005203)
Bayesian curve fitting Program using Python
IDE used : Spyder(Anaconda)

In the zip folder, the inputDataset.txt file contains 10 values for testing. The values from inputDataset.txt is stored in a list 'T' and the mean, variance and predicted 11th value is displayed. The program also computes and prints the absolute mean error and average relative error in order to evaluate performance.

In order to test for different values, change the 10 values in inputDataset.txt.
 
*Steps to run the program on Spyder IDE:
1)Open the bayes1.py file using Spyder IDE. Note that the libraries 'numpy' and 'math' need to be imported for the program to run successfully.
2)The program comprises of functions to calculate the mean and variance of the input dataset and the probability of the predicted value. The 10 input values are stored in a list 'T' in the beginning of the program.
3)Once the libraries are imported, the program can be run by clicking on the green 'play' button in the control panel displayed on top or by pressing the F5 key.
4)The mean, variance, predicted value, absolute mean error and the average relative error are displayed in the console window to the right.
5)For different values, change the 10 values in the list named 'T' and repeat step 3. The values are not imported directly from the CSV file to enhance the simplicity of the program and avoid the use of additional libraries.

In the source code submitted, parameters alpha and beta are assumed to be fixed as 0.005 and 5 and X is a list that defines the steps in the input data points. x is to denote the value which is being predicted(11th). Here M is considered as 6.
I is the unit matrix which is used to find S inverse.

