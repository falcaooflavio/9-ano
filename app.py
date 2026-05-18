import streamlit as st
import random
import re

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

# --- FUNÇÃO AUXILIAR PARA CORRIGIR COEFICIENTES 1 E -1 ---
def limpar_expressao(exp):
    # Remove coeficientes 1 positivos no início ou após sinais (+ ou -)
    exp = re.sub(r'(?<=^|[\+\-\s])1([a-zA-Z])', r'\1', exp)
    # Trata o caso do -1 virando apenas -
    exp = re.sub(r'(?<=^|[\+\-\s])\-1([a-zA-Z])', r'-\1', exp)
    # Remove espaços extras indesejados que possam surgir
    exp = exp.replace("  ", " ").strip()
    return exp

# --- GERADOR DE QUESTÕES AMPLIADO ---
def gerar_questao(subtopico):
    intervalo_20 = [x for x in range(-20, 21) if x != 0]
    quadrados_perfeitos = [(1, 1), (4, 2), (9, 3), (16, 4), (25, 5), (36, 6), (49, 7), (64, 8), (81, 9), (100, 10)]
    
    v = random.choice(['x', 'y', 'a', 'b', 'm', 'n'])
    v2 = 'y' if v == 'x' else 'x' if v != 'y' else 'b'

    # --- PRODUTOS NOTÁVEIS ---
    if subtopico == "Quadrado da soma de 2 termos":
        tipo = random.randint(1, 3)
        a = abs(random.choice([1, 2, 3, 4, 5]))
        b = abs(random.choice([1, 2, 3, 4, 5]))
        
        if tipo == 1:
            t1 = f"{a if a != 1 else ''}{v}"
            resp = f"{a**2}{v}²+{2*a*b}{v}+{b**2}"
            return limpar_expressao(f"Desenvolva o produto notável: ({t1} + {b})²"), limpar_expressao(resp)
        elif tipo == 2:
            t1 = f"{a if a != 1 else ''}{v}"
            t2 = f"{b if b != 1 else ''}{v2}"
            resp = f"{a**2}{v}²+{2*a*b}{v}{v2}+{b**2}{v2}²"
            return limpar_expressao(f"Desenvolva o produto notável: ({t1} + {t2})²"), limpar_expressao(resp)
        else:
            t1 = f"{a if a != 1 else ''}{v}²"
            t2 = f"{b if b != 1 else ''}{v}"
            resp = f"{a**2}{v}⁴+{2*a*b}{v}³+{b**2}{v}²"
            return limpar_expressao(f"Desenvolva o produto notável: ({t1} + {t2})²"), limpar_expressao(resp)

    elif subtopico == "Quadrado da diferença de 2 termos":
        tipo = random.randint(1, 3)
        a = abs(random.choice([1, 2, 3, 4, 5]))
        b = abs(random.choice([1, 2, 3, 4, 5]))
        
        if tipo == 1:
            t1 = f"{a if a != 1 else ''}{v}"
            resp = f"{a**2}{v}²-{2*a*b}{v}+{b**2}"
            return limpar_expressao(f"Desenvolva o produto notável: ({t1} - {b})²"), limpar_expressao(resp)
        elif tipo == 2:
            t1 = f"{a if a != 1 else ''}{v}"
            t2 = f"{b if b != 1 else ''}{v2}"
            resp = f"{a**2}{v}²-{2*a*b}{v}{v2}+{b**2}{v2}²"
            return limpar_expressao(f"Desenvolva o produto notável: ({t1} - {t2})²"), limpar_expressao(resp)
        else:
            t1 = f"{a if a != 1 else ''}{v}²"
            t2 = f"{b if b != 1 else ''}{v}"
            resp = f"{a**2}{v}⁴-{2*a*b}{v}³+{b**2}{v}²"
            return limpar_expressao(f"Desenvolva o produto notável: ({t1} - {t2})²"), limpar_expressao(resp)

    elif subtopico == "Produto da soma pela diferença":
        tipo = random.randint(1, 3)
        a = abs(random.choice([1, 2, 3, 4, 5]))
        b = abs(random.choice([1, 2, 3, 4, 5]))
        
        if tipo == 1:
            t1 = f"{a if a != 1 else ''}{v}"
            resp = f"{a**2}{v}²-{b**2}"
            return limpar_expressao(f"Desenvolva o produto notável: ({t1} + {b})({t1} - {b})"), limpar_expressao(resp)
        elif tipo == 2:
            t1 = f"{a if a != 1 else ''}{v}"
            t2 = f"{b if b != 1 else ''}{v2}"
            resp = f"{a**2}{v}²-{b**2}{v2}²"
            return limpar_expressao(f"Desenvolva o produto notável: ({t1} + {t2})({t1} - {t2})"), limpar_expressao(resp)
        else:
            t1 = f"{a if a != 1 else ''}{v}²"
            t2 = f"{b if b != 1 else ''}{v}"
            resp = f"{a**2}{v}⁴-{b**2}{v}²"
            return limpar_expressao(f"Desenvolva o produto notável: ({t1} + {t2})({t1} - {t2})"), limpar_expressao(resp)

    # --- FATORAÇÃO ---
    elif subtopico == "Fator comum":
        tipo = random.randint(1, 6)
        if tipo == 1:
            k = random.randint(2, 8)
            mult = random.randint(2, 5)
            sinal = random.choice(['+', '-'])
            return limpar_expressao(f"Fatore colocando o fator comum em evidência: {k}{v}² {sinal} {k*mult}"), limpar_expressao(f"{k}({v}²{sinal}{mult})")
        elif tipo == 2:
            k = random.randint(2, 6)
            mult = random.randint(2, 5)
            sinal = random.choice(['+', '-'])
            return limpar_expressao(f"Fatore colocando o fator comum em evidência: {k*mult}a{v} {sinal} {k}a"), limpar_expressao(f"{k}a({mult}{v}{sinal}1)")
        elif tipo == 3:
            k = random.choice(intervalo_20)
            return limpar_expressao(f"Fatore colocando o fator comum em evidência: {k}{v} + {k if k > 0 else abs(k)}{v2}"), limpar_expressao(f"{k}({v}+{v2})")
        elif tipo == 4:
            k = random.choice(intervalo_20)
            sinal = '-' if k > 0 else '+'
            return limpar_expressao(f"Fatore colocando o fator comum em evidência: {v}³ {sinal} {abs(k)}{v}²"), limpar_expressao(f"{v}²({v}{sinal}{abs(k)})")
        elif tipo == 5:
            k = random.randint(2, 8)
            return limpar_expressao(f"Fatore colocando o fator comum em evidência: {k*3}{v}²{v2} + {k*2}{v}{v2}²"), limpar_expressao(f"{k}{v}{v2}(3{v}+2{v2})")
        else:
            k = random.randint(2, 6)
            return limpar_expressao(f"Fatore colocando o fator comum em evidência: {k*2}{v}⁴ - {k*3}{v}² + {k}{v}"), limpar_expressao(f"{k}{v}(2{v}³-3{v}+1)")

    elif subtopico == "Agrupamento":
        tipo = random.randint(1, 3)
        if tipo == 1:
            return limpar_expressao(f"Fatore por agrupamento: m{v} + n{v} + m{v2} + n{v2}"), limpar_expressao(f"(m+n)({v}+{v2})")
        elif tipo == 2:
            k = random.choice(intervalo_20)
            return limpar_expressao(f"Fatore por agrupamento: {abs(k)}a {'+' if k>0 else '-'} {abs(k)}b + a{v} + b{v}"), limpar_expressao(f"({k}{v})(a+b)" if k < 0 else f"({v}+{k})(a+b)")
        else:
            k = random.choice(intervalo_20)
            sinal = '+' if k > 0 else '-'
            return limpar_expressao(f"Fatore por agrupamento: {v}² {'+' if k>0 else '-'} {abs(k)}{v} + 2{v} {'+' if k>0 else '-'} {2*abs(k)}"), limpar_expressao(f"({v}+2)({v}{sinal}{abs(k)})")

    elif subtopico == "Diferença de dois quadrados":
        tipo_dq = random.randint(1, 4)
        qp1, raiz1 = random.choice(quadrados_perfeitos)
        qp2, raiz2 = random.choice(quadrados_perfeitos)
        qp1_str, qp2_str = "" if qp1 == 1 else str(qp1), "" if qp2 == 1 else str(qp2)
        r1_str, r2_str = "" if raiz1 == 1 else str(raiz1), "" if raiz2 == 1 else str(raiz2)
        
        if tipo_dq == 1:
            return limpar_expressao(f"Fatore a diferença de dois quadrados: {qp2} - {qp1_str}{v}²"), limpar_expressao(f"({raiz2}+{r1_str}{v})({raiz2}-{r1_str}{v})")
        elif tipo_dq == 2:
            var_a, var_b = ('a', 'b') if v not in ['a', 'b'] else ('x', 'y')
            r_a = "" if raiz1 == 1 else str(raiz1)
            r_b = "" if raiz2 == 1 else str(raiz2)
            return limpar_expressao(f"Fatore a diferença de dois quadrados: {qp1_str}{var_a}² - {qp2_str}{var_b}²"), limpar_expressao(f"({r_a}{var_a}+{r_b}{var_b})({r_a}{var_a}-{r_b}{var_b})")
        elif tipo_dq == 3:
            return limpar_expressao(f"Fatore a diferença de dois quadrados: {v}⁴ - {v}²"), limpar_expressao(f"({v}²+{v})({v}²-{v})")
        else:
            return limpar_expressao(f"Fatore a diferença de dois quadrados: {qp1_str}{v}² - {qp2}"), limpar_expressao(f"({r1_str}{v}+{raiz2})({r1_str}{v}-{raiz2})")

    elif subtopico == "Trinômio quadrado perfeito":
        qp1, raiz1 = random.choice(quadrados_perfeitos)
        qp2, raiz2 = random.choice(quadrados_perfeitos)
        termo_central = 2 * raiz1 * raiz2
        qp1_str, r1_str = "" if qp1 == 1 else str(qp1), "" if raiz1 == 1 else str(raiz1)
        if random.choice([True, False]):
            return limpar_expressao(f"Fatore o trinômio quadrado perfeito: {qp1_str}{v}² + {termo_central}{v} + {qp2}"), limpar_expressao(f"({r1_str}{v}+{raiz2})²")
        else:
            return limpar_expressao(f"Fatore o trinômio quadrado perfeito: {qp1_str}{v}² - {termo_central}{v} + {qp2}"), limpar_expressao(f"({r1_str}{v}-{raiz2})²")

    elif subtopico == "Simplificação de frações":
        tipo = random.randint(1, 4)
        k = random.choice([2, 3, 4, 5]) 
        a = random.choice([1, 2, 3, 4, 5])
        a2 = a ** 2
        if tipo == 1:
            return rf"Simplifique a fração algébrica: \frac{{{k}{v} - {k*a}}}{{{v}^2 - {a2}}}", f"{k}/({v}+{a})"
        elif tipo == 2:
            return rf"Simplifique a fração algébrica: \frac{{{v}^2 + {2*a}{v} + {a2}}}{{{k}{v} + {k*a}}}", f"({v}+{a})/{k}"
        elif tipo == 3:
            return rf"Simplifique a fração algébrica: \frac{{{v}^2 - {a2}}}{{{v}^2 + {2*a}{v} + {a2}}}", f"({v}-{a})/({v}+{a})"
        else:
            return rf"Simplifique a fração algébrica: \frac{{{v}^2 - {2*a}{v} + {a2}}}{{{v}^2 - {a2}}}", f"({v}-{a})/({v}+{a})"

    # --- EQUAÇÕES DO 2º GRAU ---
    elif subtopico == "ax² = 0":
        a = random.choice(intervalo_20)
        return limpar_expressao(f"Determine as raízes da equação: {a}x² = 0"), "0"

    elif subtopico == "ax² + bx = 0":
        a = random.choice([x for x in range(-5, 6) if x != 0])
        x2 = random.choice([x for x in range(-15, 16) if x != 0])
        b = -a * x2
        sinal = "+" if b > 0 else "-"
        return limpar_expressao(f"Determine as raízes da equação: {a}x² {sinal} {abs(b)}x = 0"), f"0;{x2}"

    elif subtopico == "ax² + c = 0":
        if random.choice([True, False]):
            raiz = random.randint(1, 10)
            a = random.choice([1, 2, 3, 4])
            c = -(a * (raiz**2))
            sinal = "+" if c > 0 else "-"
            return limpar_expressao(f"Determine as raízes da equação: {a}x² {sinal} {abs(c)} = 0"), f"{raiz};-{raiz}"
        else:
            a = random.randint(1, 10)
            c = random.randint(1, 50)
            return limpar_expressao(f"Determine as raízes da equação: {a}x² + {c} = 0"), "não existe"

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
    st.session_state.eixo_escolhido = ""

