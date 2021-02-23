from itertools import combinations

class Vertex(object) :
    def __init__(self,label='') :
        self.label = label
    def __repr__(self) :     # 객체를 문자열로 반환하는 메서드
        return 'Vertex(%s)' % repr(self.label)
    def __eq__(self, another):
         return hasattr(another, 'label') and self.label == another.label
    def __hash__(self) :
        return hash(self.label)
    
    __str__ = __repr__   # __str__을 해도 같은 값이 나오도록
    
class Edge(tuple) :
    def __new__(cls,e1,e2) :
        return tuple.__new__(cls,(e1,e2))
    
    def __repr__(self) :
        return 'Edge(%s, %s)' %(repr(self[0]), repr(self[1]))
    
    __str__ = __repr__

class Graph(dict) :
    def __init__(self, vs=[], es=[]) :  # vs=노드, es=연결선
        for v in vs :
            self.add_vertex(v)
        for e in es :
            self.add_edge(e)
    
    def add_vertex(self, v) :
        self[v] = {}     # 외부 딕셔너리
    
    def add_edge(self, e) :  # 내부 딕셔너리에 저장하게 된다.
        v, w = e
        self[v][w] = e
        self[w][v] = e            
    
    def get_edge(self, v1, v2) :
        try :
            e = self[v1][v2]
            return e
        except KeyError :
            return None
        
    def remove_edge(self,e) :
        v1, v2 = e     # 아래의 Edge 클래스에서 tuple.__new__(cls,(e1,e2)) 정의함
        del self[v1][v2]
        del self[v2][v1]
      
    def vertices(self) : # 노드 전체 반환
        return self.keys()
    
    def edges(self) :
        a=[]
        for e_by_v in list(self.values()) :
            a += e_by_v.values()
        return list(set(a))
    
    def out_vertices(self, v) :   # 노드와 연결된 노드 반환
        return self[v].keys()
    
    def out_edges(self, v) :   # 노드와 연결된 키 반환
        return self[v].values()
    
    def add_all_edges(self) :
        for i in combinations(self.keys(),2) :
            self.add_edge(Edge(*i))
            
    def add_regular_edges(self, k):    # 모든 노드가 k-degree일 때까지 edge가 없는 노드와 연결.
        vs = self.vertices()
        n = len(vs)

        # degree가 노드 수 보다 크면 안된다.
        if k >= n:
            raise ValueError("Not enough Vertices")

        #Construction is different based on whether k is odd or even
        if is_odd(k):
            if is_odd(n):
                raise ValueError("Can't have odd k and odd length")
            self.add_regular_edges_even(k-1)
            self.add_regular_edges_odd()
        else:
            self.add_regular_edges_even(k)

    def add_regular_edges_even(self, k=2):
        vs = self.vertices()
        double = list(vs) * 2
        
        for i, v in enumerate(vs):
            for j in range(1,k//2+1):
                w = double[i+j]
                self.add_edge(Edge(v, w))

    def add_regular_edges_odd(self):
        """Adds an extra edge "across" the graph to finish off a regular
        graph with odd degree.  The number of vertices must be even."""
        vs = self.vertices()
        n = len(vs)
        reduplicated_list = vs * 2
        
        for i in range(n/2):
            v = reduplicated_list[i]
            w = reduplicated_list[i+n/2]
            self.add_edge(Edge(v, w))  
        
        
        
############


def is_odd(x):
    """Returns a True value (1) if x is odd, a False value (0) otherwise"""
    return x % 2

