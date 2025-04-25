from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import os, re
from modelo import Abmc


class Relevamiento():
       def __init__(self,master):
        
        self.master = master
        self.conmodelo = Abmc()        
                        
        self.master.geometry("750x400")
        self.master.title("RELEVAMIENTO DE PRECIOS")
        self.master.configure(bg="#ccd9df")
            
        style = ttk.Style(self.master) 
        style.theme_use("default")
        style.configure("Treeview.Heading",background="#ce8f92", foreground="white")

        self.var_id = IntVar()
        self.var_relevadorx = StringVar()
        self.var_domicilio = StringVar()
        self.var_fecha = StringVar()
        self.var_producto = StringVar()
        self.var_marca1 = StringVar()
        self.var_precio1 = DoubleVar()
        self.var_marca2 = StringVar()
        self.var_precio2 = DoubleVar()
        
        

        #IMAGEN LOGO CESOP

        BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 


        STATIC_ROOT = os.path.join(BASE_DIR, "imagenes", "CESOP solo LAM.png")  

        if not os.path.exists(STATIC_ROOT):
            raise FileNotFoundError(f"No se encontró la imagen en la ruta: {STATIC_ROOT}")

        self.logo = PhotoImage(file=STATIC_ROOT)



        #INSERTA CALENDARIO PARA SELECCIONAR FECHA

        self.calendario = Calendar(self.master,
                    background="#9eafb7",
                    selectbackground="#679ab7",
                    normalbackground="#8c8e8f",
                    weekendbackground="#d7878b",
                                        )

        self.calendario.place(x = 450, y = 50)



#label/entry


        Label(self.master,bg="#fcfafa", image= self.logo).place(x = 10, y = 10)
        Label(self.master, text = "INGRESE TIPO DE COMERCIO",background="#679ab7", foreground="white").place(x = 160, y = 10)
        barrio = Label (self.master, bg="#ce8f92", text ="BARRIO")
        barrio.place(x=160, y=100)
        relevadorx = Label (self.master,bg="#ce8f92", text ="RELEVADORX")
        relevadorx.place(x=160, y=60)
        fecha = Label(self.master,bg="#ce8f92", text ="FECHA")
        fecha.place(x=160, y=150)


        entry_fecha = Entry(self.master, textvariable=self.var_fecha, )
        entry_fecha.place(x=250, y=150)
        entry_relevadorx= ttk.Combobox(values=["ARACELI", "MARCIA", "ADMINSTRADOR"],
                                            textvariable=self.var_relevadorx)
        entry_relevadorx.place(x=250, y=60)
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
                                                "VILLA SOLDATI", "VILLA URQUIZA"],textvariable=self.var_domicilio)
        entry_domicilio.place(x=250, y=100)


        boton_super  = Button(self.master, text="SUPERMERCADO",justify=CENTER,padx=12, height=5, width=20, background="#cd6065", foreground="white",command=lambda:abrir_super( ))
        boton_super.place(x=10, y=300)
        boton_carne  = Button(self.master, text="CARNICERIA",justify=CENTER,padx=12, height=5, width=20, background="#cd6065", foreground="white",command=lambda:abrir_carne( )).place(x=190, y=300)
        boton_verdu = Button(self.master, text="VERDULERIA",justify=CENTER,padx=12, height=5, width=20, background="#cd6065", foreground="white", command=lambda:abrir_verdu( )).place(x=370, y=300)
        boton_est  = Button(self.master, text="ESTADISTICAS",justify=CENTER,padx=12, height=5, width=20, background="#cd6065", foreground="white", command=lambda:pedir_contra()).place(x=550, y=300)
        boton_fecha = Button(
                        self.master, text="SELECCIONAR FECHA", justify=CENTER, padx=25, height=1, width=10, 
                        background="#679ab7", foreground="white", 
                        command=lambda: elegir_fecha(self.calendario, self.var_fecha)
                )
        boton_fecha.place(x=510, y=240)  

      

