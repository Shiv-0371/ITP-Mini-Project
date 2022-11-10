#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Q1. Create a Dictionary of lists to store the information of shipments given in the table


# In[8]:


import datetime
shipment_list = [{"shipment_id": 101, "sender": 1, "receiver": 3, "start_date": datetime.datetime(2020, 3, 14), "delivery_date": datetime.datetime(2020, 3, 25), "sender_location": "Area1", "receiver_location": "Area6", "delivery_status": "Delivered", "shipping_cost": 198},
                 {"shipment_id": 102, "sender": 4, "receiver": 1, "start_date": datetime.datetime(2020, 6, 18), "delivery_date": datetime.datetime(
                     2020, 7, 9), "sender_location": "Area2", "receiver_location": "Area4", "delivery_status": "Delivered", "shipping_cost": 275},
                 {"shipment_id": 103, "sender": 1, "receiver": 3, "start_date": datetime.datetime(2020, 12, 1), "delivery_date": None, "sender_location": "Area5", "receiver_location": "Area1", "delivery_status": "In-Transit", "shipping_cost": 200},
                 {"shipment_id": 104, "sender": 1, "receiver": 3, "start_date": datetime.datetime(2020, 6, 23), "delivery_date": datetime.datetime(
                     2020, 6, 25), "sender_location": "Area1", "receiver_location": "Area4", "delivery_status": "Delivered", "shipping_cost": 314},
                 {"shipment_id": 105, "sender": 1, "receiver": 3, "start_date": datetime.datetime(2020, 8, 29), "delivery_date": datetime.datetime(
                     2020, 9, 20), "sender_location": "Area5", "receiver_location": "Area3", "delivery_status": "Delivered", "shipping_cost": 275},
                 {"shipment_id": 106, "sender": 1, "receiver": 3, "start_date": datetime.datetime(2020, 6, 28), "delivery_date": None, "sender_location": "Area3", "receiver_location": "Area1", "delivery_status": "In-Transit", "shipping_cost": 270}]
print(shipment_list)


# In[ ]:


#Q2  Create a Dictionary to store the information of clients given in the table.


# In[10]:


dict_client = { 1 : "Phillip"},{2:"Omega"},{ 3 : "Ramya"},{4:"Romesh"},{5:"John"}
print(dict_client)


# In[ ]:


# Q3. Write a code to replace clients' IDs with their respective names in the shipment dictionary using a loop and dictionary comprehension.


# In[43]:


d1={101:{'Sender':1,'Receiver':3,'Start date':'14-03-2020','Delivery date':'25-03-2020','Sender location':'Area 1','Receiver location':'Area 6','Delivery status':'Delivered','Shipping cost':198}, 102:{'Sender':4,'Receiver':1,'Start date':'18-06-2020','Delivery date':'09-07-2020','Sender location':'Area 2','Receiver location':'Area 4','Delivery status':'Delivered','Shipping cost':275}, 103:{'Sender':2,'Receiver':3,'Start date':'01-12-2020','Delivery date':'Null','Sender location':'Area 5','Receiver location':'Area 1','Delivery status':'In Transit','Shipping cost':200}, 104:{'Sender':1,'Receiver':5,'Start date':'23-06-2020','Delivery date':'25-06-2020','Sender location':'Area 1','Receiver location':'Area 4','Delivery status':'Delivered','Shipping cost':314}, 105:{'Sender':3,'Receiver':4,'Start date':'29-08-2020','Delivery date':'10-09-2020','Sender location':'Area 5','Receiver location':'Area 3','Delivery status':'Delivered','Shipping cost':275}, 106:{'Sender':5,'Receiver':2,'Start date':'28-06-2020','Delivery date':'Null','Sender location':'Area 3','Receiver location':'Area 1','Delivery status':'In Transit','Shipping cost':270}}

d2 = {1:'Phillip',2:'Omega',3 :'Ramya',4:'Romesh',5:'John'}
#  dictionary comprehensio
result = {key:{k: d2[v] if k in ('Sender', 'Receiver') else v for k,v in value.items()} for key, value in d1.items()}
print(result)



# In[44]:


