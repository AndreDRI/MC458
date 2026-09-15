from random import randint

vec = [5, 999, -2, 1, 1000, 2, 1, 68, -2999, 2, 4, 444]


def test(cases):
    for i in range(cases):
        print(f"[Test case {i}]")
        vector_len = randint(0, 1000000)
        vec = []
        for j in range(vector_len):
            vec.append(randint(-9999999999, 99999999999))
        vec = merge_sort(0, len(vec), vec)
        if check_sorted(vec):
            print(f"[Test case {i}]: Success")
        else:
            print(f"[Test case {i}]: Fail")
            print(f"[Test case {i}]: Result {vec} ")
    # check if output is sorted

def check_sorted(vec):
    for i in range(1, len(vec)):
        if vec[i - 1] > vec[i]:
            return False
    return True

def merge_sort(left, right, vector):
    if len(vector) == 1:
        return vector
    middle = (left + right) // 2
    #copy vectors
    left_vec = []
    right_vec = []
    for i in range(middle):
        left_vec.append(vector[i])
    for j in range(middle, right):
        right_vec.append(vector[j])

    #recursive call
    left_vec = merge_sort(0, len(left_vec), left_vec)
    right_vec = merge_sort(0, len(right_vec), right_vec)
    #merge in the right ot
    
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


test(100)
