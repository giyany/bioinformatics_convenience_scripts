import sys

##use dictionary on string
#arg 1 is the file containing strings to replace, arg 2 is the dict
            
##dictionary file. tab delimited, 2 rows
dict_file=sys.argv[2]

#open and read dictionary file
Sample_dict={}
with open(dict_file,"r") as data:
    #rows=(line.split('\n') for line in data)
    rows=(line.split('\t') for line in data)
    for row in rows:
        key=row[0]
        value=row[1].rstrip("\n")
        Sample_dict[key]=value
#print(Sample_dict)

#file to chance names in
change_file=open(sys.argv[1],"r")
tree_string=change_file.read()
#print(tree_string)
for key, value in Sample_dict.items():
#    print(str(key)+str(value))
    tree_string=tree_string.replace(key,value)
print(tree_string)

change_file=open(sys.argv[1],"w")
change_file.write(tree_string)
change_file.close()
