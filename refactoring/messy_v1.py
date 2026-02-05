def process(data):
    res=[]
    for i in data:
        if i>10:
            res.append(i*2)
    return res
