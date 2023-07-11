def readLines():
    with open('Day1\input.txt') as data:
        lines = data.read().splitlines()
    
    return lines

def transformLines(lines):
    item=[]
    result=[]

    for line in lines:
        if line:
            item.append(int(line))
        else:
            result.append(item)
            item=[]
    result.append(item)
    return result

def getMaxCal(result):
    add_result = []

    [add_result.append(sum(row)) for row in result]
    max_val = max(add_result)
    max_index = add_result.index(max(add_result))
    return max_val


def getMaxCalTop3(result, limit):
    add_result = []

    [add_result.append(sum(row)) for row in result]
    sort_results = sorted(add_result,reverse=True)
    return sum(sort_results[0:limit])


