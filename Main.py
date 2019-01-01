from TSP import TSP

tsp = TSP("ireland.tsp.txt")
tsp.find_tour()
print(tsp.get_visited_cities())
print(tsp.get_total_distance())
