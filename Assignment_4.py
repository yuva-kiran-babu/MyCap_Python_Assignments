def most_frequent(string):

    this_dict={}   
    for i in string:
        keys=this_dict.keys()
        if i not in keys:
            this_dict[i]=1
        else:
            this_dict[i]+=1
    
    sorted_this_dict=sorted(this_dict.items(), key=lambda x:x[1], reverse=True)
    converted_dict=dict(sorted_this_dict)
   
    return converted_dict
        
     

print(most_frequent("mississippi"))

