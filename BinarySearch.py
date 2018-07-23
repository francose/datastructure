"""
July 15 2018
Sadik Erisen
Data structure practice - 1

Binary Search
Duplicate removal in python lists

"""


data1 = [0, 1, 2,2, 8, 13,13, 17, 19, 32,32, 42]
data2 = [0, 1, 24, 38, 113, 127, 19, 32, 42]
finaldata = data1 + data2

#Removes the duplicate values
def remove_duplicates(test):
    mylist=[]
    seen = set()
    for x in test:
        if(x not in seen):
            mylist.append(x)
            seen.add(x)
    return mylist


# gets user input
def get_user_input(search):
    return search


# if our input is empty or we only have a single subscript and that subscript is not the item that we are search for returns false
def search_func(arr, item):
    if (len(arr) == 0 or len(arr) == 1 and arr[0] != item):
        return False
    mid = arr[len(arr)/2]
    if (item == mid):
        return True
    if(item < mid):
        return search_func(arr[:len(arr)/2],item)
    if(item > mid):
        return search_func(arr[len(arr)/2+1:],item)

#main loop
def main():
    filtered = remove_duplicates(finaldata)
    print('please enter a number : \n\n')
    search = input()
    target  = get_user_input(search)
    traverse = search_func(filtered, target)
    print traverse ,"Found ! \t", filtered



if __name__ == '__main__':
    main()
