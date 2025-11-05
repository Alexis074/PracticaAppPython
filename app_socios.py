import customtkinter as ctk
from datetime import datetime

# ---------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------
ctk.set_appearance_mode("dark")       # modo oscuro
ctk.set_default_color_theme("blue")   # acento azul moderno


# ---------------------------
# DATOS DE SOCIOS (actualizado)
# ---------------------------
socios = [
    {"n": 1, "nombre": "Kori S.A. (Surnyak)", "ruc": "80.108.621-3", "dia": 5, "monto": 100000},
    {"n": 2, "nombre": "Electro Misiones", "ruc": "1.315.770-1", "dia": 5, "monto": 40000},
    {"n": 3, "nombre": "Vidrieria San Rafael", "ruc": "1.193.972-9", "dia": 5, "monto": 100000},
    {"n": 4, "nombre": "Raul Medina (Biocentro)", "ruc": "4.951.088-6", "dia": 5, "monto": 50000},
    {"n": 5, "nombre": "Ñe'e Pora Tecnologia y Confort", "ruc": "80.105.754-0", "dia": 5, "monto": 100000},
    {"n": 6, "nombre": "Cooperativa Universitaria Ltda.", "ruc": "80.000.958-4", "dia": 5, "monto": 200000},
    {"n": 7, "nombre": "Retail S.A. (Stock)", "ruc": "80.016.096-7", "dia": 5, "monto": 500000},
    {"n": 8, "nombre": "D.A. S.R.L.", "ruc": "80.023.800-1", "dia": 5, "monto": 200000},
    {"n": 9, "nombre": "Calixta Insaurralde", "ruc": "2.583.257-3", "dia": 5, "monto": 100000},
    {"n": 10, "nombre": "Inmobiliaria del Este S.A.", "ruc": "80.001.607-6", "dia": 5, "monto": 50000},   
    {"n": 11, "nombre": "Distribuidora Mauri", "ruc": "2.192.307-8", "dia": 5, "monto": 50000},
    {"n": 12, "nombre": "La Martina", "ruc": "4.097.552-5", "dia": 26, "monto": 150000},
    {"n": 13, "nombre": "Don Francisco Comercial", "ruc": "2.609.679-0", "dia": 26, "monto": 20000},
    {"n": 14, "nombre": "Luciana Castillo de Mereles", "ruc": "1.791.307-1", "dia": 26, "monto": 10000},
    {"n": 15, "nombre": "Nilda Romero", "ruc": "1.091.191-0", "dia": 26, "monto": 20000},
    {"n": 16, "nombre": "Arnaldo Gimenez", "ruc": "1.237.873-9", "dia": 26, "monto": 30000},
    {"n": 17, "nombre": "Comercial Armin S.A", "ruc": "80.105.082-0", "dia": 26, "monto": 100000},
    {"n": 18, "nombre": "Rosita Gutierrez", "ruc": "3.008.808-9", "dia": 26, "monto": 50000},
    {"n": 19, "nombre": "Lubricantes Edgar", "ruc": "1.192.752-6", "dia": 26, "monto": 30000},
    {"n": 20, "nombre": "Victor Hugo Ferloni", "ruc": "2.375.538-7", "dia": 26, "monto": 20000},
    {"n": 21, "nombre": "OSVA", "ruc": "1.049.140-6", "dia": 26, "monto": 10000},
    {"n": 22, "nombre": "Cristina Ayala", "ruc": "1.195.207", "dia": 26, "monto": 20000},
    {"n": 23, "nombre": "Sureño S.A.", "ruc": "80.074.899-9", "dia": 26, "monto": 50000},
    {"n": 24, "nombre": "Soledad Villalba", "ruc": "3.724.837-5", "dia": 26, "monto": 100000},
    {"n": 25, "nombre": "Alido Vera Caballero", "ruc": "648.529-4", "dia": 26, "monto": 50000},
    {"n": 26, "nombre": "Luz Maria Vargas", "ruc": "591.319-5", "dia": 26, "monto": 100000},
    {"n": 27, "nombre": "Infotech", "ruc": "1.563.606-2", "dia": 26, "monto": 20000},
    {"n": 28, "nombre": "Nacho Comercial", "ruc": "1.436.445-0", "dia": 26, "monto": 50000},
    {"n": 29, "nombre": "Veterinaria El Toke", "ruc": "520.855-6", "dia": 26, "monto": 50000},
    {"n": 30, "nombre": "Los Andes S.R.L.", "ruc": "80.049.434-2", "dia": 26, "monto": 50000},
    {"n": 31, "nombre": "Diana Valdez", "ruc": "2.014.577-2", "dia": 26, "monto": 20000},
    {"n": 32, "nombre": "Valens Center", "ruc": "1.559.761-0", "dia": 26, "monto": 20000},
    {"n": 33, "nombre": "Norberto Sosa (Dulce Hogar)", "ruc": "2.035.361", "dia": 26, "monto": 20000},
    {"n": 34, "nombre": "Clinica Veterinaria Vet-Ser", "ruc": "3.415.497-2", "dia": 26, "monto": 30000},
    {"n": 35, "nombre": "Mario Gustavo Insaurralde", "ruc": "750.759-3", "dia": 26, "monto": 50000},
    {"n": 36, "nombre": "Distribuidora FW E.A.S", "ruc": "80.155.279-6", "dia": 26, "monto": 100000},
]


