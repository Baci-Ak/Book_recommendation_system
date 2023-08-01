# Book_recommendation_system

![image](https://github.com/Baci-Ak/Book_recommendation_system/assets/134199508/f495284a-bcb4-490f-93a7-85a08198a4d0)


## 📦 Overview
This project aims to build a personalized book recommendation system that suggests relevant books to users based on their preferences and similarities with other users. The system incorporates both content-based and collaborative filtering techniques, leveraging various similarity metrics to provide accurate and diverse recommendations. The dataset used for this project contains information about user ratings and book attributes, which has been preprocessed and ingested into Hadoop (HDFS) for efficient handling of large-scale data.

<img width="873" alt="Screenshot 2023-08-01 at 2 07 07 PM" src="https://github.com/Baci-Ak/Book_recommendation_system/assets/134199508/c51ebd47-5530-42cf-9dee-42363dd35f02">


### 💻 Project Structure
* Data Extraction and Preprocessing: The initial step involved extracting the Bookrating.csv and Books.csv datasets from web sources using Apache Nifi. The datasets were then joined based on important features and separated into matched and unmatched observations using item IDs. The matched dataset was ingested into Hadoop using Apache Hive.

<img width="1439" alt="Screenshot 2023-07-31 at 10 17 24 AM" src="https://github.com/Baci-Ak/Book_recommendation_system/assets/134199508/cd2d9565-26ee-4f1b-bf8d-b03c0d2aa46a">



* Exploratory Data Analysis (EDA): EDA was performed in Python to gain insights into the data distribution, identify unique users and books, and analyze rating patterns. This analysis helped in understanding the characteristics of the dataset and its suitability for building a recommendation system.

* Similarity Metrics: Four similarity metrics were implemented - Pearson correlation, Minkowski, Cosine, and Spearman - to calculate user similarities. Additionally, a K-nearest neighbors (KNN) approach was utilized to find similar users based on these metrics.

* Content-Based Recommendation: The content-based recommendation system suggests books to users based on their similarity to other users who have read and rated similar books. It provides personalized recommendations using the implemented similarity metrics.
Collaborative Filtering: Collaborative filtering techniques, such as user-based and item-based collaborative filtering, were integrated to enhance the recommendation system's accuracy and coverage.

* Validation and Evaluation: Methods for validating the recommendation system's accuracy were developed. The system was evaluated using cross-validation and the mean squared error (RMSE) to assess its performance.

* User Interface: A user-friendly interface was created to allow users to interact with the system and perform various tasks, including exploring book recommendations and customizing recommendation options.

####  🔍 Usage Instructions
To run the recommendation system and explore book recommendations:

1. Ensure you have Apache Nifi and Hadoop installed and configured if you want to automate the flow the data.
Run the data extraction and preprocessing pipeline in Apache Nifi to extract, join, and ingest the datasets into Hadoop (HDFS).

2. Execute the EDA code in Python to understand the dataset's characteristics and rating distributions.

3. Instantiate the recommendation system class, select the desired similarity metrics, and make recommendations for a target user.

4. Use the user interface function to interact with the system, explore personalized book recommendations, and customize recommendation options.
