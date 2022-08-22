
def extract_min(Q, lst):
    min_dist = 1000
    min_node = "None"
    for x in range(len(lst)):
        if lst[x][1] in Q and lst[x][2] <= min_dist:
            min_dist = lst[x][2]
            min_node = lst[x][1]
    return min_node, min_dist
            
def get_node(node, lst):
    for x in range(len(lst)):
        if lst[x][1] == node[0]:
            return lst[x]

def Dijkstra(G, node, node1):
    SD = []
    V = []
    Q = [x for x in G.keys()]
    for x in G.keys():
        if x == node:
            SD.append((node,node,0))
        else:
            SD.append(("None",x,100))
    while len(Q) != 0:
        visiting, visiting_dist = extract_min(Q, SD)
        Q.remove(visiting)
        if visiting == node1: break
        if visiting not in V:
            V.append(visiting)
            for neighbor in G[visiting]:
                if get_node(neighbor, SD)[2] >= visiting_dist + neighbor[1]:   
                    SD.remove(get_node(neighbor, SD))
                    SD.append((visiting, neighbor[0], visiting_dist + neighbor[1]))  
    return SD


def getShortestPath(G, X, Y):
    SD = Dijkstra(G, X, Y)
    SD = sorted(SD[1:])
    
    backtrack = []
    while get_node(Y, SD):
        backtrack.append(Y)
        Y = get_node(Y, SD)[0]
    backtrack.append(Y)
    shortest_path = []
    for node in backtrack:
        for v in SD:
            if v[1] == node:
                shortest_path.append(v)
                break
    return shortest_path[::-1]



G = {'A':[('D',3),('B',5),('E',6)],
         'B':[('A',5),('C',6)],
         'C':[('B',6),('G',2),('D',10)],
         'D':[('A',3),('F',8),('C',10)],
         'E':[('A',6),('F',9)],
         'F':[('G',10),('E',9),('D',8)],
         'G':[('F',10),('C',2)],
         'H':[('I',7)],
         'I':[('H',7)]
        }
print("please select location from the list below:")
for i in G:
    print(i)

print()
start = str(input("please type your start location:")).upper()
destination = str(input("please type your destination:")).upper()
SP = getShortestPath(G, start, destination)
print()
print("path of travel is:", SP)
cost=SP[len(SP)-1][2]
if cost == 100:
    print("path from", start,"to", destination,"does not exist")
else:
    print("the shortest path from", start,"to", destination,"is", cost)

