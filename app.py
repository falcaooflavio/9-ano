import streamlit as st
import random

# Configuração da página móvel
st.set_page_config(page_title="Quiz de Matemática - 2º Bimestre", page_icon="📐", layout="centered")

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

# --- GERADOR DE QUESTÕES EXPANDIDO ---
def gerar_questao(subtopico):
    quadrados_perfeitos = [(1, "1"), (4, "2"), (9, "3"), (16, "4"), (25, "5"), (36, "6"), (49, "7"), (64, "8"), (81, "9"), (100, "10")]
    v = random.choice(['x', 'y', 'a', 'b'])
    v2 = 'y' if v == 'x' else 'x' # Segunda variável se necessário

    # 1) PRODUTOS NOTÁVEIS
    if subtopico == "Quadrado da soma":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        return f"Desenvolva: ({a}{v} + {b})²", f"{a**2}{v}² + {2*a*b}{v} + {b**2}"
        
    elif subtopico == "Quadrado da diferença":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        return f"Desenvolva: ({a}{v} - {b})²", f"{a**2}{v}² - {2*a*b}{v} + {b**2}"
        
    elif subtopico == "Produto da soma pela diferença":
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        return f"Desenvolva: ({a}{v} + {b})({a}{v} - {b})", f"{a**2}{v}² - {b**2}"
    
    # 2) FATORAÇÃO (DIVERSIFICADA COM OS NOVOS EXEMPLOS)
    elif subtopico == "Fator comum":
        tipo = random.randint(1, 5)
        
        if tipo == 1:
            # Exemplo: 5x + 10 = 5(x + 2)
            k = random.randint(3, 12)
            mult = random.randint(2, 5)
            return f"Fatore colocando o fator comum em evidência: {k}{v} + {k*mult}", f"{k}({v} + {mult})"
            
        elif tipo == 2:
            # Exemplo: 10x² + 5x = 5x(2x + 1)
            k = random.randint(2, 6)
            mult = random.randint(2, 4)
            # Ex: se k=5 e mult=2, gera: 10x² + 5x
            return f"Fatore colocando o fator comum em evidência: {k*mult}{v}² + {k}{v}", f"{k}{v}({mult}{v} + 1)"
            
        elif tipo == 3:
            # Apenas número em evidência com potências: kx² + ky = k(x² + y)
            k = random.randint(2, 8)
            mult = random.randint(2, 4)
            return f"Fatore colocando o fator comum em evidência: {k}{v}² + {k*mult}{v2}", f"{k}({v}² + {mult}{v2})"
            
        elif tipo == 4:
            # Letras diferentes com número: kxy + kxz = kx(y + z)
            k = random.randint(2, 7)
            return f"Fatore colocando o fator comum em evidência: {k}{v}{v2} + {k}{v}z", f"{k}{v}({v2} + z)"
            
        else:
            # Exemplo: 2x² + 4 = 2(x² + 2)
            k = random.randint(2, 8)
            mult = random.randint(2, 5)
            return f"Fatore colocando o fator comum em evidência: {k}{v}² + {k*mult}", f"{k}({v}² + {mult})"

    elif subtopico == "Agrupamento":
        tipo = random.randint(1, 4)
        
        if tipo == 1:
            # Exemplo: ax + ay + 5x + 5y = (a + 5)(x + y)
            k = random.randint(2, 9)
            # Usando letras explícitas fixas 'a', 'x', 'y' para manter a didática clássica
            return f"Fatore por agrupamento: a{v} + a{v2} + {k}{v} + {k}{v2}", f"(a + {k})({v} + {v2})"
            
        elif tipo == 2:
            # Coeficientes numéricos em cruz: ax² + abx + cx + cb = (x + b)(ax + c)
            a = random.randint(2, 4)
            b = random.randint(2, 4)
            c = random.randint(2, 5)
            pergunta = f"Fatore por agrupamento: {a}{v}² + {a*b}{v} + {c}{v} + {c*b}"
            resposta = f"({v} + {b})({a}{v} + {c})"
            return pergunta, resposta
            
        elif tipo == 3:
            # Duas variáveis puras: xy + ay + bx + ab = (x + a)(y + b)
            a = random.randint(2, 6)
            b = random.randint(2, 6)
            pergunta = f"Fatore por agrupamento: {v}{v2} + {a}{v2} + {b}{v} + {a*b}"
            resposta = f"({v} + {a})({v2} + {b})"
            return pergunta, resposta
            
        else:
            # Polinômio cúbico limpo: x³ + ax² + bx + ab = (x² + b)(x + a)
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            pergunta = f"Fatore por agrupamento: {v}³ + {a}{v}² + {b}{v} + {a*b}"
            resposta = f"({v}² + {b})({v} + {a})"
            return pergunta, resposta

    elif subtopico == "Diferença de dois quadrados":
        qp1, raiz1 = random.choice(quadrados_perfeitos)
        qp2, raiz2 = random.choice(quadrados_perfeitos)
        r1_str = "" if raiz1 == "1" else raiz1
        qp1_str = "" if qp1 == 1 else str(qp1)
        return f"Fatore a diferença de dois quadrados: {qp1_str}{v}² - {qp2}", f"({r1_str}{v} + {raiz2})({r1_str}{v} - {raiz2})"

    elif subtopico == "Trinômio quadrado perfeito":
        tipo = random.choice([1, 2])
        qp1, raiz1 = random.choice(quadrados_perfeitos)
        qp2, raiz2 = random.choice(quadrados_perfeitos)
        r1 = int(raiz1)
        r2 = int(raiz2)
        termo_central = 2 * r1 * r2
        qp1_str = "" if qp1 == 1 else str(qp1)
        r1_str = "" if r1 == 1 else str(r1)
        
        if tipo == 1:
            return f"Fatore o trinômio quadrado perfeito: {qp1_str}{v}² + {termo_central}{v} + {qp2}", f"({r1_str}{v} + {r2})²"
        else:
            return f"Fatore o trinômio quadrado perfeito: {qp1_str}{v}² - {termo_central}{v} + {qp2}", f"({r1_str}{v} - {r2})²"
    
    # 3) EQUAÇÕES DO 2º GRAU
    elif subtopico == "ax² = 0":
        a = random.choice([x for x in range(-20, 21) if x != 0])
        return f"Resolva a equação: {a}x² = 0", "0"
        
    elif subtopico == "ax² + bx = 0":
        a = random.randint(1, 5)
        r2 = random.choice([x for x in range(-10, 11) if x != 0])
        b_calc = -a * r2
        return f"Resolva a equação: {a}x² {'+' if b_calc >= 0 else '-'} {abs(b_calc)}x = 0", f"0 e {r2}"
        
    elif subtopico == "ax² + c = 0":
        if random.choice([True, False]):
            raiz_desejada = random.randint(1, 10)
            a_limitado = random.randint(1, 4)
            c_calc = -(raiz_desejada ** 2) * a_limitado
            return f"Resolva a equação: {a_limitado}x² - {abs(c_calc)} = 0", f"-{raiz_desejada} e {raiz_desejada}"
        else:
            return f"Resolva a equação: {random.randint(1, 5)}x² + {random.randint(1, 50)} = 0", "nao possui raiz real"
            
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
    st.markdown("<h1 class='titulo'>2º BIMESTRE</h1>", unsafe_allow_html=True)
    st.markdown("<div class='sub-prof'>👨‍🏫 Professor: Flávio Antunes de Almeida</div>", unsafe_allow_html=True)
    
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
            st.session_state.num_questao = 1
            st.session_state.acertos = 0
            st.session_state.respondido = False
            st.session_state.feedback = ""
            st.rerun()

