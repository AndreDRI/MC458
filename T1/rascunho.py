vec = [5, 999, -2, 1, 1000, 2, 1, 68, -2999, 2, 4, 444]


def merge_sort(left, right, vector):
    print(f"Left: {left} Right: {right} on Vec: {vector}")
    if len(vector) == 1:
        print(f"THIS IS {vector}")
        return 
    middle = (left + right) // 2
    #copy vectors
    left_vec = []
    right_vec = []
    for i in range(middle):
        left_vec.append(vector[i])
    for j in range(middle, right):
        right_vec.append(vector[j])

    print(left_vec)
    print(right_vec)
    #recursive call
    merge_sort(0, len(left_vec), left_vec)
    merge_sort(0, len(right_vec), right_vec)
    #merge in the right ot
    

def merge():
    print("oi")

merge_sort(0, len(vec), vec)
