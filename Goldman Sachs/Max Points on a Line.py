class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_number_of_points_on_same_straightLine = 0
        for i in range(len(points) - 1):
            # For every given point; we are checking the slope with other points and storing their counts in a hashTable
            slope_count_hashTable = {}

            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]

                # Slope != 90 deg
                if x2 - x1 != 0:
                    slope = (y2 - y1) / (x2 - x1)
                    if slope in slope_count_hashTable:
                        slope_count_hashTable[slope] += 1
                    else:
                        slope_count_hashTable[slope] = 1
                # Slope = 90 deg; handled to avoid division by 0 error
                else:
                    slope = float('inf')
                    if slope in slope_count_hashTable:
                        slope_count_hashTable[slope] += 1
                    else:
                        slope_count_hashTable[slope] = 1
            
            max_number_of_points_on_same_straightLine = max(max_number_of_points_on_same_straightLine, max(slope_count_hashTable.values()) + 1)       # +1; to also accomodate / count for the current point
        return max_number_of_points_on_same_straightLine