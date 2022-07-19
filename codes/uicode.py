from PyQt5.QtWidgets import *
import sys,pickle

from PyQt5 import uic, QtWidgets ,QtCore, QtGui
from sklearn.preprocessing import LabelEncoder
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog,QLineEdit,QLabel
from PyQt5 import QtWidgets
import linear_reg,svm_model,table_display,data_visualise,logistic_reg,RandomForest
import KNN,pre_trained,add_steps, pred_mtnc
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5.uic import loadUi
from PyQt5.QtCore import QCoreApplication
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go




class error_window(QMainWindow):
    def __init__(self):
        super(error_window, self).__init__()
        uic.loadUi("ui_files/error.ui", self)
        self.ExitError = self.findChild(QPushButton, "ExitButtonError")
        self.ExitError.clicked.connect(QCoreApplication.instance().quit)
        self.back = self.findChild(QPushButton,"Back")
        self.back.clicked.connect(self.Backbut)
        self.show()

    
    
    def Backbut(self):
        self.back.clicked.connect(UI().target)
        self.close()



class home_screen(QDialog):
    def __init__(self):
        super(home_screen,self).__init__()
        loadUi("ui_files/Front Page.ui",self)
        self.Start = self.findChild(QPushButton, "pushButton")
        self.Start.clicked.connect(self.StartButton)
        self.help = self.findChild(QPushButton,"pushButton_3")
        self.help.clicked.connect(self.helpButton)

        




    def helpButton(self):
        help = help_screen()
        widget.addWidget(help)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
       

    def StartButton(self):
        self.w =model()
        self.w.show()
        


       

class model(QMainWindow):
    def __init__(self):
        super(model,self).__init__()
        
        # self.setFixedSize(780, 690)

        loadUi("ui_files/modeltype.ui",self)
        self.New_model = self.findChild(QPushButton, "newmodel")
        self.New_model.clicked.connect(self.new)

        self.Trainedmodel = self.findChild(QPushButton,"trainedmodel")
        self.Trainedmodel.clicked.connect(self.train)

        self.exitbutton = self.findChild(QPushButton,"ExitButton")
        self.exitbutton.clicked.connect(QCoreApplication.instance().quit)

    def new(self):
        pred = UI()
        widget.addWidget(pred)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.close()
        

    def train(self):
        self.filePath_pre, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home/akshay/Dekstop',"pkl(*.pkl)")
        with open(self.filePath_pre, 'rb') as file:
            self.pickle_model = pickle.load(file)
    
    def test_pretrained(self):
        self.testing=pre_trained.UI(self.pickle_model)
    
   

 #  Help button connection
class help_screen(QDialog):
    def __init__(self):
        super(help_screen,self).__init__()
        loadUi(r"ui_files/Help Centre.ui",self)

        self.Back = self.findChild(QPushButton, "pushButton")
        self.Back.clicked.connect(self.backButton)

        self.Continue = self.findChild(QPushButton,"pushButton_2")
        self.Continue.clicked.connect(self.continueButton)

    def backButton(self):
        back = home_screen()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def continueButton(self):
        cont = UI()
        widget.addWidget(cont)
        widget.setCurrentIndex(widget.currentIndex()+1)

