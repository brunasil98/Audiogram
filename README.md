# **Leveraging Audiogram Frequencies to Predict Other Frequencies**

  The goal for this Take Home Assessment was **to recreate** an audiogram, which consists of hearing thresholds from a listener in 7 different frequencies for each ear. In order to accomplish this task, recreating this audiogram leveraged 3 of these frequency values as inputs to Machine Learning models in order to predict the other threshold frequencies. Another important task for this project was to analyze the data provided.

To analyze and vizualize the peculiarities of our data, I plotted five different graph. 

- The number of missing values(NaN) for each column

![image](https://user-images.githubusercontent.com/75848451/180352319-68b41579-0540-4cba-881b-0ec78c83e08d.png)

As the graph show, the **R8k** and **L8K** represent the most all Nan value of our dataset. This will be determinant how I will handle the miss data.

- Correlation of the Features
- 
![image](https://user-images.githubusercontent.com/75848451/180350786-ca3cc102-3da5-48d2-937b-571500c4636a.png)

The graph correlation shows that the features has **higher correlation** with **freuquency closer** to them. As frequency 1k has a higher correlation with 500k and 2k

- Normal distribution of the frequency features
- 
![image](https://user-images.githubusercontent.com/75848451/180350903-9adbe903-e603-45de-8f83-6a4efb76127e.png)
![image](https://user-images.githubusercontent.com/75848451/180350955-c447533f-e580-4d8f-b444-f5e923f8afac.png)

The graphs show that **lower frequencies** have **smaller standard deviations**; consequently, making it easier to predict those frequencies. 

- Gender Proportions

![image](https://user-images.githubusercontent.com/75848451/180351979-10c2446a-8996-436b-bad8-1296d0474083.png)

There are **more men** than women in this dataset with more than a **$\frac{3}{1}$ ratio** as the graph shows. 

- Hearing Loss at Various Frequency Levels for Each Ear
- 
![image](https://user-images.githubusercontent.com/75848451/180350658-9b4a4c9d-d22b-49e5-b352-f2f0479b4bfa.png)

The **left** ear has the **worst** loss **across frequencies**.

Trainig Models

Using the Sckit_Learn and Keras libraries, I created 4 models:
- Linear Regression
- Decision Tree Report
- KNeighbors Regressor
- Artificial Neural Netork

The select the best model, it was created a line graph to vizualized what model has better accuracy using the mean absolute error (MAE) at each frequency.

![image](https://user-images.githubusercontent.com/75848451/180351816-4bc5993d-754d-4a06-a534-b6279205e2ff.png)
![image](https://user-images.githubusercontent.com/75848451/180351842-940b1bd8-7638-4220-9c6f-efc51647389d.png)

**ANN HAS THE BEST PREDICTION FOR BOTH EAR**



