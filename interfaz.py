import tkinter as tk
from tkinter import messagebox

# BASE DE DATOS TEMPORAL
clientes = {}
trabajadores = {}

# Iniciar admin
def inicio_admin(root):
    root.withdraw()

    # Crear una nueva ventana
    menu_admin = tk.Toplevel(root)
    menu_admin.title("Inicio de Administrador")
    menu_admin.geometry("600x300")

    label_bienvenida = tk.Label(menu_admin, text="Administrador", font=("Arial", 18))
    label_bienvenida.pack(pady=20)

    btn_user = tk.Label(menu_admin, text="Usuario: ", font=("Arial", 12))
    btn_user.pack(pady=10)
    user_entry = tk.Entry(menu_admin)
    user_entry.pack()

    btn_pass = tk.Label(menu_admin, text="Contraseña: ", font=("Arial", 12))
    btn_pass.pack(pady=14)
    pass_entry = tk.Entry(menu_admin, show="*")
    pass_entry.pack()

    btn_login = tk.Button(menu_admin, text="Ingresar", font=("Arial", 12), command=lambda: InterfazAdmin(user_entry.get(), pass_entry.get(), menu_admin, root))
    btn_login.pack(pady=18)

def InterfazAdmin(user, password, menu_admin, root):
    if user == 'admin' and password == 'admin123':
        messagebox.showinfo("Bienvenido", "Iniciando...")
        menu_admin.destroy()
        inicio_menu_(root)
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def inicio_menu_(root):
    # Crear una nueva ventana
    menu_admin_sist = tk.Toplevel(root)
    menu_admin_sist.title("Sistema")
    menu_admin_sist.geometry("1260x800")

    def regresar():
        menu_admin_sist.destroy()  # Destruye la ventana actual
        root.deiconify()

    back = tk.Button(menu_admin_sist, text="Regresar", font=("Arial", 8), command=regresar)
    back.pack(pady=25)

    label_titulo = tk.Label(menu_admin_sist, text="Bienvenido al Sistema", font=("Arial", 24))
    label_titulo.pack(pady=20)

    btn_registro_trabajador = tk.Button(menu_admin_sist, text="Registrar Trabajador", font=("Arial", 12), command=lambda: registrar_trabajador(root))
    btn_registro_trabajador.pack(pady=25)

def registrar_trabajador(root):
    # Crear una nueva ventana
    menu_admin_sist = tk.Toplevel(root)
    menu_admin_sist.title("Registro de Trabajador")
    menu_admin_sist.geometry("600x600")

    label_datos_basicos = tk.Label(menu_admin_sist, text="Datos Básicos", font=("Arial", 14))
    label_datos_basicos.pack(pady=20)
    
    label_nombre = tk.Label(menu_admin_sist, text="Nombre: ", font=("Arial", 12))
    label_nombre.pack()
    entry_nombre = tk.Entry(menu_admin_sist)
    entry_nombre.pack()
    
    label_apellido = tk.Label(menu_admin_sist, text="Apellido: ", font=("Arial", 12))
    label_apellido.pack()
    entry_apellido = tk.Entry(menu_admin_sist)
    entry_apellido.pack()
    
    label_cedula = tk.Label(menu_admin_sist, text="Cédula: ", font=("Arial", 12))
    label_cedula.pack()
    entry_cedula = tk.Entry(menu_admin_sist)
    entry_cedula.pack()
    
    label_telefono = tk.Label(menu_admin_sist, text="Teléfono: ", font=("Arial", 12))
    label_telefono.pack()
    entry_telefono = tk.Entry(menu_admin_sist)
    entry_telefono.pack()
    
    label_direccion = tk.Label(menu_admin_sist, text="Dirección: ", font=("Arial", 12))
    label_direccion.pack()
    entry_direccion = tk.Entry(menu_admin_sist)
    entry_direccion.pack()
    
    label_usuario = tk.Label(menu_admin_sist, text="Usuario: ", font=("Arial", 12))
    label_usuario.pack()
    entry_usuario = tk.Entry(menu_admin_sist)
    entry_usuario.pack()
    
    label_contraseña = tk.Label(menu_admin_sist, text="Contraseña: ", font=("Arial", 12))
    label_contraseña.pack()
    entry_contraseña = tk.Entry(menu_admin_sist)
    entry_contraseña.pack()

    btn_registrar = tk.Button(menu_admin_sist, text="Registrar", font=("Arial", 12), command=lambda: registrar_datos_trabajador(entry_nombre.get(), entry_apellido.get(), entry_cedula.get(), entry_telefono.get(), entry_direccion.get(), entry_usuario.get(), entry_contraseña.get()))
    btn_registrar.pack(pady=25)

    def registrar_datos_trabajador(nombre, apellido, cedula, telefono, direccion, usuario, contraseña):
        # Guardar los datos del trabajador en la base de datos
        trabajadores[usuario] = {
            'nombre': nombre,
            'apellido': apellido,
            'telefono': telefono,
            'direccion': direccion,
            'cedula': cedula,
            'contraseña': contraseña
        }
        messagebox.showinfo("Registro Exitoso", "Trabajador registrado exitosamente.")
        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_cedula.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_usuario.delete(0, tk.END)
        entry_contraseña.delete(0, tk.END)

