# Book recommendation system

![image](https://github.com/Baci-Ak/Book_recommendation_system/assets/134199508/f495284a-bcb4-490f-93a7-85a08198a4d0)


## 📦 Overview
This project aims to build a personalized book recommendation system that suggests relevant books to users based on their preferences and similarities with other users. The system incorporates both content-based and collaborative filtering techniques, leveraging various similarity metrics to provide accurate and diverse recommendations. The dataset used for this project contains information about user ratings and book attributes, which has been preprocessed and ingested into Hadoop (HDFS) for efficient handling of large-scale data.

<img width="873" alt="Screenshot 2023-08-01 at 2 07 07 PM" src="https://github.com/Baci-Ak/Book_recommendation_system/assets/134199508/c51ebd47-5530-42cf-9dee-42363dd35f02">


## 🗃️ Business Context and Problem
With the ever-increasing volume of online content and the rise of Internet-enabled devices, navigating the vast sea of available options has become a challenge. This project aims to address the information overload issue faced by an online book selling company. The company's sales have been declining due to customers struggling to find relevant books from the overwhelming selection.


## 📖 Project Objective
The objective of this project is to design and implement an intelligent recommendation engine that provides personalized book suggestions to users. By doing so, the company aims to enhance its sales and improve customers' online shopping experience.


## 🛠️ Datasets

* Books.csv: Books are identified by their respective ISBN. Invalid ISBNs have already been removed from the dataset. Moreover, some content-based information is given (Book- Title, Book-Author, Year-Of-Publication, Publisher), obtained from Amazon Web Services. Note that in case of several authors, only the first is provided. URLs linking to cover images are also given, appearing in three different flavours (Image-URL-S, Image-URL-M, Image-URL-L), i.e., small, medium, large. These URLs point to the Amazon web site.

* Book-Ratings.csv: Contains the book rating information. Ratings (Book-Rating) are either explicit, expressed on a scale from 1-10 (higher values denoting higher appreciation), or implicit, expressed by 0. [Datasets](https://github.com/Baci-Ak/Datasets)

<img width="1151" alt="Screenshot 2023-08-01 at 4 24 26 PM" src="https://github.com/Baci-Ak/Book_recommendation_system/assets/134199508/79cbd313-dd16-40c8-a949-60522a809c3e">


## 💻 Project Structure
* Data Extraction and Preprocessing: The initial step involved extracting the Bookrating.csv and Books.csv datasets from web sources using Apache Nifi. The datasets were then joined based on important features and separated into matched and unmatched observations using item IDs. The matched dataset was ingested into Hadoop (HDFS) and later create table in Apache Hive.

<img width="1439" alt="Screenshot 2023-07-31 at 10 17 24 AM" src="https://github.com/Baci-Ak/Book_recommendation_system/assets/134199508/cd2d9565-26ee-4f1b-bf8d-b03c0d2aa46a">



* Exploratory Data Analysis (EDA): EDA was performed in Python to gain insights into the data distribution, identify unique users and books, and analyze rating patterns. This analysis helped in understanding the characteristics of the dataset and its suitability for building a recommendation system.

* Similarity Metrics: Four similarity metrics were implemented - Pearson correlation, Minkowski, Cosine, and Spearman - to calculate user similarities. Additionally, a K-nearest neighbors (KNN) approach was utilized to find similar users based on these metrics.

* Content-Based Recommendation: The content-based recommendation system suggests books to users based on their similarity to other users who have read and rated similar books. It provides personalized recommendations using the implemented similarity metrics.
Collaborative Filtering: Collaborative filtering techniques, such as user-based and item-based collaborative filtering, were integrated to enhance the recommendation system's accuracy and coverage.

* Validation and Evaluation: Methods for validating the recommendation system's accuracy were developed. The system was evaluated using cross-validation and the mean squared error (RMSE) to assess its performance.

* User Interface: A user-friendly interface was created to allow users to interact with the system and perform various tasks, including exploring book recommendations and customizing recommendation options.


##  🔍 Usage Instructions
To run the recommendation system and explore book recommendations:

1. Ensure you have Apache Nifi and Hadoop installed and configured if you want to automate the flow the data.
Run the data extraction and preprocessing pipeline in Apache Nifi to extract, join, and ingest the datasets into Hadoop (HDFS).

2. Execute the EDA code in Python to understand the dataset's characteristics and rating distributions.

3. Instantiate the book_recommendation_engine class, select the desired similarity metrics, and make recommendations for a target user.

4. to make recommendation based on KNN, Instantiate the Knn_recommendationEngine class and invoke the knn_similarity method to find similarity between a user and k users, OR invoke the KNN_recommendation method to recommendation to a target user. finally, invoke the evaluate_similarity_metrics method to evaluate teh metrices used in making recommendation.

5. Use the user interface function to interact with the system, explore personalized book recommendations, and customize recommendation options.


## 🪜 Business Impact
The successful implementation of this recommendation system directly addresses the business challenge of declining sales. By suggesting relevant books to customers based on their preferences, the company aims to enhance user engagement, increase sales, and deliver a personalized shopping experience.



