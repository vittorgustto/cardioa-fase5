# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="./assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" style="border:0; width:40%; height:40%;">
  </a>
</p>

<br>


## Grupo 40

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/vittor-augusto/">Vitor Augusto Gomes</a>
- <a href="https://www.linkedin.com/in/jo%C3%A3o-vitor-lopes-beiro-59a007248/">João Vitor Lopes Beiro</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi Chiovato</a>


## 📜 Descrição

# 🫁 CardioIA - Fase 5: Assistente Cardiológico Inteligente

Este repositório contém a solução da Fase 5 do projeto CardioIA. O objetivo é apresentar um protótipo funcional de um assistente conversacional focado em saúde cardiovascular, integrando tecnologias de Processamento de Linguagem Natural (NLP), Backend em Python e Interface Web.

📋 Sobre o Projeto
O CardioIA utiliza o IBM watsonx Assistant para interpretar intenções de usuários, fornecendo orientações sobre níveis de pressão arterial e triagem de sintomas. O projeto segue princípios éticos de saúde, incluindo fluxos de urgência e tratamento de exceções.

Principais Funcionalidades:
* **Interação via NLP:** Compreensão de mensagens em linguagem natural.
* **Triagem de Sintomas:** Identificação de sinais críticos de saúde.
* **Integração Full-Stack:** Comunicação entre Frontend, Backend e Cloud AI.
* **Tratamento de Exceções:** Fluxo de "No Matches" para entradas não mapeadas.

---

🛠️ Tecnologias Utilizadas

* **IA/NLP:** IBM watsonx Assistant (Modelagem de Intents, Entities e Actions).
* **Backend:** Python 3.x com framework Flask.
* **Frontend:** HTML5, CSS3 e JavaScript (Fetch API).
* **Comunicação:** API RESTful da IBM Cloud SDK.

---

## 👥 Colaboração e Organização da Equipe

Este projeto foi desenvolvido adotando metodologias ágeis e divisão interdisciplinar de tarefas, simulando um ambiente real de HealthTech. O projeto foi executado de forma interdisciplinar, dividindo as responsabilidades entre lógica de IA, desenvolvimento backend e design de interface, garantindo que as competências técnicas se integrassem de forma coesa.

| Integrante |
| :--- |
| **[Vitor Augusto Gomes]** • Responsável pela modelagem do cérebro da IA no IBM Watson, criando a arquitetura de Intents, Entities e o fluxo de Actions. Desenvolveu o servidor Middleware em Flask, criando a ponte de comunicação via API RESTful e garantindo a segurança das chaves de acesso. |
| **[João Vitor Lopes Beiro]** • Responsável pela criação da interface do usuário (UI) em HTML5 e CSS3, focando na usabilidade e experiência do paciente. Implementou a lógica de consumo da API via JavaScript (Fetch API) para permitir a troca de mensagens assíncronas em tempo real. |

> *A colaboração e comunicação constante foram essenciais para integrar o projeto.*

---

## 🚀 Funcionalidades do Projeto

O CardioIA foi projetado para atuar como uma primeira camada de interação informativa, focando em:

* **Triagem Automatizada de Sintomas:** O assistente identifica descrições de dores ou desconfortos e diferencia dúvidas comuns de quadros que sugerem urgência.

* **Interpretação de Dados Clínicos:** Capacidade de processar valores de pressão arterial informados pelo usuário, comparando-os com os parâmetros de normalidade (12/8 mmHg).

* **Protocolo de Emergência:** Reconhecimento de palavras-chave críticas (como "infarto" ou "dor forte no peito") com disparo imediato de orientações de socorro e contato com o SAMU (192).

* **Suporte Educacional:** Respostas rápidas sobre conceitos de saúde cardíaca e prevenção, utilizando uma linguagem acessível ao paciente.

* **Resiliência no Diálogo (Fallback):** Sistema de tratamento para frases não compreendidas, evitando que o usuário fique sem resposta e redirecionando a conversa para os tópicos de domínio do bot.

---

🚀 Como Executar o Projeto
1. Pré-requisitos
Certifique-se de ter o Python instalado. Instale as bibliotecas necessárias utilizando o arquivo requirements.txt:

``
pip install -r requirements.txt
``

2. Configuração das Chaves
Por motivos de segurança, as chaves de API foram omitidas. No arquivo app.py, insira suas credenciais da IBM Cloud:

``
CHAVE_API = 'SUA_CHAVE_AQUI'
URL_SERVICO = 'SUA_URL_AQUI'
ID_ASSISTENTE = 'SEU_ID_AQUI'
``

3. Rodando o Servidor
Inicie o backend Flask:

``
python app.py
``

O servidor estará disponível em http://127.0.0.1:5000.

4. Acessando a Interface
Abra o arquivo ``index.html`` em seu navegador para iniciar a interação com o CardioIA.

``

---

## 🗂 Estrutura dos Arquivos

```
cardioia-fase4/
│
├── assets/                                  # Pasta reservada para guardar imagens estáticas e prints do projeto
│   ├── metricas_cnn_simples.png             # Print dos gráficos de desempenho do Modelo 1 (CNN Simples)
│   ├── metricas_vgg16.png                   # Print dos gráficos de desempenho do Modelo 2 (VGG16 - Transfer Learning)
│   ├── resultado_verdadeiro_positivo.png    # Print da interface acertando um caso de Pneumonia (Verdadeiro Positivo)
│   ├── resultado_verdadeiro_negativo.png    # Print da interface acertando um caso Normal (Verdadeiro Negativo)
│   └── resultado_falso_negativo.png         # Print do erro de resolução (Falso Negativo) para análise crítica
│
├── notebook/                               # Pasta dedicada aos códigos fontes e scripts
│   └── Notebook_CardioIA_Fase4Cap1.ipynb    # O arquivo principal com todo o código da Parte 1 e da Parte 2 e com o notebook interativo para apresentação dos resultados (Pré-proc, Modelos e Interface)
│
├── docs/ 
│   └── Relatorio_CardioIA_Fase4Cap1.pdf     # O documento PDF formal com a descrição técnica e justificativas
│
└── README.md                                # O arquivo de texto com a apresentação do projeto, equipe e resultados
```

---

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>docs</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).



## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>




