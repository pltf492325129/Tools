for i in range(1, 1000):
    i_str = str(i+1)
    file_name = i_str + '.txt'
    f = open(file_name, 'w')
    f.close()