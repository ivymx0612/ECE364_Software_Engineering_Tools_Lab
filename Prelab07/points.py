#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-10-17 00:00:14 -0400 (Mon, 17 Oct 2016) $
#$Revision: 94691 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Prelab07/points.py $
#$Id: points.py 94691 2016-10-17 04:00:14Z ee364a07 $

class PointND:
    def __init__(self, *args):
        self.n = 0
        self.t = ()
        for item in args:
            if isinstance(item, float):
                temp = list(self.t)
                temp.append(item)
                self.t = tuple(temp)
                self.n = self.n + 1
            else:
                raise ValueError("Cannot instantiate an object with non-float values.")

    def __str__(self):
        temp = list(self.t)
        result = "("
        for i in range(len(temp)):
            result = result + "{0:.2f}".format(temp[i]) + ", "
        result = result[:-2]
        result = result + ")"
        return result

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        if self.n == other.n:
            diff = 0.0
            for i in range(len(self.t)):
                diff = diff + (self.t[i] - other.t[i])**2
            result = (diff)**0.5
            return result
        else:
            raise ValueError("Cannot calculate distance between points of different cardinality.")
            return None

    def nearestPoint(self, points):
        if (points):
            closestP = PointND()
            closestDis = self.distanceFrom(points[0])
            closestP.n = points[0].n
            closestP.t = points[0].t
            for point in points:
                dis = self.distanceFrom(point)
                if dis < closestDis:
                    closestP.n = point.n
                    closestP.t = point.t
                    closestDis = dis
            return closestP
        else:
            raise ValueError("Input cannot be empty.")
            return None

    def clone(self):
        newPoint = PointND()
        newPoint.n = self.n
        newPoint.t = self.t

    def __add__(self, other):
        if isinstance(other, PointND):
            if self.n == other.n:
                newPoint = PointND()
                newPoint.n = self.n
                temp = []
                for i in range(len(self.t)):
                    temp.append(self.t[i] + other.t[i])
                newPoint.t = tuple(temp)
                return newPoint
            else:
                raise ValueError("Cannot operate on points with different cardinalities.")
                return None
        elif isinstance(other, float):
            newPoint = PointND()
            newPoint.n = self.n
            temp = list(self.t)
            for i in range(len(temp)):
                temp[i] = temp[i] + other
            newPoint.t = tuple(temp)
            return newPoint

    def __sub__(self, other):
        if isinstance(other, PointND):
            if self.n == other.n:
                newPoint = PointND()
                newPoint.n = self.n
                temp = []
                for i in range(len(self.t)):
                    temp.append(self.t[i] - other.t[i])
                newPoint.t = tuple(temp)
                return newPoint
            else:
                raise ValueError("Cannot operate on points with different cardinalities.")
                return None
        elif isinstance(other, float):
            newPoint = PointND()
            newPoint.n = self.n
            temp = list(self.t)
            for i in range(len(temp)):
                temp[i] = temp[i] + other
            newPoint.t = tuple(temp)
            return newPoint

    def __mul__(self, other):
        newPoint = PointND()
        newPoint.n = self.n
        temp = list(self.t)
        for i in range(len(temp)):
            temp[i] = temp[i] * other
        newPoint.t = tuple(temp)
        return newPoint

    def __truediv__(self, other):
        newPoint = PointND()
        newPoint.n = self.n
        temp = list(self.t)
        for i in range(len(temp)):
            temp[i] = temp[i] / other
        newPoint.t = tuple(temp)
        return newPoint

    def __neg__(self):
        newPoint = PointND()
        newPoint.n = self.n
        temp = list(self.t)
        for i in range(len(temp)):
            temp[i] = -1 * temp[i]
        newPoint.t = tuple(temp)
        return newPoint

    def __getitem__(self, item):
        return self.t[item]

    def __eq__(self, other):
        if self.n == other.n:
            result = True
            for i in range(len(self.t)):
                if self.t[i] != other.t[i]:
                    result = False
            return result
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

    def __ne__(self, other):
        if self.n == other.n:
            result = False
            for i in range(len(self.t)):
                if self.t[i] != other.t[i]:
                    result = True
            return result
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

    def __gt__(self, other):
        if self.n == other.n:
            OriPoint = PointND()
            OriPoint.n = self.n
            temp = []
            for i in self.t:
                temp.append(0)
            OriPoint.t = tuple(temp)
            dis1 = self.distanceFrom(OriPoint)
            dis2 = other.distanceFrom(OriPoint)
            if dis1 > dis2:
                return True
            else:
                return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

    def __ge__(self, other):
        if self.n == other.n:
            OriPoint = PointND()
            OriPoint.n = self.n
            temp = []
            for i in self.t:
                temp.append(0)
            OriPoint.t = tuple(temp)
            dis1 = self.distanceFrom(OriPoint)
            dis2 = other.distanceFrom(OriPoint)
            if dis1 >= dis2:
                return True
            else:
                return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

    def __lt__(self, other):
        if self.n == other.n:
            OriPoint = PointND()
            OriPoint.n = self.n
            temp = []
            for i in self.t:
                temp.append(0)
            OriPoint.t = tuple(temp)
            dis1 = self.distanceFrom(OriPoint)
            dis2 = other.distanceFrom(OriPoint)
            if dis1 < dis2:
                return True
            else:
                return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

    def __le__(self, other):
        if self.n == other.n:
            OriPoint = PointND()
            OriPoint.n = self.n
            temp = []
            for i in self.t:
                temp.append(0)
            OriPoint.t = tuple(temp)
            dis1 = self.distanceFrom(OriPoint)
            dis2 = other.distanceFrom(OriPoint)
            if dis1 <= dis2:
                return True
            else:
                return False
        else:
            raise ValueError("Cannot compare points with different cardinalities.")

class Point3D(PointND):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

class PointGroup:
    def __init__(self, **kwargs):
        if kwargs is None:
            self._pointMap = {}
            self.n = 0
        else:
            for key, value in kwargs.items():
                pass
            if key != "pointList":
                raise KeyError("'pointList' input parameter not found.")
            elif value == []:
                raise ValueError("'pointList' input parameter cannot be empty.")
            else:
                self.n = value[0].n
                for point in value:
                    if point.n == self.n:
                        self._pointMap[point.__hash__] = point
                    else:
                        raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point, self.n))

    def addPoint(self, point):
        if point.n == self.n:
            self._pointMap[point.__hash__] = point
        else:
            raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point, self.n))

    def count(self):
        return len(self._pointMap)

    def __add__(self, point):
        if point.n == self.n:
            self._pointMap[point.__hash__] = point
        else:
            raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point, self.n))
        return self

    def __contains__(self, point):
        if point.__hash__ in self._pointMap:
            return True
        else:
            return False

    def __sub__(self, point):
        if point.__hash__ in self._pointMap:
            del self._pointMap[point.__hash__]
        return self

if __name__ == "__main__":
    point1 = PointND(1.0, 2.0)
    result = point1.__str__()
    print(result)
    point2 = PointND(5.0, 4.0)
    result = point1.distanceFrom(point2)
    print(result)
    point3 = PointND(1.0, 2.0)
    result = point1.nearestPoint((point2, point3))
    print(result.n, result.t)
    NewG = PointGroup(pointList=[1,2])