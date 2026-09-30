# Desafio de Automacao Digital: Gestao de Pecas e Qualidade
# Aluno: Yuri - Modulo 6 (Algoritmos e Logica de Programacao)

pecas = []
caixas_fechadas = []
caixa_atual = []


def avaliar_qualidade(peso, cor, comprimento):
    motivos = []
    
    # Validando o peso (entre 95g e 105g)
    if peso < 95 or peso > 105:
        motivos.append("Peso fora do padrao (permitido: 95g a 105g)")
        
    # Validando a cor (azul ou verde)
    cor = cor.lower()
    if cor != "azul" and cor != "verde":
        motivos.append("Cor invalida (permitido apenas azul ou verde)")
        
    # Validando o comprimento (entre 10cm e 20cm)
    if comprimento < 10 or comprimento > 20:
        motivos.append("Comprimento fora do padrao (permitido: 10cm a 20cm)")
        
    if len(motivos) == 0:
        return True, motivos
    else:
        return False, motivos


def cadastrar_peca():
    global caixa_atual
    print("\n--- CADASTRO DE PECA ---")
    
    # Validacao simples para nao repetir ID
    id_peca = input("Informe o ID da peca: ")
    for p in pecas:
        if p["id"] == id_peca:
            print("Erro: Ja existe uma peca com esse ID cadastrada!")
            return

    try:
        peso = float(input("Informe o peso da peca em gramas: "))
        cor = input("Informe a cor da peca (azul/verde): ")
        comprimento = float(input("Informe o comprimento da peca em cm: "))
    except ValueError:
        print("Erro: Peso e comprimento precisam ser numeros validos.")
        return

    aprovada, motivos = avaliar_qualidade(peso, cor, comprimento)
    
    status = "Aprovada" if aprovada else "Reprovada"
    
    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status,
        "motivos": motivos
    }
    
    pecas.append(peca)
    
    if aprovada:
        caixa_atual.append(peca)
        print(f"Peca {id_peca} APROVADA! Adicionada na caixa ({len(caixa_atual)}/10).")
        
        # Fecha a caixa ao atingir 10 pecas
        if len(caixa_atual) == 10:
            caixas_fechadas.append(caixa_atual)
            caixa_atual = []
            print(f"Caixa cheia com 10 pecas! Caixa {len(caixas_fechadas)} foi fechada.")
    else:
        print(f"Peca {id_peca} REPROVADA:")
        for m in motivos:
            print(f" - {m}")


def listar_pecas():
    print("\n--- LISTAGEM DE PECAS ---")
    if len(pecas) == 0:
        print("Nenhuma peca cadastrada ate o momento.")
        return
        
    print("\n[Pecas Aprovadas]")
    tem_aprovada = False
    for p in pecas:
        if p["status"] == "Aprovada":
            print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
            tem_aprovada = True
    if not tem_aprovada:
        print("Nenhuma peca aprovada.")

    print("\n[Pecas Reprovadas]")
    tem_reprovada = False
    for p in pecas:
        if p["status"] == "Reprovada":
            print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
            for m in p["motivos"]:
                print(f"   Motivo: {m}")
            tem_reprovada = True
    if not tem_reprovada:
        print("Nenhuma peca reprovada.")


def reorganizar_caixas():
    global caixas_fechadas, caixa_atual
    caixas_fechadas = []
    caixa_atual = []
    
    for p in pecas:
        if p["status"] == "Aprovada":
            caixa_atual.append(p)
            if len(caixa_atual) == 10:
                caixas_fechadas.append(caixa_atual)
                caixa_atual = []


def remover_peca():
    print("\n--- REMOVER PECA ---")
    id_remover = input("Digite o ID da peca que deseja excluir: ")
    
    peca_alvo = None
    for p in pecas:
        if p["id"] == id_remover:
            peca_alvo = p
            break
            
    if peca_alvo is None:
        print("Peca nao encontrada.")
        return
        
    pecas.remove(peca_alvo)
    reorganizar_caixas()
    print(f"Peca {id_remover} removida com sucesso!")


def listar_caixas():
    print("\n--- CAIXAS FECHADAS ---")
    if len(caixas_fechadas) == 0:
        print("Ainda nao ha caixas fechadas.")
    else:
        for i, cx in enumerate(caixas_fechadas, start=1):
            ids = []
            for item in cx:
                ids.append(item["id"])
            print(f"Caixa {i} (10 pecas): {', '.join(ids)}")
            
    if len(caixa_atual) > 0:
        print(f"Caixa atual aberta: {len(caixa_atual)} pecas.")


def gerar_relatorio():
    print("\n================ RELATORIO FINAL ================")
    total = len(pecas)
    aprovadas = 0
    reprovadas = 0
    
    for p in pecas:
        if p["status"] == "Aprovada":
            aprovadas += 1
        else:
            reprovadas += 1
            
    print(f"Total de pecas avaliadas: {total}")
    print(f"Total de pecas aprovadas: {aprovadas}")
    print(f"Total de pecas reprovadas: {reprovadas}")
    
    total_caixas = len(caixas_fechadas)
    if len(caixa_atual) > 0:
        total_caixas += 1
    print(f"Total de caixas utilizadas: {total_caixas} (fechadas: {len(caixas_fechadas)})")
    
    print("\nMotivos de reprovacao encontrados:")
    if reprovadas == 0:
        print("Nenhuma peca reprovada.")
    else:
        for p in pecas:
            if p["status"] == "Reprovada":
                print(f"- Peca {p['id']}:")
                for m in p["motivos"]:
                    print(f"   * {m}")
    print("=================================================")


def menu():
    while True:
        print("\n=== SISTEMA DE CONTROLE DE QUALIDADE ===")
        print("1. Cadastrar nova peca")
        print("2. Listar pecas aprovadas/reprovadas")
        print("3. Remover peca cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatorio final")
        print("0. Sair")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida, tente novamente.")


if __name__ == "__main__":
    menu()