# --- TELA 4: O QUIZ ---
elif st.session_state.tela == 'quiz':
    st.write(f"**Questão {st.session_state.num_questao} de 10** — *{st.session_state.subtopico}*")
    st.markdown(f"## {st.session_state.pergunta}")
    
    resposta_aluno = st.text_input("Sua resposta:", key=f"resp_{st.session_state.num_questao}", disabled=st.session_state.respondido)
    
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
                # Normalização completa (ignora maiúsculas, minúsculas, acentos e todos os espaços)
                resp_limpa_aluno = resposta_aluno.replace(" ", "").lower().replace("ã", "a").replace("ó", "o")
                resp_limpa_certa = st.session_state.resposta_certa.replace(" ", "").lower().replace("ã", "a").replace("ó", "o")
                
                sucesso = False
                
                # Raízes em qualquer ordem para Equação do 2º grau
                if "e" in resp_limpa_certa:
                    partes_certas = resp_limpa_certa.split("e")
                    if "e" in resp_limpa_aluno:
                        partes_aluno = resp_limpa_aluno.split("e")
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

# --- ÁREA DO PROFESSOR ---
st.markdown("---")
with st.expander("🔐 Área de Notas do Professor"):
    if not st.session_state.logado_professor:
        senha = st.text_input("Digite a senha de acesso:", type="password", key="senha_prof")
        
        if st.button("Fazer Login"):
            if senha == "juju2025":
                st.session_state.logado_professor = True
                st.rerun()
            else:
                st.error("Senha incorreta. Tente novamente.")
    else:
        st.success("Acesso liberado!")
        
        if not historico_notas:
            st.info("Nenhum aluno realizou o quiz até o momento.")
        else:
            st.markdown("### 📊 Notas dos Alunos")
            notas_ordenadas = sorted(historico_notas, key=lambda x: x["Nota (Acertos)"], reverse=True)
            st.table(notas_ordenadas)
            
            st.markdown("---")
            if st.button("🚨 APAGAR TODAS AS NOTAS DEFINITIVAMENTE"):
                historico_notas.clear()
                st.warning("O histórico de notas foi completamente reinicializado!")
                st.rerun()
        
        if st.button("Sair do Painel"):
            st.session_state.logado_professor = False
            st.rerun()

# --- RODAPÉ GERAL ---
st.markdown("<div class='rodape'>Criado por: Flávio Antunes de Almeida</div>", unsafe_allow_html=True)
