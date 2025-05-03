from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import os
from modelo import Abmc
from observador import Subject
from datetime import datetime


observador_ventanas = Subject()


#FORMULA PARA INSERTAR IMAGENES
def insertar_imagen(nombre_archivo, subdirectorio="imagenes"):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.join(BASE_DIR, subdirectorio, nombre_archivo)
    
    if not os.path.exists(ruta_imagen):
        raise FileNotFoundError(f"No se encontró la imagen en la ruta: {ruta_imagen}")
    
    return PhotoImage(file=ruta_imagen)


#CLASE RELEVAMIENTO - PANTALLA INICIAL
class Relevamiento():
       def __init__(self,master):      #INICIALIZA LA CLASE
        
        self.master = master
        self.conmodelo = Abmc()   #INICIALIZA LA CLASE Abmc DE MODELO
        self.observador_ventanas = Subject()     #INICIALIZA LA CLASE Subjetc DE OBSERVADOR

        #CARACTERISITCAS DE LA VENTANA               
        self.master.geometry("750x400")
        self.master.title("RELEVAMIENTO DE PRECIOS")
        self.master.configure(bg="#ccd9df")

        #ESTILOS DE LA VENTANA    
        style = ttk.Style(self.master) 
        style.theme_use("default")
        style.configure("Treeview.Heading",background="#ce8f92", foreground="white")

        #VARIBLES DE TKINTER
        self.var_id = IntVar()
        self.var_relevadorx = StringVar()
        self.var_domicilio = StringVar()
        self.var_fecha = StringVar()
        self.var_producto = StringVar()
        self.var_marca1 = StringVar()
        self.var_precio1 = DoubleVar()
        self.var_marca2 = StringVar()
        self.var_precio2 = DoubleVar()
        
        self.logo = insertar_imagen("logo textos.png")



        #INSERTA CALENDARIO PARA SELECCIONAR FECHA

        self.calendario = Calendar(self.master,
                    background="#9eafb7",
                    selectbackground="#679ab7",
                    normalbackground="#8c8e8f",
                    weekendbackground="#d7878b",
                                        )

        self.calendario.place(x = 450, y = 50)





#LABELS Y ENTRY DE LA VENTANA PRINCIPAL

        Label(self.master,bg="#fcfafa", image= self.logo).place(x = 80, y = 180)
        Label(self.master, text = "INGRESE TIPO DE COMERCIO",background="#679ab7", foreground="white").place(x = 160, y = 10)
        
        
        #BARRIOS
        barrio = Label (self.master, bg="#d91c31", foreground="white", text ="BARRIO")
        barrio.place(x=80, y=95)
        entry_domicilio = ttk.Combobox(self.master, values=["AGRONOMIA", "ALMAGRO", "BALVANERA", "BARRACAS",
                                                "BELGRANO", "BOEDO", "CABALLITO", "CHACARITA", "COGHLAN",
                                                "COLEGIALES", "CONSTITUCION", "FLORES", "FLORESTA",
                                                "LA BOCA", "LA PATERNAL", " LINERS", "MATADEROS",
                                                "MONTECASTO", "NUEVA POPMPEYA", "NUÑEZ", "PALERMO", 
                                                "PARQUE AVELLANEDA", "PARQUE CHACABUCO0", "PARQUE CHAS", 
                                                "PARQUE PATRICIOS", "PUERTO MADERO", "RECOLETA", "RETIRO", 
                                                "SAAVEDRA", "SAN CRISTOBAL", "SAN TELMO", "VELZ SARSFIELD", 
                                                "VERSALLES", "VILLA CRESPO", "VILLA DEVOTO", "VILLA DEL PARQUE", 
                                                "VILLA GENERAL MITRE", " VILLA LUGANO", "VILLA LURO", "VILLA ORTUZAR", 
                                                "VILLA PUEYRREDON", "VILLA REAL", " VILLA REAL", "VILLA SANTA RITA", 
                                                "VILLA SOLDATI", "VILLA URQUIZA"],textvariable=self.var_domicilio, state="readonly")
        entry_domicilio.place(x=200, y=95)


        #RELEVADOR
        relevadorx = Label (self.master,bg="#d91c31",foreground="white", text ="RELEVADORX")
        relevadorx.place(x=80, y=60)
        entry_relevadorx= ttk.Combobox(values=["ARACELI", "MARCIA", "ADMINSTRADOR"],
                                            textvariable=self.var_relevadorx, state="readonly")
        entry_relevadorx.place(x=200, y=60)


        #FECHA
        fecha = Label(self.master,bg="#d91c31",foreground="white", text ="FECHA")
        fecha.place(x=80, y=140)

        entry_fecha = Entry(self.master, textvariable=self.var_fecha, )
        entry_fecha.place(x=200, y=140)
        
       

