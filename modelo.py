
import sqlite3
import re
from tkinter import messagebox, OptionMenu
from observador import Subject



#################
#MODELO
#################



class Abmc(Subject):
    def __init__(self):
            super().__init__()  # Inicializa clase Subject
            try:
                self.con = self.crear_base() 
                self.crear_tabla(self.con)    
            except:
                print("ERROR DE CONEXION")
                ###VARIABLES DE SUPERMERCADO


            self.leche = ("LA SERENISIMA", "SANCOR", "ARMONIA", "LA MARTONA", "OTRA")
            self.arroz = ("GALLO", "LUCCHETTI", "DOS HERMANOS", "MOLINOS ALA", "CAÑUELAS", "OTRA")
            self.pan_lactal = ("BIMBO", "LACTAL", "FARGO", "LA SALTEÑA", "LA PERLA", "FACILITAS", "OTRA")
            self.galletitas_de_agua = ("EXPRESS", "MEDIA TARDE", "CRIOLLITAS", "TRAVIATA", "SERRANITAS", "OTRA")
            self.galletitas_dulces = ("DIVERSION", "VARIEDAD", "SURTIDO BAGLEY", "OTRA")
            self.harina = ("MORIXE", "CAÑUELAS", "FAVORITA", "BLANCAFLOR", "CASERITA", "HARINISIMA", "OTRA")
            self.polenta = ("MORIXE", "PRESTOPRONTA", "SYP", "DEL CAMPO", "NOEL", "EGRAN", "OTRA")
            self.fideos = ("MATARAZZO", "LUCCHETTI", "FAVORITA", "KNOR", "MAROLIO", "PASTASOLA", "OTRA")
            self.azucar = ("LEDESMA", "CHANGO", "ARCOR", "SWETELLA", "LA CAMPECHANA", "DELICADA", "OTRA")
            self.mermelada = ("LA CAMPAGNOLA", "ARCOR", "EMETH", "DULCOR", "NOEL", "OTRA")
            self.dulce_de_leche = ("LA SERENISIMA COLONIAL", "LA SERENISIMA CLASICO", "SANCOR", "MILKAUT", "VERONICA", "ARMONIA","PUNTA DE AGUA", "LA PAULINA", "OTRA")
            self.arvejas = ("ARCOR", "INCA", "LA CAMPAGNOLA", "LA BANDA", "CARACAS", "INALPA", "OTRA")
            self.tomate_envasado = ("ARCOR", "INCA", "LA CAMPAGNOLA", "MOLTO", "MAROLIO", "NOEL", "CANALE", "OTRA")
            self.queso_crema = ("CASANCREM", "MENDICRIM", "LA PAULINA", "LA SERENISIMA", "LECHELITA", "FINLANDIA", "MILKAUT", "OTRA")


    def crear_base(self,):
        self.con = sqlite3.connect('relevamiento_precios.db')
        return self.con
        

    def crear_tabla(self, con):

        cursor = con.cursor()
        sql = "CREATE TABLE IF NOT EXISTS precios (id INTEGER PRIMARY KEY AUTOINCREMENT, relevadorx TEXT, domicilio TEXT, fecha TEXT, producto TEXT , marca1 TEXT, precio1 REAL, marca2 TEXT, precio2 REAL)"
        cursor.execute(sql)
        con.commit()



    



    def insertar(self, relevadorx, domicilio, fecha, producto, marca1, precio1, marca2, precio2, tree, var_producto, var_marca1, var_precio1, var_marca2, var_precio2, *args):
        cursor = self.con.cursor()
        
        #Validación de fecha con regex
        #patron = r"^\d{1,2}[-/]\d{1,2}[-/]\d{2,4}$"
        #if not re.match(patron, fecha):
            #messagebox.showinfo(message="FORMATO INVALIDO DE FECHA", title="RELEVAMIENTO DE PRECIOS")
            #return

        
        sql = """INSERT INTO precios (relevadorx, domicilio, fecha, producto, marca1, precio1, marca2, precio2)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
        data = (relevadorx, domicilio, fecha, producto, marca1, precio1, marca2, precio2)
        cursor.execute(sql, data)
        self.con.commit()

        tree.insert("", "end", values=(relevadorx, domicilio, fecha, producto, marca1, precio1, marca2, precio2))

        var_producto.set("")  
        var_marca1.set("")   
        var_precio1.set(0.0)  
        var_marca2.set("")    
        var_precio2.set(0.0)  

        messagebox.showinfo("Información", "Producto cargado correctamente, continue con el siguiente")
        self.notificar (relevadorx,domicilio)
        self.abrir_ventana_top_level()
        
        


    

    def actualizar(self, relevadorx, domicilio, fecha, producto, marca1, precio1, marca2, precio2, tree):
        selected_item = tree.selection()
        if not selected_item:  
            messagebox.showinfo("Advertencia", "No hay un producto seleccionado para actualizar")
            return
        
        # Validación de fecha con regex
        patron = r"^\d{1,2}[-/]\d{1,2}[-/]\d{2,4}$"
        if not re.match(patron, fecha):
            messagebox.showinfo(message="FORMATO INVALIDO DE FECHA", title="RELEVAMIENTO DE PRECIOS")
            return
            
                
        cursor = self.con.cursor()
        sql = """UPDATE precios SET relevadorx = ?, domicilio = ?, fecha = ?, marca1 = ?, precio1 = ?, marca2 = ?, precio2 = ? WHERE producto = ?;"""
        data = (relevadorx, domicilio, fecha, marca1, precio1, marca2, precio2, producto)
        cursor.execute(sql, data)
        self.con.commit()

        
        tree.item(selected_item, values=(relevadorx, domicilio, fecha, producto, marca1, precio1, marca2, precio2))

        messagebox.showinfo("Información", "El producto fue actualizado exitosamente")
        self.notificar(relevadorx, domicilio, "update")


    def borrar(self, producto, tree):
        selected_item = tree.selection()
        if not selected_item:  
            messagebox.showinfo("Advertencia", "No hay un producto seleccionado para eliminar")
            return
            
            
        cursor = self.con.cursor()
        sql = "DELETE FROM precios WHERE producto = ?;"
        cursor.execute(sql, (producto,))
        self.con.commit()
        tree.delete(selected_item)
        messagebox.showinfo("Información", "La carga fue eliminado exitosamente")
        self.notificar(producto, "delete")

    def elegir_marca1(self, producto, var_marca1, master):
        
        if producto == "LECHE":
            marcas = self.leche
        elif producto == "ARROZ":
            marcas = self.arroz
        elif producto == "PAN LACTAL":
            marcas = self.pan_lactal
        elif producto == "GALLETITAS DE AGUA":
            marcas = self.galletitas_de_agua
        elif producto == "GALLETITAS DULCES":
            marcas = self.galletitas_dulces
        elif producto == "HARINA":
            marcas = self.harina
        elif producto == "POLENTA":
            marcas = self.polenta
        elif producto == "FIDEOS":
            marcas = self.fideos
        elif producto == "AZUCAR":
            marcas = self.azucar
        elif producto == "MERMELADA":
            marcas = self.mermelada
        elif producto == "DULCE DE LECHE":
            marcas = self.dulce_de_leche
        elif producto == "ARVEJAS":
            marcas = self.arvejas
        elif producto == "TOMATE ENVASADO":
            marcas = self.tomate_envasado
        elif producto == "QUESO CREMA":
            marcas = self.queso_crema
        else:
            marcas = []
        
        if marcas:
            master.menu_marca1 = OptionMenu(master, var_marca1, *marcas)
            master.menu_marca1.place(x=400, y=115)  
        else:
            var_marca1.set("")  


    def elegir_marca2(self, producto, var_marca2, master):
        
        if producto == "LECHE":
            marcas = self.leche
        elif producto == "ARROZ":
            marcas = self.arroz
        elif producto == "PAN LACTAL":
            marcas = self.pan_lactal
        elif producto == "GALLETITAS DE AGUA":
            marcas = self.galletitas_de_agua
        elif producto == "GALLETITAS DULCES":
            marcas = self.galletitas_dulces
        elif producto == "HARINA":
            marcas = self.harina
        elif producto == "POLENTA":
            marcas = self.polenta
        elif producto == "FIDEOS":
            marcas = self.fideos
        elif producto == "AZUCAR":
            marcas = self.azucar
        elif producto == "MERMELADA":
            marcas = self.mermelada
        elif producto == "DULCE DE LECHE":
            marcas = self.dulce_de_leche
        elif producto == "ARVEJAS":
            marcas = self.arvejas
        elif producto == "TOMATE ENVASADO":
            marcas = self.tomate_envasado
        elif producto == "QUESO CREMA":
            marcas = self.queso_crema
        else:
            marcas = []

    
        if marcas:
            master.menu_marca2 = OptionMenu(master, var_marca2, *marcas)
            master.menu_marca2.place(x=400, y=175)  
        else:
            var_marca2.set("") 
            



   