from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# 🟡 Edite aqui a cor de fundo principal do aplicativo:
COR_FUNDO = "#4E9CC9"  # exemplo: cinza escuro, troque por qualquer outra cor!

# 🎨 Estilo adaptável com base na cor de fundo
entry_bg = "#F1F1F1" if COR_FUNDO != "#ffffff" else "#f0f0f0"
text_bg = "#000000" if COR_FUNDO != "#ffffff" else "#e0e0e0"
fg_color = "#000000" if COR_FUNDO != "#ffffff" else "#000000"
accent_color = "#1e1f20"
btn_color = "#4CAF50"
btn_clear = "#e74c3c"
font_label = ("Segoe UI", 10, "bold")
font_entry = ("Segoe UI", 10)
font_button = ("Segoe UI", 10, "bold")

# Função para calcular a diferença entre as datas
def calcular_dias():
    try:
        # Coleta os dados do usuário
        diain = int(entrada_dia_ini.get())
        mesin = int(entrada_mes_ini.get())
        anoin = int(entrada_ano_ini.get())

        diafn = int(entrada_dia_fim.get())
        mesfn = int(entrada_mes_fim.get())
        anofn = int(entrada_ano_fim.get())

        # Cria objetos de data
        data_inicial = datetime(anoin, mesin, diain)
        data_final = datetime(anofn, mesfn, diafn)
      
        def adcAnos():
            anos = []
            dias = []
            qtdint = anofn-anoin-1
            i = 0
            anolist = anoin
            while i!= qtdint:
                anolist=anolist+1
                anos.append(anolist)
                i=i+1
            for i in anos:
                if i%4==0 and i%100!=0 or i%400==0:
                    dias.append(366)
                else:
                    dias.append(365)
            soma = sum(dias)
            print(f'\nLista de Anos inteiros: {anos}')
            print(f'Lista de Dias inteiros: {dias}')
            return soma

        anosD = adcAnos()
        print("Total da soma dos dias inteiros: ",anosD)

        def inicio():
            diasm = []
            indice = mesin-1
            i=0 
            if anoin%4==0 and anoin%100!=0 or anoin%400==0:
                diasm = [31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                diasm = [31,28,31,30,31,30,31,31,30,31,30,31]
            diass = diasm[indice] - diain+1 
            diasm.reverse()
            while i!= mesin:
                diasm.pop()
                i=i+1
            somaDin = sum(diasm) + diass
            print(f'\nDias inteiros 1° ano: {diasm}') 
            print(f'Dias 1° mês: {diass}')
            return somaDin
            
        inicioD = inicio()
        print("Total da soma dos dias do 1° ano: ",inicioD)


        def fim():
            diasm = []
            mesesint = mesfn-1
            conta = 12-mesesint 
            i=0 
            if anofn%4==0 and anofn%100!=0 or anofn%400==0:
                diasm = [31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                diasm = [31,28,31,30,31,30,31,31,30,31,30,31] 
            while i!= conta:
                diasm.pop()
                i=i+1
            somaDfn = sum(diasm) + diafn
            print(f'\nDias inteiros último ano: {diasm}') 
            return somaDfn

        fimD = fim()
        print("Total da soma dos dias do último ano: ",fimD,"\n")

        def calculo():
            totalD = inicioD+fimD+anosD
            print("Soma de todos os dias: ",totalD)
            anos = totalD//365
            anq = (totalD/365 - anos)*365
            print(anq)
            meses = anq//30
            print(meses)
            dias = (anq/30 - meses)*30
            int(dias)
            resultado =f'{anos} Ano(s), {meses:.0f} Mes(es) e {dias:.0f} Dia(s)! [{totalD} dias totais]'
            return resultado
        calculo()

            # Verifica se a data final é posterior

        if ((anofn < anoin) or (mesin and mesfn >12)):
                resultado_label.config(text="Erro: a data final deve ser depois da inicial.", fg="red")     
        else:
                mensagem = f"Resultado: O(A) contribuinte possui: {calculo()}"
                resultado_label.config(text=mensagem, fg="white")

                linha_historico = (
                f"►Data Inicial: {data_inicial.strftime('%d/%m/%Y')} | Data Final: {data_final.strftime('%d/%m/%Y')} "
                f"\nResultado: {calculo()}\n\n"
                )
                
                # Salva no arquivo
                with open("historico_datas.txt", "a", encoding="utf-8") as arquivo:
                    arquivo.write(linha_historico)

                # Atualiza o campo de histórico
                carregar_historico()

    except ValueError:
           resultado_label.config(text="Por favor, insira apenas números válidos para dia, mês e ano.", fg="#a33636",font=("verdana",12,"bold"))

# Função para limpar os campos de entrada
def limpar_campos():
    entrada_dia_ini.delete(0, tk.END)
    entrada_mes_ini.delete(0, tk.END)
    entrada_ano_ini.delete(0, tk.END)
    entrada_dia_fim.delete(0, tk.END)
    entrada_mes_fim.delete(0, tk.END)
    entrada_ano_fim.delete(0, tk.END)
    resultado_label.config(text="")

# Função para carregar o histórico do arquivo e mostrar na tela
def carregar_historico():
    try:
        with open("historico_datas.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            texto_historico.config(state='normal')
            texto_historico.delete(1.0, tk.END)
            texto_historico.insert(tk.END, conteudo)
            texto_historico.config(state='disabled')
    except FileNotFoundError:
        texto_historico.config(state='normal')
        texto_historico.delete(1.0, tk.END)
        texto_historico.insert(tk.END, "Nenhum histórico disponível.")
        texto_historico.config(state='disabled')


# Criação da janela principal
janela = tk.Tk()
janela.title("CATECON - Calculadora de Dias entre Datas")
janela.configure(bg=COR_FUNDO)
janela.geometry("700x600")
janela.resizable(True, True)
janela.maxsize(width=800,height=550)
janela.minsize(width=400,height=250)

# Função para criar uma linha de entrada
def criar_entrada(linha, titulo, var1, var2, var3):
    tk.Label(frame, text=titulo, font=("Segoe UI", 13, "bold"), bg=COR_FUNDO, fg=fg_color).grid(row=linha, column=0, columnspan=6, pady=(10, 0))
    for i, (texto, var) in enumerate([("Dia:", var1), ("Mês:", var2), ("Ano:", var3)]):
        tk.Label(frame, text=texto, font=font_label, bg=COR_FUNDO).grid(row=linha+1, column=i*2)
        var.grid(row=linha+1, column=i*2+1, padx=5, pady=5)

# Frame principal
frame = tk.Frame(janela, bg=COR_FUNDO)
frame.pack(pady=10)

# Campos de entrada
entrada_dia_ini = tk.Entry(frame, width=6, font=font_entry, bg=entry_bg)
entrada_mes_ini = tk.Entry(frame, width=6, font=font_entry, bg=entry_bg)
entrada_ano_ini = tk.Entry(frame, width=7, font=font_entry, bg=entry_bg)
entrada_dia_fim = tk.Entry(frame, width=6, font=font_entry, bg=entry_bg)
entrada_mes_fim = tk.Entry(frame, width=6, font=font_entry, bg=entry_bg)
entrada_ano_fim = tk.Entry(frame, width=7, font=font_entry, bg=entry_bg)

criar_entrada(0, "Data Inicial", entrada_dia_ini, entrada_mes_ini, entrada_ano_ini)
criar_entrada(2, "Data Final", entrada_dia_fim, entrada_mes_fim, entrada_ano_fim)

# Botões
btn_frame = tk.Frame(janela, bg=COR_FUNDO)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Calcular", command=calcular_dias, font=font_button,
          bg=btn_color, fg="white", width=15).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Limpar Campos", command=limpar_campos, font=font_button,
          bg=btn_clear, fg="white", width=15).grid(row=0, column=1, padx=10)

# Resultado
resultado_label = tk.Label(janela, text="Resultado: ", font=("Segoe UI", 13), bg=COR_FUNDO, fg="white")
resultado_label.pack()

# Histórico
tk.Label(janela, text="Histórico de Cálculos", font=("Segoe UI", 11, "bold"),
         bg=COR_FUNDO, fg=accent_color).pack(pady=(8, 8))

texto_historico = tk.Text(janela, height=10, width=80, state='disabled', bg="#faffb2",
                          font=("arial", 10), wrap="none", relief="solid", bd=1)
texto_historico.pack(pady=(10, 10))

carregar_historico()

janela.mainloop()