d1={101:{'Sender':1,'Receiver':3,'Start date':'14-03-2020','Delivery date':'25-03-2020','Sender location':'Area 1','Receiver location':'Area 6','Delivery status':'Delivered','Shipping cost':198}, 102:{'Sender':4,'Receiver':1,'Start date':'18-06-2020','Delivery date':'09-07-2020','Sender location':'Area 2','Receiver location':'Area 4','Delivery status':'Delivered','Shipping cost':275}, 103:{'Sender':2,'Receiver':3,'Start date':'01-12-2020','Delivery date':'Null','Sender location':'Area 5','Receiver location':'Area 1','Delivery status':'In Transit','Shipping cost':200}, 104:{'Sender':1,'Receiver':5,'Start date':'23-06-2020','Delivery date':'25-06-2020','Sender location':'Area 1','Receiver location':'Area 4','Delivery status':'Delivered','Shipping cost':314}, 105:{'Sender':3,'Receiver':4,'Start date':'29-08-2020','Delivery date':'10-09-2020','Sender location':'Area 5','Receiver location':'Area 3','Delivery status':'Delivered','Shipping cost':275}, 106:{'Sender':5,'Receiver':2,'Start date':'28-06-2020','Delivery date':'Null','Sender location':'Area 3','Receiver location':'Area 1','Delivery status':'In Transit','Shipping cost':270}}

d2 = {1:'Phillip',2:'Omega',3 :'Ramya',4:'Romesh',5:'John'}
#using a loop
result = {}
for key, value in d1.items():
    new_value = {k: d2[v] if k in ('Sender', 'Receiver') else v for k,v in value.items()}
    result[key] = new_value
        
print(result)


# In[ ]:


#Q4 Print all shipment details that are sent by Phillip


# In[106]:


dict1 = {101: {'Sender': 'Phillip', 'Receiver': 'Ramya', 'Start date': '14-03-2020', 'Delivery date': '25-03-2020', 'Sender location': 'Area 1', 'Receiver location': 'Area 6', 'Delivery status': 'Delivered', 'Shipping cost': 198}, 102: {'Sender': 'Romesh', 'Receiver': 'Phillip', 'Start date': '18-06-2020', 'Delivery date': '09-07-2020', 'Sender location': 'Area 2', 'Receiver location': 'Area 4', 'Delivery status': 'Delivered', 'Shipping cost': 275}, 103: {'Sender': 'Omega', 'Receiver': 'Ramya', 'Start date': '01-12-2020', 'Delivery date': 'Null', 'Sender location': 'Area 5', 'Receiver location': 'Area 1', 'Delivery status': 'In Transit', 'Shipping cost': 200}, 104: {'Sender': 'Phillip', 'Receiver': 'John', 'Start date': '23-06-2020', 'Delivery date': '25-06-2020', 'Sender location': 'Area 1', 'Receiver location': 'Area 4', 'Delivery status': 'Delivered', 'Shipping cost': 314}, 105: {'Sender': 'Ramya', 'Receiver': 'Romesh', 'Start date': '29-08-2020', 'Delivery date': '10-09-2020', 'Sender location': 'Area 5', 'Receiver location': 'Area 3', 'Delivery status': 'Delivered', 'Shipping cost': 275}, 106: {'Sender': 'John', 'Receiver': 'Omega', 'Start date': '28-06-2020', 'Delivery date': 'Null', 'Sender location': 'Area 3', 'Receiver location': 'Area 1', 'Delivery status': 'In Transit', 'Shipping cost': 270}}
phillips = list(filter(lambda value: value['Sender'] == 'Phillip',dict1.values()))
print(phillips)


# In[ ]:


# Q5  Print all shipment details that are received by Ramya


# In[109]:


