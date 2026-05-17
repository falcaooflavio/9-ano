import streamlit as st
import random
import math

# Configuração da página móvel
st.set_page_config(page_title="Quiz de Matemática - 2º Bimestre", page_icon="📐", layout="centered")

# --- ESTILIZAÇÃO PERSONALIZADA (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #F8FAFC; }
    div.stButton > button:first-child {
        background-color: #2563EB; color: white; font-weight: bold; width: 100%; border-radius: 8px; height: 3em;
    }
    .titulo { color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- GERADOR DE QUESTÕES ---
def gerar_questao(subtopico):
    # Lista de quadrados perfeitos até 100
    quadrados_perfeitos = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
    # Gerador de coeficientes de -20 a 20 (evitando o zero para manter a estrutura)
    a = random.choice([x for x in range(-20, 21) if x != 0])
    b = random.choice([x for x in range(-20, 21) if x != 0])
    v = random.choice(['x', 'y', 'a', 'b'])
    
    # 1) PRODUTOS NOTÁVEIS (a e b de -20 a 20)
    if subtopico == "Quadrado da soma":
        # (ax + b)² = a²x² + 2abx + b²
        sinal_central = "+" if (2*a*b) >= 0 else "-"
        return f"Desenvolva: ({a}{v} + ({b}))²", f"{a**2}{v}² {sinal_central} {abs(2*a*b)}{v} + {b**2}"
        
    elif subtopico == "Quadrado da diferença":
        # (ax - b)² = a²x² - 2abx + b²
        sinal_central = "-" if (2*a*b) >= 0 else "+"
        return f"Desenvolva: ({a}{v} - ({b}))²", f"{a**2}{v}² {sinal_central} {abs(2*a*b)}{v} + {b**2}"
        
    elif subtopico == "Produto da soma pela diferença":
        # (ax + b)(ax - b) = a²x² - b²
        return f"Desenvolva: ({a}{v} + ({b}))({a}{v} - ({b}))", f"{a**2}{v}² - {b**2}"
        
    # 2) FATORAÇÃO (Fator comum e Agrupamento: -20 a 20 | Quadrados Perfeitos para os demais)
    elif subtopico == "Fator comum":
        return f"Fatore: {a}{v}² + {a*b}{v}", f"{a}{v}({v} + {b})" if b >= 0 else f"{a}{v}({v} - {abs(b)})"
        
    elif subtopico == "Agrupamento":
        # x² + ax + bx + ab = (x + a)(x + b)
        sinal_a = "+" if a >= 0 else "-"
        sinal_b = "+" if b >= 0 else "-"
        termo_misto = a + b
        sinal_misto = "+" if termo_misto >= 0 else "-"
        termo_ind = a * b
        sinal_ind = "+" if termo_ind >= 0 else "-"
        
        pergunta = f"Fatore: x² {sinal_misto} {abs(termo_misto)}x {sinal_ind} {abs(termo_ind)}"
        resposta = f"(x {sinal_a} {abs(a)})(x {sinal_b} {abs(b)})"
        return pergunta, resposta
        
    elif subtopico == "Diferença de dois quadrados":
        # Usa quadrados perfeitos do conjunto selecionado
        qp1 = random.choice(quadrados_perfeitos)
        qp2 = random.choice(quadrados_perfeitos)
        raiz1 = int(math.sqrt(qp1))
        raiz2 = int(math.sqrt(qp2))
        return f"Fatore: {qp1}{v}² - {qp2}", f"({raiz1}{v} + {raiz2})({raiz1}{v} - {raiz2})"
        
    elif subtopico == "Trinômio quadrado perfeito":
        qp1 = random.choice(quadrados_perfeitos)
        qp2 = random.choice(quadrados_perfeitos)
        raiz1 = int(math.sqrt(qp1))
        raiz2 = int(math.sqrt(qp2))
        termo_central = 2 * raiz1 * raiz2
        return f"Fatore: {qp1}{v}² + {termo_central}{v} + {qp2}", f"({raiz1}{v} + {raiz2})²"
        
    # 3) EQUAÇÕES DO 2º GRAU
    elif subtopico == "ax² = 0":
        # a variando de -20 a 20
        return f"Resolva: {a}x² = 0", "0"
        
    elif subtopico == "ax² + bx = 0":
        # Para a raiz ser inteira, b deve ser múltiplo de a. Sorteamos a raiz inteira r2.
        r2 = random.choice([x for x in range(-20, 21) if x != 0])
        # ax² + bx = 0 -> x(ax + b) = 0 -> x = 0 ou x = -b/a. Logo, -b/a = r2 -> b = -a * r2
        b_calc = -a * r2
        sinal_b = "+" if b_calc >= 0 else "-"
        
        # Organiza as raízes em ordem crescente para validação correta
        raizes = sorted([0, r2])
        return f"Resolva: {a}x² {sinal_b} {abs(b_calc)}x = 0", f"{raizes[0]} e {raizes[1]}"
        
    elif subtopico == "ax² + c = 0":
        # Sorteia se a equação terá raízes reais ou não (50% de chance para cada)
        com_raiz_real = random.choice([True, False])
        
        if com_raiz_real:
            # Para ter raiz real exata, -c/a deve ser um quadrado perfeito positivo (ex: 4, 9, 16...)
            raiz_desejada = random.randint(1, 10) # gera raizes de 1 a 10 (cujos quadrados vão até 100)
            qp = raiz_desejada ** 2
            
            # Escolhemos um 'a' de -4 a 4 (exceto 0) para que o 'c' não estoure muito o limite de 100
            a_limitado = random.choice([x for x in range(-4, 5) if x != 0])
            # qp = -c / a -> c = -qp * a
            c_calc = -qp * a_limitado
            
            sinal_c = "+" if c_calc >= 0 else "-"
            return f"Resolva: {a_limitado}x² {sinal_c} {abs(c_calc)} = 0", f"-{raiz_desejada} e {raiz_desejada}"
        else:
            # Caso não tenha raiz real: a e c precisam ter o mesmo sinal (assim -c/a fica negativo)
            a_limitado = random.choice([x for x in range(-10, 11) if x != 0])
            c_calc = random.choice([x for x in range(1, 101)])
            if a_limitado < 0:
                c_calc = -c_calc # Garante que possuem o mesmo sinal
                
            sinal_c = "+" if c_calc >= 0 else "-"
            return f"Resolva: {a_limitado}x² {sinal_c} {abs(c_calc)} = 0", "nao possui raiz real"
            
    return "2 + 2", "4"

# --- CONTROLE DE ESTADO DO APP ---
if 'tela' not in st.session_state:
    st.session_state.tela = 'inicio'
    st.session_state.nome = ''
    st.session_state.turma = ''
    st.session_state.acertos = 0
    st.session_state.num_questao = 1

# --- TELA 1: IDENTIFICAÇÃO ---
if st.session_state.tela == 'inicio':
    st.markdown("<h1 class='titulo'>2º BIMESTRE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748B;'>Quiz de Matemática Interativo</p>", unsafe_allow_html=True)
    
    nome = st.text_input("Nome Completo:")
    turma = st.text_input("Sua Turma (Ex: 9º A):")
    
    if st.button("ENTRAR"):
        if nome and turma:
            st.session_state.nome = nome
            st.session_state.turma = turma
            st.session_state.tela = 'topicos'
            st.rerun()
        else:
            st.error("Por favor, preencha seu nome e turma.")

# --- TELA 2: SELEÇÃO DE TÓPICOS ---
elif st.session_state.tela == 'topicos':
    st.markdown(f"### Olá, {st.session_state.nome}! Escolha um tópico:")
    
    t1 = st.button("Produtos Notáveis")
    t2 = st.button("Fatoração")
    t3 = st.button("Equação do 2º Grau")
    
    if t1: st.session_state.topico = "Produtos Notáveis"; st.session_state.tela = 'subtopicos'; st.rerun()
    if t2: st.session_state.topico = "Fatoração"; st.session_state.tela = 'subtopicos'; st.rerun()
    if t3: st.session_state.topico = "Equação do 2º Grau"; st.session_state.tela = 'subtopicos'; st.rerun()

# --- TELA 3: SUBTÓPICOS ---
elif st.session_state.tela == 'subtopicos':
    st.markdown(f"### {st.session_state.topico}")
    st.write("Escolha o conteúdo específico do seu teste:")
    
    opcoes = []
    if st.session_state.topico == "Produtos Notáveis":
        opcoes = ["Quadrado da soma", "Quadrado da diferença", "Produto da soma pela diferença"]
    elif st.session_state.topico == "Fatoração":
        opcoes = ["Fator comum", "Agrupamento", "Diferença de dois quadrados", "Trinômio quadrado perfeito"]
    elif st.session_state.topico == "Equação do 2º Grau":
        opcoes = ["ax² = 0", "ax² + bx = 0", "ax² + c = 0"]
        
    for opcao in opcoes:
        if st.button(opcao):
            st.session_state.subtopico = opcao
            st.session_state.pergunta, st.session_state.resposta_certa = gerar_questao(opcao)
            st.session_state.tela = 'quiz'
            st.rerun()

# --- TELA 4: O QUIZ EM SI ---
elif st.session_state.tela == 'quiz':
    st.write(f"**Questão {st.session_state.num_questao} de 10** — Conteúdo: *{st.session_state.subtopico}*")
    st.markdown(f"## {st.session_state.pergunta}")
    
    st.caption("Dica de formatação: não use espaços na sua resposta. Para duas raízes, use o formato: 'val1 e val2' ou 'nao possui raiz real' se for o caso.")
    resposta_aluno = st.text_input("Sua resposta:", key=f"resp_{st.session_state.num_questao}")
    
    if st.button("Enviar Resposta"):
        # Normalização básica para ajudar na correção de strings (remove espaços, acentos comuns e deixa minúsculo)
        resp_limpa_aluno = resposta_aluno.replace(" ", "").lower().replace("ã", "a").replace("ó", "o")
        resp_limpa_certa = st.session_state.resposta_certa.replace(" ", "").lower().replace("ã", "a").replace("ó", "o")
        
        if resp_limpa_aluno == resp_limpa_certa:
            st.success("Correto! 🎉")
            st.session_state.acertos += 1
        else:
            st.error(f"Errado. A resposta correta era: {st.session_state.resposta_certa}")
            
        if st.session_state.num_questao < 10:
            st.session_state.num_questao += 1
            st.session_state.pergunta, st.session_state.resposta_certa = gerar_questao(st.session_state.subtopico)
            st.button("Próxima Questão")
        else:
            # Salva o resultado localmente no servidor do site
            with open("resultados.csv", "a", encoding="utf-8") as f:
                f.write(f"{st.session_state.nome},{st.session_state.turma},{st.session_state.subtopico},{st.session_state.acertos}\n")
            st.session_state.tela = 'fim'
            st.rerun()

# --- TELA 5: FIM ---
elif st.session_state.tela == 'fim':
    st.balloons()
    st.markdown("<h2 style='color:#10B981; text-align:center;'>Quiz Concluído!</h2>", unsafe_allow_html=True)
    st.write(f"Parabéns, **{st.session_state.nome}** da turma **{st.session_state.turma}**!")
    st.metric(label="Sua Nota Final", value=f"{st.session_state.acertos} / 10")
    
    if st.button("Voltar ao Início"):
        st.session_state.tela = 'inicio'
        st.session_state.num_questao = 1
        st.session_state.acertos = 0
        st.rerun()
        
    # --- ÁREA SECRETA DO PROFESSOR ---
    st.markdown("---")
    with st.expander("🔐 Área do Professor (Clique para abrir)"):
        senha = st.text_input("Digite a senha de acesso:", type="password", key="senha_prof")
        
        if senha == "juju2025": 
            st.success("Acesso liberado!")
            try:
                # Abre o arquivo onde as notas foram acumuladas
                with open("resultados.csv", "r", encoding="utf-8") as f:
                    dados_csv = f.read()
                
                # Botão para baixar a planilha
                st.download_button(
                    label="📥 Baixar Planilha de Notas (Excel/CSV)",
                    data=dados_csv,
                    file_name="notas_dos_alunos.csv",
                    mime="text/csv"
                )
            except FileNotFoundError:
                st.warning("Nenhum aluno realizou o quiz ainda nesta sessão.")        return f"Fatore: {a**2}{v}² + {2*a*b}{v} + {b**2}", f"({a}{v} + {b})²"
    elif subtopico == "ax² = 0":
        return f"Resolva: {a}x² = 0", "0"
    elif subtopico == "ax² + bx = 0":
        return f"Resolva: x² + {b}x = 0", f"0, {-b}" if -b > 0 else f"{-b}, 0"
    elif subtopico == "ax² + c = 0":
        return f"Resolva: x² - {b**2} = 0", f"-{b} e {b}"
    return "2 + 2", "4"

# --- CONTROLE DE ESTADO DO APP ---
if 'tela' not in st.session_state:
    st.session_state.tela = 'inicio'
    st.session_state.nome = ''
    st.session_state.turma = ''
    st.session_state.acertos = 0
    st.session_state.num_questao = 1

# --- TELA 1: IDENTIFICAÇÃO ---
if st.session_state.tela == 'inicio':
    st.markdown("<h1 class='titulo'>2º BIMESTRE</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748B;'>Quiz de Matemática Interativo</p>", unsafe_allow_html=True)
    
    nome = st.text_input("Nome Completo:")
    turma = st.text_input("Sua Turma (Ex: 9º A):")
    
    if st.button("ENTRAR"):
        if nome and turma:
            st.session_state.nome = nome
            st.session_state.turma = turma
            st.session_state.tela = 'topicos'
            st.rerun()
        else:
            st.error("Por favor, preencha seu nome e turma.")

# --- TELA 2: SELEÇÃO DE TÓPICOS ---
elif st.session_state.tela == 'topicos':
    st.markdown(f"### Olá, {st.session_state.nome}! Escolha um tópico:")
    
    t1 = st.button("Produtos Notáveis")
    t2 = st.button("Fatoração")
    t3 = st.button("Equação do 2º Grau")
    
    if t1: st.session_state.topico = "Produtos Notáveis"; st.session_state.tela = 'subtopicos'; st.rerun()
    if t2: st.session_state.topico = "Fatoração"; st.session_state.tela = 'subtopicos'; st.rerun()
    if t3: st.session_state.topico = "Equação do 2º Grau"; st.session_state.tela = 'subtopicos'; st.rerun()

# --- TELA 3: SUBTÓPICOS ---
elif st.session_state.tela == 'subtopicos':
    st.markdown(f"### {st.session_state.topico}")
    st.write("Escolha o conteúdo específico do seu teste:")
    
    opcoes = []
    if st.session_state.topico == "Produtos Notáveis":
        opcoes = ["Quadrado da soma", "Quadrado da diferença", "Produto da soma pela diferença"]
    elif st.session_state.topico == "Fatoração":
        opcoes = ["Fator comum", "Agrupamento", "Diferença de dois quadrados", "Trinômio quadrado perfeito"]
    elif st.session_state.topico == "Equação do 2º Grau":
        opcoes = ["ax² = 0", "ax² + bx = 0", "ax² + c = 0"]
        
    for opcao in opcoes:
        if st.button(opcao):
            st.session_state.subtopico = opcao
            st.session_state.pergunta, st.session_state.resposta_certa = gerar_questao(opcao)
            st.session_state.tela = 'quiz'
            st.rerun()

# --- TELA 4: O QUIZ EM SI ---
elif st.session_state.tela == 'quiz':
    st.write(f"**Questão {st.session_state.num_questao} de 10** — Conteúdo: *{st.session_state.subtopico}*")
    st.markdown(f"## {st.session_state.pergunta}")
    
    resposta_aluno = st.text_input("Sua resposta:", key=f"resp_{st.session_state.num_questao}")
    
    if st.button("Enviar Resposta"):
        resp_limpa_aluno = resposta_aluno.replace(" ", "").lower()
        resp_limpa_certa = st.session_state.resposta_certa.replace(" ", "").lower()
        
        if resp_limpa_aluno == resp_limpa_certa:
            st.success("Correto! 🎉")
            st.session_state.acertos += 1
        else:
            st.error(f"Errado. A resposta correta era: {st.session_state.resposta_certa}")
            
        if st.session_state.num_questao < 10:
            st.session_state.num_questao += 1
            st.session_state.pergunta, st.session_state.resposta_certa = gerar_questao(st.session_state.subtopico)
            st.button("Próxima Questão")
        else:
            # Salva o resultado localmente no servidor do site
            with open("resultados.csv", "a", encoding="utf-8") as f:
                f.write(f"{st.session_state.nome},{st.session_state.turma},{st.session_state.subtopico},{st.session_state.acertos}\n")
            st.session_state.tela = 'fim'
            st.rerun()

# --- TELA 5: FIM ---
elif st.session_state.tela == 'fim':
    st.balloons()
    st.markdown("<h2 style='color:#10B981; text-align:center;'>Quiz Concluído!</h2>", unsafe_allow_html=True)
    st.write(f"Parabéns, **{st.session_state.nome}** da turma **{st.session_state.turma}**!")
    st.metric(label="Sua Nota Final", value=f"{st.session_state.acertos} / 10")
    
    if st.button("Voltar ao Início"):
        st.session_state.tela = 'inicio'
        st.session_state.num_questao = 1
        st.session_state.acertos = 0
        st.rerun()
