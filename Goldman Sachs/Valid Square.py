class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        for it1 in range(len(points) - 1):
            for it2 in range(it1 + 1, len(points)):
                # ALL 4 POINTS MUST BE UNIQUE; IF NOT; POINTS CANNOT FORM A SQUARE
                if points[it1] == points[it2]:
                    return False

        # CONDITION TO FORM A SQUARE: FROM ANY GIVEN POINT, TWO OTHER POINTS SHOULD BE AT AN EQUAL DISTANCE FROM IT AND THE THIRD POINT SHOULD BE AT A (√2 * (DISTANCE AT WHAT THE OTHER TWO POINTS WERE AT))
        for i in range(len(points)):
            # MAINTAIN AN UNORDERED SET TO STORE DISTANCE ENTRIES
            distance_set = set()

            x1, y1 = points[i][0], points[i][1]
            for j in range(len(points)):
                x2, y2 = points[j][0], points[j][1]
                if (x1 == x2) and (y1 == y2):
                    continue

                # dx1y1x2y2 => DISTANCE BETWEEN `points[u]` & `points[v]`
                dx1y1x2y2 = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
                distance_set.add(dx1y1x2y2)


            # IF NUMBER OF ENTRIES IN THE `distance_set` > 2; MEANS OUR POINTS CANNOT FORM A SQUARE IN THE 2D SPACE.
            # ROUNDED VALUES FOR MORE ACCURATE AND UNIFORM COMPARISON
            if (len(distance_set) > 2) or (round(max(distance_set), 5) != round(math.sqrt(2) * min(distance_set), 5)):
                return False
        
        return True