dict1 = {101: {'Sender': 'Phillip', 'Receiver': 'Ramya', 'Start date': '14-03-2020', 'Delivery date': '25-03-2020', 'Sender location': 'Area 1', 'Receiver location': 'Area 6', 'Delivery status': 'Delivered', 'Shipping cost': 198}, 102: {'Sender': 'Romesh', 'Receiver': 'Phillip', 'Start date': '18-06-2020', 'Delivery date': '09-07-2020', 'Sender location': 'Area 2', 'Receiver location': 'Area 4', 'Delivery status': 'Delivered', 'Shipping cost': 275}, 103: {'Sender': 'Omega', 'Receiver': 'Ramya', 'Start date': '01-12-2020', 'Delivery date': 'Null', 'Sender location': 'Area 5', 'Receiver location': 'Area 1', 'Delivery status': 'In Transit', 'Shipping cost': 200}, 104: {'Sender': 'Phillip', 'Receiver': 'John', 'Start date': '23-06-2020', 'Delivery date': '25-06-2020', 'Sender location': 'Area 1', 'Receiver location': 'Area 4', 'Delivery status': 'Delivered', 'Shipping cost': 314}, 105: {'Sender': 'Ramya', 'Receiver': 'Romesh', 'Start date': '29-08-2020', 'Delivery date': '10-09-2020', 'Sender location': 'Area 5', 'Receiver location': 'Area 3', 'Delivery status': 'Delivered', 'Shipping cost': 275}, 106: {'Sender': 'John', 'Receiver': 'Omega', 'Start date': '28-06-2020', 'Delivery date': 'Null', 'Sender location': 'Area 3', 'Receiver location': 'Area 1', 'Delivery status': 'In Transit', 'Shipping cost': 270}}
Ramyas = list(filter(lambda value: value['Receiver'] == 'Ramya',dict1.values()))
print(Ramyas)


# In[ ]:


# Q6 Print all shipments which are in 'In-Transit' status


# In[114]:


dict1 = {101: {'Sender': 'Phillip', 'Receiver': 'Ramya', 'Start date': '14-03-2020', 'Delivery date': '25-03-2020', 'Sender location': 'Area 1', 'Receiver location': 'Area 6', 'Delivery status': 'Delivered', 'Shipping cost': 198}, 102: {'Sender': 'Romesh', 'Receiver': 'Phillip', 'Start date': '18-06-2020', 'Delivery date': '09-07-2020', 'Sender location': 'Area 2', 'Receiver location': 'Area 4', 'Delivery status': 'Delivered', 'Shipping cost': 275}, 103: {'Sender': 'Omega', 'Receiver': 'Ramya', 'Start date': '01-12-2020', 'Delivery date': 'Null', 'Sender location': 'Area 5', 'Receiver location': 'Area 1', 'Delivery status': 'In Transit', 'Shipping cost': 200}, 104: {'Sender': 'Phillip', 'Receiver': 'John', 'Start date': '23-06-2020', 'Delivery date': '25-06-2020', 'Sender location': 'Area 1', 'Receiver location': 'Area 4', 'Delivery status': 'Delivered', 'Shipping cost': 314}, 105: {'Sender': 'Ramya', 'Receiver': 'Romesh', 'Start date': '29-08-2020', 'Delivery date': '10-09-2020', 'Sender location': 'Area 5', 'Receiver location': 'Area 3', 'Delivery status': 'Delivered', 'Shipping cost': 275}, 106: {'Sender': 'John', 'Receiver': 'Omega', 'Start date': '28-06-2020', 'Delivery date': 'Null', 'Sender location': 'Area 3', 'Receiver location': 'Area 1', 'Delivery status': 'In Transit', 'Shipping cost': 270}}
In_Transit = list(filter(lambda value: value[-2] == 'In-Transit',dict1.values()))
print(In_Transit)


# In[ ]:


# Q7 Print all shipments which are delivered within 7 days of courier Start date


# In[74]:


from datetime import datetime
a = {101: {'Sender': 'Phillip', 'Receiver': 'Ramya', 'Start date': '14-03-2020', 'Delivery date': '25-03-2020', 'Sender location': 'Area 1', 'Receiver location': 'Area 6', 'Delivery status': 'Delivered', 'Shipping cost': 198}, 102: {'Sender': 'Romesh', 'Receiver': 'Phillip', 'Start date': '18-06-2020', 'Delivery date': '09-07-2020', 'Sender location': 'Area 2', 'Receiver location': 'Area 4', 'Delivery status': 'Delivered', 'Shipping cost': 275}, 103: {'Sender': 'Omega', 'Receiver': 'Ramya', 'Start date': '01-12-2020', 'Delivery date': 'Null', 'Sender location': 'Area 5', 'Receiver location': 'Area 1', 'Delivery status': 'In Transit', 'Shipping cost': 200}, 104: {'Sender': 'Phillip', 'Receiver': 'John', 'Start date': '23-06-2020', 'Delivery date': '25-06-2020', 'Sender location': 'Area 1', 'Receiver location': 'Area 4', 'Delivery status': 'Delivered', 'Shipping cost': 314}, 105: {'Sender': 'Ramya', 'Receiver': 'Romesh', 'Start date': '29-08-2020', 'Delivery date': '10-09-2020', 'Sender location': 'Area 5', 'Receiver location': 'Area 3', 'Delivery status': 'Delivered', 'Shipping cost': 275}, 106: {'Sender': 'John', 'Receiver': 'Omega', 'Start date': '28-06-2020', 'Delivery date': 'Null', 'Sender location': 'Area 3', 'Receiver location': 'Area 1', 'Delivery status': 'In Transit', 'Shipping cost': 270}}


