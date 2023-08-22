#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[4]:


#i import pandas for data anlysis and manipulations
import pandas as pd


# In[ ]:





# In[5]:


df = pd.read_csv("Book_ratingC>400.csv")
df.head()


# In[ ]:





# In[8]:


from book_recommendation_engine import recommendersystem



# In[ ]:





# In[13]:


def main(df):
 

    #exception handling
    try:
        #calling the similarity class
        s = recommendersystem(df)
        
        #specifying the operation the user want to perform on each of the class methods

        choice = int(input('\nEnter 1 for similarity between two users, 2 for similarity between a user and nth users, 3 for recommendation to a target user, and 4 for evaluating the metrices : '))
        
                  #condition for similarity between two users
        if(choice == 1):

            user1 = int(input('\nplease enter the first userID number : '))   # recieve input from users
            user2 = int(input('\nplease enter the second user ID number : '))
            print("Available metrices for finding similarity blw users are :")
            print("1: Pearson similarity")
            print("2: Minkowski similarity")
            print("3: cosine similarity")
            print("4: spearman correlation similarity")
            print('\nplease only choose a digit that represents your choice of metric')
            metric = int(input('\nChose the similarity matrix to use:'))
            
            if metric not in [1, 2, 3, 4]:
                print("Invalid input. Please enter a valid number.")
                return
    
            
                      #invoking the minkowski method of the class to find similarity between two users
            if(metric == 1):
                
                print(f'the pearson similarity between {user1} & {user2} : {s.pearson_similarity(user1, user2):.9f}')
        
                   #invoking the squared_euclidean_similarity of the class to find similarity between two users
            elif(metric == 2):
                print(f'\nthe minkowski similarity between {user1} & {user2} : {s.minkowski_similarity(user1, user2):.4f}')
            
            elif(metric == 3):
                print(f'\nthe cosine similarity between {user1} & {user2} : {s.cosine_similarity(user1, user2):.4f}')
            
            #invoking the chebyshev_similarity of the class to find similarity between two user
            elif(metric == 4):
                print(f'the spearman correlation similarity between {user1} & {user2} : {s.spearman_correlation_similarity(user1, user2):.4f}')
                
            else:
                print(f'similarity between {user1} & {user2} : {s.cosine_similarity(user1, user2):.4f}')
            
          
          
                 #condition to find similarity between a user and the nth users
        elif(choice == 2):
            
            target_user = int(input('please enter a userID of the target user to compute the similarity between the nth users : '))
            n = int(input('Number of similar users : '))
            print("\Availabele similarity metrices to use and find n similar users to a target user are :")
            print("1: cosine")
            print("2: pearson")
            print("3: minkowski")
            print("4: spearman")
            print('\nplease only choose a digit that represents your choice of metric')
            metric = int(input(f"enter the similarity matric to use and find similarity blw the user and {n} other users"))
            
            if metric not in [1, 2, 3, 4]:
                print("Invalid input. Please enter a valid number.")
                return
            
            if(metric == 1):
                print(f'\nthe similarity between {target_user} & {n} top users using cosine similarity metric are : ')
                print(s.n_similar_users(target_user, n, metric='cosine'))
        
               
            elif(metric == 2):
                    print(f'\nthe similarity between {target_user} & {n} top users using perason similarity metric are : ')
                    print(s.n_similar_users(target_user, n, metric='pearson'))
            
            elif(metric == 3):
                print(f'\nthe similarity between {target_user} & {n} top users using minkowski similarity metric are : ')
                print(s.n_similar_users(target_user, n, metric='minkowski'))
            

            elif(metric == 4):
                print(f'\nthe similarity between {target_user} & {n} top users using spearman similarity metric are : ')
                print(s.n_similar_users(target_user, n, metric='spearman'))
                
            else:
                print(f'the similarity between {target_user} & {n} top users using cosine similarity metric are : ')
                print(s.n_similar_users(target_user, n, metric='cosine'))
            
          
            
              #condition to make n recommendation to a target user
        elif(choice == 3):
            print("\nAvailabele metrices to use and make recommendations are :")
            target_user = int(input('please enter a userID of the target user to make recommendation to : '))
            n = int(input(f'enter Number of recommendations to {target_user} : '))
            print("\nAvailabele metrices to use and make recommendations are :")
            print("1. cosine")
            print("2. pearson")
            print("3. minkowski")
            print("4. spearman")
            metric = int(input(f"enter the similarity matric to use and make {n} recommendation to {target_user}"))
            
            if metric not in [1, 2, 3, 4]:
                print("Invalid input. Please enter a valid number.")
                return
            
            if(metric == 1):
                print(f'\nthe {n} recommendations for {target_user} based on cosine similarity metric are : ')
                print(s.make_recommendation(target_user, n, metric='cosine'))
        
               
            elif(metric == 2):
                    print(f'\nthe {n} recommendations for {target_user} based on pearson similarity metric are : ')
                    print(s.make_recommendation(target_user, n, metric='pearson'))
            
            elif(metric == 3):
                print(f'\nthe {n} recommendations for {target_user} based on mikowski similarity metric are : ')
                print(s.make_recommendation(target_user, n, metric='mikowski'))
            

            elif(metric == 4):
                print(f'\nthe {n} recommendations for {target_user} based on spearman similarity metric are : ')
                print(s.make_recommendation(target_user, n, metric='spearman'))
                
            else:
                print(f'\nthe {n} recommendations for {target_user} are : ')
                print(s.make_recommendation(target_user, n))
                
        elif(choice == 4):
            target_user = int(input('please enter a userID of the target user to validate the metrices used in making recommendation : '))
            n = int(input('Enter Number recommendations to find the accuracy : '))
            print('\nthe validation scores of the metrices used in recommendations are :')
            print(s.evaluate_similarity_metrics_cor(target_user, n, similarity_metrics=['cosine', 'pearson', 'mikowski', 'spearman']))
            
        else:
            target_user = int(input('please enter a userID of the target user to compute the similarity between the nth users : '))
            n = int(input('Number of similar users : '))
            print(f'\nthe {n} recommendations for {target_user} are : ')
            print(s.make_recommendation(target_user, n))
            
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except ValueError:
        print('input for what you want to do and number of recommendation can only be integer values, please check and try again')
    except:
        print("Some other exception happened.")


# In[ ]:




