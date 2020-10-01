from queue import PriorityQueue
import json

class Graph():

    def __init__(self):
        super().__init__()

        with open('cities.json', encoding='utf-8') as json_file:
            self.adjacency_list = json.load(json_file)

    # dijkstra
    def get_path(self, source, destiny):
        pq = PriorityQueue()
        dist = dict()
        
        for i in self.adjacency_list:
            dist[i] = (999999, '')

        dist[source] = (0, source)
        pq.put((0, source))
        
        while not pq.empty():
            d, u = pq.get()
            for dest in self.adjacency_list[u]:
                w = self.adjacency_list[u][dest]
                if(dist[dest][0] > d + w):
                    dist[dest] = (d + w, u)
                    pq.put((dist[dest][0], dest))
                    
        path = [] 
        d = destiny
        path.append(d)
        
        
        trip_fare = dist[d][0]
        
        while path[-1] != source:
            path.append(dist[d][1])
            d = dist[d][1]
        path.reverse()

        return path, trip_fare
