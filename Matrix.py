## MATRIX CLASS ASSIGNMENT
## Author: Bryan Epperson

## TODO
## Implement a helper function to return the dot product of a 1 x n vector and
## an n x 1 vector - i.e. a row and a column.  They must be the same length,
## otherwise the function needs to exit without error.
def dot( vec1, vec2 ):
    answer = 0
    if len(vec1) != len(vec2):
        return False
    for i in range(len(vec1)):
        answer += vec1[i]*vec2[i]
    return answer







class Matrix():

    ## Initialize a Matrix object with an input matrix, stored as a list-of-lists.
    def __init__( self, matrix ):

        ## TODO
        ## Implement a class attribute to keep track of the matrix values.
        ## This attribute just stores the input data.  Be sure to check that
        ## 'matrix' is a list of lists before setting this value.
        ## REMINDER: set a class attribute by using 'self.attr_name = value'.
        self.rows = len(matrix)
        self.col = len(matrix[0])
        self.m = matrix


        ## TODO
        ## Implement class attributes to keep track of the number of rows and the
        ## number of columns.  You can use these to compare dimensions.



    ## TODO
    ## Implement helper function that returns the i-th row in the matrix.
    ## Should return a list of numbers (e.g. a 1 x m matrix).
    def get_row( self, n ):
        row = self.m[n]
        return row



    ## TODO
    ## Implement helper function that returns the j-th column in the matrix.
    ## Should return a list of lists, each of size 1 (e.g. an n x 1 matrix).
    def get_col( self, j ):
        column = []
        for i in range(self.rows):
            c = [self.m[i][j]]
            column.append(c)
        return column


    ## TODO
    ## Check that the dimensions of self and other are compatible.
    ## Return a Matrix equal to the sum of self and other.
    def add( self, other ):
        if self.rows == other.rows and self.col == other.col:
            result_matrix = []
            for i in range(self.rows):
                temp_result = []
                for j in range(self.col):
                    r = self.m[i][j] + other.m[i][j]
                    temp_result.append(r)
                result_matrix.append(temp_result)
            resMat = Matrix(result_matrix)
            return result_matrix
        return False



    ## TODO
    ## Check that the dimensions of self and other are compatible.
    ## Return a Matrix equal to the difference of self and other.
    def sub( self, other ):
        if self.rows == other.rows and self.col == other.col:
            result_matrix = []
            for i in range(self.rows):
                temp_result = []
                for j in range(self.col):
                    r = self.m[i][j] - other.m[i][j]
                    temp_result.append(r)
                result_matrix.append(temp_result)
            resMat = Matrix(result_matrix)
            return result_matrix
        pass




    ## TODO
    ## First, check whether other is a scalar or a matrix.
    ## If it is a scalar, return the product other * self.
    ## If it is a Matrix, return the matrix product of self
    ## and other.  This is to be accomplished by using the
    ## dot function defined above.
    def mult( self, other ):
        transpose_col = other.transpose()
        Mult_result = []
        if self.rows == other.col:
            for i in range(self.rows): ## rows of first matrix = colums of second matrix
                temp_result = []
                for j in range (other.cols):
                    mr = self.m[i][j] * other.transpose(j)
                    temp_result.append(mr)
                Mult_result.append(temp_result)
            return Mult_result
        pass



    ## TODO
    ## Return a Matrix that is the transpose of self.
    def transpose( self ):
        t_matrix = []
        for i in range(self.col):
            current_col = self.get_col(i)
            row = []
            for j in range(self.rows):
                row.append(current_col[j][0])
            t_matrix.append(row)




        # print(t_matrix)
        # for j in range(self.col):

        return t_matrix






m = Matrix([[1,2,3],[4,5,6]])
other = Matrix([[7,8,9],[10,11,12]])
print(m.add(other))
print(m.sub(other))
print(dot([1,2,3],[4,5,6]))
print(m.transpose())
m.mult(other)

