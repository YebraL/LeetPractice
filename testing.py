# get the d of the circle
circle = 3.14 * r^2

def Get_area( diameter ):
    radius = diameter / 2
    area_circle = 3.14 * radius^2
    return area_circle

# recive the array of int
# return the sum from the array

#  (last * (last + 1)) / 2 ==> Gaussian
def get_sum( number_list ):
    
    sum_total = 0
    
    for number in number_list:
        sum_total += number
        
    return sum_total

# set any properties to a node 
# Container = {}

def find_cycle( node_list ):
    
    if node_list == None:
        return False
    else:
        if node_list.visited == True:
            return True
        else:
            node_list.visited = True
            
        if find_cycle( node_list.left ) == True:
            return True
        if find_cycle( node_list.right ) == True:
            return True
        return False
        