# --- TELA 1: IDENTIFICAÇÃO ---
if st.session_state.tela == 'inicio':
    st.markdown("<h1 class='titulo'>EXERCÍCIOS PARA PRATICAR</h1>", unsafe_allow_html=True)
    st.markdown("<div class='sub-prof'>👨‍🏫 Professor: Flávio Antunes de Almeida</div>", unsafe_allow_html=True)
    
    nome = st.text_input("Nome Completo do Estudante:")
    turma = st.text_input("Sua Turma (Ex: 9º A):")
    
    if st.button("INICIAR QUIZ"):
        if nome and turma:
            st.session_state.nome = nome
            st.session_state.turma = turma
            st.session_state.tela = 'eixos_principais'
            st.rerun()
        else:
            st.error("Por favor, preencha seu nome e turma.")

# --- TELA 1B: EIXOS PRINCIPAIS ---
elif st.session_state.tela == 'eixos_principais':
    st.markdown(f"### Olá, {st.session_state.nome}! Selecione a grande área do conteúdo:")
    
    if st.button("PRODUTOS NOTÁVEIS"):
        st.session_state.eixo_escolhido = "produtos_notaveis"
        st.session_state.tela = 'subtopicos'
        st.rerun()
        
    if st.button("FATORAÇÃO"):
        st.session_state.eixo_escolhido = "fatoracao"
        st.session_state.tela = 'subtopicos'
        st.rerun()
        
    if st.button("EQUAÇÃO DO SEGUNDO GRAU"):
        st.session_state.eixo_escolhido = "equacao_2grau"
        st.session_state.tela = 'subtopicos'
        st.rerun()

