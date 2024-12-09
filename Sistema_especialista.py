# Sistema Especialista: IA para Apoio a Pessoas com Necessidades Especiais

# Base de fatos (ferramentas e suas aplicações)
ferramentas_apoio = {
    "ChatGPT": [
        "Comunicação alternativa para pessoas com deficiência verbal",
        "Criação de conteúdos educativos inclusivos",
        "Assistência personalizada para responder dúvidas"
    ],
    "DALL-E": [
        "Geração de imagens acessíveis",
        "Criação de ilustrações personalizadas para inclusão",
        "Desenvolvimento de materiais visuais educativos"
    ],
    "Fotor": [
        "Criação de materiais visuais adaptados",
        "Representação da diversidade",
        "Edição de imagens para adequação a públicos específicos"
    ],
    "Synthesia": [
        "Geração de vídeos com linguagem de sinais",
        "Criação de avatares inclusivos para comunicação",
        "Produção de vídeos educacionais com legendas automáticas"
    ],
    "Tactiq": [
        "Transcrição automática de áudio para texto",
        "Geração de legendas acessíveis",
        "Documentação de reuniões e eventos ao vivo"
    ],
    "Seeing AI": [
        "Descrição de imagens para pessoas com deficiência visual",
        "Leitura de textos a partir de imagens",
        "Identificação de objetos e cenas"
    ],
    "Voiceitt": [
        "Reconhecimento de fala não padrão",
        "Tradução de fala de pessoas com dificuldades na comunicação",
        "Facilitação de interações em tempo real"
    ],
    "Be My Eyes": [
        "Assistência visual remota",
        "Conexão com voluntários para suporte visual",
        "Suporte para tarefas diárias de pessoas com deficiência visual"
    ]
}

# Regras de inferência (associação entre necessidades e ferramentas)
def recomendar_ferramentas(necessidades_usuario):
    recomendacoes = {}
    for ferramenta, aplicacoes in ferramentas_apoio.items():
        for necessidade in necessidades_usuario:
            if necessidade.lower() in " ".join(aplicacoes).lower():
                recomendacoes.setdefault(ferramenta, []).append(necessidade)
    return recomendacoes

# Função principal
def sistema_especialista():
    controle = "sim"
    while controle == "sim":
        # Entrada de necessidades com validação
        while True:
            try:
                print("\n=== Sistema Especialista: IA para Apoio a Pessoas com Necessidades Especiais ===")
                print("Digite as necessidades específicas separadas por vírgula (ex: comunicação alternativa, legendas acessíveis):")
                necessidades_entrada = input("Necessidades: ").strip().lower().split(", ")

                if not necessidades_entrada or necessidades_entrada == ['']:
                    raise ValueError("A lista de necessidades não pode estar vazia.")
                break
            except ValueError as e:
                print(f"Erro na entrada: {e}. Tente novamente.")

        # Recomendações
        recomendacoes = recomendar_ferramentas(necessidades_entrada)

        if recomendacoes:
            print("\nBaseado nas suas necessidades, as ferramentas recomendadas são:")
            for ferramenta, necessidades in recomendacoes.items():
                print(f"- {ferramenta}: Atende às seguintes necessidades: {', '.join(necessidades)}")
        else:
            print("\nNenhuma ferramenta foi encontrada para atender às necessidades fornecidas.")

        # Adicionar novas ferramentas e aplicações com validação
        while True:
            try:
                adicionar = input("\nDeseja adicionar uma nova ferramenta ao sistema? (sim/não): ").strip().lower()
                if adicionar not in ["sim", "não"]:
                    raise ValueError("Digite apenas 'sim' ou 'não'.")
                break
            except ValueError as e:
                print(f"Erro na escolha de adicionar nova ferramenta: {e}. Tente novamente.")

        if adicionar == "sim":
            while True:
                try:
                    nova_ferramenta = input("Digite o nome da nova ferramenta: ").strip()
                    if not nova_ferramenta:
                        raise ValueError("O nome da ferramenta não pode estar vazio.")

                    aplicacoes_associadas = input("Digite as aplicações associadas, separadas por vírgula: ").strip().split(", ")
                    if not aplicacoes_associadas or aplicacoes_associadas == ['']:
                        raise ValueError("A lista de aplicações não pode estar vazia.")

                    ferramentas_apoio[nova_ferramenta] = aplicacoes_associadas
                    print("Nova ferramenta adicionada com sucesso!")
                    print("\nBase de fatos atualizada:")
                    for ferramenta, keys in ferramentas_apoio.items():
                        print(f"Ferramenta: '{ferramenta}' - Aplicações: {keys}")
                    break
                except ValueError as e:
                    print(f"Erro na adição de nova ferramenta: {e}. Tente novamente.")

        # Controle para continuar ou finalizar com validação
        while True:
            try:
                controle = input("\nDeseja continuar usando o sistema? (sim/não): ").strip().lower()
                if controle not in ["sim", "não"]:
                    raise ValueError("Digite apenas 'sim' ou 'não'.")
                break
            except ValueError as e:
                print(f"Erro na escolha de continuar: {e}. Tente novamente.")

sistema_especialista()
print("\n=== Finalizando o Sistema Especialista... ===")
