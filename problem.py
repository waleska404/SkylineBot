buildings = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25), (19,18,22), (23,13,29),
(24,4,28),(56,21,58)]
  
edges = []
edges.extend([building[0],building[2]] for building in buildings)
print(edges)
edges = sorted(sum(edges,[])) #sorting and flatening the list of building edges
print(edges)
 
current = 0
points = []
  
for i in edges:
  active = []
  active.extend(building for building in buildings if (building[0] <= i and building[2] > i)) 
  #current observed point is within borders of these buildings (active buildings)
  print(i,active)
  if not active: 
    #if there is no active buildings, highest point is 0
    current = 0
    points.append((i,0))
    continue
  max_h = max(building[1] for building in active)
  if max_h != current:
    
    #if current highest point is lower then highest point of current active buildings change current highest point
    current = max_h
    points.append((i,max_h))
     
print(points)
l = []
for index, item in enumerate(points):
  if index < len(points)-1:
    #print('ACTUAL:')
    #print(item)
    a = item[0]
    b = item[1]
    #print('SIGUIENTE')
    #print(points[index+1])
    elem = points[index+1]
    c = elem[0]
    if b != 0:
        l.append((a,b,c))

print(l)  