#BOTONES Y FUNCIONES DE APERTURA DE MODULOS
        #SUPERMERCADO       
        boton_super  = Button(self.master, text="SUPERMERCADO",justify=CENTER,padx=12, height=5, width=20,
                                background="#d91c31", foreground="white",
                              command=lambda: abrir_super( ))
        boton_super.place(x=10, y=300)
        def abrir_super():
            supermercado = Toplevel(self.master)
            supermercado.title("INGRESE LOS PRODUCTOS RELEVADOS")
            supermercado.geometry("750x600")
            supermercado.configure(bg="#fcfafa") 
            #LLAMA A LA CLASE TRAYENDO LOS ELEMENTOS DE CLASE RELEVAMIENTO
            Supermercado (supermercado, self.var_relevadorx, self.var_domicilio, self.var_fecha)
        
            
        
            # NOTIFICA AL OBSERVADOR
            observador_ventanas.notificar( self.var_relevadorx.get()+ "Se abrió la ventana de Supermercado")

    
        #CARNICERIA
        boton_carne  = Button(self.master, text="CARNICERIA",justify=CENTER,padx=12, height=5, width=20,
                               background="#d91c31", foreground="white",
                               command=lambda:abrir_carne()).place(x=190, y=300)
        def abrir_carne():
            carne = Toplevel()
            carne.title("INGRESE LOS PRODUCTOS DE CARNICERIA RELEVADOS")
            carne.geometry("700x600")
            carne.configure(bg="#fcfafa") 

            #LLAMA A LA CLASE TRAYENDO LOS ELEMENTOS DE CLASE RELEVAMIENTO               
            Carniceria (carne, self.var_relevadorx, self.var_domicilio, self.var_fecha)

             # NOTIFICA AL OBSERVADOR
            observador_ventanas.notificar(self.var_relevadorx.get() + "Se abrió la ventana de Carnicería")


        #VERDULERIA
        boton_verdu = Button(self.master, text="VERDULERIA", justify=CENTER,padx=12, height=5, width=20, background="#d91c31", foreground="white", command=lambda:abrir_verdu( )).place(x=370, y=300)
        def abrir_verdu():
            verdu = Toplevel()
            verdu.title("INGRESE LOS PRODUCTOS DE CARNICERIA RELEVADOS")
            verdu.geometry("700x600")
            verdu.configure(bg="#fcfafa") 
   
            #LLAMA A LA CLASE TRAYENDO LOS ELEMENTOS DE CLASE RELEVAMIENTO  
            Verduleria(verdu, self.var_relevadorx, self.var_domicilio, self.var_fecha)

            # NOTIFICA AL OBSERVADOR
            observador_ventanas.notificar( self.var_relevadorx.get() + "Se abrió la ventana de Verdulería")

        #FUNCIONES PARA ABRIR LA VENTANA ESTADISTICAS 
        def abrir_estadistica():
            ventana = Toplevel()
            ventana.title("bienvenido al modulo ESTADISTICAS")
            ventana.geometry("700x600")
            ventana.configure(bg="#fcfafa")
            
            Estadisticas(ventana)
            #NOTIFICA AL OBSERVADOR
            observador_ventanas.notificar("Se abrió la ventana de Estadísticas")


        #ESTADISTICAS
        ###########################
        #OJO DESACTIVE PEDIR CONTRASEñA LA FORMULA CORRECTA A LA QUE LLAMA EL BOTON ES PEDIR CONTRASEñA
        ###########################
        boton_est  = Button(self.master, text="ESTADISTICAS",justify=CENTER,padx=12, height=5, width=20, 
                                background="#d91c31", foreground="white",
                                command=lambda:abrir_estadistica()).place(x=550, y=300)
        
        #ELEGIR FECHA
        boton_fecha = Button(self.master, text="SELECCIONAR FECHA", justify=CENTER, padx=25, height=1, width=10, 
                                background="#679ab7", foreground="white", 
                                command=lambda: elegir_fecha(self.calendario, self.var_fecha)
                )
        boton_fecha.place(x=510, y=240)  

      
#CLASE QUE ADMINISTRA LA VENTANA SUPERMERCADO
class Supermercado():
    
            def __init__(self,master, var_relevador, var_domicilio, var_fecha):    #INICIALIZA LA CLASE
                
                self.supermercado = master
                self.conmodelo = Abmc()  #INICIALIZA LA CLASE Abmc DE MODELO
                
                #VARIABLES DE TKINTER Y LAS QUE VIENENE DE CLASE Y VENTANA RELEVAMIENTO
                self.var_id = IntVar()
                self.var_relevadorx =var_relevador
                self.var_domicilio =var_domicilio
                self.var_fecha =var_fecha
                self.var_producto = StringVar()
                self.var_marca1 = StringVar()
                self.var_precio1 = DoubleVar()
                self.var_marca2 = StringVar()
                self.var_precio2 = DoubleVar()

                #VARIABLE PARA LLAMAR A INSERTAR IMAGEN
                self.logo = insertar_imagen("CESOP solo LAM.png") 
                
                
                #ESTILO DE VENTANA
                style = ttk.Style(self.supermercado) 
                style.theme_use("default")
                style.configure("Treeview.Heading", background="#cd6065", foreground="white")

