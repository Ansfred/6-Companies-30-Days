class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0
            
        boomerangs = 0
        for i in range(len(points)):
            distanceCount_hashMap = {}
            for j in range(len(points)):
                if i == j:
                    continue
                dij = (((points[j][0] - points[i][0]) ** 2) + ((points[j][1] - points[i][1]) ** 2)) ** 0.5

                if dij in distanceCount_hashMap:
                    distanceCount_hashMap[dij] += 1
                else:
                    distanceCount_hashMap[dij] = 1

            for distance in distanceCount_hashMap:
                boomerangs += distanceCount_hashMap[distance] * (distanceCount_hashMap[distance] - 1)
        
        return boomerangs