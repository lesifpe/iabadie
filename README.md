# 🎓 IAbadie — A IA para responder dúvidas sobre o curso de ADS

Um sistema de perguntas e respostas com busca semântica local. Você digita uma pergunta com suas próprias palavras e o sistema encontra a resposta mais relevante do FAQ — mesmo que você não use as palavras exatas.

Tudo roda localmente no seu computador, sem enviar dados para nenhum serviço externo.

---

## Sumário

- [🎓 IAbadie — A IA para responder dúvidas sobre o curso de ADS](#-iabadie--a-ia-para-responder-dúvidas-sobre-o-curso-de-ads)
  - [Sumário](#sumário)
  - [O que você vai precisar](#o-que-você-vai-precisar)
  - [Passo a passo para rodar o projeto](#passo-a-passo-para-rodar-o-projeto)
    - [1 — Clonar o repositório](#1--clonar-o-repositório)
    - [2 — Criar o ambiente virtual](#2--criar-o-ambiente-virtual)
    - [3 — Ativar o ambiente virtual](#3--ativar-o-ambiente-virtual)
    - [4 — Instalar as dependências](#4--instalar-as-dependências)
    - [5 — Gerar os embeddings do FAQ](#5--gerar-os-embeddings-do-faq)
    - [6 — Rodar o app](#6--rodar-o-app)
  - [Estrutura do projeto](#estrutura-do-projeto)
  - [Como adicionar perguntas ao FAQ](#como-adicionar-perguntas-ao-faq)
  - [Tecnologias utilizadas](#tecnologias-utilizadas)
  - [Problemas comuns](#problemas-comuns)

---

## O que você vai precisar

Antes de começar, instale:

- **Python 3.10 ou superior** — [python.org/downloads](https://www.python.org/downloads/)
- **Git** — [git-scm.com/downloads](https://git-scm.com/downloads)
- **Microsoft Visual C++ Redistributable** (apenas Windows) — [download aqui](https://aka.ms/vs/17/release/vc_redist.x64.exe)

> Para verificar se o Python já está instalado, abra o terminal e digite:
> ```
> python --version
> ```

---

## Passo a passo para rodar o projeto

### 1 — Clonar o repositório

Abra o terminal, navegue até a pasta onde quer salvar o projeto e rode:

```bash
git clone git@github.com:lesifpe/iabadie.git
cd iabadie
```

---

### 2 — Criar o ambiente virtual

O ambiente virtual isola as dependências do projeto do resto do seu computador.

```bash
python -m venv venv
```

---

### 3 — Ativar o ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

> Você saberá que funcionou quando aparecer `(venv)` no início da linha do terminal.

---

### 4 — Instalar as dependências

```bash
pip install sentence-transformers streamlit faiss-cpu
```

> Isso pode demorar alguns minutos na primeira vez.

---

### 5 — Gerar os embeddings do FAQ

Esse passo transforma as perguntas do FAQ em vetores numéricos que o sistema usa para fazer a busca semântica. Na primeira execução, o modelo de linguagem (~400MB) será baixado automaticamente.

```bash
python src/generate_embeddings.py
```

Aguarde até aparecer:
```
Embeddings salvos em ./embeddings/faq.index
```

> As próximas execuções serão instantâneas — o modelo fica em cache local.

---

### 6 — Rodar o app

```bash
streamlit run src/app.py
```

O navegador vai abrir automaticamente em `http://localhost:8501`. Se não abrir, acesse esse endereço manualmente.

---

## Estrutura do projeto

```
iabadie/
├── data/
│   └── faq.json              # perguntas e respostas do FAQ
├── embeddings/               # gerado automaticamente — não commitar
│   └── faq.index
├── src/
│   ├── generate_embeddings.py  # gera e salva os vetores do FAQ
│   ├── search.py               # função de busca semântica
│   └── app.py                  # interface visual do chat
└── README.md
```

---

## Como adicionar perguntas ao FAQ

Abra o arquivo `data/faq.json` e adicione um novo objeto seguindo o padrão:

```json
{
  "id": 10,
  "question": "Sua pergunta aqui?",
  "answer": "A resposta aqui.",
  "tagList": ["tag1", "tag2"],
  "sourceList": ["https://link-da-fonte.com"]
}
```

Depois de salvar, rode novamente o comando do Passo 5 para atualizar os embeddings:

```bash
python src/generate_embeddings.py
```

---

## Tecnologias utilizadas

| Tecnologia                                         | Para que serve                                                          |
| -------------------------------------------------- | ----------------------------------------------------------------------- |
| [sentence-transformers](https://www.sbert.net/)    | Transforma perguntas em vetores que representam o significado semântico |
| [FAISS](https://github.com/facebookresearch/faiss) | Busca vetorial eficiente — encontra os vetores mais similares           |
| [Streamlit](https://streamlit.io/)                 | Interface visual de chat no navegador                                   |
| Modelo `paraphrase-multilingual-MiniLM-L12-v2`     | Modelo de linguagem leve com suporte a português, roda 100% local       |

---

## Problemas comuns

**`OSError: [WinError 126]` ao importar sentence-transformers**
Instale o Visual C++ Redistributable: [download aqui](https://aka.ms/vs/17/release/vc_redist.x64.exe). Depois feche e abra o terminal novamente.

**`(venv)` aparece no terminal mas não reconhece como comando**
O `(venv)` não é um comando — é só um indicador de que o ambiente virtual está ativo. Isso é o comportamento correto.

**Resposta "Não encontrei uma resposta para essa pergunta"**
O sistema não encontrou nenhuma pergunta no FAQ com similaridade suficiente. Tente reformular a pergunta ou adicione perguntas mais abrangentes ao `faq.json`.

<!-- versão da branch A -->