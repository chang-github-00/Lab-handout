# Lab-handout： AI引论自然语言处理小班课RNN编程作业


基于charRNN训练一个语言模型，生成不同国家的名字

### 作业要求 
填充、简要注释已给代码

提交代码(不包括训练好的模型、和数据集文件)

1-2页的实验报告,内容需要包括以下方面：数据预处理描述，模型描述，训练可视化结果(loss), 注释中三个问题解答， 结果分析与思考

### Lab-handout 使用说明
填充“...”处的代码

main.py注释中有详细instructions


### Some Tips
- How to organize a pytorch project ? 

  - checkpoints/: 保存训练好的模型

  - data/: 数据相关文件，包括数据预处理，dataset实现
  
  - model/: 模型定义，可以有多个模型
  
  - utils/: 可能用到的工具函数
  
  - main.py: 主文件，训练和测试程序的入口，可通过不同的命令来指定不同的操作和参数
  
  - config.py : 配置文件，所以可配置的变量都集中在此，并提供默认值，这里将参数之间定义在主文件中
  
  - requirements.txt :程序依赖的第三方库
  
  - ReadME.me : 提供程序的必要说明
- 关于__init.py__ 
  
  一个目录如果包含了 init.py 文件，那么它就变成了一个包（package）。

  __ init.py__ 可以为空，也可以定义包的属性和方法，但其必须存在，其它程序才能从这个目录中导入相应的模块或函数。




### Hints 
Conditional RNN P(xt| category, x0,x1,...)

使用本机cpu训练 <5min 

