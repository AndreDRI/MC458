def slice(start, end, vector):

    middle = (start + end) // 2
    
    left_vec = []
    right_vec = []
    
    for i in range(middle):
        left_vec.append(vector[i])
    for j in range(middle, end):
        right_vec.append(vector[j])
    
    return left_vec, right_vec

def merge_sort(left, right, vector, x_or_y):

    if len(vector) == 1:
        return vector
    
    left_vec, right_vec = slice(left, right, vector)
    
    left_vec = merge_sort(0, len(left_vec), left_vec, x_or_y)
    right_vec = merge_sort(0, len(right_vec), right_vec, x_or_y)
    
    return merge(left_vec, right_vec, x_or_y)
    
def merge(left_vec, right_vec, x_or_y):
    i = 0
    j = 0
    k = 0
    axis = 2
    aux_vec = left_vec + right_vec
    if x_or_y == "X":
        axis = 0
    else:
        axis = 1
    while k != len(aux_vec):
        if i > len(left_vec) - 1:
            aux_vec[k] = right_vec[j]
            j += 1
            k += 1
        elif j > len(right_vec) - 1:
            aux_vec[k] = left_vec[i]
            i += 1
            k += 1
        elif left_vec[i][axis] <= right_vec[j][axis]:
            aux_vec[k] = left_vec[i]
            i += 1
            k += 1
        else:
            aux_vec[k] = right_vec[j]
            j += 1
            k += 1
    return aux_vec

def read_input():
    P = []
    N = int(input())
    for i in range(N):
        P.append([int(x) for x in input().split()])
    return P

def main():
    points = read_input()
    sorted_x = merge_sort(0, len(points), points, "X")
    sorted_y = merge_sort(0, len(points), points, "Y")
    print(closestPair(sorted_x, sorted_y))

def distance(point_A, point_B):
    return sqrt(((point_A[0] - point_B[0]) ** 2) + ((point_A[1] - point_B[1]) ** 2))

def sqrt(expression):
    return expression ** (1 / 2)

def slice_y(vec_y, mid_x, left_mid_count):
    left_y = []
    right_y = []
    for i in range(len(vec_y)):
        if vec_y[i][0] < mid_x:
            left_y.append(vec_y[i])
        elif vec_y[i][0] == mid_x and left_mid_count > 0:
            left_y.append(vec_y[i])
            left_mid_count -= 1
        else:
            right_y.append(vec_y[i])
    return left_y, right_y

# Using a Divide and Conquer Method
def closestPair(vec_x, vec_y):
    # N points in 2D Space
    N = len(vec_x)
    # Base Cases
    if (N == 2):
        return distance(vec_x[0], vec_x[1])
    if (N == 3):
        return min(distance(vec_x[0], vec_x[1]), distance(vec_x[0], vec_x[2]), distance(vec_x[1], vec_x[2]))
    # Divide Step, dividing 2D plane on smaller planes, and recursively calculating
    # Left and Right Halves
    left_plane, right_plane = slice(0, len(vec_x), vec_x)

    # Finding the midpoint X-Coordinate
    mid_x = left_plane[len(left_plane) - 1][0]

    # Counting points on the boundary
    left_mid_count = 0
    for i in range(len(left_plane)):
        if left_plane[i][0] == mid_x:
            left_mid_count += 1

    # Spliting vec_y into left and right y
    left_plane_y, right_plane_y = slice_y(vec_y, mid_x, left_mid_count)

    # Recursion
    left_plane_distance = closestPair(left_plane, vec_y)
    right_plane_distance = closestPair(right_plane, vec_y)
    epsilon = min(left_plane_distance, right_plane_distance)

    # Combine Step, be S which are the points in Y whose x-coor are in range of (x - d, x + d)
    # Building strip
    strip = []
    for i in range(len(vec_y)):
        if abs(vec_y[i][0] - mid_x) < epsilon:
            strip.append(vec_y[i])

    # Checking strip for the seven neighboring points
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            if ((strip[j][1] - strip[i][1]) >= epsilon):
                break
            epsilon = min(epsilon, distance(strip[i], strip[j]))

    return epsilon

main()