#LABELS Y ENTRY


                Label(self.supermercado, text = "INGRESE LOS PRODUCTOS RELEVADOS",background="#679ab7", foreground="white",).place(x = 250, y = 10)
                Label(self.supermercado, image= self.logo).place(x = 400, y = 100)
                
               #PRODUCTOS DE SUPERMERCADO 
                producto = Label(self.supermercado,bg="#fcfafa", text ="PRODUCTO")
                producto.place(x=50, y=80)
                entry_producto = ttk.Combobox(self.supermercado, values=["LECHE", "ARROZ", "PAN LACTAL", "GALLETITAS DE AGUA",
                                                        "GALLETITAS DULCES", "HARINA", "POLENTA", "FIDEOS", "AZUCAR",
                                                        "MERMELADA", "DULCE DE LECHE", "ARVEJAS", "TOMATE ENVASADO",
                                                        "QUESO CREMA"],textvariable=self.var_producto, state="readonly")
                entry_producto.place(x=130, y=80)
                
                #MARCA 1
                marca1 = Label(self.supermercado, bg="#fcfafa",text ="MARCA1")
                marca1.place(x=50, y=110)
                entry_marca1 = Entry(self.supermercado, textvariable=self.var_marca1)
                entry_marca1.place(x=130, y=110)

                #PRECIO 1
                precio1 = Label(self.supermercado, bg="#fcfafa",text ="PRECIO1")
                precio1.place(x=50, y=140)
                entry_precio1 = Entry(self.supermercado, textvariable=self.var_precio1)
                entry_precio1.place(x=130, y=140)

                 #MARCA 2
                marca2 = Label(self.supermercado, bg="#fcfafa",text ="MARCA2")
                marca2.place(x=50, y=170)
                entry_marca2 = Entry(self.supermercado, textvariable=self.var_marca2)
                entry_marca2.place(x=130, y=170)

                #PRECIO 2
                precio2 = Label(self.supermercado, bg="#fcfafa",text ="PRECIO2")
                precio2.place(x=50, y=200)
                entry_precio2 = Entry(self.supermercado, textvariable=self.var_precio2)
                entry_precio2.place(x=130, y=200)      


                # TREEVIWE
                #ESTILO DEL TREEVIEW
                style = ttk.Style()
                style.configure("Custom.Treeview", 
                                background="#f0f0f0", 
                                fieldbackground="#f0f0f0",
                                foreground="black")
                               
                #ESTILO DE HEAD DEL TREEVIEW               
                style.configure("Custom.Treeview.Heading", 
                                background="#d91c31",  
                                foreground="white",    
                                font=('Helvetica', 8 , 'bold'))  

                
                self.tree = ttk.Treeview(self.supermercado, style="Custom.Treeview")
                self.tree.tag_configure('oddrow', background="#f2f2f2")   #FILAS DE DISTINTOS COLORES
                self.tree.tag_configure('evenrow', background="white")   

                #COLUMNAS DEL TREEVIEW
                self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8")
                self.tree.column("#0", width=0, minwidth=0, anchor=W)
                self.tree.column("col1", width=100, minwidth=80, anchor=W)
                self.tree.column("col2", width=100, minwidth=80, anchor=W)
                self.tree.column("col3", width=100, minwidth=80, anchor=W)
                self.tree.column("col4", width=100, minwidth=80, anchor=W)
                self.tree.column("col5", width=100, minwidth=80, anchor=W)
                self.tree.column("col6", width=50, minwidth=30, anchor=W)
                self.tree.column("col7", width=100, minwidth=80, anchor=W)
                self.tree.column("col8", width=50, minwidth=30, anchor=W)

                #NOMBRES PARA EL HEADING
                self.tree.heading("#0", text="")
                self.tree.heading("col1",text ="RELEVADORX")
                self.tree.heading("col2",text ="DOMICILIO")
                self.tree.heading("col3",text="FECHA")
                self.tree.heading("col4", text="PRODUCTO")
                self.tree.heading("col5", text="MARCA1")
                self.tree.heading("col6",text="PRECIO1")
                self.tree.heading("col7", text="MARCA2")
                self.tree.heading("col8",text="PRECIO2")



                self.tree.place(x =10, y = 280)
            


            #BOTONES DE OPERACION
                
                #BOTON ELEGIR MARCA 1
                self.boton_e1  = Button(self.supermercado, text="ELEGIR MARCA 1",justify=CENTER,padx=9, height=1, width=10, background="#d91c31", foreground="white",
                                command=lambda: self.conmodelo.elegir_marca1(self.var_producto.get(), self.var_marca1, self.supermercado))         
                self.boton_e1.place(x=300, y=115)
                


                 #BOTON ELEGIR MARCA 2
                self.boton_e2 = Button(self.supermercado, text="ELEGIR MARCA 2",justify=CENTER,padx=9, height=1, width=10, background="#d91c31", foreground="white", 
                                command=lambda: self.conmodelo.elegir_marca2(self.var_producto.get(), self.var_marca2, self.supermercado))
                self.boton_e2.place(x=300, y=175)


                #BOTON GUARDAR
                self.boton_g = Button(self.supermercado, text="GUARDAR", justify=CENTER, padx=9, height=1, width=10, 
                                background="#679ab7", foreground="white", 
                                command=lambda: self.conmodelo.insertar(
                                    self.var_relevadorx.get(), 
                                    self.var_domicilio.get(),  
                                    self.var_fecha.get(),      
                                    self.var_producto.get(),    
                                    self.var_marca1.get(),     
                                    self.var_precio1.get(),     
                                    self.var_marca2.get(),     
                                    self.var_precio2.get(),     
                                    self.tree,                 
                                    self.var_producto,        
                                    self.var_marca1,           
                                    self.var_precio1,          
                                    self.var_marca2,           
                                    self.var_precio2           
                                ))
                self.boton_g.place(x=300, y=230)
                

               


                #BOTON ACRUALIZAR
                self.boton_a = Button(self.supermercado, text="ACTUALIZAR",justify=CENTER,padx=6, height=1, width=10, background="#679ab7", foreground="white",
                                command=lambda: self.conmodelo.actualizar(
                                                        self.var_relevadorx.get(),
                                                        self.var_domicilio.get(),
                                                        self.var_fecha.get(), 
                                                        self.var_producto.get(), 
                                                        self.var_marca1.get(), 
                                                        self.var_precio1.get(), 
                                                        self.var_marca2.get(), 
                                                        self.var_precio2.get(),
                                                        self.tree))
                self.boton_a.place(x=300, y=520)
                
                #BOTON ELIMINAR                        
                self.boton_b = Button(self.supermercado, text="ELIMINAR", justify=CENTER, padx=6, height=1, width=10, 
                                        background="#679ab7", foreground="white", 
                                        command=lambda: self.conmodelo.borrar(self.var_producto.get(), self.tree))
                self.boton_b.place(x=400, y=520)

                #BOTON SELECCIONAR FECHAS
                self.boton_f = Button(self.supermercado, text="SELECCIONAR FECHA", justify=CENTER, padx=25, height=1, width=10, 
                                        background="#679ab7", foreground="white", 
                                        command=lambda: self.conmodelo.elegir_fecha(self.calendario, self.var_fecha))
                

