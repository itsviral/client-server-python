
# coding: utf-8

# In[1]:


import socket, pickle

with open('client1.inputdat.txt', 'r') as f:
    fline = f.readlines()
    
    data = []
    
    for lines in fline:
        
        data.append(lines)
        
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 12389

ip = socket.gethostbyname(socket.gethostname())

address = (ip , PORT) 

server.connect(address)

data_string = pickle.dumps(data)

server.send(data_string)

data = server.recv(4096)

sorted_arr = pickle.loads(data)


for item in sorted_arr:
    
    print(item)