def inicio_trabajador():
    # Crear una nueva ventana
    menu_trabajador = tk.Toplevel()
    menu_trabajador.geometry("600x300")
    menu_trabajador.title("Inicio de Trabajadores")

    label_bienvenida = tk.Label(menu_trabajador, text="Trabajador de turno", font=("Arial", 18))
    label_bienvenida.pack(pady=20)

    btn_user = tk.Label(menu_trabajador, text="Usuario: ", font=("Arial", 12))
    btn_user.pack(pady=10)
    user_entry = tk.Entry(menu_trabajador)
    user_entry.pack()

    btn_pass = tk.Label(menu_trabajador, text="Contraseña: ", font=("Arial", 12))
    btn_pass.pack(pady=14)
    pass_entry = tk.Entry(menu_trabajador, show="*")
    pass_entry.pack()

    btn_entrar = tk.Button(menu_trabajador, text="Iniciar sesión", font=("Arial", 12), command=lambda: validar_trabajador(user_entry.get(), pass_entry.get(), menu_trabajador))
    btn_entrar.pack(pady=16)

def validar_trabajador(usuario, contraseña, menu_trabajador):
    # Validar si el usuario y la contraseña coinciden con lo registrado
    if usuario in trabajadores and trabajadores[usuario]['contraseña'] == contraseña:
        messagebox.showinfo("Bienvenido", "Inicio de sesión exitoso.")
        menu_trabajador.destroy()  # Cerrar la ventana de inicio de sesión
        sist_trabajador(trabajadores[usuario]['nombre'], trabajadores[usuario]['apellido'])  # Pasar nombre y apellido del trabajador
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def sist_trabajador(nombre, apellidos):
    sist_trabajador = tk.Toplevel()
    sist_trabajador.geometry("1260x800")
    sist_trabajador.title("Sistema Trabajador de turno")

    #Etiqueta del trabajador de turno
    label_turno = tk.Label(sist_trabajador, text=f"Trabajador de turno \n {nombre} {apellidos}", font=("Arial", 18))
    label_turno.pack(pady=20)

    registar_clientes = tk.Button(sist_trabajador, text="Registrar clientes nuevos")
    registar_clientes.pack(pady=25)

########## INICIADOR ##############
def inicio():
    root = tk.Tk()
    root.title("Gym")
    root.geometry("300x200")

    # Frame para inicio de sesión
    frame_inicio = tk.Frame(root)
    frame_inicio.pack()

    ############### LOGIN EN LA VENTANA PRINCIPAL #################

    # Botón Para admin.
    label_inicio_titulo = tk.Button(frame_inicio, text="Admin", font=("Arial", 12), command=lambda: inicio_admin(root))
    label_inicio_titulo.pack(pady=12)

    def destruir_y_mostrar_trabajador():
        root.withdraw()  # Oculta la ventana principal
        inicio_trabajador()  # Muestra la ventana de trabajador

    # Botón para Trabajador
    boton_trabajador = tk.Button(frame_inicio, text="Trabajador", font=("Arial", 12), command=destruir_y_mostrar_trabajador)
    boton_trabajador.pack(pady=15)

    # Botón para Cliente (Funcionalidad no implementada)
    boton_cliente = tk.Button(frame_inicio, text="Cliente", font=("Arial", 12))
    boton_cliente.pack(pady=17)

    # Iniciar la aplicación
    root.mainloop()

# Llamar a la función inicio para arrancar la aplicación
inicio()
