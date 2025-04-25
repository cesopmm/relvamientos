def pedir_contra():
    master = Toplevel()
    master.geometry("300x200")
    master.title("Acceso a Estadísticas")
    master.configure(bg="#ccd9df")
    master.resizable(False, False)  # Evita que se redimensione

    # Variables para almacenar usuario y contraseña
    usuario_var = StringVar()
    contra_var = StringVar()

    # Configuración de estilo
    style = ttk.Style(master)
    style.theme_use("default")
    style.configure("Treeview.Heading", background="#ce8f92", foreground="white")

    # Etiquetas y campos de entrada
    Label(master, bg="#ccd9df", text="USUARIO:").place(x=20, y=50)
    usuario_entry = Entry(master, textvariable=usuario_var)
    usuario_entry.place(x=120, y=50)

    Label(master, bg="#ccd9df", text="CONTRASEÑA:").place(x=20, y=90)
    contra_entry = Entry(master, textvariable=contra_var, show="*")  # Oculta la contraseña
    contra_entry.place(x=120, y=90)

    # Función interna para verificar credenciales
    def verificar_credenciales():
        usuario = usuario_var.get().strip()  # Elimina espacios en blanco
        contra = contra_var.get().strip()

        if usuario == USUARIO_VALIDO and contra == CONTRASEÑA_VALIDA:
            master.destroy()  # Cierra la ventana de login
            abrir_estadistica()  # Abre la ventana de estadísticas
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            usuario_var.set("")  # Limpia el campo de usuario
            contra_var.set("")  # Limpia el campo de contraseña
            usuario_entry.focus_set()  # Devuelve el foco al campo de usuario

    # Botón para ingresar
    Button(
        master,
        text="INGRESAR",
        command=verificar_credenciales,
        bg="#679ab7",
        fg="white",
        padx=10,
        pady=5
    ).place(x=120, y=140)

    # Enfocar el campo de usuario al abrir la ventana
    usuario_entry.focus_set()

def abrir_estadistica():
    estas = Toplevel()
    estas.title("Bienvenido/a al módulo ESTADÍSTICAS")
    estas.geometry("750x600")
    estas.configure(bg="#fcfafa")

    # Aquí puedes inicializar tu clase de estadísticas
    Estadisticas(estas)