class Supermercado():
    
            def __init__(self,pato):
                self.supermercado = pato
                self.conmodelo = Abmc()
                

                self.var_id = IntVar()
                self.var_relevadorx = StringVar()
                self.var_domicilio = StringVar()
                self.var_fecha = StringVar()
                self.var_producto = StringVar()
                self.var_marca1 = StringVar()
                self.var_precio1 = DoubleVar()
                self.var_marca2 = StringVar()
                self.var_precio2 = DoubleVar()


                style = ttk.Style(self.supermercado) 
                style.theme_use("default")
                style.configure("Treeview.Heading", background="#cd6065", foreground="white")

                #label/entry


                Label(self.supermercado, text = "INGRESE LOS PRODUCTOS RELEVADOS",background="#679ab7", foreground="white").place(x = 250, y = 10)
                
                
                producto = Label(self.supermercado,bg="#fcfafa", text ="PRODUCTO")
                producto.place(x=50, y=80)
                marca1 = Label(self.supermercado, bg="#fcfafa",text ="MARCA1")
                marca1.place(x=50, y=110)
                precio1 = Label(self.supermercado, bg="#fcfafa",text ="PRECIO1")
                precio1.place(x=50, y=140)
                marca2 = Label(self.supermercado, bg="#fcfafa",text ="MARCA2")
                marca2.place(x=50, y=170)
                precio2 = Label(self.supermercado, bg="#fcfafa",text ="PRECIO2")
                precio2.place(x=50, y=200)

               


                entry_producto = ttk.Combobox(self.supermercado, values=["LECHE", "ARROZ", "PAN LACTAL", "GALLETITAS DE AGUA",
                                                        "GALLETITAS DULCES", "HARINA", "POLENTA", "FIDEOS", "AZUCAR",
                                                        "MERMELADA", "DULCE DE LECHE", "ARVEJAS", "TOMATE ENVASADO",
                                                        "QUESO CREMA"],textvariable=self.var_producto)
                entry_producto.place(x=130, y=80)
                
                entry_marca1 = Entry(self.supermercado, textvariable=self.var_marca1)
                entry_marca1.place(x=130, y=110)
                entry_precio1 = Entry(self.supermercado, textvariable=self.var_precio1)
                entry_precio1.place(x=130, y=140)
                entry_marca2 = Entry(self.supermercado, textvariable=self.var_marca2)
                entry_marca2.place(x=130, y=170)
                entry_precio2 = Entry(self.supermercado, textvariable=self.var_precio2)
                entry_precio2.place(x=130, y=200)



                # Treeview
                self.tree = ttk.Treeview(self.supermercado)
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
                
                self.boton_e1  = Button(self.supermercado, text="ELEGIR MARCA 1",justify=CENTER,padx=9, height=1, width=10, background="#cd6065", foreground="white",
                                command=lambda: self.conmodelo.elegir_marca1(self.var_producto.get(), self.var_marca1, self.supermercado))
                
                self.boton_e1.place(x=300, y=115)

                self.boton_e2 = Button(self.supermercado, text="ELEGIR MARCA 2",justify=CENTER,padx=9, height=1, width=10, background="#cd6065", foreground="white", 
                                command=lambda: self.conmodelo.elegir_marca2(self.var_producto.get(), self.var_marca2, self.supermercado))
                self.boton_e2.place(x=300, y=175)

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
                self.supermercado.lift()
                self.supermercado.focus_force()

               



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
                
                                        
                self.boton_b = Button(
                self.supermercado, text="ELIMINAR", justify=CENTER, padx=6, height=1, width=10, 
                background="#679ab7", foreground="white", 
                command=lambda: self.conmodelo.borrar(self.var_producto.get(), self.tree))
                self.boton_b.place(x=400, y=520)


                self.boton_f = Button(
                self.supermercado, text="SELECCIONAR FECHA", justify=CENTER, padx=25, height=1, width=10, 
                background="#679ab7", foreground="white", 
                command=lambda: self.conmodelo.elegir_fecha(self.calendario, self.var_fecha))
                


