'''
1.数据集采集
    特征组+目标值
2.机器学习算法分类
    监督学习：
        目标值：类别--> 分类问题          如: 猫狗识别
            算法：K-近邻算法， 贝叶斯， 决策树与随机森林， 逻辑回归
        目标值为连续性的数据 --> 回归问题  如：预测房价
            算法：线性回归， 岭回归
    无监督学习：
        没有目标值   无监督学习
            算法： 聚类K-means
3.开发流程
    1）获取数据
    2）数据处理
    3）特征工程
    4）机器学习算法训练--模型
    5）模型评估  检测训练的效果是否满足
4.特征工程
    1）sklearn数据集
        sklearn.datasets.load_*()   数据集较小包含在sk库内，如datasets.load_iris()
    2)数据集大
        ----subset可选train，test，all选择要的数据，*替换的为调用的api名，不指定data_home就下载到home目录下
        sklearn.datasets.fetch_*()  网络上的大数据，如sklearn.datasets.fetch_20newsgroups(data_home='', subset='')
    3）数据返回值
        datasets.base.Bunch继承自字典
        根据键取相应的值，data，target，target_names, DESCR
    4)数据集的划分
        X为特征值, Y为目标值, test_size测试集大小，float类型, random_state数据是否随机
        x_train, x_target, y_train, y_target = sklearn.model_selection.train_test_split(X, Y, test_size, random_state=True)
    5）特征提取
        ----字典特征提取  将类别的转换成one-hot编码。   如：将性别特征，转换为男，女两个特质
        sklearn.feature_extraction.DictVectorizer()
            什么情况下会使用：数据集当中，类别特种比较多
                1.将数据集特征 -> 字典类型
                2.DicVectorizer转换
        ----文本特征提取
            sklearn.feature_extraction.text下的CountVectorizer类
                1.实例转换器类
                    transfer = CountVectorizer(stop_words=[])  参数：选择不需要进行计数的词
                2.调用fit_transform()
                    data_new = transfer.transform(data)    返回的是sparse矩阵（稀疏矩阵）
                    transfer.get_feature_names()    获取特征名
                    data_new.toarray()
                    这里与DictVectorizer返回的sparse矩阵都可以通过toarray()方法来返回数组的结果
        ----特征预处理：归一化/标准化
            无量纲化    特征单位或大小相差很大，容易影响目标结果
                归一化：将特征映射到自定义的范围，比如[0,1]之间
                    sklearn.preprocessing.minmax_scale(feature_range=[0,1])   默认为映射到0，1
                    缺点：容易受到异常值的影响，异常值如果出现很大或者很小，就容易受到很大影响，适合小数据场景
                标准化：适用于大数据
                    (x-mean)/std
                    这里映射到-1到1之间，越接近1表示正相关越强，越接近-1负相关越强
                    sklearn.preprocessing.StandardScaler()  用法同上
        ----降维：降低特征个数
            特征选择：
                Filter选择法
                    方差选择法： 低方差特征过滤
                        过滤掉方差低于2的特征
                        sklearn.feature_selection.VarianceThreshold(threshold=2)
                    相关系数：  特征之间相关程度，相关程度高的可以考虑过滤
                        scipy.stats.pearsonr(列名1， 列名2)  求列1与列2的相关系数
                Embeded嵌入式
                    决策树
                    正则化
                    深度学习
            主成分分析(PCA)：
                参数n_components填整数表示把原特征降成多少特征,如果是小数，表示保留原特征的百分之多少
                sklearn.decomposition.PCA(n_components=3)
5.分类算法
    1)转换器与估计器
        转化器：
            1.实例化
            2.调用fit_transform()
        估计器：sklearn机器学习的算法实现基础
            1.实例化一个estimator
            2.estimator.fit(x_train, y_train) 计算
                --调用完，模型生成
            3.模型预估
                --直接比对真实值与预测值
                    y_predict = estimator.predict(x_test)
                    y_test == y_predict
                --计算准确率
                    accuracy = estimator.score(x_test, y_test)
    2)KNN算法
        原理：
            根据k个邻居的类别来判断自己的类别
        模型选择与调优
        1.什么是交叉验证(cross validation)
            如将训练集分4组，每次选择不同的测试集与3组训练集。然后计算准确率，将四次准确率求平均得到最后交叉验证结果
            能让最后得到的数据更准确
        2.超参数搜索--网格搜索(Gird Search)
            参数： 预估器， 字典类型的n_neighbors的选择列表， 训练集要分成的组数
            sklearn.model_selection.GridSearchCV(estimator, param_gird={"n_neighbors": [1, 3, 5]}, cv=5)
            GridSearchCV类的属性中有最佳参数， 交叉验证结果等可以查看
    3）朴素贝叶斯算法：基于概率的算法
        联合概率， 条件概率， 相互独立
            联合概率：包含多个条件，且所有条件成立的概率
                P(程序员，身材匀称)     P(程序员，超重|喜欢)    特征|目标值
                P(A,B)
            条件概率：事件A在另一个事件B已经发生的条件下发生的概率
                P(程序员|喜欢)   P(程序员，超重|喜欢)
                P(A|B)
            相互独立：A概率*B概率等于P(A,B)概率
                P(A,B) = P(A)P(B) <=> 事件A与事件B相互独立
        为什么叫朴素：
            假设特征之间是相互独立的，那就满足相互独立的特性。A概率*B概率等于P(A,B)概率
        应用场景：
            文本分类：单词作为特征，词与词之间可以认为相互独立
        拉普拉斯平滑系数
        优缺点：
            对缺失数据不敏感，算法简单，分类准确度高，速度快
            特征之间有关联时，效果不明显
    4)决策树
        --特征的先后顺序来进行快速决策： 比如姑娘相亲
        1.原理分析：
            已知四个特征 预测 是否贷款
            先看是否有房，然后是否有车，年龄，信贷
        2.信息论基础：
            1）香农：消除随机性不定性的东西
            2）信息的衡量 - 信息量 - 信息熵
                g(D, A) = H(D) - 条件熵H(D|A)
            3）决策树的划分依据 -- 信息增益
        3.决策树的可视化
            参数：预估器， 文件名， 特征名(避免生成的决策树比较难看懂)
            export_graphviz(estimator, out_file='tree.doc', feature_names=iris.feature_names)
        4.决策树总结
            优点：
                可视化 - 可解释能力强
            缺点：
                容易产生过拟合
            改进：
                随机森林
                剪枝card算法
    5）集成学习方法 - 随机森林
        包含多个决策树的分类器
        原理：
            训练集：N个
            特征个数： M个
            --两个随机
                训练集随机 -- 随机有放回的抽样N个
                特征随机  -- 从M个特征中抽取m个特种   M >> m
        总结：
            准确性高，适合大数据
            处理高维度数据，不需要降维

'''