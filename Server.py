
# coding: utf-8

# In[4]:


import socket, pickle

import os

def msort(x):
    
    if len(x) < 2:
        return x
    
    result = []     
    mid = int(len(x) / 2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
            
    result += y
    result += z
    return result

def main():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    PORT = 12389

    ip = socket.gethostbyname(socket.gethostname())

    address = (ip , PORT) 

    server.bind(address)
    
    server.listen(3)
    
    conn, addr = server.accept()
    
    print 'Connected by', addr 
    
    while True:
        
        data = conn.recv(4096)
        
        if not data: break
            
        sorted_data = []
            
        for item in pickle.loads(data):
            
            temp_sorted = msort(item.split())
            
            temp_str = " ".join(temp_sorted)
            
            sorted_data.append(temp_str)
               
        conn.send(pickle.dumps(sorted_data))
        
if __name__ == "__main__":
    
    main()

