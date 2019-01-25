
variables = {"A":True, "B":True, "C":True, "D":True}
predicates = []

def setup(input):
    predicates.append(input)
    
def truth_table():
    print ('A ' 'B ' 'C ' 'D ' '|' '| ' 'Y ' )
    print('------------')
    
    counter = 1
    while counter<=16:       
        
        if 0<= counter <=8:
            variables['A'] = True
        else:
            variables['A'] = False
                       
        if 0<= counter <=4 or 9 <= counter <= 12:
            variables['B'] = True       
        else:
            variables['B'] = False
            
        if counter%4 == 0 or counter%4==3:
            variables['C'] = False       
        else:
            variables['C'] = True
            
        if counter%2 == 0:
            variables['D'] = False       
        else:
            variables['D'] = True

        x = str(eval(predicates[0], variables))[0]

        a = str(variables['A'])[0]
        b = str(variables['B'])[0]
        c = str(variables['C'])[0]
        d = str(variables['D'])[0]
        print(a, b, c, d, '||', x)
        counter = counter + 1


        
