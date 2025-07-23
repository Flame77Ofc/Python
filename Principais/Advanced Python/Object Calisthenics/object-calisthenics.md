1. Não use else
    Códigos **Hadouken** são os códigos que possuem inúmeros else's, e isso dificulta muito a leitura e a legibilidade do código. A recomendação de "Early Return/Fail First" busca eliminar o código Hadouken e substituir essa "mal prática" por outras técnicas mais eficientes e com maior legibilidade.

    # Técnicas
    1. Early Return: Retornar cedo
        ## Sem Early Return

            def pode_acessar(usuario):
            if usuario.ativo:
                if not usuario.bloqueado:
                    if usuario.email_confirmado:
                        return True
            return False

        ## Com Early Return
            def pode_acessar(usuario):
                if not usuario.ativo:
                    return False

                if usuario.bloqueado:
                    return False

                if not usuario.email_confirmado:
                    return False

                return True
    2. Fail First: Falhar primeiro
        ## Sem Fail First

            def processar_pedido(pedido):
            if pedido:
                if pedido.valor > 0:
                    if pedido.estoque_disponivel():
                        # processar o pedido
                        return "Pedido processado"
                    else:
                        return "Sem estoque"
                else:
                    return "Valor inválido"
            else:
                return "Pedido inexistente"

        ## Com Fail First
            def processar_pedido(pedido):
                if not pedido:
                    return "Pedido inexistente"

                if pedido.valor < 0:
                    return "Valor inválido"

                if not pedido.estoque_disponivel():
                    return "Sem estoque"

                return "Pedido processado"


