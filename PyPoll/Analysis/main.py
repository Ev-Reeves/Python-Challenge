#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import os
import pandas as pd


# In[132]:


election = "/Users/evanreeves/Desktop/ucb-ber-data-pt-06-2020-u-c/02-Homework/03-Python/Python-Challenge/PyPoll/Resources/election_data.csv"
election_ = pd.read_csv(election)
election_analysis = os.path.join("election_analysis.csv")


# In[67]:


unique_votes = election_["Voter ID"].unique()

unique_candidates = election_["Candidate"].unique()

vote_percentage = [election_["Candidate"].value_counts("Khan")]

popular_vote = [election_["Candidate"].value_counts()]        


# In[115]:


election_winner = election_["Candidate"].mode(0)
winner = election_winner[0]
print(winner)


# In[131]:


print("Total votes: " + str(len(unique_votes)))
print("Vote Percentages: ")
print(str(vote_percentage))
print("Popular Vote: ")
print(str(popular_vote))
print("Winner: " + str(winner)) 


# In[134]:


with open(election_analysis, "w", newline="") as ea:
    writer = csv.writer(ea)
    writer.writerow(["Total votes: " + str(len(unique_votes))])
    writer.writerow(["Vote Percentages: "])
    writer.writerow([str(vote_percentage)])
    writer.writerow(["Popular Vote: "])
    writer.writerow([str(popular_vote)])
    writer.writerow(["Winner: " + str(winner)])


# In[ ]:




