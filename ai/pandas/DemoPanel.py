import numpy as np
import pandas as pd



#创建面板
##从3D ndarray创建
data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)
print("--"*40)
##从DataFrame对象的dict创建面板
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)
print("--"*40)

#从面板中选择数据
##使用Items
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p['Item1'])
print("--"*40)
##使用panel.major_axis(index)方法访问数据
print(p.major_xs(1))
##使用minor_axis
print(p.minor_xs(1))