#CLASE QUE ADMINISTRA LA VENTANA CARNICERIA
class Carniceria():
    
            def __init__(self,master, var_relevador, var_domicilio, var_fecha):    #INICIALIZA LA CLASE
                self.carne = master
                        
                self.conmodelo = Abmc()      #INICIALIZA LA CLASE Abmc DE MODELO
                
                #VARIABLES DE TKINTER Y LAS QUE VIENENE DE RELEVAMIENTO
                self.var_id = IntVar()
                self.var_relevadorx = var_relevador
                self.var_domicilio = var_domicilio
                self.var_fecha = var_fecha
                self.var_producto = StringVar()
                self.var_marca1 = StringVar()
                self.var_precio1 = DoubleVar()
                self.var_marca2 = StringVar()
                self.var_precio2 = DoubleVar()

                #VARIABLE PARA LLAMAR A FUNCION INSERTAR IMAGEN
                self.logo = insertar_imagen("CESOP solo LAM.png")

                #ESTILO DE VENTANA CARNICERIA
                style = ttk.Style(self.carne) 
                style.theme_use("default")
                style.configure("Treeview.Heading", background="#cd6065", foreground="white")


#LABELS Y ENTRYS


                
                Label(self.carne, text = "INGRESE LOS PRODUCTOS RELEVADOS",background="#679ab7", foreground="white").place(x = 250, y = 10)
                Label(self.carne, image= self.logo).place(x = 400, y = 100)
                
                #PRODUCTO
                producto = Label(self.carne ,bg="#fcfafa", text ="PRODUCTO")
                producto.place(x=50, y=80)
                entry_producto = ttk.Combobox(self.carne, values=["ASADO", "CARNAZA", "ESPINAZO",
                                                                  "PALETA", "CARNE PICADA", "NALGA",
                                                                  "POLLO", "HIGADO", "FILET DE MERLUZA"],
                                                                  textvariable=self.var_producto, state="readonly")
                entry_producto.place(x=130, y=80)

                #PRECIO 
                precio1 = Label(self.carne, bg="#fcfafa",text ="PRECIO")
                precio1.place(x=50, y=110)
                entry_precio1 = Entry(self.carne, textvariable=self.var_precio1)
                entry_precio1.place(x=130, y=110)
                
               

                # TREEVIEW
                self.tree = ttk.Treeview(self.carne)
                
                #ESTILO TREEVIEW
                self.tree = ttk.Treeview(self.carne, style="Custom.Treeview")
                self.tree.tag_configure('oddrow', background="#f2f2f2")   
                self.tree.tag_configure('evenrow', background="white")   

                #COLUMNAS DEL TREEVIEW
                self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8")
                self.tree.column("#0", width=0, minwidth=0, anchor=W)
                self.tree.column("col1", width=100, minwidth=80, anchor=W)
                self.tree.column("col2", width=100, minwidth=80, anchor=W)
                self.tree.column("col3", width=100, minwidth=80, anchor=W)
                self.tree.column("col4", width=100, minwidth=80, anchor=W)
                self.tree.column("col5", width=100, minwidth=80, anchor=W)
                self.tree.column("col6", width=50, minwidth=30, anchor=W)
                self.tree.column("col7", width=100, minwidth=80, anchor=W)
                self.tree.column("col8", width=50, minwidth=30, anchor=W)



                #NOMBRES DE LAS COLUMNAS
                self.tree.heading("#0", text="")
                self.tree.heading("col1",text ="RELEVADORX")
                self.tree.heading("col2",text ="DOMICILIO")
                self.tree.heading("col3",text="FECHA")
                self.tree.heading("col4", text="PRODUCTO")
                self.tree.heading("col5", text="MARCA1")
                self.tree.heading("col6",text="PRECIO1")
                self.tree.heading("col7", text="MARCA2")
                self.tree.heading("col8",text="PRECIO2")



                self.tree.place(x =10, y = 230)





            #BOTONES DE OPERACION
                
               

                #BOTON GUARDAR
                self.boton_g = Button(self.carne, text="GUARDAR", justify=CENTER, padx=9, height=1, width=10, 
                                background="#679ab7", foreground="white", 
                                command=lambda: self.conmodelo.insertar(
                                    self.var_relevadorx.get(), 
                                    self.var_domicilio.get(),  
                                    self.var_fecha.get(),      
                                    self.var_producto.get(),    
                                    self.var_marca1.get(),     
                                    self.var_precio1.get(),     
                                    self.var_marca2.get(),     
                                    self.var_precio2.get(),     
                                    self.tree,                 
                                    self.var_producto,        
                                    self.var_marca1,           
                                    self.var_precio1,          
                                    self.var_marca2,           
                                    self.var_precio2           
                                ))
                self.boton_g.place(x=300, y=180)
                

                #BOTON ACTUALIZAR
                self.boton_a = Button(self.carne, text="ACTUALIZAR",justify=CENTER,padx=6, height=1, width=10, background="#679ab7", foreground="white",
                                command=lambda: self.conmodelo.actualizar(
                                                        self.var_relevadorx.get(),
                                                        self.var_domicilio.get(),
                                                        self.var_fecha.get(), 
                                                        self.var_producto.get(), 
                                                        self.var_marca1.get(), 
                                                        self.var_precio1.get(), 
                                                        self.var_marca2.get(), 
                                                        self.var_precio2.get(),
                                                        self.tree))
                self.boton_a.place(x=300, y=500)
                
                #BOTON ELIMINAR                      
                self.boton_b = Button(self.carne, text="ELIMINAR", justify=CENTER, padx=6, height=1, width=10, 
                                        background="#679ab7", foreground="white", 
                                        command=lambda: self.conmodelo.borrar(self.var_producto.get(), self.tree))
                self.boton_b.place(x=400, y=500)

         
