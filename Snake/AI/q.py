def end_dist(start,end):
    (x1, y1) = start
    (x2, y2) = end
    return abs(x1 - x2) + abs(y1 - y2)

p = (25,35)
q = (25,30)

print(end_dist(p,q))
