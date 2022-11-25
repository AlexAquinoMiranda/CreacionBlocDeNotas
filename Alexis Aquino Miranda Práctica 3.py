from PySide6.QtCore import QLibraryInfo, QTranslator
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton,QHBoxLayout,QWidget,QVBoxLayout,QTextEdit,QMenu
from PySide6.QtGui import *

class VentanaPrincipal(QMainWindow):
    textNotas = " "
    
    """ class utilizado para el tercer proyecto que trata de un bloc de notas """
   
    
    def __init__(self):
        super().__init__()
        #titulo, icono y tamaño de app
        self.setWindowTitle('Bloc de notas')

        self.setWindowIcon(QIcon("logoBlocNotas.jpg"))
        self.resize(500,600)

        #creación de layout
        layout_Horizontal = QHBoxLayout()
        layout_Vertical = QVBoxLayout()

        #botones esto puede estar en un metodo
        #abrir arcivo
        self.abrirArchivo = QPushButton("Open")
        self.abrirArchivo.setIcon(QIcon("open-file.png"))
        self.abrirArchivo.setStyleSheet("font-weight: bold;")
        #add action abrir arcivo
        self.accion = QAction("Abir archivo", self)
        
        self.accion.setShortcut(QKeySequence("ctrl+o"))
        self.accion.triggered.connect(self.openArchive)
        self.abrirArchivo.addAction(self.accion)
        self.abrirArchivo.clicked.connect(self.openArchive)

        #guardar archivo
        self.guardar = QPushButton("Save as...")
        self.guardar.setStyleSheet("font-weight: bold;")
        self.guardar.clicked.connect(self.mostrar_dialogo)
        self.guardar.setIcon(QIcon("save.jpg"))
        #add action guardar
        self.accionSave = QAction("&guardar archivo como", self)
        self.accionSave.setShortcut(QKeySequence("ctrl+s"))
        self.accionSave.triggered.connect(self.mostrar_dialogo)
        self.abrirArchivo.addAction(self.accionSave)


        #boton guardar 
        self.guardarRapido = QPushButton("Save")
        self.guardarRapido.setIcon(QIcon("save.jpg"))
        self.guardarRapido.setStyleSheet("font-weight: bold;")
        self.guardarRapido.clicked.connect(self.guardarFichero)

        #action guardar rapido
        self.accionSaveRap = QAction("&guardar archivo", self)
        self.accionSaveRap.setShortcut(QKeySequence("ctrl+d"))
        self.accionSaveRap.triggered.connect(self.guardarFichero)
        self.guardarRapido.addAction(self.accionSaveRap)


        #boton editar (usado para salir)
        self.edit = QPushButton("Exit")
        self.edit.setIcon(QIcon("exit.jpg"))
        self.edit.clicked.connect(self.salirApp)
        self.edit.setStyleSheet("font-weight: bold;")
        #ADD action
        self.accionExit = QAction("exit", self)
        self.accionExit.setShortcut(QKeySequence("ctrl+q"))
        self.accionExit.triggered.connect(self.salirApp)
        self.edit.addAction(self.accionExit)
        

        #texto editable
        self.textoIn=  QTextEdit("")
        self.textoIn.setStyleSheet("background-color: rgb(255, 255, 255); color:black;")
        

        #agg en el menu las acciones
        self.Barra_menu = self.menuBar()
        self.menu =  self.Barra_menu.addMenu("&menu")
        self.menu.addAction(  self.accionSave)
        self.menu.addAction(self.accionSaveRap)
        self.menu.addAction(self.accion)
        self.menu.addAction(  self.accionExit)
     

      
      



        #add de botones 
    
        layout_Horizontal.addWidget(self.abrirArchivo)
        layout_Horizontal.addWidget(self.guardar)
        layout_Horizontal.addWidget(self.guardarRapido)
        layout_Horizontal.addWidget(self.edit)
        #add de panel de botones en la parte de arriba y abajo el texto editable
        layout_Vertical.addLayout(layout_Horizontal)
        layout_Vertical.addWidget(self.textoIn )

        componentePrincipal  = QWidget()
        componentePrincipal.setLayout(layout_Vertical)

        componentePrincipal.setStyleSheet("background-color: rgb(224, 224, 224);")
        
        self.setCentralWidget(componentePrincipal)

    def creacionBotones(self):
        print('botones')
        #open
        self.btnOpen = QPushButton("Open")
        self.btnOpen.setIcon(QIcon("open-file.png"))
        self.btnOpen.setStyleSheet("font-weight: bold;")

        #save as
        self.btnSaveAs = QPushButton("Save as...")
        self.btnSaveAs.setStyleSheet("font-weight: bold;")
        #self.btnSaveAs.clicked.connect(self.mostrar_dialogo)
        self.btnSaveAs.setIcon(QIcon("save.jpg"))

        #save
        self.btnSave = QPushButton("Save")
        self.btnSave.setIcon(QIcon("save.jpg"))
        self.btnSave.setStyleSheet("font-weight: bold;")
        #self.btnSave.clicked.connect(self.guardarFichero)

        #exit
        self.btnExit = QPushButton("Exit")
        self.btnExit.setIcon(QIcon("exit.jpg"))
       # self.btnExit.clicked.connect(self.salirApp)
        self.btnExit.setStyleSheet("font-weight: bold;")



    def imprimir(self):
        self.textNotas= self.textoIn.toPlainText()#te muestra el texto que tiene actuaalmente
        print("abriendo el archivo")
        print(self.textNotas)


    def guardarFichero(self):
        try:
            f = open(self.archivoAbrir,'w') 
            f.write(self.textoIn.toPlainText())
            f.close()
            print(exit())
        except AttributeError:
            self.mostrar_dialogo()
            print('save as')


    def mostrar_dialogo(self):
        """ metodo para guardar el archivo en alguna dirección que se elija por el usuario"""
        try:
            ventana_dialogo = QFileDialog.getSaveFileName(
                self, caption="Guardar archivo como...", dir=".",
                filter="Documentos de texto (*.txt); \n documento sql (*.sql); \n document python (*.py);\n documento java (*.java);\n documento json (*.json);",
                selectedFilter="Documentos de texto (*.txt); \n document python (*.py);\ndocumento sql (*.sql); \n documento java (*.java); \n documento json (*.json);")
            archivo = ventana_dialogo[0]
            f = open(archivo,'w')
            f.write(self.textoIn.toPlainText())
            f.close()
        except:
            print('no se ha elegido una ruta.')

        
        print(archivo)


    def salirApp(self):
        """ metodo para salir de la aplicación """
        print(exit())

    def guardarMismaPos(self):
        dato = self.textoIn.toPlainText()
        self.f.write(dato)
        self.f.close()
    def modeOscuro (self):
        self.textoIn.setStyleSheet('background: black; color:white')
       
   
    def openArchive(self):
        """ metodo para abrir archivos y mostrarlos en el panel del texto editable"""
        ventana_dialogo = QFileDialog.getOpenFileName(self, caption="Abrir archivo.", dir=".",
        filter="Documentos de texto (*.txt); \ndocumento sql (*.sql);\n document python (*.py); \n documento java (*.java) \n documento json (*.json);",
        selectedFilter="Documentos de texto (*.txt);\n document python (*.py);\n;documento sql (*.sql); \n documento java (*.java); \n documento json (*.json);")
        self.archivoAbrir = ventana_dialogo[0]
        print(self.archivoAbrir)#este print muestrs la ruta

        #for para mostrar datos
        self.f = open(self.archivoAbrir,'r') 
        data = ""
        for line in self.f: 
            data += line
            self.textoIn.setText(data) 
        self.f.close()

def cargar_traductor(app):
    translator = QTranslator(app)
    translations = QLibraryInfo.location(QLibraryInfo.TranslationsPath)#is deprecated QLibraryInfo
    translator.load("qt_es", translations)
    app.installTranslator(translator)




#run aplication
app = QApplication([])

cargar_traductor(app)

ventana_principal = VentanaPrincipal()
ventana_principal.show()

app.exec()