# ---------------------------
# CLASE PRINCIPAL DE LA APP
# ---------------------------
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Socios Protectores")
        self.geometry("1200x700")
        self.resizable(True, True)

        self.dia_actual = None
        self.indice = 0
        self.socios_filtrados = []

        self.crear_pantalla_principal()

    # ---------------------------
    # FUNCIÓN PARA MOSTRAR LA FECHA ACTUAL (formato 05-11-2025)
    # ---------------------------
    def mostrar_fecha_actual(self):
        ahora = datetime.now()
        fecha_texto = ahora.strftime("%d-%m-%Y")  # formato de factura
        etiqueta_fecha = ctk.CTkLabel(self, text=fecha_texto,
                                      font=("Segoe UI", 38, "bold"),
                                      text_color="#FF0000")
        etiqueta_fecha.place(x=20, y=20)

    # ---------------------------
    # PANTALLA PRINCIPAL
    # ---------------------------
    def crear_pantalla_principal(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.mostrar_fecha_actual()
        ctk.CTkLabel(self, text="Seleccionar grupo de día",
                     font=("Segoe UI", 36, "bold")).pack(pady=80)

        for dia in sorted(set(s["dia"] for s in socios)):
            total = sum(s["monto"] for s in socios if s["dia"] == dia)

            frame = ctk.CTkFrame(self)
            frame.pack(pady=15)

            btn = ctk.CTkButton(frame, text=f"Grupo Día {dia}",
                                width=300, height=70,
                                font=("Segoe UI", 24, "bold"),
                                command=lambda d=dia: self.mostrar_socios(d))
            btn.pack(side="left", padx=10)

            ctk.CTkLabel(frame, text=f"Total a recaudar: {total:,} Gs.",
                         font=("Segoe UI", 20),
                         text_color="#00BFFF").pack(side="left", padx=10)

    # ---------------------------
    # MOSTRAR SOCIOS UNO POR UNO
    # ---------------------------
    def mostrar_socios(self, dia):
        self.dia_actual = dia
        self.socios_filtrados = [s for s in socios if s["dia"] == dia]
        self.indice = 0
        self.actualizar_vista()

    def actualizar_vista(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.mostrar_fecha_actual()
        socio = self.socios_filtrados[self.indice]

        ctk.CTkLabel(self, text=f"Socio {self.indice + 1} de {len(self.socios_filtrados)}",
                     font=("Segoe UI", 20, "italic")).pack(pady=(60, 5))
        ctk.CTkLabel(self, text=f"N° {socio['n']}", font=("Segoe UI", 32, "bold")).pack(pady=(10, 0))
        ctk.CTkLabel(self, text=f"{socio['nombre']}", font=("Segoe UI", 30, "bold"),
                     wraplength=1000).pack(pady=15)
        ctk.CTkLabel(self, text=f"RUC: {socio['ruc']}", font=("Segoe UI", 26)).pack(pady=5)
        ctk.CTkLabel(self, text=f"Día: {socio['dia']}", font=("Segoe UI", 26)).pack(pady=5)
        ctk.CTkLabel(self, text=f"Monto: {socio['monto']:,} Gs", font=("Segoe UI", 32, "bold"),
                     text_color="#00BFFF").pack(pady=25)

        # Aviso especial
        nombres_con_aviso = {"D.A. S.R.L.", "Cooperativa Universitaria Ltda."}
        if socio["nombre"] in nombres_con_aviso:
            mes_actual = datetime.now().strftime("%B").capitalize()
            texto_aviso = f"Aporte Voluntario del Mes de {mes_actual} — POR FAVOR INCLUIR EL MES EN LETRAS"
            ctk.CTkLabel(self, text=texto_aviso,
                         font=("Segoe UI", 18, "bold"),
                         text_color="#FF3333").pack(pady=(0, 20))

        # Botones de navegación
        frame_botones = ctk.CTkFrame(self)
        frame_botones.pack(pady=30)

        ctk.CTkButton(frame_botones, text="⬅️ Anterior", width=200, height=60,
                      font=("Segoe UI", 20, "bold"),
                      command=self.anterior).grid(row=0, column=0, padx=20)
        ctk.CTkButton(frame_botones, text="➡️ Siguiente", width=200, height=60,
                      font=("Segoe UI", 20, "bold"),
                      command=self.siguiente).grid(row=0, column=1, padx=20)

        ctk.CTkButton(self, text="↩️ Volver al Menú", width=300, height=60,
                      font=("Segoe UI", 20, "bold"),
                      fg_color="#333333", hover_color="#555555",
                      command=self.crear_pantalla_principal).pack(pady=20)

    def siguiente(self):
        if self.indice < len(self.socios_filtrados) - 1:
            self.indice += 1
            self.actualizar_vista()

    def anterior(self):
        if self.indice > 0:
            self.indice -= 1
            self.actualizar_vista()


# ---------------------------
# EJECUCIÓN
# ---------------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()

# ---------------------------
# ALEXIS ALMIRON - 2025
# ---------------------------
