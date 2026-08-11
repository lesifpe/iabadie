# Documento de Requisitos - IAbadie

## Requisitos Funcionais

- RF01: Permitir pesquisa por linguagem natural
- RF02: Buscar as perguntas mais similares no FAQ usando embeddings semânticos (busca por similaridade, top 3 resultados)
- RF03: Filtrar respostas com score de similaridade abaixo de um limiar mínimo (0.35), evitando respostas de baixa confiança
- RF04: Exibir a pergunta similar encontrada, a resposta e o percentual de confiança
- RF05: Informar ao usuário quando nenhuma resposta relevante for encontrada
- RF06: Manter histórico de mensagens da conversa durante a sessão

## Requisitos Não Funcionais

- RNF01: Responder utilizando informações presentes em documentos oficiais
- RNF02: Informar ou referenciar a fonte da resposta
- RNF03: Disponibilizar acesso por interface Web
- RNF04: Disponibilizar integração com Whatsapp (pendente de pesquisa)
- RNF05: Respostas claras e objetivas
- RNF06: baixo tempo de resposta
- RNF07: Facilidade de uso
- RNF08: Confiabilidade das informações apresentadas
- RNF09: Disponibilidade em 90% do tempo
