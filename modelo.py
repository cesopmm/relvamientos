
import sqlite3
import re
from tkinter import messagebox, OptionMenu
from observador import Subject
import pandas as pd
from datetime import datetime




#################
#MODELO
#################



class Abmc(Subject):
    def __init__(self):
            super().__init__()  #INICIA CLASE SUBJECT
            try:
                self.con = self.crear_base() 
                self.crear_tablas(self.con)    
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

#CREACION BASE SQL
    def crear_base(self,):
        self.con = sqlite3.connect('relevamiento_precios.db')
        return self.con
    
    def conectar():
        conn = sqlite3.connect('relevamiento_precios.db')
        cursor = conn.cursor()
        return conn, cursor
    
#CREA TABLA PRECIOS y ESTADISTICAS
    def crear_tablas(self,):
        conn, cursor = self.conectar()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto TEXT,
                marca TEXT,
                precio REAL,
                fecha TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS estadisticas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto TEXT,
                precio_min REAL,
                precio_max REAL,
                precio_medio REAL,
                precio_ponderado REAL,
                fecha_calculo TEXT
            )
        ''')
        conn.commit()
        conn.close()
    


#AGREGA PRODUCTOS PRECIOS MARCAS A LA TABLA
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

        #TREVIEW CAMBIA DE COLOR POR FILAS
        current_items = len(tree.get_children())
        if current_items % 2 == 0:
                    tree.insert("", "end", values=(relevadorx, domicilio, fecha, producto, marca1, precio1, marca2, precio2), tags=('evenrow',))
        else:
                    tree.insert("", "end", values=(relevadorx, domicilio, fecha, producto, marca1, precio1, marca2, precio2), tags=('oddrow',))

        var_producto.set("")  
        var_marca1.set("")   
        var_precio1.set(0.0)  
        var_marca2.set("")    
        var_precio2.set(0.0)  

        messagebox.showinfo("Información", "Producto cargado correctamente, continue con el siguiente")
        self.notificar (relevadorx,domicilio)
        self.supermercado.lift()
        self.supermercado.focus_force()
        
#ACTUALIZA TABLA Y TREEVIER 
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

#ELIMINA ITEM SELECCIONADO DEL TREEVIEW
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

#PERMITE ELEGIR LA MARCA DEL PRODUCTO SELECCIONADO
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
            

#PERMITE ELEGIR LA MARCA DEL PRODUCTO SELECCIONADO 2
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



#FORMULAS ESTADISTICAS
    def agregar_producto(self,producto, marca, precio, fecha):
        conn, cursor = self.conectar()
        cursor.execute('INSERT INTO productos (producto, marca, precio, fecha) VALUES (?, ?, ?, ?)',
                    (producto, marca, precio, fecha))
        conn.commit()
        conn.close()

    def obtener_productos_unicos(self,):
        conn, cursor = self.conectar()
        cursor.execute('SELECT DISTINCT producto FROM productos')
        productos = [fila[0] for fila in cursor.fetchall()]
        conn.close()
        return productos

    def obtener_marcas_por_producto(self, producto):
        conn, cursor = self.conectar()
        cursor.execute('SELECT DISTINCT marca FROM productos WHERE producto = ?', (producto,))
        marcas = [fila[0] for fila in cursor.fetchall()]
        conn.close()
        return marcas

    def calcular_estadisticas_filtradas(self, producto=None, marca=None, fecha_inicio=None, fecha_fin=None):
        conn, cursor = self.conectar()

        query = "SELECT producto, marca, precio FROM productos WHERE 1=1"
        parametros = []

        if producto:
            query += " AND producto = ?"
            parametros.append(producto)

        if marca:
            query += " AND marca = ?"
            parametros.append(marca)

        if fecha_inicio:
            query += " AND fecha >= ?"
            parametros.append(fecha_inicio)

        if fecha_fin:
            query += " AND fecha <= ?"
            parametros.append(fecha_fin)

        cursor.execute(query, parametros)
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return None

        precios = [row[2] for row in rows]
        producto_nombre = rows[0][0] if producto else "(varios)"

        # VARIABLES PA  PRECIO MIN MAX MED
        precio_min = min(precios)
        precio_max = max(precios)
        precio_medio = sum(precios) / len(precios)

        # PONDERA POR MARCAS
        conteo_marcas = {}
        suma_marcas = {}
        for row in rows:
            marca = row[1]
            precio = row[2]
            conteo_marcas[marca] = conteo_marcas.get(marca, 0) + 1
            suma_marcas[marca] = suma_marcas.get(marca, 0) + precio

        total_entradas = sum(conteo_marcas.values())
        precio_ponderado = sum((suma_marcas[m] / conteo_marcas[m]) * (conteo_marcas[m] / total_entradas)
                            for m in conteo_marcas)

        return {
            'producto': producto_nombre,
            'precio_min': precio_min,
            'precio_max': precio_max,
            'precio_medio': precio_medio,
            'precio_ponderado': precio_ponderado,
            'fecha_calculo': datetime.now().strftime('%Y-%m-%d')
        }

    def guardar_estadisticas(self, stats):
        conn, cursor = self.conectar()
        cursor.execute('''
            INSERT INTO estadisticas (producto, precio_min, precio_max, precio_medio, precio_ponderado, fecha_calculo)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            stats['producto'],
            stats['precio_min'],
            stats['precio_max'],
            stats['precio_medio'],
            stats['precio_ponderado'],
            stats['fecha_calculo']
        ))
        conn.commit()
        conn.close()
