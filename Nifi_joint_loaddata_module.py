#!/usr/bin/env python
# coding: utf-8

# # load book datasets module

# In[1]:


#define the load data class


#importing libraries that i need to load the datasets


#used for core computing
import numpy as np
# use for data manipulation and analysis
import pandas as pd
#system
import warnings
warnings.filterwarnings("ignore")

class loaddataset:
   #initializer method for initializing objects of the class loaddataset: 
    def __init__(self, ratings, books, users, book_ratings2):
        self.ratings = ratings
        self.books = books
        self.users = users
        self.book_ratings2 = book_ratings2

    def get_book_ratings(self):
        #Handling exceptions
        try:
            #reading the book rating dataset into a pandas dataframe
            self.ratings = pd.read_csv('Book-Ratings.csv', sep=';', error_bad_lines=False, warn_bad_lines=False, encoding="latin-1")
            
            #changing the book dataframe columns
            self.ratings.columns = ['user_id', 'book_id', 'bookrating']
            return self.ratings
        
        except FileNotFoundError:
            print('the file you are trying to read is not in this working directory, please make sure the file you want to read is in this current working directory')
        except OSError as err:
            print("OS error: {0}".format(err))
        except NameError :
            print('there is a name in the class method that is not defined, please check to fix this')
        except:
            print("Some other exception happened.")
    
    
    ##A method that returns the book titles of a loaddataset object
    def get_books(self):
        #Handling exceptions
        try:
            #reading the books dataset into a pandas dataframe i called books
            self.books = pd.read_csv('Books.csv', sep=';', error_bad_lines=False, warn_bad_lines=False, encoding="latin-1")
            #renaming the columns for easy understanding
            self.books.columns = ['book_id', 'booktitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']
            return self.books
        
        except FileNotFoundError:
            print('the file you are trying to read is not in this working directory, please make sure the file you want to read is in this current working directory')
        except OSError as err:
            print("OS error: {0}".format(err))
        except NameError :
            print('there is a name in the class method that is not defined, please check to fix this')
        except:
            print("Some other exception happened.")
    
    
    #A method that returns the userID of a loaddataset object: 
    def get_userid(self):
        #Handling exceptions
        try:
            #reading the users dataset into a pandas dataframe i called users
            self.users = pd.read_csv('Users.csv', sep=';', error_bad_lines=False, warn_bad_lines=False, encoding="latin-1")
            #here i rename the columns for easy understanding
            self.users.columns = ['user_id', 'Location', 'Age']
            
            return self.users
        
        except FileNotFoundError:
            print('the file you are trying to read is not in this working directory, please make sure the file you want to read is in this current working directory')
        except OSError as err:
            print("OS error: {0}".format(err))
        except NameError :
            print('there is a name in the class method that is not defined, please check to fix this')
        except:
            print("Some other exception happened.")
            
    
    def get_book_ratings2(self):
        #Handling exceptions
        try:
            #reading the book rating dataset into a pandas dataframe
            self.book_ratings2 = pd.read_csv('Book-Ratings2.csv', sep=';', error_bad_lines=False, warn_bad_lines=False, encoding="latin-1")
            
            #changing the book dataframe columns
            self.book_ratings2.columns = ['user_id', 'book_id', 'bookrating', 'booktittle', 'book_author', 'year_of_pub']
            return self.book_ratings2
        
        except FileNotFoundError:
            print('the file you are trying to read is not in this working directory, please make sure the file you want to read is in this current working directory')
        except OSError as err:
            print("OS error: {0}".format(err))
        except NameError :
            print('there is a name in the class method that is not defined, please check to fix this')
        except:
            print("Some other exception happened.")
        

        


# In[2]:


s = loaddataset('ratings', 'books', 'users', 'book_ratings2')
df = s.get_book_ratings()
df


# In[ ]:




