 # write a program to output the skyline formed by input buildings collectively
 #input:  [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 
 #output: [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]



def merge(left, right):
    left_indx = 0
    right_indx = 0
    result = []
    h1 = None
    h2 = None

    while i<len(left) and j<len(right):
        if left[left_indx][0] < right[right_indx][0] :
            h1 = left[left_indx][1]
            new = [left[left_indx][0], max(h1, h2)]
            if result == [] or result[-1][1] != new[1]:
                result.append(new)
            left_indx +=1
         if left[left_indx][0] > right[right_indx][0] :
            h2 = right[right_indx][1]
            new = [right[right_indx][0], max(h1, h2)]
            if result == [] or result[-1][1] != new[1]:
                result.append(new)
            right_indx +=1

        else:
            h1 = left[left_indx][1]
            h2 = right[right_indx][1]
            new = [right[right_indx][0], max(h1,h2)]
            if result == [] or result[-1][1] != new[1]:
                result.append(new)
            left_indx +=1
            right_indx +=1
            
        while i<len(left):
            if result==[] or result[-1][1]!=left[i][1]:
                result.append(left[i][:])
            i+=1
        while j<len(right):
            if result==[] or result[-1][1]!=right[j][1]:
                result.append(right[j][:])
            j+=1
            
        return result

def skyline(building):
    
    if buildings == []:
        return []

    if len(buildings) == 1:
                #start          #y                    #end            #y
        return [[buildings[0][0],buildings[0][2]], [buildings[0][1], 0]]

    mid = (len(buildings)-1)/2
    left = buildings[:mid]
    right = buildings[mid:]
    return merge(left, right)







print skyline([2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8]])