class Carniceria():
    
            def __init__(self,pato):
                self.carne = pato
                        
                self.conmodelo = Abmc()

                self.var_id = IntVar()
                self.var_relevadorx = StringVar()
                self.var_domicilio = StringVar()
                self.var_fecha = StringVar()
                self.var_producto = StringVar()
                self.var_marca1 = StringVar()
                self.var_precio1 = DoubleVar()
                self.var_marca2 = StringVar()
                self.var_precio2 = DoubleVar()


                style = ttk.Style(self.carne) 
                style.theme_use("default")
                style.configure("Treeview.Heading", background="#cd6065", foreground="white")


                #label/entry


                
                Label(self.carne, text = "INGRESE LOS PRODUCTOS RELEVADOS",background="#679ab7", foreground="white").place(x = 250, y = 10)
                
                producto = Label(self.carne ,bg="#fcfafa", text ="PRODUCTO")
                producto.place(x=50, y=80)
                precio1 = Label(self.carne, bg="#fcfafa",text ="PRECIO1")
                precio1.place(x=50, y=110)
                
                entry_producto = ttk.Combobox(self.carne, values=["ASADO", "CARNAZA", "ESPINAZO",
                                                                  "PALETA", "CARNE PICADA", "NALGA",
                                                                  "POLLO", "HIGADO", "FILET DE MERLUZA"],
                                                                  textvariable=self.var_producto)
                entry_producto.place(x=130, y=80)
               
                
                entry_precio1 = Entry(self.carne, textvariable=self.var_precio1)
                entry_precio1.place(x=130, y=110)
                


                # Treeview
                self.tree = ttk.Treeview(self.carne)
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
                self.var_producto.focus_set


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
                
                                        
                self.boton_b = Button(
                self.carne, text="ELIMINAR", justify=CENTER, padx=6, height=1, width=10, 
                background="#679ab7", foreground="white", 
                command=lambda: self.conmodelo.borrar(self.var_producto.get(), self.tree))
                self.boton_b.place(x=400, y=500)


            

class Verduleria():
    
            def __init__(self,pato):
                self.verdu = pato
                        
                self.conmodelo = Abmc()

                self.var_id = IntVar()
                self.var_relevadorx = StringVar()
                self.var_domicilio = StringVar()
                self.var_fecha = StringVar()
                self.var_producto = StringVar()
                self.var_marca1 = StringVar()
                self.var_precio1 = DoubleVar()
                self.var_marca2 = StringVar()
                self.var_precio2 = DoubleVar()


                style = ttk.Style(self.verdu) 
                style.theme_use("default")
                style.configure("Treeview.Heading", background="#cd6065", foreground="white")

               

                #label/entry


               
                Label(self.verdu, text = "INGRESE LOS PRODUCTOS RELEVADOS",background="#679ab7", foreground="white").place(x = 250, y = 10)
                
                producto = Label(self.verdu ,bg="#fcfafa", text ="PRODUCTO")
                producto.place(x=50, y=80)
                precio1 = Label(self.verdu, bg="#fcfafa",text ="PRECIO1")
                precio1.place(x=50, y=110)
                
                entry_producto = ttk.Combobox(self.verdu, values=["ACELGA", "CEBOLLA", "LECHUGA",
                                                                  "TOMATE REDONDO", "ZANAHORIA", "PAPA BLANCA",
                                                                  "PAPA NEGRA", "BATATA", "MANZANA ROJA",
                                                                  "MANDARINA", "NARANJA", "BANANA", "PERA"],
                                                                  textvariable=self.var_producto)
                entry_producto.place(x=130, y=80)
               
                
                entry_precio1 = Entry(self.verdu, textvariable=self.var_precio1)
                entry_precio1.place(x=130, y=110)
                


                # Treeview
                self.tree = ttk.Treeview(self.verdu)
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
                
                                        
                self.boton_b = Button(
                self.verdu, text="ELIMINAR", justify=CENTER, padx=6, height=1, width=10, 
                background="#679ab7", foreground="white", 
                command=lambda: self.conmodelo.borrar(self.var_producto.get(), self.tree))
                self.boton_b.place(x=400, y=500)


                self.boton_f = Button(
                self.verdu, text="SELECCIONAR FECHA", justify=CENTER, padx=25, height=1, width=10, 
                background="#679ab7", foreground="white", 
                command=lambda: self.conmodelo.elegir_fecha(self.calendario, self.var_fecha))



