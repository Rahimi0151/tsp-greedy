import constants
import math

class TSP:

    __coordinate_x = []
    __coordinate_y = []
    __city_name = []
    __weighted_graph = []
    __visited_cities = []
    __total_distance = 0

    def get_visited_cities(self):
        return self.__visited_cities

    def get_total_distance(self):
        return self.__total_distance

    def __split_to_three_arrays(self , text):
        splited_text = text.split("\n")                 #splitting every row

        for i in range(len(splited_text[0:100])) :      #putting every piece of data in the right place
            self.__city_name.append(int(splited_text[i].split(" ")[0]))
            self.__coordinate_x.append(float(splited_text[i].split(" ")[1]))
            self.__coordinate_y.append(float(splited_text[i].split(" ")[2]))

    def __read_data(self , file_name):
        text = open( file_name , "r").read()
        cleaned_text = text[187:-3]                         #removing metadata
        self.__split_to_three_arrays(cleaned_text)

    def __caculate_direct_distance(self ,coordinate):
        return math.sqrt( ( coordinate["origin_x"] - coordinate["destination_x"] )**2 + ( coordinate["origin_y"] - coordinate["destination_y"] )**2 )
    
    def __create_graph_from_coordinates(self):                                 #converting coordinates to graph
        temp = []                                           #to store a row of graph
        temp_coordinate = {}
        
        for i in range(len(self.__city_name)):
            temp = []
            for j in range(len(self.__city_name)):
                temp_coordinate["origin_x"] = self.__coordinate_x[i]
                temp_coordinate["origin_y"] = self.__coordinate_y[i]
                temp_coordinate["destination_x"] = self.__coordinate_x[j]
                temp_coordinate["destination_y"] = self.__coordinate_y[j]
                temp.append(self.__caculate_direct_distance(temp_coordinate))
            self.__weighted_graph.append(temp)

    def __find_where_to_start(self):
        first_city = 0
        least_distance = constants.MAX_INT
        for i in range(len(self.__weighted_graph)):
            for j in range(len(self.__weighted_graph)):
                if self.__weighted_graph[i][j] == 0:
                    continue
                if self.__weighted_graph[i][j] < least_distance:
                    first_city = i+1
                    least_distance = self.__weighted_graph[first_city-1][j]
        self.__visited_cities.append(first_city)

    def find_tour(self):
        current_city = self.__visited_cities[0]                  #to store which city we are currently in

        while ( len(self.__visited_cities) != len(self.__weighted_graph) ) :
            nearest_city = current_city
            nearest_city_distance = constants.MAX_INT

            for i in range(len(self.__weighted_graph)):
                if i+1 in self.__visited_cities or i+1 == current_city:
                    continue
                if self.__weighted_graph[current_city-1][i] < nearest_city_distance:
                    nearest_city = i + 1
                    nearest_city_distance = self.__weighted_graph[current_city-1][i]
            current_city = nearest_city
            self.__visited_cities.append(current_city)
            self.__total_distance += nearest_city_distance

    def __init__(self , file_name):
        self.__read_data(file_name)
        self.__create_graph_from_coordinates()
        self.__find_where_to_start()
