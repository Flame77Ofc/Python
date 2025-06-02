DDDs = {
    11: "São Paulo (Capital)",
    34: "Minas Gerais (Uberlândia)",
    41: "Paraná (Curitiba)",
    42: "Paraná (Ponta Grossa)",
    43: "Paraná (Londrina)",
    44: "Paraná (Maringá)",
    45: "Paraná (Cascavel)",
    47: "Santa Catarina (Sul)",
    67: "Mato Grosso do Sul (Campo Grande)",
    68: "Acre (Rio Branco)",
    69: "Rondônia (Porto Velho)",
    71: "Bahia (Salvador)",
    91: "Pará (Belém)",
    93: "Pará (Santarém)",
    96: "Amapá (Macapá)",
    97: "Amazonas (Interior)",
    98: "Maranhão (São Luís)",
    99: "Maranhão (Imperatriz)"
}

ddd = int(input('Digite o seu DDD: '))

if ddd in DDDs:
    print(f'Seu estado é {DDDs[ddd]}')
else:
    print('Infelizmente seu DDD não foi encontrado!')