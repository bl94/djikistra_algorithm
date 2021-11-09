"""
DjikistraAlgorithm
"""
import math
from random import randint

class DjikistraAlgorithm():
    """
    class DjikistraAlgorithm
    create minimum spanning tree path
    """
    def __init__(self):
        self.matrix=[]
        self.vertex=''
        self.num_vertices=self.input_vertex()
        self.create_matrix()

    def create_matrix(self):
        '''
        method - create adjacency matrix - represantation of graph
        '''
        self.matrix=[[randint(0,15) if row!=column else 0 for column in range(0,self.num_vertices)]for row in range(0,self.num_vertices)]
        #customization values in matrix
        for row in range(0,self.num_vertices):
            for column in range(0,self.num_vertices):
                self.matrix[column][row]=self.matrix[row][column]
        #if one vertices has not edges, create new matrix again
        for array in self.matrix:
            if any(array)<1:
                self.create_matrix()

    def display_matrix(self):
        """
        method - display matrix
        """
        for nums in self.matrix:
            print(nums)

    def input_vertex(self):
        """
        method - input number of vertices
        """
        while self.vertex not in range(0,10):
            self.vertex=int(input("Choose number of vertices in range[0,10]: "))
        return self.vertex

    def start_minimum_spanning_tree(self):
        """
        method - create minimum spanning tree
        """
        #create list of vertices, only first vertex is active
        selected_vector=[False if x!=0 else True for x in range(0,self.num_vertices)]
        weight=0
        connections_between_vertices=0
        #if there are less connections between vertices than number vertices-1,perform operations
        while connections_between_vertices<self.num_vertices-1:
            index_of_row_minimum_value=0
            index_of_column_minimum_value=0
            minimum=math.inf
            for row in range(0,self.num_vertices):
                if selected_vector[row]:
                    for column in range(0,self.num_vertices):
                        if (self.matrix[row][column]>0 and not selected_vector[column]):
                            if self.matrix[row][column]<minimum:
                                minimum=self.matrix[row][column]
                                index_of_row_minimum_value=row
                                index_of_column_minimum_value=column
            #if value of edges is chosen,we change the value on 0
            self.matrix[index_of_row_minimum_value][index_of_column_minimum_value]=0
            self.matrix[index_of_column_minimum_value][index_of_row_minimum_value]=0
            #added minimum value to weight
            weight+=minimum
            #we activate vector which is bound by edge which we selected
            selected_vector[index_of_column_minimum_value]=True
            #added minimum value to edges next vector which was selected
            for value in range(0,self.num_vertices):
                if self.matrix[index_of_column_minimum_value][value]!=0:
                    self.matrix[index_of_column_minimum_value][value]+=minimum
            print(f"Edge ({index_of_row_minimum_value}-{index_of_column_minimum_value}) and weight of edge={minimum}. All weight of edges={weight}")
            selected_vector[index_of_column_minimum_value]=True
            #added minimum value to weight vertices which are selected
            connections_between_vertices+=1
        print(f'Minimum spanning tree weight={weight}')

def __main__():
    djkistra=DjikistraAlgorithm()
    djkistra.display_matrix()
    djkistra.start_minimum_spanning_tree()

if __name__=="__main__":
    __main__()