#CLASE QUE ADMINISTRA LA VENTANA VERDULERIA
class Verduleria():
    
            def __init__(self,master, var_relevador, var_domicilio, var_fecha):   #INICIALIZA LA CLASE
                self.verdu = master
                        
                self.conmodelo = Abmc()        #INICIALIZA LA CLASE Abmc DE MODELO

                #VARIABLES DE TKINTER Y DE LA CLASE RELEVAMIENTO
                self.var_id = IntVar()
                self.var_relevadorx = var_relevador
                self.var_domicilio = var_domicilio
                self.var_fecha = var_fecha
                self.var_producto = StringVar()
                self.var_marca1 = StringVar()
                self.var_precio1 = DoubleVar()
                self.var_marca2 = StringVar()
                self.var_precio2 = DoubleVar()

                #VAIRABLE PARA INSERTAR IMAGEN
                self.logo = insertar_imagen("CESOP solo LAM.png")
                

                #ESTILO DE VENTANA
                style = ttk.Style(self.verdu) 
                style.theme_use("default")

               
#LABELS Y ENTRYS


               
                Label(self.verdu, text = "INGRESE LOS PRODUCTOS RELEVADOS",background="#679ab7", foreground="white").place(x = 250, y = 10)
                Label(self.verdu, image= self.logo).place(x = 400, y = 100)
                #PRODUCTO
                producto = Label(self.verdu ,bg="#fcfafa", text ="PRODUCTO")
                producto.place(x=50, y=80)
                entry_producto = ttk.Combobox(self.verdu, values=["ACELGA", "CEBOLLA", "LECHUGA",
                                                                  "TOMATE REDONDO", "ZANAHORIA", "PAPA BLANCA",
                                                                  "PAPA NEGRA", "BATATA", "MANZANA ROJA",
                                                                  "MANDARINA", "NARANJA", "BANANA", "PERA"],
                                                                  textvariable=self.var_producto, state="readonly")
                entry_producto.place(x=130, y=80)

                #PRECIO
                precio1 = Label(self.verdu, bg="#fcfafa",text ="PRECIO1")
                precio1.place(x=50, y=110)
                entry_precio1 = Entry(self.verdu, textvariable=self.var_precio1)
                entry_precio1.place(x=130, y=110)
                


