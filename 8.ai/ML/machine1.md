1.Machine Learn : Looking for Function


2.Regression : The function outputs a scalar
    想预测明天pm2.5值
     
		(1)首先预备一个函数
		(2)准备用于预测的数据 例今天的pm2.5 气温 O₃


3.Classification : Given  options(classes),  the function      
    outputs the correct one
	从一个范围内选择一个输出
	   
	例 (1)bool(输出trul false)        (2) 围棋


4.Structured Learning : 
	在机器中创建结构 创造


5.机器学习找函数的过程
	Function with Unknown Parameters
	
	y=wx+b 称为一个model  
	x y 称 feature
	w 称 weight
	b 称 bias
	
	
	(1)写出一个带有未知参数的函数(猜测)  
		based on domain knowledge
	(2)Define Loss (b,w)
		from Training Data  训练资料 数据
		loss is a function of parameters  L(b, w)
		根据数据差距可以预估并改变设定的b w值 
		使其接近我的预测结果
		真实的y值为label
	(3) 将每个函数值与数据之间的差值(误差)加起来 取平均值 得到loss
	loss值越大 说明数据越不好

	作业1 e=|y-y^|²


6.if y and y^ are both probability distributions -> Cross-entropy
	如果y是几率分布 我们使用Cross-entropy


7.机器学习优化过程 Optimization
	解最佳化过程   找一个w*、b* 使loss值最小
	方法 : Gradient Descent
	
		对w: (1) 随机选取初始点w⁰
			 (2) 计算在w＝w⁰时 w对loss的微分  ∫ldw (l是函数值 w是自变量)
				   即计算在w⁰点处的切线斜率
				   如果斜率是负的 即左边比较高 右边比较低
				   我们就让w的值变大 loss就变小 反之w值变小
				   斜率数值大 改变的就大一点 反之就改变小一点
				   同时η: learning rate (学习速率)
				   对w的取值有影响的参数: 斜率、η
				   w¹= w⁰-η∫ldw

					η通过自己设定 这种通过自己设定的量 称为hyperparameters
					
			  (3) 不断改变w的位置 重复上述操作 到最后
				   理想状况 当w取某一值时 斜率为0 就停止
				   
					在理想状况下能够让loss取最小的w位置称 global minima
					实际状况下能取到的loss最小值的w位置称 local minima (假议题)


		对w、d:  (1) 分别选取w⁰ d⁰
			    (2) 求切线斜率 对w⁰ d⁰处对w求微分 再对w⁰ d⁰处对d求微分 
			    (3) w¹= w⁰-η∫ldw  b¹= b⁰-η∫ldb
				(4) 决定改变数值的方向并重复该过程	

					
8.如果y和x之间本身有复杂的关系 

	并不是通过minima model就能把函数表示出来 那么就说明我们的Linear models线性关系太简单 在实际情况下有所限制 
	Linear models have severe limitation -> Model Bias

	我们可以看作 实际的线 = constant + linear models(n个只有一段的线)
    constant 取和Linear models 在y轴上交点
    
    Linear models 的起始斜率设置为和实际线同向 其他位置均水平直线 从实际线第一个转角位置改变Linear models
    
	然后设置第二个Linear models 从第二个转折点开始 与实际线转折后的斜率相同 其他位置均水平直线
	
	重复这个过程
	得到结果 All Piecewise Linear Curves = constant + sum of a set of


9.sum of a set of :

	 Sigmoid Function函数 (hyperparameters)  
	 c sigmoid(b+wx₁) S型函数
	 常见: Hard Sigmoid
	 
$$
y = c*1/[1+e^(-b-wx₁^)]
$$

	改变w 改变斜率坡度
	改变b 左右移动
	改变c 改变直线高度

	因此我们把所有的蓝色线描述为sigmoid函数
	那么 实际线y
	
$$
	y = b + ∑ci * sigmoid  (bi + wi * x₁)
$$


	New Model: More Features
		
$$
y = b + ∑ci * sigmoid  (bi + ∑wij * xj)
$$

$$
	设r = b + wx
$$
	
$$
a = sigmoid(r) = 1/[1+e^(-r^)]  -> a = σ(r)
$$

$$
y = b+∑c^Ta
$$	
	反复进行这个操作


10.Function with unknown parameters

$$
y = b + c^T * σ(b. + Wx)   (内外的b不是同一个量)
$$
	
	
	x            feature 变量
	W b c^T b.   Unknown parameters 未知参数
	将未知参数写入一个向量 Θ


11.Loss(Θ)
	Loss is a function of parameters
	Loss means how good a set of values is
	
	y = b + c^T * σ(b. + Wx) 
	
$$
Loss = 1/N * ∑e 
$$


