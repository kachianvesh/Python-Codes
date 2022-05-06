it={61:'abc', 62:'xyz',63:'pqr', 64:'lmn'}
print (it)                      #prints all dictionary values
print(it[63])                   #prints the respective key value
print(it.keys())                #prints all the keys of given dictionary
print(it.values())              #prints all the values of given dictionary
print(it.items())               #prints all the list of items in the dictionary
it['shiva']=123                 #Adding new element to the dictionary
print (it)                      #displaying new items in the dictionary
it[61]='kaalbairav'             #updating the value of a key-61
print (it.items())              #prints all the new updated items in the dictionary
print ("length of the dictioary :", len(it))    #Displays the length of IT

vce={101:'shiva', 102:'eshwar', 103:'bhairav'} #Taking new dictionary
print (vce)                     #printing the elements in the dictionary
del vce[101]                    #deletes a particular items in the dictionary
print (vce)
"""
vce.clear()                    #clears all the items in the dictionary
print (vce)                    #prints empty dictionary
del vce                        #it deletes the complete dictionary

"""
clge=vce.copy()                 #Copying the content of vce to clge               
print ("The new copy of clge is :", clge)  #Printing the new copied content

