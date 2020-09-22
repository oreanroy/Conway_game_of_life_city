
import random

class Board:
    def __init__(self, arr):
        #arr = [random.randint(0, 1)*10]*10
        self.arr = arr
        self.row = len(arr)
        self.col = len(arr[0])
        #print(arr)

    def get_arr(self):
        return self.arr
    def get_row(self):
        return self.row
    def get_col(self):
        return self.col
    def set_arr_live(self, i, j):
        self.arr[i][j] = 1

    def render(self):
        # renders the board depending upon the array
        for row in self.arr:
            print(row)
#If the cell is alive, then it stays alive if it has either 2 or 3 live neighbors
#If the cell is dead, then it springs to life only in the case that it has 3 live neighbors

    def get_live_neighbours(self, i, j):
        liveNeigbours = 0
        #if arr[i-1][j-1]==1:
        #    liveNeigbours = liveNeigbours+1
        liveNeigbours += self.arr[(i-1)%self.row][(j-1)%self.col]
        liveNeigbours += self.arr[(i-1)%self.row][(j)%self.col]
        liveNeigbours += self.arr[(i-1) % self.row][(j + 1) % self.col]
        liveNeigbours += self.arr[(i)%self.row][(j-1)%self.col]
        liveNeigbours += self.arr[(i+1)%self.row][(j+1)%self.col]
        liveNeigbours += self.arr[(i+1)%self.row][(j)%self.col]
        liveNeigbours += self.arr[(i)%self.row][(j+1)%self.col]
        liveNeigbours += self.arr[(i+1) % self.row][(j-1) % self.col]
        return liveNeigbours

        #if i > 0 and self.arr[i-1][j]==1:
        #    liveNeigbours = liveNeigbours+1
        #if j > 0 and self.arr[i][j-1]==1:
        #    liveNeigbours = liveNeigbours+1
        #if i < self.row-1 and self.arr[i+1][j]==1:
        #    liveNeigbours = liveNeigbours+1
        #if j < self.col-1 and self.arr[i][j+1]==1:
        #    liveNeigbours = liveNeigbours+1
        #return liveNeigbours


    def update(self):
        #upadtes the array depeding upon the rules
        trr = [[0 for i in range(self.col)] for j in range(self.row) ]
        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                if (self.get_live_neighbours(i, j) == 2 or self.get_live_neighbours(i, j) == 3):
                    if self.arr[i][j] == 1:
                        trr[i][j] = 1
                    elif self.get_live_neighbours(i, j) == 3 and self.arr[i][j] == 0:
                        trr[i][j] = 1
        self.arr = trr




