def check_is_toeplitz_matrix(matrix,size):
    current = matrix[:size]
    for i in xrange(size,len(matrix),size):
        observed = matrix[i:i+size]
        if not (observed[1:] == current[:-1]):
            return False
        current = observed
    return True

if __name__ == "__main__":
    print check_is_toeplitz_matrix([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],5)
