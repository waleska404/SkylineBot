
lim11=1
lim12=24

lim21 = 2
lim22 = 24
buildings1 = [(1,2,3),(4,1,8),(8,5,9),(10,4,11),(13,4,14),(16,2,17),(19,4,22),(22,3,24)]
buildings2 = [(2,3,5),(7,3,9),(10,3,12),(12,2,15),(15,2,18),(19,3,21),(22,2,24)]

edges1 = []
edges1.extend([building[0],building[2]] for building in buildings1)
edges1 = sorted(sum(edges1,[])) #sorting and flatening the list of building edges
#print(edges1)


edges2 = []
edges2.extend([building[0],building[2]] for building in buildings2)
edges2 = sorted(sum(edges2,[])) #sorting and flatening the list of building edges
#print(edges2)

limLeft = max(lim11, lim21)
limRight = min(lim12, lim22)

print('LIM LEFT RIGHT')
print(limLeft, limRight)
 
current = 0
points = []

edaux = edges1 + edges2
edaux = sorted(edaux)
#print(edaux)
edges = [edg for edg in edaux if(edg >= limLeft and edg <= limRight)]
edges = set(edges)
edges = list(edges)
print('EDGES')
print(edges)

buildings1bis = [b for b in buildings1 if((b[0] > limLeft and b[0] < limRight) or (b[2] > limLeft and b[2] < limRight) or (b[0] <= limLeft and b[2] >= limRight))]
buildings2bis = [b for b in buildings2 if((b[0] > limLeft and b[0] < limRight) or (b[2] > limLeft and b[2] < limRight) or (b[0] <= limLeft and b[2] >= limRight))]
buildings = buildings1bis + buildings2bis
print('BUILDINGS')
print(buildings)
  
for i in edges:
  active = []
  active.extend(building for building in buildings if ((building[0] <= i and building[2] > i) or (building[0] < i and building[2] > i)))
  #active.extend(building for building in buildings) 
  #current observed point is within borders of these buildings (active buildings)
  print('RONDA', i)
  print(i,active)
  if len(active) <= 1: 
    print('ENTRO EN NOT ACTIVE')
    #if there is no active buildings, highest point is 0
    current = 0
    points.append((i,0))
    continue
  min_h = min(building[1] for building in active)
  min_ed = i
  #for elems in active:
   #   if 
  print('MIN')
  print(min_h)
  print(current)
  if min_h != current:
    #if current highest point is lower then highest point of current active buildings change current highest point
    current = min_h
    print('APPEND')
    print((i,min_h))
    points.append((i,min_h))

print('POINTS:')
last = edges[-1]
points.append((last, 0))
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
