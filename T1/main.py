def merge_sort(left, right, vector):

    if len(vector) == 1:
        return vector
    middle = (left + right) // 2

    left_vec = []
    right_vec = []
    
    for i in range(middle):
        left_vec.append(vector[i])
    for j in range(middle, right):
        right_vec.append(vector[j])

    left_vec = merge_sort(0, len(left_vec), left_vec)
    right_vec = merge_sort(0, len(right_vec), right_vec)
    
    return merge(left_vec, right_vec)
    
def merge(left_vec, right_vec):
    i = 0
    j = 0
    k = 0
    aux_vec = left_vec + right_vec
    while k != len(aux_vec):
        if i > len(left_vec) - 1:
            aux_vec[k] = right_vec[j]
            j += 1
            k += 1
        elif j > len(right_vec) - 1:
            aux_vec[k] = left_vec[i]
            i += 1
            k += 1
        elif left_vec[i] <= right_vec[j]:
            aux_vec[k] = left_vec[i]
            i += 1
            k += 1
        else:
            aux_vec[k] = right_vec[j]
            j += 1
            k += 1
    return aux_vec

def read_input():
    vec_x = []
    vec_y = []
    N = int(input())
    for i in range(N):
        pair = [int(x) for x in input().split()]
        vec_x.append(pair[0]) 
        vec_y.append(pair[1])
    return vec_x, vec_y

def main():
    points_x, points_y = read_input()
    sorted_x = merge_sort(0, len(points_x), points_x)
    sorted_y = merge_sort(0, len(points_y), points_y)
    print(sorted_x)
    print(sorted_y)
    
def check_sorted(vec):
    for i in range(1, len(vec)):
        if vec[i - 1] > vec[i]:
            return False
    return True

main()

