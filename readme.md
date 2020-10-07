# Purpose of algorithm
The purpose of this algorithm is to allow the user, to change elements within a list. Search if an element exists within a list, and a list within a list.   
As well as, being able to search for the value of an element behind a key for a dictionary. Furthermore, having the ability to replace the value with something of use.  
  
Currently the __readme.md__ file has documentation(this term is relative) on the only algorithm I wrote, which is LSR(List search replace). And DS (Dictionary Search), therefore, this readme will only contain documentation for the aforementioned algorithms.    
  
Once I have written more algorithms. Each individual algorithm will be contained in it's on folder. With it's own readme file, outlining its use, and limitations.
  
# A few features:
1. Able to search, and replace elements within a list. Even if the list is two layers deep. Meaning it has a list inside a list. While searching there will be return values. If you have a two layered list, it will return two values index1 and index2. Which will get you to that element, for you to replace it or change it.

2. Able to do the same to a dictionary of lists. And will also let you replace the value of the list, as the key and the index will be the return values for you to use.

# Known limitations:
1. The replace method is unable to change a specific element, if the overall data type of the list is mixed, such as a list of integers, strings, and doubles.  
Using the replace method will only be able to change the first element, and if it is a nested list, no elements will be affected. This **may potentially be incorrect** 
I am currently experimenting if you can scan the entire list, and change everything, thus, this may be a possible work in progress.

# Features to be added: 
1. Type casting an entire list to a specific data type. ie. Strings to integers. This option will be implemented where available.  
You don't expect to be able to cast a string into an integer, that doesn't make sense.

# Contributing
If you wish to contribute to this repository, feel free to do so under the __add ons__  
branch. Name the file after youself, and outline what you have done. When you commit.
