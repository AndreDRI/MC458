
def split_and_sort():
    points_x = []
    points_y = []
    print("ok")
    

def read_input():
    vec = []
    N = int(input())
    for i in range(N):
        vec.append([int(x) for x in input().split()])
    return vec

def main():
    points = read_input()
    print(points)

main()

