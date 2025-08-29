def verifica_paginas():
    paginas = []

    # Verifica as páginas de 1 até 1000
    try:
        for i in range(1, 1000):
            if i > 0 and i < 10:
                arquivo = open(f"pages/blogs/blog00{i}.py", "r")
                if arquivo:
                    paginas.append(f"pages/blogs/blog00{i}.py")
            elif i > 10 and i < 100:
                arquivo = open(f"pages/blogs/blog0{i}.py", "r")
                if arquivo:
                    paginas.append(f"pages/blogs/blog0{i}.py")
            elif i > 100 and i < 1000:
                arquivo = open(f"pages/blogs/blog{i}.py", "r")
                if arquivo:
                    paginas.append(f"pages/blogs/blog{i}.py")
    except:
        pass

    return paginas


def retorna_nova_pagina():
    paginas = verifica_paginas()

    if not paginas:
        nova_pagina = "pages/blogs/blog001.py"
        return nova_pagina

    pagina = paginas[-1]
    numero = str(int(pagina[-6:-3]) + 1)

    for i in range(1, 4):
        if len(numero) == i:
            zeros = "0" * abs(i-3)
            nova_pagina = f"pages/blogs/blog{zeros}{numero}.py"

    return nova_pagina


print(retorna_nova_pagina())