for i, j in a.items():
    diff = j[3]-j[2]
    if diff.days > 7:
        print(j)



# In[ ]:


# Q8 Print all shipments which are delivered after 15 days of courier start date or have not yet been delivered.


# In[99]:


a = {101: {'Sender': 'Phillip', 'Receiver': 'Ramya', 'Start date': '14-03-2020', 'Delivery date': '25-03-2020', 'Sender location': 'Area 1', 'Receiver location': 'Area 6', 'Delivery status': 'Delivered', 'Shipping cost': 198}, 102: {'Sender': 'Romesh', 'Receiver': 'Phillip', 'Start date': '18-06-2020', 'Delivery date': '09-07-2020', 'Sender location': 'Area 2', 'Receiver location': 'Area 4', 'Delivery status': 'Delivered', 'Shipping cost': 275}, 103: {'Sender': 'Omega', 'Receiver': 'Ramya', 'Start date': '01-12-2020', 'Delivery date': 'Null', 'Sender location': 'Area 5', 'Receiver location': 'Area 1', 'Delivery status': 'In Transit', 'Shipping cost': 200}, 104: {'Sender': 'Phillip', 'Receiver': 'John', 'Start date': '23-06-2020', 'Delivery date': '25-06-2020', 'Sender location': 'Area 1', 'Receiver location': 'Area 4', 'Delivery status': 'Delivered', 'Shipping cost': 314}, 105: {'Sender': 'Ramya', 'Receiver': 'Romesh', 'Start date': '29-08-2020', 'Delivery date': '10-09-2020', 'Sender location': 'Area 5', 'Receiver location': 'Area 3', 'Delivery status': 'Delivered', 'Shipping cost': 275}, 106: {'Sender': 'John', 'Receiver': 'Omega', 'Start date': '28-06-2020', 'Delivery date': 'Null', 'Sender location': 'Area 3', 'Receiver location': 'Area 1', 'Delivery status': 'In Transit', 'Shipping cost': 270}}


for i, j in a.items():
    diff = j[3]-j[2]
    if diff.days > 15:
        print(j)


# In[ ]:


# Q9 The graph is used to represent networks of pickup and delivery areas. Consider below the graph diagram for given area locations in the table.


# In[67]:


def retunpath(startindex):
    possible = []
    for x in range(0, len(route[startindex-1])):
        if(route[startindex-1][x] == 1):
            possible.append(x+1)
    return possible
route = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0]
]
level = 1 #level 
start = 1 # starting node
end = 5 # which destination you want to reach
possiblepath = [] # returns all the possible node from which we can travel
visitednode = {}  #save the path against level
flowstart = [] #in which  flow we are moving
temp = []
front = True # going down and up
while(1):
    if(front):
        flowstart.append(start)
    possiblepath = retunpath(start).copy()
    if(not front):
        for y in visitednode[level]:
            temp = [y[0], y[1]]
            if(temp in visitednode[level] and (possiblepath.count(y[1]))):
                possiblepath.pop(possiblepath.index(y[1]))
    temp = []
    for x in possiblepath:  
        if(flowstart.count(x) < 1):
            temp.append([start, x])
            if(end == x):
                print("pathfound", flowstart+[x])
            try:
                visitednode[level].append([start, x])
            except:
                visitednode[level]=temp
            start = x
            level = level+1
            front=True
            break
    else:
        print("back")
        flowstart.pop()
        start = flowstart[len(flowstart)-1]
        level = level-1
        front=False
        if(flowstart == [start]):
            if(len(visitednode[level]) == len(retunpath(start))):
                break


# In[ ]:




