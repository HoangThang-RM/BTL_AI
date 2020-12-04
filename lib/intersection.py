import math

# Find point closer to the starting point
def ClosestIntersection(cx, cy, radius, lineStart, lineEnd): #cx,cy is center point of the circle
    intersection1 = (0,0)
    intersection2 = (0,0)
    intersections,intersection1,intersection2 = FindLineCircleIntersections(cx, cy, radius, lineStart, lineEnd)

    if (intersections == 1):
        return intersection1 # one intersection

    if (intersections == 2):
        dist1 = Distance(intersection1, lineStart)
        dist2 = Distance(intersection2, lineStart)

        if (dist1 < dist2):
            return intersection1
        else:
            return intersection2

    return None # no intersections at all

def Distance(p1,  p2):
    return math.sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))


# Find the points of intersection.
def FindLineCircleIntersections(cx, cy, radius, point1, point2):
    #dx, dy, A, B, C, det, t
    intersection1 = (0,0)
    intersection2 = (0,0)

    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]

    A = dx * dx + dy * dy
    B = 2 * (dx * (point1[0] - cx) + dy * (point1[1] - cy))
    C = (point1[0] - cx) * (point1[0] - cx) + (point1[1] - cy) * (point1[1] - cy) - radius * radius

    det = B * B - 4 * A * C

    if ((A <= 0.0000001) or (det < 0)):
        # No real solutions.
        intersection1 = None
        intersection2 = None
        return 0,intersection1,intersection2
    
    elif (det == 0):
        # One solution.
        t = -B / (2 * A)
        intersection1 = (int(point1[0] + t * dx), int(point1[0] + t * dy))
        intersection2 = None
        return 1,intersection1,intersection2
    
    else:
        # Two solutions.
        t = (-B + math.sqrt(det)) / (2 * A)
        intersection1 = (int(point1[0] + t * dx), int(point1[1] + t * dy))
        t = (-B - math.sqrt(det)) / (2 * A)
        intersection2 = (int(point1[0] + t * dx), int(point1[1] + t * dy))
        return 2,intersection1,intersection2

if __name__ == "__main__":
    print(ClosestIntersection(0,0,5,(12,21),(0,0)))
