import tkinter as tk
from tkinter import messagebox
import numpy_financial as npf

# Función para abrir las ventanas de cada operación
def open_window(title):
    def placeholder():
        messagebox.showinfo("Información", f"Este módulo es para {title}. Aquí puedes implementar el código.")
    
    window = tk.Toplevel()
    window.title(title)
    window.geometry("400x300")
    
    tk.Label(window, text=f"Módulo: {title}", font=("Arial", 16)).pack(pady=20)
    tk.Button(window, text="Ejecutar", command=placeholder, width=15).pack(pady=10)
    tk.Button(window, text="Cerrar", command=window.destroy, width=15).pack(pady=10)


def open_simple_interest_module():
    def calculate_si():
        try:
            p = float(principal_entry.get())
            t = float(time_entry.get())
            r = float(rate_entry.get())
            
            # Convertir tiempo a años según la unidad seleccionada
            unit = time_unit.get()
            if unit == "Meses":
                t /= 12  # Convertir meses a años
            elif unit == "Días":
                t /= 365  # Convertir días a años
            
            si = (p * t * r) / 100  # Calcular interés simple
            amount = p + si  # Calcular monto (valor futuro)
            
            result_label.config(text=f"Interés Simple: {si:.2f}\nMonto (Futuro): {amount:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")
    
    window = tk.Toplevel()
    window.title("Interés Simple")
    window.geometry("400x400")
    
    tk.Label(window, text="Cálculo de Interés Simple", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(window, text="Principal (P):").pack()
    principal_entry = tk.Entry(window)
    principal_entry.pack(pady=5)
    
    tk.Label(window, text="Tiempo (T):").pack()
    time_entry = tk.Entry(window)
    time_entry.pack(pady=5)
    
    tk.Label(window, text="Unidad de Tiempo:").pack()
    time_unit = tk.StringVar(value="Años")
    units = ["Años", "Meses", "Días"]
    tk.OptionMenu(window, time_unit, *units).pack(pady=5)
    
    tk.Label(window, text="Tasa de Interés (R):").pack()
    rate_entry = tk.Entry(window)
    rate_entry.pack(pady=5)
    
    tk.Button(window, text="Calcular", command=calculate_si).pack(pady=10)
    
    result_label = tk.Label(window, text="Interés Simple: \nMonto (Futuro): ")
    result_label.pack(pady=10)
    
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def open_compound_interest_module():
    def calculate_ci():
        try:
            p = float(principal_entry.get())
            r = float(rate_entry.get())
            t = float(time_entry.get())
            
            # Convertir tiempo a años según la unidad seleccionada
            unit = time_unit.get()
            if unit == "Meses":
                t /= 12  # Convertir meses a años
            elif unit == "Días":
                t /= 365  # Convertir días a años
            
            # Calcular interés compuesto
            amount = p * ((1 + r / 100) ** t)
            ci = amount - p  # Interés compuesto
            
            result_label.config(text=f"Interés Compuesto: {ci:.2f}\nMonto (Futuro): {amount:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")
    
    
    window = tk.Toplevel()
    window.title("Interés Compuesto")
    window.geometry("400x400")
    
    tk.Label(window, text="Cálculo de Interés Compuesto", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(window, text="Principal (P):").pack()
    principal_entry = tk.Entry(window)
    principal_entry.pack(pady=5)
    
    tk.Label(window, text="Tiempo (T):").pack()
    time_entry = tk.Entry(window)
    time_entry.pack(pady=5)
    
    tk.Label(window, text="Unidad de Tiempo:").pack()
    time_unit = tk.StringVar(value="Años")
    units = ["Años", "Meses", "Días"]
    tk.OptionMenu(window, time_unit, *units).pack(pady=5)
    
    tk.Label(window, text="Tasa de Interés (R):").pack()
    rate_entry = tk.Entry(window)
    rate_entry.pack(pady=5)
    
    tk.Button(window, text="Calcular", command=calculate_ci).pack(pady=10)
    
    result_label = tk.Label(window, text="Interés Compuesto: \nMonto (Futuro): ")
    result_label.pack(pady=10)
    
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def open_amortization_module():
    def calculate_amortization():
        try:
            p = float(principal_entry.get())
            r = float(rate_entry.get()) / 100 / 12  # Convertir tasa anual a mensual (por defecto)
            n = int(period_entry.get())
            
            # Calcular cuota de amortización
            x = (1 + r) ** n
            amortization_amount = p * (r * x) / (x - 1)
            
            # Generar cronograma de amortización
            schedule_text.delete(1.0, tk.END)  # Limpiar resultados previos
            balance = p
            schedule_text.insert(tk.END, "N°\tCuota\tInterés\tPrincipal\tSaldo\n")
            schedule_text.insert(tk.END, "-" * 40 + "\n")
            for i in range(1, n + 1):
                interest = balance * r
                principal_payment = amortization_amount - interest
                balance = balance - principal_payment
                balance = max(0, balance)  # Evitar valores negativos
                schedule_text.insert(
                    tk.END,
                    f"{i}\t{amortization_amount:.2f}\t{interest:.2f}\t{principal_payment:.2f}\t{balance:.2f}\n"
                )
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")
    
    window = tk.Toplevel()
    window.title("Amortización")
    window.geometry("500x500")
    
    tk.Label(window, text="Cálculo de Amortización", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(window, text="Principal (P):").pack()
    principal_entry = tk.Entry(window)
    principal_entry.pack(pady=5)
    
    tk.Label(window, text="Tasa de Interés Anual (%):").pack()
    rate_entry = tk.Entry(window)
    rate_entry.pack(pady=5)
    
    tk.Label(window, text="Periodo (en meses):").pack()
    period_entry = tk.Entry(window)
    period_entry.pack(pady=5)
    
    tk.Button(window, text="Calcular", command=calculate_amortization).pack(pady=10)
    
    tk.Label(window, text="Cronograma de Amortización:").pack(pady=10)
    schedule_text = tk.Text(window, height=20, width=60)
    schedule_text.pack(pady=5)
    
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def open_american_amortization_module():
    def calculate_american_amortization():
        try:
            p = float(principal_entry.get())
            r = float(rate_entry.get()) / 100 / 12  # Convertir tasa anual a mensual
            n = int(period_entry.get())
            
            # Calcular solo los intereses
            interest_payment = p * r
            total_interest = interest_payment * n
            final_payment = p  # El pago final es el principal
            
            # Generar cronograma de amortización
            schedule_text.delete(1.0, tk.END)  # Limpiar resultados previos
            schedule_text.insert(tk.END, "N°\tCuota\tInterés\tSaldo\n")
            schedule_text.insert(tk.END, "-" * 40 + "\n")
            for i in range(1, n + 1):
                schedule_text.insert(
                    tk.END,
                    f"{i}\t{interest_payment:.2f}\t{interest_payment:.2f}\t{p:.2f}\n"
                )
            # Al final, agregar el pago total (principal)
            schedule_text.insert(tk.END, f"\nPago Final: {final_payment:.2f}\n")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")
    
    window = tk.Toplevel()
    window.title("Amortización Americana")
    window.geometry("500x500")
    
    tk.Label(window, text="Cálculo de Amortización Americana", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(window, text="Principal (P):").pack()
    principal_entry = tk.Entry(window)
    principal_entry.pack(pady=5)
    
    tk.Label(window, text="Tasa de Interés Anual (%):").pack()
    rate_entry = tk.Entry(window)
    rate_entry.pack(pady=5)
    
    tk.Label(window, text="Periodo (en meses):").pack()
    period_entry = tk.Entry(window)
    period_entry.pack(pady=5)
    
    tk.Button(window, text="Calcular", command=calculate_american_amortization).pack(pady=10)
    
    tk.Label(window, text="Cronograma de Amortización:").pack(pady=10)
    schedule_text = tk.Text(window, height=20, width=60)
    schedule_text.pack(pady=5)
    
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def open_german_amortization_module():
    def calculate_german_amortization():
        try:
            p = float(principal_entry.get())
            r = float(rate_entry.get()) / 100 / 12  # Convertir tasa anual a mensual
            n = int(period_entry.get())
            
            # Calcular amortización fija del principal
            fixed_principal_payment = p / n
            total_interest = 0
            total_payment = 0
            
            # Generar cronograma de amortización
            schedule_text.delete(1.0, tk.END)  # Limpiar resultados previos
            balance = p
            schedule_text.insert(tk.END, "N°\tCuota\tInterés\tPrincipal\tSaldo\n")
            schedule_text.insert(tk.END, "-" * 40 + "\n")
            for i in range(1, n + 1):
                interest_payment = balance * r
                total_payment_this_month = interest_payment + fixed_principal_payment
                balance -= fixed_principal_payment
                balance = max(0, balance)  # Evitar valores negativos
                total_interest += interest_payment
                total_payment += total_payment_this_month
                
                schedule_text.insert(
                    tk.END,
                    f"{i}\t{total_payment_this_month:.2f}\t{interest_payment:.2f}\t{fixed_principal_payment:.2f}\t{balance:.2f}\n"
                )
            
            schedule_text.insert(tk.END, f"\nTotal Intereses: {total_interest:.2f}\n")
            schedule_text.insert(tk.END, f"Total Pagado: {total_payment:.2f}\n")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")
    
    window = tk.Toplevel()
    window.title("Amortización Alemana")
    window.geometry("500x500")
    
    tk.Label(window, text="Cálculo de Amortización Alemana", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(window, text="Principal (P):").pack()
    principal_entry = tk.Entry(window)
    principal_entry.pack(pady=5)
    
    tk.Label(window, text="Tasa de Interés Anual (%):").pack()
    rate_entry = tk.Entry(window)
    rate_entry.pack(pady=5)
    
    tk.Label(window, text="Periodo (en meses):").pack()
    period_entry = tk.Entry(window)
    period_entry.pack(pady=5)
    
    tk.Button(window, text="Calcular", command=calculate_german_amortization).pack(pady=10)
    
    tk.Label(window, text="Cronograma de Amortización:").pack(pady=10)
    schedule_text = tk.Text(window, height=20, width=60)
    schedule_text.pack(pady=5)
    
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def open_anualidad_vencida_module():
    def calculate_present_value():
        try:
            payment = float(payment_entry.get())
            frequency = float(frequency_entry.get())
            nominal_rate = float(rate_entry.get()) / 100
            investment_years = float(years_entry.get())
            
            # Calculate Present Value of Ordinary Annuity
            pv = valor_presente_anualidad_ordinaria(payment, frequency, nominal_rate, investment_years)
            
            # Calculate Future Value of Ordinary Annuity
            fv = valor_futuro_anualidad_ordinaria(payment, frequency, nominal_rate, investment_years)
            
            # Update result labels
            pv_label.config(text=f"Valor Presente: ${pv:,.2f}")
            fv_label.config(text=f"Valor Futuro: ${fv:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores numéricos válidos.")
    
    def valor_presente_anualidad_ordinaria(pago, frecuencia, tasa_nominal, anios_inversion):
        tasa_ajustada = tasa_nominal /frecuencia
        periodos = anios_inversion * frecuencia
        valor_presente = pago * ((1 - (1 + tasa_ajustada) ** (-periodos)) / tasa_ajustada)
        return valor_presente
    
    def valor_futuro_anualidad_ordinaria(pago, frecuencia, tasa_nominal, anios_inversion):
        tasa_ajustada = tasa_nominal /frecuencia
        periodos = anios_inversion * frecuencia
        valor_futuro = pago * (((1 + tasa_ajustada) ** periodos) - 1) / tasa_ajustada
        return valor_futuro
    
    window = tk.Toplevel()
    window.title("Anualidad Vencida")
    window.geometry("400x500")
    
    tk.Label(window, text="Cálculo de Anualidad Vencida", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(window, text="Pago Periódico:").pack()
    payment_entry = tk.Entry(window)
    payment_entry.pack(pady=5)
    
    tk.Label(window, text="Frecuencia (pagos por año):").pack()
    frequency_entry = tk.Entry(window)
    frequency_entry.pack(pady=5)
    
    tk.Label(window, text="Tasa de Interés Nominal (%):").pack()
    rate_entry = tk.Entry(window)
    rate_entry.pack(pady=5)
    
    tk.Label(window, text="Años de Inversión:").pack()
    years_entry = tk.Entry(window)
    years_entry.pack(pady=5)
    
    tk.Button(window, text="Calcular", command=calculate_present_value).pack(pady=10)
    
    pv_label = tk.Label(window, text="Valor Presente: ", font=("Arial", 12))
    pv_label.pack(pady=5)
    
    fv_label = tk.Label(window, text="Valor Futuro: ", font=("Arial", 12))
    fv_label.pack(pady=5)
    
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def open_gradiente_aritmetico_module():
    def calculate_gradient():
        try:
            first_payment = float(first_payment_entry.get())
            gradient = float(gradient_entry.get())
            rate = float(rate_entry.get()) / 100
            periods = float(periods_entry.get())
            
            # Calculate Present Value of Arithmetic Gradient
            pv_gradient = valor_presente_gradiente_aritmetico(
                first_payment, 
                gradient, 
                rate, 
                periods
            )
            
            # Calculate Future Value of Arithmetic Gradient
            fv_gradient = valor_futuro_gradiente_aritmetico(
                first_payment, 
                gradient, 
                rate, 
                periods
            )
            
            # Update result labels
            pv_label.config(text=f"Present Value: ${pv_gradient:,.2f}")
            fv_label.config(text=f"Future Value: ${fv_gradient:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")
    
    def valor_presente_gradiente_aritmetico(first_payment, gradient, periodic_rate, periods):
        rate = periodic_rate / 100  # Conversión de porcentaje a decimal
    
        if rate == 0:
            return first_payment * periods + (gradient * periods * (periods - 1) / 2)
        
        # Término 1
        term1 = first_payment * ((1 + rate)**periods - 1) / (rate * (1 + rate)**periods)
        
        # Término 2
        term2 = (gradient / rate) * (
            ((1 + rate)**periods - 1) / (rate * (1 + rate)**periods) - (periods / (1 + rate)**periods)
        )
        
        return term1 + term2


    
    def valor_futuro_gradiente_aritmetico(first_payment, gradient, periodic_rate, periods):
    

        if periodic_rate == 0:
            # Special case when rate is zero
            return first_payment * periods + (gradient * periods * (periods - 1) / 2)
        
        # Future Value formula for arithmetic gradient
        term1 = first_payment * (
            ((1 + periodic_rate) ** periods - 1) / periodic_rate
        )
        term2 = (gradient / periodic_rate) * (
            ((1 + periodic_rate) ** periods - 1) / periodic_rate -
            periods
        )
        
        return term1 + term2
    
    window = tk.Toplevel()
    window.title("Arithmetic Gradient")
    window.geometry("400x500")
    
    tk.Label(window, text="Arithmetic Gradient Calculations", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(window, text="First Payment:").pack()
    first_payment_entry = tk.Entry(window)
    first_payment_entry.pack(pady=5)
    
    tk.Label(window, text="Gradient (Increment):").pack()
    gradient_entry = tk.Entry(window)
    gradient_entry.pack(pady=5)
    
    tk.Label(window, text="Nominal Interest Rate (%):").pack()
    rate_entry = tk.Entry(window)
    rate_entry.pack(pady=5)
    
    tk.Label(window, text="Number of Periods:").pack()
    periods_entry = tk.Entry(window)
    periods_entry.pack(pady=5)
    
    tk.Button(window, text="Calculate", command=calculate_gradient).pack(pady=10)
    
    pv_label = tk.Label(window, text="Present Value: ", font=("Arial", 12))
    pv_label.pack(pady=5)
    
    fv_label = tk.Label(window, text="Future Value: ", font=("Arial", 12))
    fv_label.pack(pady=5)
    
    # Brief explanation
    explanation_label = tk.Label(window, 
        text="Arithmetic Gradient: Series of payments\n"
             "with constant increment", 
        font=("Arial", 10)
    )
    explanation_label.pack(pady=10)
    
    tk.Button(window, text="Close", command=window.destroy).pack(pady=10)
    
def open_van_module():
    def calculate_van():
        try:
            cash_flows = [float(value) for value in cash_flows_entry.get().split(",")]
            discount_rate = float(discount_rate_entry.get()) / 100
            
            # Calcular VAN
            van = sum(cf / ((1 + discount_rate) ** i) for i, cf in enumerate(cash_flows))
            
            result_label.config(text=f"VAN: ${van:,.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores válidos separados por comas.")
    
    window = tk.Toplevel()
    window.title("Valor Actual Neto (VAN)")
    window.geometry("400x300")
    
    tk.Label(window, text="Cálculo del Valor Actual Neto (VAN)", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(window, text="Flujos de Caja (separados por comas):").pack()
    cash_flows_entry = tk.Entry(window)
    cash_flows_entry.pack(pady=5)
    
    tk.Label(window, text="Tasa de Descuento (%):").pack()
    discount_rate_entry = tk.Entry(window)
    discount_rate_entry.pack(pady=5)
    
    tk.Button(window, text="Calcular", command=calculate_van).pack(pady=10)
    
    result_label = tk.Label(window, text="VAN: ", font=("Arial", 12))
    result_label.pack(pady=5)
    
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)


def open_tir_module():
    def calculate_tir():
        try:
            # Obtener los flujos de caja ingresados por el usuario y convertirlos a una lista de números
            cash_flows = [float(value) for value in cash_flows_entry.get().split(",")]
            
            # Calcular la TIR utilizando numpy_financial.irr
            tir = npf.irr(cash_flows)
            
            if tir is None:
                messagebox.showerror("Error", "No se pudo calcular la TIR, verifique los flujos de caja.")
            else:
                # Mostrar el resultado en formato de porcentaje con 2 decimales
                result_label.config(text=f"TIR: {tir*100:.2f}%")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores válidos separados por comas.")
    
    window = tk.Toplevel()
    window.title("Tasa Interna de Retorno (TIR)")
    window.geometry("400x300")
    
    tk.Label(window, text="Cálculo de la Tasa Interna de Retorno (TIR)", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(window, text="Flujos de Caja (separados por comas):").pack()
    cash_flows_entry = tk.Entry(window)
    cash_flows_entry.pack(pady=5)
    
    tk.Button(window, text="Calcular", command=calculate_tir).pack(pady=10)
    
    result_label = tk.Label(window, text="TIR: ", font=("Arial", 12))
    result_label.pack(pady=5)
    
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)



def open_per_module():
    def calculate_per():
        try:
            price = float(price_entry.get())
            earnings = float(earnings_entry.get())
            
            if earnings == 0:
                raise ValueError("El beneficio por acción no puede ser 0.")
            
            per = price / earnings
            result_label.config(text=f"PER: {per:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
    
    window = tk.Toplevel()
    window.title("Relación Precio/Beneficio (PER)")
    window.geometry("400x300")
    
    tk.Label(window, text="Cálculo del PER (Price to Earnings Ratio)", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(window, text="Precio por acción:").pack()
    price_entry = tk.Entry(window)
    price_entry.pack(pady=5)
    
    tk.Label(window, text="Beneficio por acción:").pack()
    earnings_entry = tk.Entry(window)
    earnings_entry.pack(pady=5)
    
    tk.Button(window, text="Calcular", command=calculate_per).pack(pady=10)
    
    result_label = tk.Label(window, text="PER: ", font=("Arial", 12))
    result_label.pack(pady=5)
    
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def open_payback_module():
    def calculate_payback():
        try:
            # Obtener los flujos de caja ingresados por el usuario
            cash_flows = [float(value) for value in cash_flows_entry.get().split(",")]
            
            # Comprobar que la inversión inicial (primer flujo de caja) es negativa
            if cash_flows[0] >= 0:
                messagebox.showerror("Error", "El flujo de caja inicial debe ser negativo (inversión inicial).")
                return
            
            # Acumular los flujos de caja hasta que la inversión inicial sea recuperada
            cumulative_cash_flow = 0
            payback_period = 0
            
            for i, cash_flow in enumerate(cash_flows):
                cumulative_cash_flow += cash_flow
                if cumulative_cash_flow >= 0:
                    payback_period = i + (cumulative_cash_flow - cash_flow) / cash_flow
                    break
            
            if payback_period == 0:
                messagebox.showinfo("Resultado", "La inversión no se recupera en el plazo especificado.")
            else:
                # Mostrar el resultado
                result_label.config(text=f"Payback: {payback_period:.2f} periodos")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce valores válidos separados por comas.")
    
    window = tk.Toplevel()
    window.title("Cálculo de Payback")
    window.geometry("400x300")
    
    tk.Label(window, text="Cálculo del Payback", font=("Arial", 16)).pack(pady=10)
    
    tk.Label(window, text="Flujos de Caja (separados por comas):").pack()
    cash_flows_entry = tk.Entry(window)
    cash_flows_entry.pack(pady=5)
    
    tk.Button(window, text="Calcular", command=calculate_payback).pack(pady=10)
    
    result_label = tk.Label(window, text="Payback: ", font=("Arial", 12))
    result_label.pack(pady=5)
    
    tk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)

def main_menu():
    root = tk.Tk()
    root.title("Calculadora Financiera")
    root.geometry("300x600")
    
    tk.Label(root, text="Elige la operación:", font=("Arial", 14)).pack(pady=20)
    
    tk.Button(root, text="Interés Simple", command=open_simple_interest_module, width=25).pack(pady=5)
    tk.Button(root, text="Interés Compuesto", command=open_compound_interest_module, width=25).pack(pady=5)
    tk.Button(root, text="Amortización", command=open_amortization_module, width=25).pack(pady=5)
    tk.Button(root, text="Amortización Americana", command=open_american_amortization_module, width=25).pack(pady=5)
    tk.Button(root, text="Amortización Alemana", command=open_german_amortization_module, width=25).pack(pady=5)
    tk.Button(root, text="Anualidad Vencida", command=open_anualidad_vencida_module, width=25).pack(pady=5)
    tk.Button(root, text="VAN (Valor Actual Neto)", command=open_van_module, width=25).pack(pady=5)
    tk.Button(root, text="TIR (Tasa Interna de Retorno)", command=open_tir_module, width=25).pack(pady=5)
    tk.Button(root, text="Payback", command=open_payback_module, width=25).pack(pady=5)
    tk.Button(root, text="Cerrar", command=root.destroy, width=25).pack(pady=20)
    
    root.mainloop()

# Iniciar la aplicación
main_menu()


