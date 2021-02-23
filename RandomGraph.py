import random
import numpy as np
import matplotlib.pyplot as plt
from Graph import *
from collections import deque


class RandomGraph(Graph) :
    def add_random_edges(self, p) :  # 모든 노드를 p의 확률로 연결시킴.
        for i in combinations(self.vertices(),2) :
            if random.random() < p :
                self.add_edge(Edge(*i))
        
    def bfs(self, s, visit=None) :   # 너비우선탐색(클러스터를 탐색한다.)
        visited = set()
        queue = deque([s])    # 시작노드로 초기화
        # deque : double-ended queue; 양쪽으로 수정이 가능하다.
        
        # 큐가 비어있게 될때까지 조회.
        
        while queue :    # 비어있는 자료형, 0은 False로 친다. 그외는 True
            v = queue.popleft()
            
            if v in visited: continue   # while loop를 다시 돈다.
            visited.add(v)
            if visit : visit(v)         # visit이 어떤 함수라면 실행한다. 
            queue.extend(self.out_vertices(v))  # extend : append와 유사하나, 요소를 각각 넣는다.
            
        return visited
    
    def is_connected(self) :     # 그래프가 연결이 되어있는지 검사한다.
        vs = self.vertices()
        visited = self.bfs(list(vs)[0])
        return len(visited) == len(vs)
    
    
def N_vertices(n) :
    verts=[]
    for i in range(n) :
        verts.append( Vertex(str(i)) )
    return RandomGraph(verts)

def test_graph(n, p) :
    ng = N_vertices(n)
    ng.add_random_edges(p=p)
    return ng.is_connected()

def test_p(n,p,num) :    # 노드,확률, 횟수
    count=0
    for i in range(num) :
        if test_graph(n,p) :
            count+=1
    return count/num