12 .Optimization of New Model

	Θ* = arg min L
	
	随机选取一个Θ初值Θ⁰    Randomly Pick initial values Θ⁰ 
	对每一个位置上的Θ 进行微分求L的微分斜率 得到一个向量gradient
	
	g = [∫L dΘ1, ∫L dΘ2, ..., ∫L dΘn]  ->  g = ▼L(Θ⁰)
	
$$
[Θ^1] = [Θ^0] - [η*g(Θ = 0)]  ->  Θ¹ = Θ⁰ - ηg
$$
	
	以此类推得到	 Θ²  Θ³ 
	重复这个过程至无限或g=0
	
	实际操作方法: 将所有的数据N分成若干个batch 每个batch计算出一个Loss 得到g (在这里batch的大小 batch size是自主决定的 因此是一个hyperparameter)
	compute gradient g = ▼L¹(Θ⁰)
	update Θ¹ = Θ⁰ - ηg
	....

	将所有的update组合到一起就得到一个epoch
	1 epoch = see all the batches once


13 .不使用sigmoid -> 使用ReLU

	Rectified Linear Unit(ReLU) 
	c max(0, b + wx₁)  在0和b + wx₁ 中选择更大的数输出
	将两个ReLU叠加 就是一个 Hard Sigmoid

$$
y = b + ∑ci * max (0, bi + ∑wij * xj)
$$

	此处的∑求和需要两倍的i 两倍的ReLU


14 .Activation function

	在机器学习中 我们把sigmoid max这样的计算称之为Activation function


15 .神经网络

	在上述过程中 我们把每一个a 也就是每一个蓝色线描述为一个Neuron神经元 
	包括sigmoid ReLU
	
	把许多神经元排列在一起 称为Neural Network 神经网络
	
	把每一组蓝色线 也就是a 称为hidden layer
	把所有的hidder layer组合在一起 称 Deep Learning
	我们把训练资料和测试资料的不同 称为 Overfitting


16 .对作业的整理

	作业一 计算
	作业二 语言辨识
	作业三 影像辨识
	作业四 愚者辨识系统
	作业五 翻译语言 机器翻译


17 .Framework of ML

	（总结）
	step1: 设定一个含有未知参量的函数 y=f0(x)   函数f(x) 其中的未知参量由向量0表示
	step2: 设定一个loss 求未知参量 L(0)
	step3: 优化optimization 将loss尽可能小 0* = arg min L

	从optimization中得到了能使loss尽可能小的0值 代回原y=f(x) 得到函数 得到所需数据


18 .做法指南
	（1）loss on training data 记录训练数据
	（2）分支一 ： 如果得到的loss 大 有两种情况 
	
			1.model bias 太简单 
				需求的loss没有得到 没有在function的范围内
				loss不够低 我们需要重新设置一个更大的model 
				可以使用 sIgmoid ReLU
			 2.Optimization 
				loss处于减小状态 但不靠近需求最小值
				找不到最小的loss
				
			判断是model bias 还是 Optimization问题
			(层级越高 说明弹性越高 model bias较好 
			1.如果在此 loss反而更大 说明optimization不够好)
				我们可以先跑一个小的或者浅的model
			2.也可以使用非deep learning方法
				比如linear model
				容易做出好的optimization方法:
				support accommission、support mvictmachine


---
	（3）分支二 :  如果得到了较小的loss 有两种情况
	
		1.与loss on testing data相比也小 -> 直接输出
		2.与loss on testing data相比更大 有两种情况
		   (1. overfitting
			例如我们现在有一个一无是处的function 
			(x输入 如果x在训练资料里 输出对应y 如果x不在训练资料里 输出一个随机的值 
			也就是这个一无是处的函数什么都没干)
			
			但这个一无是处的函数 loss值为0 为loss最小的函数 
			也就是训练资料和测试资料完全相同
			
			通过训练资料training data上的点 我们可以得到曲线 但真正的数据据只有点 
			在曲线上会有很多freestyle 也就是自由曲线位置
			
			在通过testing data的数据得到另一条曲线 已知testing data的loss可能偏大
			因此曲线就与training data中的不同 这就是overfitting
			
			解决overfitting的方法一: 增加训练资料 数据
			方法二: 通过对事件的理解 自己创造一个训练资料
			举例说明 我们有图片 将其反转或选取一部分截下来
			
			假设model是y=a+bx 找不到点 模型测试限制太大了 
			这不是overfitting 是modelbias的问题
			当model非常复杂时 testing loss可能会很大 
			使得testing loss和trainingloss相差大
			这时我们可以选择tesing loss最小的位置 也就是test和train最接近的位置
			
			选取这个model
			首先要把training set训练资料分成两部分 training set和validation set
			在training set得到了模型 放到validation set上衡量这个分数
			
			选取validaton set方法  N-fold Cross Vaildation
			将所有的training分成三等分 依次取其中一份为validation 取3次
			然后观察哪一次分数最高就取哪次为validation 
			
		   (2. mismatch
			   训练资料和测试资料分布不一样