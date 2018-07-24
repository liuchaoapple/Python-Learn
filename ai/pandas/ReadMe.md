#Pandas核心理念
    1.A set of labeled array data structures, 
    the primary of which are Series and DataFrame.
    2.Index objects enabling both simple axis indexing and multi-level / hierarchical axis indexing.
    3.An integrated group by engine for aggregating and transforming data sets.
    4.Date range generation (date_range) and custom date offsets enabling the implementation of customized frequencies.
    5.Input/Output tools: loading tabular data from flat files (CSV, delimited, Excel 2003), and saving and loading 
    pandas objects from the fast and efficient PyTables/HDF5 format.
    6.Memory-efficient “sparse” versions of the standard data structures for storing data that is mostly missing or
     mostly constant (some fixed value).
    7.Moving window statistics (rolling mean, rolling standard deviation, etc.).
##数据结构
    系列(Series)
        系列是具有均匀数据的一维数组结构。
        关键点:
            一维。
            标记均匀数组。
            大小不变。
    数据帧(DataFrame)
        数据帧(DataFrame)是一个具有异构数据的二维数组
        关键点:
            二维。
            异构数据。
            大小可变。
            数据可变。
    面板(Panel)
        面板是具有异构数据的三维数据结构。在图形表示中很难表示面板。但是一个面板可以说明为DataFrame的容器。
        关键点：
            异构数据
            大小可变
            数据可变
##pandas.Series
    pandas.Series( data, index, dtype, copy)
        1	data	数据采取各种形式，如：ndarray，list，constants
        2	index	索引值必须是唯一的和散列的，与数据的长度相同。 默认np.arange(n)如果没有索引被传递。
        3	dtype	dtype用于数据类型。如果没有，将推断数据类型
        4	copy	复制数据，默认为false。
        
##pandas.DataFrame
    数据帧(DataFrame)是二维数据结构，即数据以行和列的表格方式排列。
    数据帧(DataFrame)的功能特点：
        潜在的列是不同的类型
        大小可变
        标记轴(行和列)
        可以对行和列执行算术运算
    pandas.DataFrame( data, index, columns, dtype, copy)
        1	data	数据采取各种形式，如:ndarray，series，map，lists，dict，constant和另一个DataFrame。
        2	index	对于行标签，要用于结果帧的索引是可选缺省值np.arrange(n)，如果没有传递索引值。
        3	columns	对于列标签，可选的默认语法是 - np.arange(n)。 这只有在没有索引传递的情况下才是这样。
        4	dtype	每列的数据类型。
        5	copy	如果默认值为False，则此命令(或任何它)用于复制数据。
    Pandas数据帧(DataFrame)创建方式
        列表
        字典
        系列
        Numpy ndarrays
        另一个数据帧(DataFrame)
        
##Pandas.Panel
    面板(Panel)是3D容器的数据。面板数据一词来源于计量经济学，部分源于名称：Pandas - pan(el)-da(ta)-s。
    3轴(axis)这个名称旨在给出描述涉及面板数据的操作的一些语义。它们是
        items - axis 0，每个项目对应于内部包含的数据帧(DataFrame)。
        major_axis - axis 1，它是每个数据帧(DataFrame)的索引(行)。
        minor_axis - axis 2，它是每个数据帧(DataFrame)的列。
    pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
        参数描述
            data	数据采取各种形式，如：ndarray，series，map，lists，dict，constant和另一个数据帧(DataFrame)
            items	axis=0
            major_axis	axis=1
            minor_axis	axis=2
            dtype	每列的数据类型
            copy	复制数据，默认 - false