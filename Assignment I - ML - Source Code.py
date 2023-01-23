#!/usr/bin/env python
# coding: utf-8

# In[4]:


import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sorts age list in ascending order by default
ages.sort()
print ("Sorted age:", ages)
# Minimum age
print ("Min:", min(ages))
# Maximum age
print ("Max:", max(ages))
# Adding again min and max values
ages.append(min(ages))
ages.append(max(ages))
print ("Added min and max values again:",ages) 
# Median
mdn_age = statistics.median(ages) 
print ("Median:", mdn_age)
# Average age
average= sum(ages)/len(ages) 
print ("Avg = ", average)
# Range
rng=max(ages)-min(ages) 
print ("Range = ", rng)


# In[7]:


# Dog dictionary is created with given key and values
dog = {'name':'Tommy','color':'white','breed':'husky','legs':'4','age':'2'}
print ("Dog Dictionary Created:",dog)
# Student dictionary is created with given key and values
student = {'first_name':'Kalyan','last_name':'Badeti','Gender':'Male','age':'26','marital_status':'single',
'skills':'sportsperson','Country':'India','City':'Hyderabad','Address':'1/148'} 
print ("Student Dictionary Created:",student)
# Create another dictionary for skills
skills = {'sportsperson':'1','singer':'2','coder':'3'} 
print ("Skills Dictionary Created:",skills) 
# Find the length of student dictionary
print ("Length of student:", len(student))
# Check the datatype of skills
print ("Datatype of skills:",type(skills))
# Get values of skills dictionary
print ("Values of skills:",skills.values())
# Add one item to skills
skills['artist'] = 4
print ("New skill added:",skills)
# Get dog and student key and values
print ("Dog keys:",dog.keys())
print ("Student values:",student.values())


# In[9]:


my_sisters = ('Mounica', 'Durga','Pavani','Ayesha') 
my_brothers = ('Sriman','Sriram','Prasad','Santosh')
# Create another tuple as siblings and join the sister’s and brother’s tuple
siblings = my_sisters + my_brothers
# Displays siblings’ output and length of siblings
print("Siblings:", siblings) 
print("Length of Siblings:", len(siblings))
# Create another tuple as family_members and add father and mother name to it
family_members = siblings + ('Srinivas','Vijaya') 
# Displays family_members output 
print("Family_members:",family_members)


# In[15]:


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} 
print("Length of it_companies:", len(it_companies))
#Add twitter
it_companies.add('Twitter')
print("After adding another item:",it_companies)
#Add multiple it_companies 
it_companies.update({'Infosys','Capgemini','Wipro','TCS'}) 
print("After adding multiple items:",it_companies) 
#Remove
it_companies.remove('TCS')
print("After removing one company:",it_companies)
#Discard
it_companies.discard('TCS')
print("After discarding company:",it_companies)
#Discard doesn't raise any error if any item is not present in the set #Join A & B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("Join A and B:", A.union(B))
#Intersection
print("Intersection of A and B:", A.intersection(B))
#Subset
print("Subset of A and B:", A.issubset(B))
#Disjoint
print("Disjoint:", A.isdisjoint(B))
#Convert list to set
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Converting list to set:", set(age))
#Length of set
print("Length of set:",len(set(age)))
#Length of list
print("Length of list:",len(age))
#Symmetric diff- returns values which are not in common with other set 
print("Symmetric diff:",A.symmetric_difference(B))
#delete set 
A.clear() 
print(A) 
B.clear()
print(B)


# In[26]:


# Initialise r where r value can be read from user inpt
r = int(input("enter r:"))
# Calculate area of circle and circumference of circle
_area_of_circle = 3.14*r*r
_circum_of_circle = 2*3.14*r
# Display area of circle and circumference of circle 
print("Area of Circle:",_area_of_circle) 
print("Circumference of Circle:",_circum_of_circle)


# In[27]:


st = "I am a teacher and I love to inspire and teach people"
# Use split method to separate the words and set to get the unique values
spt=set(st.split(" ")) 
print(spt)
print ("Length:",len(spt))


# In[45]:


a= "Name\t Age\t Country\t City\t\nKalyan   25\t USA\t         Kansas" 
print(a)


# In[15]:


#Using String format method
print(f'radius = 10') 
print(f'area = 3.14*radius**2')
print(f'"The area of circle with radius {r} is {3.14*r*r} meters square"')


# In[24]:


#Creating a list(L1) for weights(lbs) of N students
L1=[int(num) for num in input().split(" ")]
#Creating another list called W_kg
W_kg=[]
#Using for loop to iterate the values and appending the list
for i in L1: 
    W_kg.append(round(i/2.205,2))
#Displaying the values in kgs after conversion
print ("Values are:",W_kg)


# In[ ]:




