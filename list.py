def list_ys():
    alist =[0,2,3,4,5,]
    print(alist[2])
    print(alist[1:4])
    alist.pop(3)
    alist.append(6)
    alist.append(7)
    alist[0]='5'
    print(len(alist))
    print(alist)

# 题: 新建一个字典变量,里面有两个键值对,通过key访问一个值,
# 删除一个键值对,添加一个键值对,更改任意一个值,再新建一个字典,将两个合并
www ={"qwer":"aa1","bb2":"cc3"}
def dd_a():
    print(www)
    print(www["qwer"])
    www.pop("qwer")
    print(www)
    www["zxc"] = 20
    print(www)
    www["qwer"]="qmh"
    print(www)
    jkl = {"a": [1, 2, 3], "o": [7, 8]}
    www.update(jkl)
    print(www)

bbb = {'xr':'xx','ccd':'bbc'}
def xr_a():
    print(bbb)
    print(bbb['xr'])
    bbb.pop('xr')
    print(bbb)
    bbb['xr']=111
    print(bbb)
    bbb['xr']='bb'
    print(bbb)
    zxr = {'dmh':[1,2,3,4,],"o":[8,9]}
    bbb.update(zxr)
    print(bbb)



if __name__ == '__main__':
    xr_a()