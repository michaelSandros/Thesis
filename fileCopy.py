def fileCopy():
        # open file for reading
        f1 = open('C:/Users/Mike/Desktop/links-anon.txt','r')
        # open file for writing
        f2 = open('txtfiles/realData.txt','w')
        # counter
        counter = 0
        # maximum lines of f1
        maximum = 15000
        # for each line in f1
        for line in f1:
                # final line of f1
                if (counter == maximum - 1):
                        #replace newline in the end of the line with empty character
                        f2.write(line.replace('\n',''))
                        break
                # copy f1's line to f2
                else:
                        f2.write(line)
                        # increment counter
                        counter = counter + 1
        f2.close()
        f1.close()

fileCopy()