class UI(QMainWindow):
    # global dict_val
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r'ui_files\Mainwindow.ui', self)
        global data,steps, dict_val

        
        data=data_visualise.data_()
        steps=add_steps.add_steps()

        
        self.Browse = self.findChild(QPushButton,"Browse")
        self.Drop_btn = self.findChild(QPushButton,"Drop")
        self.exitbutton = self.findChild(QPushButton,"ExitButton")
        self.exitbutton.clicked.connect(QCoreApplication.instance().quit)
        self.plot_win= self.findChild(QListWidget,"plotwidget")
        self.con_btn = self.findChild(QPushButton,"convert_btn")
        self.columns= self.findChild(QListWidget,"column_list")
        self.cat_column=self.findChild(QComboBox,"cat_column")
        self.table = self.findChild(QTableView,"tableView")
        self.dropcolumns=self.findChild(QComboBox,"dropcolumn")
        self.data_shape = self.findChild(QLabel,"shape")
        self.submit_btn = self.findChild(QPushButton,"Submit")
        self.target_col =self.findChild(QLabel,"target_col")
        self.model_select=self.findChild(QComboBox,"model_select")
        self.scatter_x=self.findChild(QComboBox,"scatter_x")
        self.scatter_y=self.findChild(QComboBox,"scatter_y")
        self.scatter_mark=self.findChild(QComboBox,"scatter_mark")
        self.scatter_c=self.findChild(QComboBox,"scatter_c")
        self.scatter_btn = self.findChild(QPushButton,"scatterplot")
        self.hist_column=self.findChild(QComboBox,"hist_column")
        self.hist_column_add=self.findChild(QComboBox,"hist_column_add")
        self.hist_add_btn = self.findChild(QPushButton,"hist_add_btn")
        self.hist_remove_btn = self.findChild(QPushButton,"hist_remove_btn")
        self.histogram_btn = self.findChild(QPushButton,"histogram")
        self.train=self.findChild(QPushButton,"train")
        self.heatmap_btn = self.findChild(QPushButton,"heatmap")
        self.null_column=self.findChild(QComboBox,"null_column")
        self.nullbtn=self.findChild(QPushButton,"null_2")


        self.X_combo=self.findChild(QComboBox,"X_combo")
        self.Y_combo=self.findChild(QComboBox,"Y_combo")
        self.Z_combo=self.findChild(QComboBox,"Z_combo")
        self.color_combo=self.findChild(QComboBox,"color_combo")
        self.plot3d_btn= self.findChild(QPushButton,"visualize")

        self.Browse.clicked.connect(self.getCSV)
        self.Drop_btn.clicked.connect(self.dropc)
        self.scatter_btn.clicked.connect(self.scatter_plot)
        self.hist_add_btn.clicked.connect(self.hist_add_column)
        self.hist_remove_btn.clicked.connect(self.hist_remove_column)
        self.histogram_btn.clicked.connect(self.histogram_plot)
        self.heatmap_btn.clicked.connect(self.heatmap_gen)
        self.visualize.clicked.connect(self.plt3d)
        self.con_btn.clicked.connect(self.con_cat)
        self.columns.clicked.connect(self.target)
        self.submit_btn.clicked.connect(self.set_target)
        self.train.clicked.connect(self.train_func)
        self.scale_btn.clicked.connect(self.scale_value)

        self.nullbtn.clicked.connect(self.fillme)
   
        self.show()

    def scale_value(self):
        if self.scaler.currentText()=='StandardScale':
            self.df,func_name = data.StandardScale(self.df,self.target_value)
        elif self.scaler.currentText()=='MinMaxScale':
            self.df,func_name = data.MinMaxScale(self.df,self.target_value)
        elif self.scaler.currentText()=='PowerScale':
            self.df,func_name = data.PowerScale(self.df,self.target_value)
        
        steps.add_text(self.scaler.currentText()+" applied to data")
        steps.add_pipeline(self.scaler.currentText(),func_name)
        self.filldetails()


    def hist_add_column(self):
        
        self.hist_column_add.addItem(self.hist_column.currentText())
        self.hist_column.removeItem(self.hist_column.findText(self.hist_column.currentText()))


    def hist_remove_column(self):
        
        self.hist_column.addItem(self.hist_column_add.currentText())
        self.hist_column_add.removeItem(self.hist_column_add.findText(self.hist_column_add.currentText()))


    def histogram_plot(self):
        
        AllItems = [self.hist_column_add.itemText(i) for i in range(self.hist_column_add.count())]
        for i in AllItems:
            data.plot_histogram(self.df,i)
            self.graphWidget.setBackground('w')
            self.graphWidget.plot(self.df,i)
        

    def plt3d(self):
        # pio.renderers.default= 'chrome'
        # fig= px.scatter_3d(data_frame= self.df, x= self.X_combo.currentText(), y=self.Y_combo.currentText(), z=self.Z_combo.currentText(), color=self.color_combo.currentText())
        # return(pio.show(fig))    
        fig= go.Figure(data= px.scatter_3d(data_frame= self.df, x= self.X_combo.currentText(), y=self.Y_combo.currentText(), z=self.Z_combo.currentText(), color=self.color_combo.currentText())) 
        return(fig.show())

    def heatmap_gen(self):
        data.plot_heatmap(self.df)

    def set_target(self):
        try:
            self.target_value=str(self.item.text()).split()[0]
            steps.add_code("target=data['"+self.target_value+"']")
            self.target_col.setText(self.target_value)
        except:
                self.w =error_window()
                self.w.show()



    def target(self):
        
            self.item=self.columns.currentItem()
        
        
        

    def filldetails(self,flag=1):
         
        if(flag==0):  
            self.df = data.read_file(str(self.filePath))
        
        
        self.columns.clear()
        self.column_list=data.get_column_list(self.df)
        self.empty_list=data.get_empty_list(self.df)
        self.cat_col_list=data.get_cat(self.df)
        for i ,j in enumerate(self.column_list):
            stri=j+ " -------   " + str(self.df[j].dtype)
            self.columns.insertItem(i,stri)
            

        self.fill_combo_box() 
        shape_df="Shape:  Rows:"+ str(data.get_shape(self.df)[0])+" ,  Columns: "+str(data.get_shape(self.df)[1])
        self.data_shape.setText(shape_df)

    def fill_combo_box(self):
        
        self.dropcolumns.clear()
        self.dropcolumns.addItems(self.column_list)
        self.cat_column.clear()
        self.cat_column.addItems(self.cat_col_list)
        self.scatter_x.clear()
        self.scatter_x.addItems(self.column_list)
        self.scatter_y.clear()
        self.scatter_y.addItems(self.column_list)
        self.null_column.clear()
        self.null_column.addItems(self.column_list)
        self.X_combo.clear()
        self.X_combo.addItems(self.column_list)
        self.Y_combo.clear()
        self.Y_combo.addItems(self.column_list)
        self.Z_combo.clear()
        self.Z_combo.addItems(self.column_list)
        self.color_combo.clear()
        self.color_combo.addItems(self.column_list)
       
        color= ['red', 'green', 'blue', 'yellow']
        self.scatter_c.clear()
        self.scatter_c.addItems(color)
        self.hist_column.clear()
        self.hist_column.addItems(data.get_numeric(self.df))
        self.hist_column.addItem("All")
        x=table_display.DataFrameModel(self.df)
        self.table.setModel(x)
        


    def con_cat(self):
        
        a = str(self.cat_column.currentText())

        self.df2 = self.df[[a]].copy()
        # print(self.df2.iloc[:,0])
        self.df[a],func_name =data.convert_category(self.df,a)
        self.dict_val = dict(zip(self.df[a],self.df2.iloc[:,0]))
        print(self.dict_val)
        steps.add_text("Column "+ a + " converted using Lab elEncoder")
        # print(self.dict_val)    
        steps.add_pipeline("LabelEncoder",func_name)
        self.filldetails()


    def decode(self):
        return self.dict_val

    



    def fillme(self):

        self.df[self.null_column.currentText()]=data.fillmean(self.df,self.null_column.currentText())
        code="data['"+self.null_column.currentText()+"'].fillna(data['"+self.null_column.currentText()+"'].mean(),inplace=True)"
        steps.add_code(code)
        steps.add_text("No Empty Values")
        self.filldetails()

    def getCSV(self):
        self.filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '',"csv(*.csv)")
        self.columns.clear()
        code="data=pd.read_csv('"+str(self.filePath)+"')"
        steps.add_code(code)
        steps.add_text("File "+self.filePath+" read")
        if(self.filePath!=""):
            self.filldetails(0)

    def dropc(self):

        if (self.dropcolumns.currentText() == self.target_value):
            self.target_value=""
            self.target_col.setText("")
        self.df=data.drop_columns(self.df,self.dropcolumns.currentText())
        steps.add_code("data=data.drop('"+self.dropcolumns.currentText()+"',axis=1)")
        steps.add_text("Column "+ self.dropcolumns.currentText()+ " dropped")
        self.filldetails()  

    def scatter_plot(self):

        data.scatter_plot(df=self.df,x=self.scatter_x.currentText(),y=self.scatter_y.currentText(),c=self.scatter_c.currentText(),marker=self.scatter_mark.currentText())
     
    def train_func(self):

        myDict={ "Linear Regression":linear_reg , "SVM":svm_model , "Logistic Regression":logistic_reg ,"Random Forest":RandomForest,
        "K-Nearest Neighbour":KNN ,"Predictive Maintenace":pred_mtnc}

        
        if(self.target_value!=""):
            
            self.win = myDict[self.model_select.currentText()].UI(self.df,self.target_value,steps)


app = QApplication(sys.argv)
welcome = home_screen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome) 
widget.setFixedHeight(920)
widget.setFixedWidth(1408)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("exiting..")