class Estadisticas():
    def __init__(self, pato):
        self.ventana = pato
        self.conmodelo = Abmc()
        self.ventana.title("ESTADÍSTICAS DE RELEVAMIENTOS")
        self.ventana.geometry("750x600")
           


def abrir_super():
    supermercado = Toplevel()
    supermercado.title("INGRESE LOS PRODUCTOS RELEVADOS")
    supermercado.geometry("750x600")
    supermercado.configure(bg="#fcfafa") 
   
               
    op1 = Supermercado (supermercado)

def abrir_carne():
    carne = Toplevel()
    carne.title("INGRESE LOS PRODUCTOS DE CARNICERIA RELEVADOS")
    carne.geometry("700x600")
    carne.configure(bg="#fcfafa") 
   
               
    op2 = Carniceria(carne)

def abrir_verdu():
    verdu = Toplevel()
    verdu.title("INGRESE LOS PRODUCTOS DE CARNICERIA RELEVADOS")
    verdu.geometry("700x600")
    verdu.configure(bg="#fcfafa") 
   
               
    op2 = Verduleria(verdu)

def abrir_estadistica():
            estas = Toplevel()
            estas.title("bienvenido al modulo ESTADITICAS")
            estas.geometry("700x600")
            estas.configure(bg="#fcfafa") 
            Estadisticas(estas)



def pedir_contra():        
        verif = Toplevel()
        verif.geometry ("300x200")
        verif.configure(bg="#ccd9df")
        verif.resizable(False, False)

        contra_var = StringVar()
        usuario_var = StringVar()
        style = ttk.Style(verif) 
        style.theme_use("default")
        style.configure("Treeview.Heading",background="#ce8f92", foreground="white")
                
        Label(verif,bg="#ccd9df", text = "USUARIO").place(x = 20, y = 50)
        usuario_entry = Entry (verif, textvariable = usuario_var)
        usuario_entry .place(x=150, y= 50)
        usuario_entry.focus_set() 
        Label(verif,bg="#ccd9df", text = "CONTRASEÑA").place(x = 20, y = 125)
        contra_entry = Entry (verif, textvariable= contra_var, show = "*")
        contra_entry .place(x=150, y=125)
        Button(verif, text="INGRESAR", bg="#cd6065", fg="white", command=lambda:verificar(usuario_var,contra_var, verif)).place(x=110, y=160)
        
    
        
def verificar(usuario_var, contra_var,ventana):
      
      #contra_var = StringVar()
      #usuario_var = StringVar()
      USUARIO_VALIDO = "admin"
      CONTRASEÑA_VALIDA = "1234"
      
      if  usuario_var.get() == USUARIO_VALIDO and  contra_var.get() == CONTRASEÑA_VALIDA:
       
       ventana.destroy()
       abrir_estadistica()
      else:
            messagebox.showinfo("USUARIO O CONTRASEÑA INCORRECTA")
                 

def elegir_fecha(calendario, var_fecha):
        fecha_seleccionada = calendario.get_date()
        var_fecha.set(fecha_seleccionada)
      
       