# TREVIEW

                 #ESTILO DEL TREEVIEW
                self.tree = ttk.Treeview(self.verdu, style="Custom.Treeview")
                self.tree.tag_configure('oddrow', background="#f2f2f2")     #FILAS DE UN COLOR Y OTRO 
                self.tree.tag_configure('evenrow', background="white")   
                
                #ESTILO DEL HEADING DEL TREEVIEW
                style.configure("Treeview.Heading", background="#cd6065", foreground="white")
                              


                #COLUMNAS DEL TREEVIEW
                self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8")
                self.tree.column("#0", width=0, minwidth=0, anchor=W)
                self.tree.column("col1", width=100, minwidth=80, anchor=W)
                self.tree.column("col2", width=100, minwidth=80, anchor=W)
                self.tree.column("col3", width=100, minwidth=80, anchor=W)
                self.tree.column("col4", width=100, minwidth=80, anchor=W)
                self.tree.column("col5", width=100, minwidth=80, anchor=W)
                self.tree.column("col6", width=50, minwidth=30, anchor=W)
                self.tree.column("col7", width=100, minwidth=80, anchor=W)
                self.tree.column("col8", width=50, minwidth=30, anchor=W)



                #NOMBRE DE COLUMNAS
                self.tree.heading("#0", text="")
                self.tree.heading("col1",text ="RELEVADORX")
                self.tree.heading("col2",text ="DOMICILIO")
                self.tree.heading("col3",text="FECHA")
                self.tree.heading("col4", text="PRODUCTO")
                self.tree.heading("col5", text="MARCA1")
                self.tree.heading("col6",text="PRECIO1")
                self.tree.heading("col7", text="MARCA2")
                self.tree.heading("col8",text="PRECIO2")



                self.tree.place(x =10, y = 230)





            #BOTONES DE OPERACION
                
               

                #BOTON GUARDAR
                self.boton_g = Button(self.verdu, text="GUARDAR", justify=CENTER, padx=9, height=1, width=10, 
                                background="#679ab7", foreground="white", 
                                command=lambda: self.conmodelo.insertar(
                                    self.var_relevadorx.get(), 
                                    self.var_domicilio.get(),  
                                    self.var_fecha.get(),      
                                    self.var_producto.get(),    
                                    self.var_marca1.get(),     
                                    self.var_precio1.get(),     
                                    self.var_marca2.get(),     
                                    self.var_precio2.get(),     
                                    self.tree,                 
                                    self.var_producto,        
                                    self.var_marca1,           
                                    self.var_precio1,          
                                    self.var_marca2,           
                                    self.var_precio2           
                                ))
                self.boton_g.place(x=300, y=180)

                #BOTON ACTUALIZAR
                self.boton_a = Button(self.verdu, text="ACTUALIZAR",justify=CENTER,padx=6, height=1, width=10, background="#679ab7", foreground="white",
                                command=lambda: self.conmodelo.actualizar(
                                                        self.var_relevadorx.get(),
                                                        self.var_domicilio.get(),
                                                        self.var_fecha.get(), 
                                                        self.var_producto.get(), 
                                                        self.var_marca1.get(), 
                                                        self.var_precio1.get(), 
                                                        self.var_marca2.get(), 
                                                        self.var_precio2.get(),
                                                        self.tree))
                self.boton_a.place(x=300, y=500)
                
                #BOTON ELIMINAR     
                self.boton_b = Button(self.verdu, text="ELIMINAR", justify=CENTER, padx=6, height=1, width=10, 
                                     background="#679ab7", foreground="white", 
                                    command=lambda: self.conmodelo.borrar(self.var_producto.get(), self.tree))
                self.boton_b.place(x=400, y=500)

                #BOTON SELECCIONAR FECHA
                self.boton_f = Button(self.verdu, text="SELECCIONAR FECHA", justify=CENTER, padx=25, height=1, width=10, 
                                        background="#679ab7", foreground="white", 
                                        command=lambda: self.conmodelo.elegir_fecha(self.calendario, self.var_fecha))


