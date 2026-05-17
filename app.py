import streamlit as st
import random
import math

# Configuração da página móvel
st.set_page_config(page_title="Quiz de Matemática - 2º Bimestre", page_icon="📐", layout="centered")

# --- BANCO DE DADOS EM MEMÓRIA COMPARTILHADA ---
# @st.cache_resource garante que todos os usuários (alunos e professor) acessem a mesma lista na memória do servidor
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
    .titulo { color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- GERADOR DE QUESTÕES ---
def gerar_questao(subtopico):
    quadrados_perfeitos = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
    a_pos = random.randint(1, 12)
    b_pos = random.randint(1, 12)
    v = random.choice(['x', 'y', 'a', 'b'])
    
    if subtopico == "Quadrado da soma":
        return f"Desenvolva: ({a_pos}{v} + {b_pos})²", f"{a_pos**2}{v}² + {2*a_pos*b_pos}{v} + {b_pos**2}"
    elif subtopico == "Quadrado da diferença":
        return f"Desenvolva: ({a_pos}{v} - {b_pos})²", f"{a_pos**2}{v}² - {2*a_pos*b_pos}{v} + {b_pos**2}"
    elif subtopico == "Produto da soma pela diferença":
        return f"Desenvolva: ({a_pos}{v} + {b_pos})({a_pos}{v} - {b_pos})", f"{a_pos**2}{v}² - {b_pos**2}"
    elif subtopico == "Fator comum":
        return f"Fatore: {a_pos}{v}² + {a_pos*b_pos}{v}", f"{a_pos}{v}({v} + {b_pos})"
    elif subtopico == "Agrupamento":
        termo_misto = a_pos + b_pos
        termo_ind = a_pos * b_pos
        return f"Fatore: x² + {termo_misto}x + {termo_ind}", f"(x + {a_pos})(x + {b_pos})"
    elif subtopico == "Diferença de dois quadrados":
        qp1, qp2 = random.choice(quadrados_perfeitos), random.choice(quadrados_perfeitos)
        raiz1, raiz2 = int(math.sqrt(qp1)), int(math.sqrt(qp2))
        r1_str = "" if raiz1 == 1 else str(raiz1)
        qp1_str = "" if qp1 == 1 else str(qp1)
        return f"Fatore: {qp1_str}{v}² - {qp2}", f"({r1_str}{v} + {raiz2})({r1_str}{v} - {raiz2})"
    elif subtopico == "Trinômio quadrado perfeito":
        qp1, qp2 = random.choice(quadrados_perfeitos), random.choice(quadrados_perfeitos)
        raiz1, raiz2 = int(math.sqrt(qp1)), int(math.sqrt(qp2))
        termo_central = 2 * raiz1 * raiz2
        r1_str = "" if raiz1 == 1 else str(raiz1)
        qp1_str = "" if qp1 == 1 else str(qp1)
        return f"Fatore: {qp1_str}{v}² + {termo_central}{v} + {qp2}", f"({r1_str}{v} + {raiz2})²"
    elif subtopico == "ax² = 0":
        a = random.choice([x for x in range(-20, 21) if x != 0])
        return f"Resolva: {a}x² = 0", "0"
    elif subtopico == "ax² + bx = 0":
        a = random.randint(1, 5)
        r2 = random.choice([x for x in range(-10, 11) if x != 0])
        b_calc = -a * r2
        return f"Resolva: {a}x² {'+' if b_calc >= 0 else '-'} {abs(b_calc)}x = 0", f"0 e {r2}"
    elif subtopico == "ax² + c = 0":
        if random.choice([True, False]):
            raiz_desejada = random.randint(1, 10)
            a_limitado = random.randint(1, 4)
            c_calc = -(raiz_desejada ** 2) * a_limitado
            return f"Resolva: {a_limitado}x² - {abs(c_calc)} = 0", f"-{raiz_desejada} e {raiz_desejada}"
        else:
            return f"Resolva: {random.randint(1, 5)}x² + {random.randint(1, 50)} = 0", "nao possui raiz real"
    return "2 + 2", "4"

# --- CONTROLE DE ESTADO DO APP ---
if 'tela' not in st.session_state:
    st.session_state.tela = 'inicio'
    st.session_state.nome = ''
    st.session_state.turma = ''
    st.session_state.acertos = 0
    st.session_state.num_questao = 1
    st.session_state.respondido = False

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
            st.session_state.num_questao = 1
            st.session_state.acertos = 0
            st.session_state.respondido = False
            st.rerun()

# --- TELA 4: O QUIZ ---
elif st.session_state.tela == 'quiz':
    st.write(f"**Questão {st.session_state.num_questao} de 10** — Conteúdo: *{st.session_state.subtopico}*")
    st.markdown(f"## {st.session_state.pergunta}")
    st.caption("Dica: Não use espaços. Para duas raízes, use o formato: 'val1 e val2'.")
    
    resposta_aluno = st.text_input("Sua resposta:", key=f"resp_{st.session_state.num_questao}", disabled=st.session_state.respondido)
    
    if not st.session_state.respondido:
        if st.button("Enviar Resposta"):
            if resposta_aluno.strip() == "":
                st.warning("Por favor, digite uma resposta.")
            else:
                resp_limpa_aluno = resposta_aluno.replace(" ", "").lower().replace("ã", "a").replace("ó", "o")
                resp_limpa_certa = st.session_state.resposta_certa.replace(" ", "").lower().replace("ã", "a").replace("ó", "o")
                
                sucesso = False
                if "e" in resp_limpa_certa:
                    partes_certas = resp_limpa_certa.split("e")
                    if "e" in resp_limpa_aluno:
                        partes_aluno = resp_limpa_aluno.split("e")
                        if sorted(partes_certas) == sorted(partes_aluno): sucesso = True
                else:
                    if resp_limpa_aluno == resp_limpa_certa: sucesso = True

                if sucesso:
                    st.success("Correto! 🎉")
                    st.session_state.acertos += 1
                else:
                    st.error(f"Errado. A resposta correta era: {st.session_state.resposta_certa}")
                
                st.session_state.respondido = True
                st.rerun()
    else:
        if st.button("Avançar"):
            if st.session_state.num_questao < 10:
                st.session_state.num_questao += 1
                st.session_state.pergunta, st.session_state.resposta_certa = gerar_questao(st.session_state.subtopico)
                st.session_state.respondido = False
                st.rerun()
            else:
                # CADASTRO DIRETO NA MEMÓRIA COMPARTILHADA DO SERVIDOR
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

# --- ÁREA DO PROFESSOR (Visível de forma independente no rodapé) ---
st.markdown("---")
with st.expander("🔐 Área de Notas do Professor (Acesso Restrito)"):
    senha = st.text_input("Digite a senha de acesso:", type="password", key="senha_prof")
    
    if senha == "juju2025": 
        st.success("Acesso liberado!")
        
        if len(historico_notas) == 0:
            st.info("Nenhum aluno realizou o quiz até o momento.")
        else:
            st.markdown("### 📊 Notas dos Alunos (Ordenadas da Maior para a Menor)")
            
            # Ordena a lista de dicionários nativamente por nota decrescente
            notas_ordenadas = sorted(historico_notas, key=lambda x: x["Nota (Acertos)"], reverse=True)
            
            # Exibe os dados de forma elegante em uma tabela nativa
            st.table(notas_ordenadas)
            
            st.markdown("---")
            st.markdown("⚠️ **Zona de Perigo**")
            # Botão para limpar a memória do servidor de forma definitiva
            if st.button("🚨 APAGAR TODAS AS NOTAS DEFINITIVAMENTE"):
                historico_notas.clear()
                st.warning("O histórico de notas foi completamente reinicializado!")
                st.rerun()            raiz_desejada = random.randint(1, 10)
            qp = raiz_desejada ** 2
            a_limitado = random.randint(1, 4)
            c_calc = -qp * a_limitado
            return f"Resolva: {a_limitado}x² - {abs(c_calc)} = 0", f"-{raiz_desejada} e {raiz_desejada}"
        else:
            a_limitado = random.randint(1, 5)
            c_calc = random.randint(1, 50)
            return f"Resolva: {a_limitado}x² + {c_calc} = 0", "nao possui raiz real"
            
    return "2 + 2", "4"

# --- CONTROLE DE ESTADO DO APP ---
if 'tela' not in st.session_state:
    st.session_state.tela = 'inicio'
    st.session_state.nome = ''
    st.session_state.turma = ''
    st.session_state.acertos = 0
    st.session_state.num_questao = 1
    st.session_state.respondido = False

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
            st.session_state.num_questao = 1
            st.session_state.acertos = 0
            st.session_state.respondido = False
            st.rerun()

# --- TELA 4: O QUIZ EM SI ---
elif st.session_state.tela == 'quiz':
    st.write(f"**Questão {st.session_state.num_questao} de 10** — Conteúdo: *{st.session_state.subtopico}*")
    st.markdown(f"## {st.session_state.pergunta}")
    
    st.caption("Dica de formatação: Não use espaços. Para duas raízes, use o formato: 'val1 e val2' ou 'nao possui raiz real'.")
    
    # Desabilita o campo se o aluno já enviou a resposta para ele ver o feedback antes de avançar
    resposta_aluno = st.text_input("Sua resposta:", key=f"resp_{st.session_state.num_questao}", disabled=st.session_state.respondido)
    
    if not st.session_state.respondido:
        if st.button("Enviar Resposta"):
            if resposta_aluno.strip() == "":
                st.warning("Por favor, digite uma resposta antes de enviar.")
            else:
                resp_limpa_aluno = resposta_aluno.replace(" ", "").lower().replace("ã", "a").replace("ó", "o")
                resp_limpa_certa = st.session_state.resposta_certa.replace(" ", "").lower().replace("ã", "a").replace("ó", "o")
                
                sucesso = False
                if "e" in resp_limpa_certa:
                    partes_certas = resp_limpa_certa.split("e")
                    if "e" in resp_limpa_aluno:
                        partes_aluno = resp_limpa_aluno.split("e")
                        if sorted(partes_certas) == sorted(partes_aluno):
                            sucesso = True
                else:
                    if resp_limpa_aluno == resp_limpa_certa:
                        sucesso = True

                if sucesso:
                    st.success("Correto! 🎉")
                    st.session_state.acertos += 1
                else:
                    st.error(f"Errado. A resposta correta era: {st.session_state.resposta_certa}")
                
                st.session_state.respondido = True
                st.rerun()
    else:
        if st.button("Avançar"):
            if st.session_state.num_questao < 10:
                st.session_state.num_questao += 1
                st.session_state.pergunta, st.session_state.resposta_certa = gerar_questao(st.session_state.subtopico)
                st.session_state.respondido = False
                st.rerun()
            else:
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
                with open("resultados.csv", "r", encoding="utf-8") as f:
                    dados_csv = f.read()
                
                st.download_button(
                    label="📥 Baixar Planilha de Notas (Excel/CSV)",
                    data=dados_csv,
                    file_name="notas_dos_alunos.csv",
                    mime="text/csv"
                )
            except FileNotFoundError:
                st.warning("Nenhum aluno realizou o quiz ainda nesta sessão.")"):
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
