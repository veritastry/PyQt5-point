#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("")
window.resize(500,500)

text=QTextEdit(window)
text.setOverwriteMode(True)             #设置覆盖模式，在光标处输入，则，光标之后的东西会被覆盖掉


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())