def fileCopy():
        
        f1 = open('C:/Users/Mike/Desktop/links-anon.txt','r')
        f2 = open('nodesFile.txt','w')
        counter = 0
        maximum = 5000
        for line in f1:
                if (counter == maximum -1):
                        f2.write(line.replace('\n',''))
                        break
                else:
                        f2.write(line)
                        counter = counter + 1
        f2.close()
        f1.close()
