import streamlit as st
import random

# Configuração da página móvel
st.set_page_config(page_title="Quiz de Matemática - 9º Ano", page_icon="📐", layout="centered")

# --- BANCO DE DADOS EM MEMÓRIA COMPARTILHADA ---
@st.cache_resource
def obter_banco_dados():
    return []

historico_notas = obter_banco_dados()

# --- ESTILIZAÇÃO PERSONALIZADA (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #F8FAFC; }
    div.stButton > button:first-child {
        background-color: #2563EB; color: white; font-weight: bold; width: 100%; border-radius: 8px; height: 3em;
    }
    .titulo { color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; text-align: center; font-weight: bold; margin-bottom: 5px; }
    .sub-prof { color: #475569; font-family: 'Helvetica Neue', sans-serif; text-align: center; font-size: 1.2rem; font-weight: 500; margin-bottom: 25px; }
    .rodape { text-align: center; color: #94A3B8; font-size: 0.85rem; margin-top: 50px; padding-top: 20px; border-top: 1px solid #E2E8F0; }
    </style>
    """, unsafe_allow_html=True)

# --- GERADOR DE QUESTÕES ALINHADO COM AS ADAPTAÇÕES ---
def gerar_questao(subtopico):
    # Intervalo amplo solicitado (-20 a 20, exceto 0)
    intervalo_amplo = [x for x in range(-20, 21) if x != 0]
    
    # Quadrados perfeitos até 100
    quadrados_perfeitos = [(1, 1), (4, 2), (9, 3), (16, 4), (25, 5), (36, 6), (49, 7), (64, 8), (81, 9), (100, 10)]
    
    v = random.choice(['x', 'y', 'a', 'b', 'm', 'n'])
    v2 = 'y' if v == 'x' else 'x' if v != 'y' else 'b'

    # 1) FATOR COMUM EM EVIDÊNCIA (TODOS OS CASOS POSSÍVEIS)
    if subtopico == "Fator comum":
        tipo = random.randint(1, 6)
        
        if tipo == 1:
            # Caso: 2x² - 4 = 2(x² - 2)
            k = random.randint(2, 8)
            mult = random.randint(2, 5)
            sinal = random.choice(['+', '-'])
            return f"Fatore colocando o fator comum em evidência: {k}{v}² {sinal} {k*mult}", f"{k}({v}²{sinal}{mult})"
            
        elif tipo == 2:
            # Caso: 15ax + 3a = 3a(5x + 1)
            k = random.randint(2, 6)
            mult = random.randint(2, 5)
            sinal = random.choice(['+', '-'])
            return f"Fatore colocando o fator comum em evidência: {k*mult}a{v} {sinal} {k}a", f"{k}a({mult}{v}{sinal}1)"
            
        elif tipo == 3:
            # Caso: kx + ky = k(x + y)
            k = random.choice(intervalo_amplo)
            sinal = '+' if k > 0 else ''
            return f"Fatore colocando o fator comum em evidência: {k}{v} + {k if k > 0 else abs(k)}{v2}", f"{k}({v}+{v2})"
            
        elif tipo == 4:
            # Caso: x³ - kx² = x²(x - k)
            k = random.choice(intervalo_amplo)
            sinal = '-' if k > 0 else '+'
            return f"Fatore colocando o fator comum em evidência: {v}³ {sinal} {abs(k)}{v}²", f"{v}²({v}{sinal}{abs(k)})"
            
        elif tipo == 5:
            # Caso com duas variáveis: 18a²b + 12ab² = 6ab(3a + 2b)
            k = random.randint(2, 8)
            return f"Fatore colocando o fator comum em evidência: {k*3}{v}²{v2} + {k*2}{v}{v2}²", f"{k}{v}{v2}(3{v}+2{v2})"
            
        else:
            # Caso trinômio: ky⁴ - k_mult*y² + k*y
            k = random.randint(2, 6)
            return f"Fatore colocando o fator comum em evidência: {k*2}{v}⁴ - {k*3}{v}² + {k}{v}", f"{k}{v}(2{v}³-3{v}+1)"

    # 2) FATORAÇÃO POR AGRUPAMENTO
    elif subtopico == "Agrupamento":
        tipo = random.randint(1, 3)
        if tipo == 1:
            return f"Fatore por agrupamento: m{v} + n{v} + m{v2} + n{v2}", f"(m+n)({v}+{v2})"
        elif tipo == 2:
            k = random.choice(intervalo_amplo)
            return f"Fatore por agrupamento: {abs(k)}a {'+' if k>0 else '-'} {abs(k)}b + a{v} + b{v}", f"({k}{v})(a+b)" if k < 0 else f"({v}+{k})(a+b)"
        else:
            k = random.choice(intervalo_amplo)
            sinal = '+' if k > 0 else '-'
            return f"Fatore por agrupamento: {v}² {'+' if k>0 else '-'} {abs(k)}{v} + 2{v} {'+' if k>0 else '-'} {2*abs(k)}", f"({v}+2)({v}{sinal}{abs(k)})"

    # 3) DIFERENÇA DE DOIS QUADRADOS (ORDEM INVERSA, DUAS VARIÁVEIS E QUARTA ORDEM)
    elif subtopico == "Diferença de dois quadrados":
        tipo_dq = random.randint(1, 4)
        qp1, raiz1 = random.choice(quadrados_perfeitos)
        qp2, raiz2 = random.choice(quadrados_perfeitos)
        
        qp1_str = "" if qp1 == 1 else str(qp1)
        qp2_str = "" if qp2 == 1 else str(qp2)
        r1_str = "" if raiz1 == 1 else str(raiz1)
        r2_str = "" if raiz2 == 1 else str(raiz2)
        
        if tipo_dq == 1:
            # Ordem inversa clássica: B - Ax² (Ex: 1 - x²)
            return f"Fatore a diferença de dois quadrados: {qp2} - {qp1_str}{v}²", f"({raiz2}+{r1_str}{v})({raiz2}-{r1_str}{v})"
            
        elif tipo_dq == 2:
            # Duas variáveis elevadas ao quadrado (Ex: 4a² - 9b²)
            var_a, var_b = ('a', 'b') if v not in ['a', 'b'] else ('x', 'y')
            r_a = "" if raiz1 == 1 else str(raiz1)
            r_b = "" if raiz2 == 1 else str(raiz2)
            return f"Fatore a diferença de dois quadrados: {qp1_str}{var_a}² - {qp2_str}{var_b}²", f"({r_a}{var_a}+{r_b}{var_b})({r_a}{var_a}-{r_b}{var_b})"
            
        elif tipo_dq == 3:
            # Potências de quarta ordem pura (Ex: y⁴ - y²)
            return f"Fatore a diferença de dois quadrados: {v}⁴ - {v}²", f"({v}²+{v})({v}²-{v})"
            
        else:
            # Padrão direto: Ax² - B
            return f"Fatore a diferença de dois quadrados: {qp1_str}{v}² - {qp2}", f"({r1_str}{v}+{raiz2})({r1_str}{v}-{raiz2})"

    # 4) TRINÔMIO QUADRADO PERFEITO
    elif subtopico == "Trinômio quadrado perfeito":
        qp1, raiz1 = random.choice(quadrados_perfeitos)
        qp2, raiz2 = random.choice(quadrados_perfeitos)
        termo_central = 2 * raiz1 * raiz2
        qp1_str = "" if qp1 == 1 else str(qp1)
        r1_str = "" if raiz1 == 1 else str(raiz1)
        
        if random.choice([True, False]):
            return f"Fatore o trinômio quadrado perfeito: {qp1_str}{v}² + {termo_central}{v} + {qp2}", f"({r1_str}{v}+{raiz2})²"
        else:
            return f"Fatore o trinômio quadrado perfeito: {qp1_str}{v}² - {termo_central}{v} + {qp2}", f"({r1_str}{v}-{raiz2})²"

    # 5) SIMPLIFICAÇÃO DE FRAÇÕES ALGÉBRICAS
    elif subtopico == "Simplificação de frações":
        tipo = random.randint(1, 3)
        if tipo == 1:
            k = random.choice(intervalo_amplo)
            return f"Simplifique a fração algébrica: \\\\frac{{{k}{v} - {k}}}{{{v}² - 1}}", f"{k}/({v}+1)"
        elif tipo == 2:
            _, k = random.choice(quadrados_perfeitos)
            return f"Simplifique a fração algébrica: \\\\frac{{{v}² + {2*k}{v} + {k**2}}}{{{v} + {k}}}", f"{v}+{k}"
        else:
            _, k = random.choice(quadrados_perfeitos)
            return f"Simplifique a fração algébrica: \\\\frac{{{v}² - {k**2}}}{{{v}² + {2*k}{v} + {k**2}}}", f"({v}-{k})/({v}+{k})"

    return "2 + 2", "4"

# --- CONTROLE DE ESTADO DO APP ---
if 'tela' not in st.session_state:
    st.session_state.tela = 'inicio'
    st.session_state.nome = ''
    st.session_state.turma = ''
    st.session_state.acertos = 0
    st.session_state.num_questao = 1
    st.session_state.respondido = False
    st.session_state.feedback = ""
    st.session_state.feedback_tipo = "info"
    st.session_state.logado_professor = False

# --- TELA 1: IDENTIFICAÇÃO ---
if st.session_state.tela == 'inicio':
    st.markdown("<h1 class='titulo'>LISTA DE EXERCÍCIOS 2</h1>", unsafe_allow_html=True)
    st.markdown("<div class='sub-prof'>👨‍🏫 Professor: Flávio Antunes de Almeida</div>", unsafe_allow_html=True)
    
    nome = st.text_input("Nome Completo do Estudante:")
    turma = st.text_input("Sua Turma (Ex: 9º A):")
    
    if st.button("INICIAR QUIZ"):
        if nome and turma:
            st.session_state.nome = nome
            st.session_state.turma = turma
            st.session_state.tela = 'subtopicos'
            st.rerun()
        else:
            st.error("Por favor, preencha seu nome e turma.")

# --- TELA 2: SELEÇÃO DE SUBTÓPICOS ---
elif st.session_state.tela == 'subtopicos':
    st.markdown(f"### Olá, {st.session_state.nome}! Selecione a seção da lista para treinar:")
    
    opcoes = [
        "Fator comum", 
        "Agrupamento", 
        "Diferença de dois quadrados", 
        "Trinômio quadrado perfeito",
        "Simplificação de frações"
    ]
        
    for opcao in opcoes:
        if st.button(opcao):
            st.session_state.subtopico = opcao
            st.session_state.pergunta, st.session_state.resposta_certa = gerar_questao(opcao)
            st.session_state.tela = 'quiz'
            st.session_state.num_questao = 1
            st.session_state.acertos = 0
            st.session_state.respondido = False
            st.session_state.feedback = ""
            st.rerun()

# --- TELA 3: O QUIZ ---
elif st.session_state.tela == 'quiz':
    st.write(f"**Questão {st.session_state.num_questao} de 10** — *{st.session_state.subtopico}*")
    
    if "frac" in st.session_state.pergunta:
        st.markdown(f"### {st.session_state.pergunta.split(':')[0]}:")
        st.latex(st.session_state.pergunta.split(':')[1].strip())
    else:
        st.markdown(f"## {st.session_state.pergunta}")
    
    resposta_aluno = st.text_input("Sua resposta fatorada (não use espaços):", key=f"resp_{st.session_state.num_questao}", disabled=st.session_state.respondido)
    
    if st.session_state.feedback:
        if st.session_state.feedback_tipo == "success":
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

    if not st.session_state.respondido:
        if st.button("Enviar Resposta"):
            if resposta_aluno.strip() == "":
                st.warning("Por favor, digite uma resposta.")
            else:
                resp_limpa_aluno = resposta_aluno.replace(" ", "").lower().replace("–", "-")
                resp_limpa_certa = st.session_state.resposta_certa.replace(" ", "").lower()
                
                sucesso = False
                
                # Permite ordens trocadas de fatores ex: (a+b)(a-b) ou (a-b)(a+b)
                if ")(" in resp_limpa_certa:
                    partes_certas = resp_limpa_certa.strip("()").split(")(")
                    if ")(" in resp_limpa_aluno:
                        partes_aluno = resp_limpa_aluno.strip("()").split(")(")
                        if sorted(partes_certas) == sorted(partes_aluno): sucesso = True
                else:
                    if resp_limpa_aluno == resp_limpa_certa: sucesso = True

                if sucesso:
                    st.session_state.feedback = "Correto! 🎉"
                    st.session_state.feedback_tipo = "success"
                    st.session_state.acertos += 1
                else:
                    st.session_state.feedback = f"Errado. A resposta correta era: {st.session_state.resposta_certa}"
                    st.session_state.feedback_tipo = "error"
                
                st.session_state.respondido = True
                st.rerun()
    else:
        if st.button("Avançar para a Próxima"):
            st.session_state.feedback = "" 
            if st.session_state.num_questao < 10:
                st.session_state.num_questao += 1
                st.session_state.pergunta, st.session_state.resposta_certa = gerar_questao(st.session_state.subtopico)
                st.session_state.respondido = False
                st.rerun()
            else:
                historico_notas.append({
                    "Nome": st.session_state.nome,
                    "Turma": st.session_state.turma,
                    "Conteúdo": st.session_state.subtopico,
                    "Nota (Acertos)": st.session_state.acertos
                })
                st.session_state.tela = 'fim'
                st.rerun()

# --- TELA 4: FIM ---
elif st.session_state.tela == 'fim':
    st.balloons()
    st.markdown("<h2 style='color:#10B981; text-align:center;'>Exercícios Concluídos!</h2>", unsafe_allow_html=True)
    st.write(f"Muito bem, **{st.session_state.nome}** da turma **{st.session_state.turma}**!")
    st.metric(label="Rendimento Final", value=f"{st.session_state.acertos} / 10 acertos")
    
    if st.button("Voltar ao Menu Principal"):
        st.session_state.tela = 'inicio'
        st.session_state.num_questao = 1
        st.session_state.acertos = 0
        st.rerun()

# --- ÁREA DO PROFESSOR ---
st.markdown("---")
with st.expander("🔐 Painel de Notas do Professor"):
    if not st.session_state.logado_professor:
        senha = st.text_input("Digite a senha de acesso:", type="password", key="senha_prof")
        
        if st.button("Acessar Notas"):
            if senha == "juju2025":
                st.session_state.logado_professor = True
                st.rerun()
            else:
                st.error("Senha incorreta. Tente novamente.")
    else:
        st.success("Acesso liberado!")
        
        if not historico_notas:
            st.info("Nenhum aluno realizou o treino até o momento.")
        else:
            st.markdown("### 📊 Relatório Estatístico")
            notas_ordenadas = sorted(historico_notas, key=lambda x: x["Nota (Acertos)"], reverse=True)
            st.table(notas_ordenadas)
            
            st.markdown("---")
            if st.button("🚨 LIMPAR HISTÓRICO DE NOTAS DEFINITIVAMENTE"):
                historico_notas.clear()
                st.warning("O histórico de notas foi resetado!")
                st.rerun()
        
        if st.button("Fechar Painel"):
            st.session_state.logado_professor = False
            st.rerun()

# --- RODAPÉ GERAL ---
st.markdown("<div class='rodape'>Criado por: Flávio Antunes de Almeida</div>", unsafe_allow_html=True)
