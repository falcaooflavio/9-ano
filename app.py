import streamlit as st
import random

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
    a = random.randint(1, 5)
    b = random.randint(1, 9)
    v = random.choice(['x', 'y', 'a', 'b'])
    
    if subtopico == "Quadrado da soma":
        return f"Desenvolva: ({a}{v} + {b})²", f"{a**2}{v}² + {2*a*b}{v} + {b**2}"
    elif subtopico == "Quadrado da diferença":
        return f"Desenvolva: ({a}{v} - {b})²", f"{a**2}{v}² - {2*a*b}{v} + {b**2}"
    elif subtopico == "Produto da soma pela diferença":
        return f"Desenvolva: ({a}{v} + {b})({a}{v} - {b})", f"{a**2}{v}² - {b**2}"
    elif subtopico == "Fator comum":
        return f"Fatore: {a}{v}² + {a*b}{v}", f"{a}{v}({v} + {b})"
    elif subtopico == "Agrupamento":
        return f"Fatore: x² + {a}x + {b}x + {a*b}", f"(x + {a})(x + {b})"
    elif subtopico == "Diferença de dois quadrados":
        return f"Fatore: {a**2}{v}² - {b**2}", f"({a}{v} + {b})({a}{v} - {b})"
    elif subtopico == "Trinômio quadrado perfeito":
        return f"Fatore: {a**2}{v}² + {2*a*b}{v} + {b**2}", f"({a}{v} + {b})²"
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