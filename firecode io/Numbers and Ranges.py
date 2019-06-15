'''
Given a sorted list and an input number as inputs, write a function to return a Range object, consisting of the indices of the first and last occurrences of the input number in the list. Check out the Use Me section to examine the structure of the Range class.

Note: The List can have duplicate numbers. The indices within the Range object should be zero based.

Examples:
Input List  : [1,2,5,5,8,8,10]
Input Number : 8
Output : [4,5]

Input List  : [1,2,5,5,8,8,10]
Input Number : 2
Output : [1,1]
'''
def find_range(input_list,input_number):
    a=[]
    for i in range(len(input_list)):
        if input_list[i]==input_number:
            a.append(i)
    if len(a)==1:
        return a*2
    return a
print(find_range([1,2,5,5,8,8,10],8))
print(find_range([1,2,5,5,8,8,10],2))