#CLASE QUE ADMINISTRA LA VENTANA ESTADISTICAS
class Estadisticas():
    #INICIALIZA LA CLASE
    def __init__(self, master):
        self.ventana = master
        self.conmodelo = Abmc     #INICIALIZA LA CLASE Abmc DE MODELO
        self.conmodelo.crear_tablas(self)
        #ESTILO DE VENTANA
        style = ttk.Style(self.ventana) 
        style.theme_use("default")
        self.ventana.title("ESTADÍSTICAS DE RELEVAMIENTOS")
        self.ventana.geometry("750x600")
        

        #VARIABLES DE TKINTER Y QUE VIENEN DE RELEVAMIENTO
        self.producto_var = StringVar()
        self.marca_var = StringVar()

            
        #VARIABLE PARA INSERTAR IMAGEN
        self.logo = insertar_imagen("CESOP solo LAM.png")

#LABELS Y ENTRY
        Label(self.ventana, text = "MODULO ESTADISTICAS",background="#679ab7", foreground="white").place(x = 250, y = 10)
        
        #Label(self.ventana , image = self.logo).place(x = 400, y = 100)
        
        #PRODUCTOS (POR AHORA SOLO SUPERMERCADO)
        Label(self.ventana, bg="#d91c31", foreground="white", text ="PRODUCTO").place(x = 20, y=70)
        productos = self.conmodelo.obtener_productos_unicos()
        self.producto_menu = OptionMenu(self.ventana, self.producto_var, "")
        self.producto_menu.place(x=150, y=70)
        
        #MARCA
        Label(self.ventana, bg="#d91c31", foreground="white", text="MARCA").place(x = 20, y = 120)
        self.marca_menu = OptionMenu(self.ventana, self.marca_var, "")
        self.marca_menu.place(x=150, y=120)

        self.producto_var.trace_add("write", self.actualizar_marcas)
#FECHA DE INICIO
        Label(self.ventana, bg="#d91c31", foreground="white", text="FECHA DE INICIO (YYYY-MM-DD):").place(x = 20, y=110)
        self.fecha_inicio_entry = Entry(self.ventana)
        self.fecha_inicio_entry.place(x=150, y=110)
        
