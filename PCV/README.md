## About PCV
PCV is a pure Python library for computer vision based on the book "Programming Computer Vision with Python" by Jan Erik Solem. 

More details on the book (and a pdf version of the latest draft) can be found at [programmingcomputervision.com](http://programmingcomputervision.com/).

### Dependencies
You need to have Python 2.6+ and as a minimum:

* [NumPy](http://numpy.scipy.org/)
* [Matplotlib](http://matplotlib.sourceforge.net/)

Some parts use:

* [SciPy](http://scipy.org/)

Many sections show applications that require smaller specialized Python modules. See the book or the individual examples for full list of these dependencies. 

### Structure 
结构

*PCV/*  the code. 
代码

*pcv_book/*  contains a clean folder with the code exactly as used in the book at time of publication. 
原书发布时用到的代码，包含在一个干净的文件夹里

*examples/*  contains sample code. Some examples use data available at [programmingcomputervision.com](http://programmingcomputervision.com/). 
包含的实例代码，实例中的一个数据可以访问[programmingcomputervision.com](http://programmingcomputervision.com/).

### Installation
安装

Open a terminal in the PCV directory and run (with sudo if needed on your system):
在PCV目录下打开终端，并运行下面命令：

	python setup.py install

Now you should be able to do
现在你可以通过下面命令在你的脚本导入PCV模块：

	import PCV
	
in your Python session or script. Try one of the sample code examples to check that the installation works.
试着运行其中的实例代码，验证一下是否安装成功。

### License

All code in this project is provided as open source under the BSD license (2-clause "Simplified BSD License"). See LICENSE.txt. 


---
-Jan Erik Solem