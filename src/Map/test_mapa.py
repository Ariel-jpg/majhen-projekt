from MapGenerator import Map
from Event import Event

m1 = Map(8, 8)

e1 = Event("1")
e2 = Event(2)

i = 0
j = 0
#for c in m1._list:
 #   k = 0
  #  for space in m1._list[i]:
   #     m1.assign_value(i, k, "M")
    #    k += 1
     #   j += 1
   # i += 1
m1.assign_event(0, 0, e1)
m1.assign_value(4, 4, "1")
m1.print_map()