#FECHA DE CIERRE
        Label (self.ventana, bg="#d91c31", foreground="white", text="FECHA DE CIERRE (YYYY-MM-DD):").grid(row=3, column=0, sticky="e")
        self.fecha_fin_entry = ttk.Entry(self.ventana)
        self.fecha_fin_entry.place(x=150, y=150)


         #BOTONES DE OPERACION
        #BOTON CALCULAR ESTADISITICA
        
        self.boton_calcular = Button(self.ventana, text="CALCULAR ESTADISTICA", justify=CENTER, padx=12, height=5,width=15,
                                     background= "#d91c31", foreground="white",
                                     command=self.calcular)
        self.boton_calcular.place(x=50, y=250)

        self.resultado_text = Text(self.ventana, height=10, width=60)
        self.resultado_text.place(x=150, y=250)

        
    def actualizar_marcas(self, *args):
        producto = self.producto_var.get()
        marcas = self.conmodelo.obtener_marcas_por_producto(producto) if producto else []

        menu = self.marca_menu["menu"]
        menu.delete(0, "end")
        for marca in marcas:
            menu.add_command(label=marca, command=lambda m=marca: self.marca_var.set(m))
        self.marca_var.set("")

    def calcular(self):
        producto = self.producto_var.get()
        marca = self.marca_var.get()
        fecha_inicio = self.fecha_inicio_entry.get() or None
        fecha_fin = self.fecha_fin_entry.get() or None

        try:
            if fecha_inicio:
                datetime.strptime(fecha_inicio, '%Y-%m-%d')
            if fecha_fin:
                datetime.strptime(fecha_fin, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Use YYYY-MM-DD.")
            return

        resultado = self.conmodelo.calcular_estadisticas_filtradas(producto or None, marca or None, fecha_inicio, fecha_fin)

        self.resultado_text.delete("1.0", Tk.END)

        if resultado:
            texto = f"Producto: {resultado['producto']}\n"
            texto += f"Precio mínimo: {resultado['precio_min']:.2f}\n"
            texto += f"Precio máximo: {resultado['precio_max']:.2f}\n"
            texto += f"Precio medio: {resultado['precio_medio']:.2f}\n"
            texto += f"Precio ponderado: {resultado['precio_ponderado']:.2f}\n"
            texto += f"Fecha de cálculo: {resultado['fecha_calculo']}\n"
            self.resultado_text.insert(tk.END, texto)
            self.conmodelo.guardar_estadisticas(resultado)
        else:
            self.resultado_text.insert(Tk.END, "No se encontraron datos para los filtros seleccionados.")



"""#TREEVIEW
 

        self.tree = ttk.Treeview(self.ventana)
        self.tree.tag_configure('oddrow', background="#f2f2f2")   #UN COLOR Y OTRO EN LAS FILAS
        self.tree.tag_configure('evenrow', background="white")   

        #ESTILO DEL TREEVIEW
        style.configure("Treeview.Heading", background="#cd6065", foreground="white")
        #ESTILO  DEL HEADING DEL TREEVIEW
        style.configure("Custom.Treeview.Heading", 
                                background="#d91c31",  
                                foreground="white",    
                                font=('Helvetica', 8 , 'bold')) 
        
        
      
        #COLUMNAS DEL TREEVIEW
        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8")
        self.tree.column("#0", width=0, minwidth=0, anchor=W)
        self.tree.column("col1", width=100, minwidth=80, anchor=W)
        self.tree.column("col2", width=100, minwidth=80, anchor=W)
        self.tree.column("col3", width=100, minwidth=80, anchor=W)
        self.tree.column("col4", width=100, minwidth=80, anchor=W)
        self.tree.column("col5", width=100, minwidth=80, anchor=W)
        self.tree.column("col6", width=50, minwidth=30, anchor=W)
        self.tree.column("col7", width=100, minwidth=80, anchor=W)
        self.tree.column("col8", width=50, minwidth=30, anchor=W)

        #NOMBRES DE COLUMNAS
        self.tree.heading("#0", text="")
        self.tree.heading("col1",text ="RELEVADORX")
        self.tree.heading("col2",text ="DOMICILIO")
        self.tree.heading("col3",text="FECHA")
        self.tree.heading("col4", text="PRODUCTO")
        self.tree.heading("col5", text="MARCA1")
        self.tree.heading("col6",text="PRECIO1")
        self.tree.heading("col7", text="MARCA2")
        self.tree.heading("col8",text="PRECIO2")

        self.tree.place(x=10, y=350, width=700, height=200)"""

       
   

#FUNCIONES AUXILIARES? DE LA VISTA
#FUNCION GENERAL DE ELEGIR FECHA DEL CALENDARIO
def elegir_fecha(calendario, var_fecha):
        fecha_seleccionada = calendario.get_date()
        var_fecha.set(fecha_seleccionada)



#PIDE CONTASEñA
def pedir_contra():        
        #CREA VENTANA EMERGENTE
        verif = Toplevel()
        verif.geometry ("300x200")
        verif.configure(bg="#ccd9df")
        verif.resizable(False, False)

        #VARIABLES DE TKINTER
        contra_var = StringVar()
        usuario_var = StringVar()

        #ESTILO DE VENTANA
        style = ttk.Style(verif) 
        style.theme_use("default")
        style.configure("Treeview.Heading",background="#ce8f92", foreground="white")

#LABELS Y ENTRYS
        #USUARIO           
        Label(verif,bg="#ccd9df", text = "USUARIO").place(x = 20, y = 50)
        usuario_entry = Entry (verif, textvariable = usuario_var)
        usuario_entry .place(x=150, y= 50)
        usuario_entry.focus_set() 
        #CONTRASEñA
        Label(verif,bg="#ccd9df", text = "CONTRASEÑA").place(x = 20, y = 125)
        contra_entry = Entry (verif, textvariable= contra_var, show = "*")
        contra_entry .place(x=150, y=125)
        #BOTON INGRESAR
        Button(verif, text="INGRESAR", bg="#d91c31", fg="white", command=lambda:verificar(usuario_var,contra_var, verif)).place(x=110, y=160)
        
#VERIFICA CONTRASEñA Y USUARIO     
def verificar(usuario_var, contra_var,ventana):
      
      #contra_var = StringVar()
      #usuario_var = StringVar()
      #DEFINE VALORES VALIDOS PARA USUARIO Y CONTRASEñA
      USUARIO_VALIDO = "admin"
      CONTRASEÑA_VALIDA = "1234"
      
      if  usuario_var.get() == USUARIO_VALIDO and  contra_var.get() == CONTRASEÑA_VALIDA:
       
       ventana.destroy()
       abrir_estadistica()
      else:
            messagebox.showinfo("USUARIO O CONTRASEÑA INCORRECTA")
                 


      
       















