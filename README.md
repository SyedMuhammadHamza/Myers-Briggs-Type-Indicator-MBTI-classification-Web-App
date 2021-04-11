# Myers-Briggs-Type-Indicator-MBTI-classification-Web-App

## Web Application
![Alt Text](https://github.com/SyedMuhammadHamza/Myers-Briggs-Type-Indicator-MBTI-classification-Web-App/blob/main/Images/screenrecording.gif)

## Overview
During my sophomore year of bachelors, I stumbled upon a book titled  ["Gifts differing: understanding personality type"](https://www.amazon.com/Gifts-Differing-Understanding-Personality-Type/dp/089106074X
) by Isabel Briggs Myers and Peter B. Myers through a friend I met on Reddit
"This book distinguishes four categories of personality styles and shows how these qualities determine the way you perceive the world and come to conclusions about what you've seen"  
later that same year, I came across a self-report by the same author titled "Myers–Briggs Type Indicator (MBTI)" designed to identify a person's personality type, strengths, and preferences, and based on this study people are identified as having one of 16 personality types

### The MBTI Types

* ISTJ - The Inspector
* ISTP - The Crafter
* ISFJ - The Protector
* ISFP - The Artist
* INFJ - The Advocate
* INFP - The Mediator
* INTJ - The Architect
* INTP - The Thinker
* ESTP - The Persuader
* ESTJ - The Director
* ESFP - The Performer
* ESFJ - The Caregiver
* ENFP - The Champion
* ENFJ - The Giver
* ENTP - The Debater
* ENTJ - The Commander

![Alt Text](https://github.com/SyedMuhammadHamza/Myers-Briggs-Type-Indicator-MBTI-classification-Web-App/blob/main/Images/gif.gif)


Around the same time, I became interested in Machine learning and data science. One of the most fascinating aspects that got me interested in ML was the fact how most dating applications don't use  Machine learning for matching people this article explains how Tinder was matching people for so long let me quote some of it here

"A few years ago, Tinder let Fast Company reporter Austin Carr look at his “secret internal Tinder rating,” and vaguely explained to him how the system worked. Essentially, the app used an Elo rating system, which is the same method used to calculate the skill levels of chess players: You rose in the ranks based on how many people swiped right on (“liked”) you, but that was weighted based on who the swiper was. The more right swipes that person had, the more their right swipe on you meant for your score.
Tinder would then serve people with similar scores to each other more often, assuming that people whom the crowd had similar opinions of would be in approximately the same tier of what they called “desirability.” (Tinder hasn’t revealed the intricacies of its points system, but in chess, a newbie usually has a score of around 800 and a top-tier expert has anything from 2,400 up.) (Also, Tinder declined to comment for this story.) "

Influenced by all these facts, I came up with the idea of
Myers–Briggs Type Indicator (MBTI) classification where my classifier can classify your personality type based on Isabel Briggs Myers self-study Myers–Briggs Type Indicator (MBTI). 
The classification result can be further used to match people with the most compatible personality types


## Data Collection
One of the most difficult challenges for me was the identification of what kind of data to be collected and used to classify Myers–Briggs personality types. During my final year research project at my university, I collected data from Reddit specifically posts from mental health communities in Reddit. By
analyzing and learning posting information written by users, my proposed model could accurately identify whether a user’s post belongs to a specific mental disorder, I used similar reasoning in this project, moreover to my surprise there are all 16 personality types subreddits on Reddit some even with 133k members tho there are some subreddit with only few thousand members I collected data from all theses 16 subreddits using Pushshift Reddit API 

### Reddit Data Collection Using Pushshift Reddit API [Code Link](https://github.com/SyedMuhammadHamza/Myers-Briggs-Type-Indicator-MBTI-classification-Web-App/blob/main/Model/Reddit%20Posts%20and%20Comments%20Data%20Collection%20with%20Pushshift.py)

## Dataset

|  Subreddit   | Number of subscribers    |  Number of posts collected  |
| ------------ |:------------------------:| ---------------------------:|
|   [ISTJ](https://www.reddit.com/r/ISTJ/)        |   12k  |      2600      |
|  [INFJ](https://www.reddit.com/r/infj/)       |  101K   |    10,000        |
|    [INTJ](https://www.reddit.com/r/intj/)       |    108K |     6,400      |
|   [ENFJ](https://www.reddit.com/r/enfj/)        |   18.9K  |     6,600       |
|    [ISTP](https://www.reddit.com/r/istp/)       |  19.3K   |     9,200       |
|    [ESFJ](https://www.reddit.com/r/ESFJ/)       |   4K  |      800      |
|     [INFP](https://www.reddit.com/r/infp/)      |  133K   |    8,600       |
|   [ESTP](https://www.reddit.com/r/estp/)        |  5K   |     830       |
|     [ENFP](https://www.reddit.com/r/ENFP/)      |  68K   |     1200       |
|     [ESTP](https://www.reddit.com/r/estp/)      |   5K  |      1700     |
|     [ESTJ](https://www.reddit.com/r/ESTJ/)      |  2.8K   |     700       |
|     [ENTJ](https://www.reddit.com/r/entj/)      |  20K   |     9000       |
|    [INTP](https://www.reddit.com/r/INTP/)       |  121K   |     12,000       |
|     [ISFJ](https://www.reddit.com/r/isfj/)      |   12K  |     4,400       |
|    [ENTP](https://www.reddit.com/r/entp/)       |  44K   |     7,600       |
|    [ISFP](https://www.reddit.com/r/isfp/)     |  16K   |      4,100      |

### Content
following data has been collected in a total of 16 CSV files during Data cleaning and preprocessing these 16 files has been concatenated into a final CSV file
|  Subreddit   | Body    |  Date |
| ------------ |:------------------------:|:------------------------:|
|  Subreddit name of post|Text of post  |  Posting date|




## Data cleaning and preprocessing
Data cleaning and preprocessing included the following

* Removing rows with Links in Body feature
* Removing rows with Emojis in Body feature
* Removing rows with HTML elements in the Body feature
* Removing rows with punctuations in the Body feature
* Removing rows with stopwords in the Body feature
* Removing rows with [removed] in Body feature
* Removing rows with [deleted] in Body feature
* Removing rows with just numbers in the Body feature

## Exploratory Data Analysis
Exploratory Data Analysis included the following
* Class Imbalance check
* N-gram Analysis
* Generating WordClouds

### PROBLEM ENCOUNTERED DURING EDA
During data collection, I noticed there were not many posts in some subreddits, reflected by the fact my code collected little amount of data for ESTJ, ESTP, ESFP, ESFJ, ISTJ, and ISFJ subreddits as a result during EDA I noticed the class imbalance

<img src="https://github.com/SyedMuhammadHamza/Myers-Briggs-Type-Indicator-MBTI-classification-Web-App/blob/main/Images/class_Imbalance.png"/>

One of the most effective ways to solve the problem of Class Imbalance for NLP tasks is to use an oversampling technique called SMOTE( Synthetic Minority Oversampling Technique oversampling methods) hence I solved Class Imbalance using SMOTE for this problem 

## Feature engineering
For Multinomial Regression, I have used  Bag of words and
TF-IDF Embeddings of each Reddit Post
### PROBLEM ENCOUNTERED DURING FEATURE ENGINEERING 
during Visualization of my high dimensional embeddings 
I converted my higher dimensional TF-IDF Embedding/Bag of words Embedding into two-dimensional using Truncated-SVD then visualized my 2D embeddings the resultant visualization is not linearly separable in 2D hence models like SVM and Logistic regression will not perform well that was the rationale for Using RNN architecture with LSTM in this project

<img src="https://github.com/SyedMuhammadHamza/Myers-Briggs-Type-Indicator-MBTI-classification-Web-App/blob/main/Images/embedding1.png"/>

## Model Building and Evaluation
For this project, I trained three models
1. Multinomial Logistic Regression with  Bag of words Embeddings, 
  Logistic regression, by default, is limited to two-class classification problems. Some extensions like one-vs-rest can allow logistic regression to be used for multi-class classification problems, although they require that the classification problem first be transformed into multiple binary classification problems. Instead, the multinomial logistic regression algorithm is an extension to the logistic regression model that involves changing the loss function to cross-entropy loss and predict probability distribution to a multinomial probability distribution to natively support multi-class classification problems.
2. Multinomial Logistic Regression with  TF-IDF Embeddings, 
  Logistic regression, by default, is limited to two-class classification problems. Some extensions like one-vs-rest can allow logistic regression to be used for multi-class classification problems, although they require that the classification problem first be transformed into multiple binary classification problems. Instead, the multinomial logistic regression algorithm is an extension to the logistic regression model that involves changing the loss function to cross-entropy loss and predict probability distribution to a multinomial probability distribution to natively support multi-class classification problems.
3. Recurrent Neural Networks with LSTM,
  Feed-forward neural networks have no memory of the input they receive and are bad at predicting what’s coming next. Because a feed-forward network only considers the current input, it has no notion of order in time. It simply can’t remember anything about what happened in the past except its training. In a RNN the information cycles through a loop. When it makes a decision, it considers the current input and also what it has learned from the inputs it received previously.
  A long short-term memory (LSTM) network is a type of RNN model that avoids the vanishing gradient problem by adding ’forget’ gates.


## Model performance

| Algorithm        | Accuracy           |  Recall |  Precision |  F1  | 
| ---------------- |:------------------:| -------:|-----------:|-----:|
|Multinomial Logistic Regression with  Bag of words Embeddings Score|  45.17% | 0.48 |0.47 | 0.45|
|Multinomial Logistic Regression with  TF-IDF Embeddings Model| 50.20% | 0.55 |0.58 | 0.56|
|Recurrent Neural Networks with LSTM|  95.33% | 0.70 |0.69 | 0.69|

<img src="https://github.com/SyedMuhammadHamza/Myers-Briggs-Type-Indicator-MBTI-classification-Web-App/blob/main/Images/plots1.png"/>
<img src="https://github.com/SyedMuhammadHamza/Myers-Briggs-Type-Indicator-MBTI-classification-Web-App/blob/main/Images/plots2.png"/>

Looking at the train and test accuracy plots or loss plots over epochs it's visible our model started to overfit after 8 epochs hence the final Model has been trained through 8 epochs

## Future Improvements
The data collected for the problem is not representative enough especially for some classes where collected posts were few hundreds 
I tried learning curve analysis for eight different sizes of datasets and the result of the learning curve confirmed there was a gap between training and test score pointing towards High Variance problem hence in the future if more posts can be collected then the resultant dataset will improve the performance of these models

## User interface
*  Used HTML,CSS and JavaScript,

## Productionization
* Deployed model to production using Flask


## Technologies 
* Python
* Scikit-learn
* Matplotlib & Seaborn for data visualization
* NLTK
* TensorFlow
* Sklearn for model building
* Python flask for HTTP server
* HTML/CSS/Javascript for  UI


## References
[1]. [https://link.springer.com/referenceworkentry/10.1007%2F978-3-319-28099-8_50-1](https://link.springer.com/referenceworkentry/10.1007%2F978-3-319-28099-8_50-1) <br/>
[2]. [https://arxiv.org/abs/1106.1813](https://arxiv.org/abs/1106.1813) <br>
[3]. [https://www.mentalhelp.net/psychological-testing/myers-briggs-type-indicator/](https://www.mentalhelp.net/psychological-testing/myers-briggs-type-indicator/)




©SyedMuhammadHamza Licensed under [MIT License](https://github.com/SyedMuhammadHamza/Myers-Briggs-Type-Indicator-MBTI-classification-Web-App/blob/main/LICENSE)




