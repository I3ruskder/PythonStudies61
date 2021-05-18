def triangle(row):
    tempRow = ""
    if len(row)==1:
        return row
    for i in range(len(row)-1):
        combination = row[i]+row[i+1]
        if combination == 'RB' or combination == 'BR' :
            tempRow+= "G"
        elif combination == 'BG' or combination == 'GB' :
            tempRow += "R"
        elif combination == 'RG' or combination == 'GR' :
            tempRow += "B"
        elif row[i]==row[i+1]:
            tempRow+=row[i]
    print(tempRow)
    return triangle(tempRow)

triangle('RBRGBRBGGRRRBGBBBGG')