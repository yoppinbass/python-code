# from stack import *
from color import *
# 自前のスタックよりももともとあるやつをスタック運用したほうが楽
def depth_first_search(graph, first_state, target):

    print(color("depth first search\n", "green"))

    # 初期化
    vertexes, edges = graph
    open_list = []
    open_list.append(first_state)
    closed_list = []
    print(" open: {}\tclosed:{}".format(open_list, closed_list))

    # 探査
    while closed_list != vertexes and open_list != []:
        a = open_list.pop()
        for e in edges:
            if a == e[0]:
                if e[1] not in open_list and e[1] not in closed_list:
                    open_list.append(e[1])
        closed_list.append(a)
        print(" open: {}\tclosed:{}".format(open_list, closed_list))
        if target in closed_list:
            print("found!!")
            return
    return 0

def breadth_first_search(graph, first_state, target):

    print(color("breadth first search\n", "green"))

    # 初期化
    vertexes, edges = graph
    open_list = []
    open_list.insert(0,first_state)
    closed_list = []
    print(" open: {}\tclosed:{}".format(open_list, closed_list))

    # 探査
    while closed_list != vertexes and open_list != []:
        a = open_list.pop()
        for e in edges:
            if a == e[0]:
                if e[1] not in open_list and e[1] not in closed_list:
                    open_list.insert(0, e[1])
        closed_list.insert(0, a)
        print(" open: {}\tclosed:{}".format(open_list, closed_list))
        if target in closed_list:
            print("found!!")
            return
    return 0

if __name__ == '__main__':
    vertexes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (3, 5),(1, 4)]
    graph = (vertexes, edges)
    depth_first_search(graph, 1, 5)
    breadth_first_search(graph, 1, 5)
