import constants

def read_data(city_name , coordinate_x , coordinate_y):
    text = open("ireland.tsp.txt" , "r").read()         #reading file
    cleaned_text = text[187:-3]                         #removing metadata
    splited_text = cleaned_text.split("\n")             #splitting every row

    for i in range(len(splited_text[0:100])) :           #putting every piece of data in the right place
        city_name.append(int(splited_text[i].split(" ")[0]))
        coordinate_x.append(float(splited_text[i].split(" ")[1]))
        coordinate_y.append(float(splited_text[i].split(" ")[2]))

def create_graph(w):                                    #converting coordinates to graph
    temp = []                                           #to store a row of graph
    tempx1 = 0
    tempy1 = 0
    tempx2 = 0
    tempy2 = 0
    
    for i in range(len(city_name)):
        temp = []
        for j in range(len(city_name)):
            tempx1 = coordinate_x[i]
            tempy1 = coordinate_y[i]
            tempx2 = coordinate_x[j]
            tempy2 = coordinate_y[j]
            temp.append( ( tempx1 - tempx2 )**2 + ( tempy1 - tempy2 )**2 )
        w.append(temp)

def find_tour(w , city_name , visited_cities , total_distance):
    visited_cities = [1]                                #to store cities we already visited
    current_city = 1                                    #to store which city we are currently in
    nearest_city = current_city                         #to store name of the nearest city
    nearest_city_distance = constants.MAX_INT           #to store distance to the nearest city
    total_distance = 0                                  #to store how much we have came so far 

    while ( len(visited_cities) != len(w) ) :
        nearest_city = current_city
        nearest_city_distance = constants.MAX_INT

        for i in range(len(w)):
            if i+1 in visited_cities:
                continue
            if i+1 == current_city:
                continue
            if w[current_city-1][i] < nearest_city_distance:
                nearest_city = i + 1
                nearest_city_distance = w[current_city-1][i]
        current_city = nearest_city
        visited_cities.append(current_city)
        total_distance = total_distance + nearest_city_distance

    print(total_distance)

city_name = []
coordinate_x = []
coordinate_y = []
w = []                                                  #graph
path = [1]                                              #to store the path
total_distance = 0                                      #to store total distance we have to go

read_data(city_name , coordinate_x , coordinate_y)
create_graph(w)
find_tour(w , city_name , path , total_distance)

z = input()









# used_nodes = [0]                                        #a random node as an start point
# nearest_city = 0                                        #temp data to have name of nearest city
# min_distance = constants.INFINITE                       #temp data to have distance to the nearest city
#
# while not (len(used_nodes) == len(city_name)):
#     nearest_city = 0
#     min_distance = constants.INFINITE
#
#     for i in range(len(used_nodes)-1):
#
#         for j in range(len(city_name)-1):
#             if city_name[j] in used_nodes:
#                 continue
#             if min_distance < w[i][j]:
#                 min_distance = w[i][j]
#                 nearest_city = city_name[j+1]
#         used_nodes.append(nearest_city)
# print(used_nodes)