# --- TELA 2: SELEÇÃO DE SUBTÓPICOS ---
elif st.session_state.tela == 'subtopicos':
    st.markdown("### Selecione o tópico específico para treinar:")
    
    opcoes = []
    if st.session_state.eixo_escolhido == "produtos_notaveis":
        opcoes = ["Quadrado da soma de 2 termos", "Quadrado da diferença de 2 termos", "Produto da soma pela diferença"]
    elif st.session_state.eixo_escolhido == "fatoracao":
        opcoes = ["Fator comum", "Agrupamento", "Diferença de dois quadrados", "Trinômio quadrado perfeito", "Simplificação de frações"]
    elif st.session_state.eixo_escolhido == "equacao_2grau":
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
            
    if st.button("⬅ Voltar aos Temas Principais"):
        st.session_state.tela = 'eixos_principais'
        st.rerun()

# --- TELA 3: O QUIZ ---
elif st.session_state.tela == 'quiz':
    st.write(f"**Questão {st.session_state.num_questao} de 10** — *{st.session_state.subtopico}*")
    
    eh_equacao = "equação" in st.session_state.pergunta.lower()
    
    if eh_equacao:
        st.info("💡 Insira a resposta dentro das chaves separando as raízes por ponto e vírgula. Se não houver raízes reais, apague tudo dentro das chaves e digite: não existe")

    # Renderização correta da fração em LaTeX
    if "frac" in st.session_state.pergunta:
        partes = st.session_state.pergunta.split(":")
        enunciado = partes[0] + ":"
        expressao_latex = partes[1].strip()
        
        st.markdown(f"## {enunciado}")
        st.latex(expressao_latex)
    else:
        st.markdown(f"## {st.session_state.pergunta}")
    
    # Campo pré-escrito para equações ou campo limpo para produtos/fatoração
    valor_padrao = "S = { }" if eh_equacao else ""
    resposta_aluno = st.text_input("Sua resposta:", value=valor_padrao, key=f"resp_{st.session_state.num_questao}", disabled=st.session_state.respondido)
    
    if st.session_state.feedback:
        if st.session_state.feedback_tipo == "success":
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

    if not st.session_state.respondido:
        if st.button("Enviar Resposta"):
            if resposta_aluno.strip() == "" or (eh_equacao and resposta_aluno.strip() == "S = { }"):
                st.warning("Por favor, digite uma resposta válida.")
            else:
                resp_limpa_aluno = resposta_aluno.replace(" ", "").lower().replace("–", "-")
                resp_limpa_certa = st.session_state.resposta_certa.replace(" ", "").lower()
                
                # Se for equação, extrai o conteúdo de dentro de S={} para verificar as raízes
                if eh_equacao:
                    match_aluno = re.search(r's=\{(.*?)\}', resp_limpa_aluno)
                    if match_aluno:
                        resp_limpa_aluno = match_aluno.group(1)
                    else:
                        # Se o aluno deletou o S={} e digitou diretamente "não existe"
                        resp_limpa_aluno = resp_limpa_aluno.replace("s={", "").replace("}", "")

                sucesso = False
                
                # Validação para duas raízes separadas por ";" (Permite inversão)
                if ";" in resp_limpa_certa:
                    partes_certas = resp_limpa_certa.split(";")
                    if ";" in resp_limpa_aluno:
                        partes_aluno = resp_limpa_aluno.split(";")
                        if sorted(partes_certas) == sorted(partes_aluno): 
                            sucesso = True
                # Validação para ordens trocadas de fatores algébricos ex: (a+b)(a-b)
                elif ")(" in resp_limpa_certa:
                    partes_certas = resp_limpa_certa.strip("()").split(")(")
                    if ")(" in resp_limpa_aluno:
                        partes_aluno = resp_limpa_aluno.strip("()").split(")(")
                        if sorted(partes_certas) == sorted(partes_aluno): 
                            sucesso = True
                else:
                    if resp_limpa_aluno == resp_limpa_certa: 
                        sucesso = True

                if sucesso:
                    st.session_state.feedback = "Correto! 🎉"
                    st.session_state.feedback_tipo = "success"
                    st.session_state.acertos += 1
                else:
                    gabarito_exibicao = f"S = {{ {st.session_state.resposta_certa} }}" if eh_equacao and st.session_state.resposta_certa != "não existe" else st.session_state.resposta_certa
                    st.session_state.feedback = f"Errado. A resposta correta era: {gabarito_exibicao}"
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
                st.error("Senha incorre
