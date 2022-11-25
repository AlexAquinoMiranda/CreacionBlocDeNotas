from PySide6.QtCore import QLibraryInfo, QTranslator
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton,QHBoxLayout,QWidget,QVBoxLayout,QTextEdit,QMenu
from PySide6.QtGui import *

class VentanaPrincipal(QMainWindow):

    """ class VentanaPrincipal para la creación de un bloc de notas """
    
    def __init__(self):
        super().__init__()
        #titulo, icono y tamaño de app
        self.setWindowTitle('Bloc de notas')
        self.setWindowIcon(QIcon("logoBlocNotas.jpg"))
        self.resize(500,600)
        #botones
        self.creacionBotones()
        #atajos
        self.atajosTeclado()
        #menu
        self.miMenu()
        #textoEdit
        self.textoPlano()
        #layout
        self.misLayouts()
        #eventos
        self.eventosBotones()
        #show 
        self.mostrarAplicacion()
        

    def mostrarAplicacion(self):
        """ Metodo que visualiza el contenido de mi aplicación"""
        componentePrincipal  = QWidget()
        componentePrincipal.setLayout(self.layout_Vertical)
        componentePrincipal.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.setCentralWidget(componentePrincipal)

    def eventosBotones(self):
        #evento open  
        self.btnOpen.clicked.connect(self.abrirFichero)
        self.accionOpen.triggered.connect(self.abrirFichero)
        #evento save 
        self.btnSave.clicked.connect(self.guardarFichero)
        self.accionSave.triggered.connect(self.guardarFichero)
        #evento save as 
        self.btnSaveAs.clicked.connect(self.guardarComo)
        self.accionSaveAs.triggered.connect(self.guardarComo)
        #evento exit
        self.btnExit.clicked.connect(self.salirApp)
        self.accionExit.triggered.connect(self.salirApp)
        #evento new 
        self.btnNew.clicked.connect(self.nuevoFichero)
        self.accionNew.triggered.connect(self.nuevoFichero)



    def misLayouts(self):
        """ Metodo en donde se crea layouts y se les agrega botones y el panel de texto editable """
        layout_Horizontal = QHBoxLayout()
        self.layout_Vertical = QVBoxLayout()
        #añado botones de manera horizontal 
        layout_Horizontal.addWidget(self.btnNew)
        layout_Horizontal.addWidget(self.btnOpen)
        layout_Horizontal.addWidget(self.btnSave)
        layout_Horizontal.addWidget(self.btnSaveAs)
        layout_Horizontal.addWidget(self.btnExit)
        #añado mi layout horizontal para que se quede hacia arriba
        #  y hacia abajo el texto editable
        self.layout_Vertical.addLayout(layout_Horizontal)
        self.layout_Vertical.addWidget(self.textoEditable )

    def textoPlano(self):
        """creacion de  elemento para escribir y mostrar los datos """
        self.textoEditable=  QTextEdit("")
        self.textoEditable.setStyleSheet("background-color: rgb(255, 255, 255); color:black;")

    def miMenu(self):
        """ creación de un menú en donde contiene los atajos que podemos realizar"""
         #agg en el menu las acciones
        self.Barra_menu = self.menuBar()
        self.Barra_menu.setStyleSheet("background-color: rgb(224, 224, 224);")
        self.menu =  self.Barra_menu.addMenu("&menu")
        self.menu.addAction(  self.accionNew) 
        self.menu.addAction(  self.accionSave)
        self.menu.addAction(self.accionSaveAs)
        self.menu.addAction(self.accionOpen)
        self.menu.addAction(  self.accionExit)
        self.menu.setStyleSheet("background-color: rgb(224, 224, 224);")
        
    def atajosTeclado(self):
        """Creación de atajos para facilitar ciertas tareas """
        #atajo open
        self.accionOpen = QAction("Abir archivo.", self)
        self.accionOpen.setShortcut(QKeySequence("ctrl+o"))
        self.btnOpen.addAction(self.accionOpen)

        #atajo save as
        self.accionSaveAs = QAction("&guardar archivo como...", self)
        self.accionSaveAs.setShortcut(QKeySequence("ctrl+s"))
        self.btnSaveAs.addAction(self.accionSaveAs)

        #atajo save 
        self.accionSave = QAction("&guardar archivo.", self)
        self.accionSave.setShortcut(QKeySequence("ctrl+d"))
        self.btnSave.addAction(self.accionSave)

        #atajo exit 
        self.accionExit= QAction("&Exit", self)
        self.accionExit.setShortcut(QKeySequence("ctrl+q"))
        self.btnExit.addAction(self.accionExit)

        #atajo new 
        self.accionNew = QAction("Nuevo archivo.", self)
        self.accionNew.setShortcut(QKeySequence("ctrl+n"))
        self.btnNew.addAction(self.accionNew)
        
    def creacionBotones(self):
        """Creación de botones para gestionar cosas que deseemos hacer en nuestra aplicación """
        #open
        self.btnOpen = QPushButton("Open")
        self.btnOpen.setIcon(QIcon("open-file.png"))
        self.btnOpen.setStyleSheet("font-weight: bold;")

        #save as
        self.btnSaveAs = QPushButton("Save as...")
        self.btnSaveAs.setStyleSheet("font-weight: bold;")
        self.btnSaveAs.setIcon(QIcon("save.jpg"))

        #save
        self.btnSave = QPushButton("Save")
        self.btnSave.setIcon(QIcon("save.jpg"))
        self.btnSave.setStyleSheet("font-weight: bold;")

        #exit
        self.btnExit = QPushButton("Exit")
        self.btnExit.setIcon(QIcon("exit.jpg"))
        self.btnExit.setStyleSheet("font-weight: bold;")

        #new 
        self.btnNew = QPushButton("New")
        self.btnNew.setIcon(QIcon("new.png"))
        self.btnNew.setStyleSheet("font-weight: bold;")

    def nuevoFichero(self):
        #el text se ponde vacion
        self.textoEditable.setText("")
        self.archivoAbrir = ""
        print('nuevo fichero')


    def guardarFichero(self):
        try:
            f = open(self.archivoAbrir,'w') 
            f.write(self.textoEditable.toPlainText())
            f.close()
        except AttributeError :
            self.guardarComo()
        except FileNotFoundError:
            self.guardarComo()

    def guardarComo(self):
        """ Save as metodo para guardar el archivo en alguna dirección que se elija por el usuario"""
        try:
            ventana_dialogo = QFileDialog.getSaveFileName(
                self, caption="Guardar archivo como...", dir=".",
                filter="Documentos de texto (*.txt); \n documento sql (*.sql); \n document python (*.py);\n documento java (*.java);\n documento json (*.json);",
                selectedFilter="Documentos de texto (*.txt); \n document python (*.py);\ndocumento sql (*.sql); \n documento java (*.java); \n documento json (*.json);")
            archivo = ventana_dialogo[0]
            f = open(archivo,'w')
            f.write(self.textoEditable.toPlainText())
            f.close()
        except:
            print('no se ha elegido una ruta.')

    def salirApp(self):
        """ metodo para salir de la aplicación """
        print(exit())
   
    def abrirFichero(self):
        """ metodo para abrir archivos y mostrarlos en el panel del texto editable"""
        ventana_dialogo = QFileDialog.getOpenFileName(self, caption="Abrir archivo.", dir=".",
        filter="Documentos de texto (*.txt); \ndocumento sql (*.sql);\n document python (*.py); \n documento java (*.java) \n documento json (*.json);",
        selectedFilter="Documentos de texto (*.txt);\n document python (*.py); \n;documento sql (*.sql); \n documento java (*.java); \n documento json (*.json);")
        self.archivoAbrir = ventana_dialogo[0]
       
        #for para mostrar datos
        self.f = open(self.archivoAbrir,'r') 
        data = ""
        for line in self.f: 
            data += line
            self.textoEditable.setText(data) 
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