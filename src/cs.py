import csv
import random
from datetime import datetime, timedelta

# Definir zonas eleitorais e municípios correspondentes em Sergipe
loc_municipios = {
    1: "Aracaju", 
    2: "Barra dos Coqueiros", 
    3: random.choice(["Aquidabã", "Cedro de São João" , "Graccho Cardoso"]), 
    4: random.choice(["Boquim", "Arauá", "Pedrinhas", "Riachão do Dantas"]), 
    5: random.choice(["Capela", "Malhada dos Bois", "Muribeca" , "Siriri"]), 
    6: "Estância", 
    8: random.choice(["Gararu", "Canhoba", "Itabi", "Nossa Senhora de Lourdes"]), 
    9: "Itabaiana", 
    11: random.choice(["Japaratuba", "Pirambu" ,"Santo Amaro das Brotas"]), 
    12: "Lagarto", 
    13: random.choice(["Laranjeiras", "Areia Branca" , "Riachuelo"]), 
    14: random.choice(["Maruim", "Carmópolis", "Divina Pastora", "General Maynard" , "Rosário do Catete"]), 
    15: random.choice(["Neópolis", "Brejo Grande", "Ilha das Flores", "Pacatuba" , "Santana do São Francisco"]), 
    16: random.choice(["Nossa Senhora das Dores", "Cumbe" , "Feira Nova"]), 
    17: random.choice(["Nossa Senhora da Glória" , "São Miguel do Aleixo"]), 
    18: random.choice(["Porto da Folha", "Monte Alegre"]), 
    19: random.choice(["Propriá", "Amparo de São Francisco", "Japoatã", "São Francisco" , "Telha"]), 
    21: "São Cristóvão", 
    22: random.choice(["Simão Dias", "Poço Verde"]), 
    23: "Tobias Barreto", 
    24: random.choice(["Campo do Brito", "Frei Paulo", "Macambira" , "São Domingos"]), 
    26: random.choice(["Ribeirópolis", "Malhador", "Moita Bonita", "Nossa Senhora Aparecida" , "Santa Rosa de Lima"]), 
    27: "Aracaju", 
    28: random.choice(["Canindé de São Francisco", "Poço Redondo"]), 
    29: random.choice(["Carira", "Pedra Mole", "Pinhão"]), 
    30: random.choice(["Cristinápolis", "Itabaianinha" , "Tomar do Geru"]), 
    31: random.choice(["Itaporanga d'Ajuda", "Salgado"]), 
    34: "Nossa Senhora do Socorro", 
    35: random.choice(["Umbaúba", "Indiaroba" , "Santa Luzia do Itanhy"])
}

zonas_municipios = {
    1: "Aracaju", 
    2: "Barra dos Coqueiros", 
    3: "Aquidabã", 
    4: "Boquim", 
    5: "Capela", 
    6: "Estância", 
    8: "Gararu", 
    9: "Itabaiana", 
    11: "Japaratuba", 
    12: "Lagarto", 
    13: "Laranjeiras", 
    14: "Maruim", 
    15: "Neópolis", 
    16: "Nossa Senhora das Dores", 
    17: "Nossa Senhora da Glória", 
    18: "Porto da Folha", 
    19: "Propriá", 
    21: "São Cristóvão", 
    22: "Simão Dias", 
    23: "Tobias Barreto", 
    24: "Campo do Brito", 
    26: "Ribeirópolis", 
    27: "Aracaju", 
    28: "Canindé de São Francisco", 
    29: "Carira", 
    30: "Cristinápolis", 
    31: "Itaporanga d'Ajuda", 
    34: "Nossa Senhora do Socorro", 
    35: "Umbaúba"
}

# Definir tipos de RAE com pesos (alguns são mais comuns)
tipos_rae = ["Alistamento", "Revisão" ,"Transferência"]
pesos_rae = [0.5, 0.3, 0.1]

# Definir situação do RAE com pesos
situacao_rae = [
    "Atualizado (deferido)", "Cancelado de coincidência", 
    "Cancelado de coincidência com mudança de competência - atualizado", "Excluído", 
    "Excluído do banco de erros", "Excluído do banco de erros - prazo expirado", 
    "Rejeitado", "Em Diligência", "Indeferido", "Deligenciado"
]

pesos_situacao = [0.5, 0.05, 0.05, 0.1, 0.1, 0.05, 0.1, 0.05, 0.1, 0.2]

# Definir final de prazo e título NET com pesos
final_prazo = ["Sim", "Não"]
pesos_prazo = [0.2, 0.8]  # "Sim" menos comum

titulo_net = ["Atendimento presencial", "TituloNET"]
pesos_titulo_net = [0.6, 0.4]

# Definir biometria com pesos
biometria = ["Com biometria", "Sem biometria", "Pendente de biometria"]
pesos_biometria = [0.7, 0.2, 0.1]

def ajustar_pesos(pesos):
    soma_pesos = sum(pesos)
    return [peso / soma_pesos for peso in pesos]  # Normaliza os pesos

# Gerar datas com tendência para certos meses
def gerar_datas_ponderadas():
    data_inicial = datetime(2022, 1, 1)
    data_final = datetime.now()
    delta = data_final - data_inicial
    datas_geradas = []
    for _ in range(random.randint(5, 30)):  # Variar o número de registros por zona
        dias_aleatorios = random.gauss(delta.days // 2, delta.days // 6)  # Gerar datas com tendência para o meio do ano
        data = data_inicial + timedelta(days=int(abs(dias_aleatorios)))  # Converter para uma data válida
        datas_geradas.append(data)
    return datas_geradas

# Criar arquivo CSV
with open('dados_eleitorais_aleatorios.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Zona Eleitoral", "Município_zona", "Municipio", "Período (Data)", "Tipo de RAE", "Final de Prazo", "Título Net", "Situação do RAE","Situação de Requerimento", "Biometria", "Tipos de Pendência Biometrica", "Tipo de Biometria que está Pendente"])
    
    for _ in range(1000):  # Ajuste o número de entradas desejado
        zona = random.choice(list(zonas_municipios.keys()))  # Selecionar uma zona eleitoral aleatoriamente
        municipio = zonas_municipios[zona]
        municipio_loc = loc_municipios[zona]
        datas = gerar_datas_ponderadas()
        


        for data in datas:
            pesos_rae_ajustados = ajustar_pesos(pesos_rae)
            pesos_situacao_ajustados = ajustar_pesos(pesos_situacao)
            pesos_prazo_ajustados = ajustar_pesos(pesos_prazo)
            pesos_titulo_net_ajustados = ajustar_pesos(pesos_titulo_net)
            pesos_biometria_ajustados = ajustar_pesos(pesos_biometria)
            prazo = random.choices(final_prazo, weights=pesos_prazo, k=1)[0]
            net = random.choices(titulo_net, weights=pesos_titulo_net, k=1)[0]
            requerimento = None
            pendencia_bio = None
            if net == 'TituloNET':
                tipo_rae = random.choice(["Sem RAE","Alistamento", "Revisão", "Transferência"])
                situacao = random.choice([
                    "AGUARDANDO RESULTADO DO BATIMENTO BIOMÉTRICO",
                    "ATUALIZADO",
                    "BATIMENTO EM ANDAMENTO",
                    "BATIMENTO OK",
                    "CANCELADO DE COINCIDÊNCIA",
                    "CANCELADO DE COINCIDÊNCIA COM MUDANÇA DE COMPETÊNCIA",
                    "CANCELADO DE COINCIDÊNCIA COM MUDANÇA DE COMPETÊNCIA-ATUALIZADO",
                    "COM ERRO",
                    "CANCELADO DE COINCIDÊNCIA COM MUDANÇA DE COMPETÊNCIA CRITICADO",
                    "COM PENDÊNCIA BIOMÉTRICA",
                    "CORRIGIDO",
                    "CRITICADO",
                    "CRITICADO APÓS BATIMENTO",
                    "DIGITADO",
                    "DILIGENCIADO",
                    "DILIGÊNCIA VIRTUAL RESPONDIDA",
                    "DUPLICIDADE/PLURALIDADE-CRITICADO",
                    "ELEITOR CANCELADO EM REVISÃO OU TRANSFERÊNCIA-CRITICADO",
                    "ELEITOR CANCELADO EM REVISÃO OU TRANSFERÊNCIA-LIDERADO",
                    "ELEITOR LIBERADO DE DUPLICIDADE/PLURALIDADE",
                    "EM DILIGÊNCIA",
                    "EM DILIGÊNCIA VIRTUAL",
                    "ENVIADO",
                    "ENVOLVIDO EM DUPLICIDADE/PLURALIDADE",
                    "EXCLUÍDO",
                    "EXCLUÍDO DO BANCO DE ERROS",
                    "EXCLUÍDO DO BANCO DE ERROS - PRAZO EXPIRADO",
                    "FECHADO",
                    "GÊMEO EM DUPLICIDADE/PLURALIDADE - CRITICADO",
                    "GÊMEO ENVOLVIDO EM DUPLICIDADE/PLURALIDADE INDEFERIDO",
                    "PAGAMENTO DE MULTA PENDENTE REJEITADO"
                ])
                requerimento = random.choice([
                    "AGUARDANDO ANÁLISE",
                    "EXCLUÍDO",
                    "EM PROCESSAMENTO",
                    "EXCLUÍDO POR DECURSO DE PRAZO LEGAL COM PENDÊNCIA",
                    "PENDENTE DE DOCUMENTOS",
                    "EM ANÁLISE",
                    "EM PROCESSAMENTO COM PENDÊNCIA",
                    "FINALIZADO COM SUCESSO",
                    "ARQUIVOS DELETADOS",
                    "FINALIZADO COM INSUCESSO (DECISÃO DA AUTORIDADE JUDICIÁRIA)",
                    "FINALIZADO COM INSUCESSO (IDENTIFICADO ERROS)",
                    "FINALIZADO COM INSUCESSO (INVIABILIZADO DE SER SUBMETIDO AO PROCESSAMENTO)",
                    "FINALIZADO COM INSUCESSO (INDEFERIDO APÓS DILIGÊNCIA)",
                    "FINALIZADO COM INSUCESSO (RECUSADO AUTOMATICAMENTE PELO SISTEMA)",
                    "FINALIZADO COM INSUCESSO (PERÍODO DE SOLICITAÇÃO INVÁLIDO)",
                    "PENDENTE DE COLETA BIOMÉTRICA"])
                
            elif net == "Atendimento presencial":
                situacao = random.choice([    "Com Banco de Erros",
                                            "Em Coincidência",
                                            "Em Pendência de Biometria",
                                            "Em Diligência",
                                        "Diligenciado"])
                tipo_rae = random.choices(tipos_rae, weights=pesos_rae_ajustados, k=1)[0]  # Usar pesos ajustados
            pendencia_bio = None
            if situacao == "Em Pendência de Biometria":
                
                pendencia_bio = random.choice([
                        "Coleta",
                        "Envio",
                        "Recebimento",
                        "Processamento",
                        "Arquivo Inválido"
                ])
                pendencia_bio = pendencia_bio.upper()
            tipo_bio_pen = None
            if pendencia_bio == "COLETA":
                tipo_bio_pen = random.choice([
                    "ASSINATURA",
                    "FOTO",
                    "DIGITAL"
                ])
            
  # Usar pesos ajustados
            bio = random.choices(biometria, weights=pesos_biometria_ajustados, k=1)[0]  # Usar pesos ajustados
            zona_formatada = f"{zona:02d}"
            writer.writerow([zona_formatada, municipio, municipio_loc, data.strftime("%Y-%m-%d"), tipo_rae, prazo, net, situacao.upper(), requerimento, bio, pendencia_bio, tipo_bio_pen])


print("Arquivo CSV gerado com sucesso.")

loc_municipios_fixos = {
    1: ["Aracaju"], 
    2: ["Barra dos Coqueiros"], 
    3: ["Aquidabã", "Cedro de São João", "Graccho Cardoso"], 
    4: ["Boquim", "Arauá", "Pedrinhas", "Riachão do Dantas"], 
    5: ["Capela", "Malhada dos Bois", "Muribeca", "Siriri"], 
    6: ["Estância"], 
    8: ["Gararu", "Canhoba", "Itabi", "Nossa Senhora de Lourdes"], 
    9: ["Itabaiana"], 
    11: ["Japaratuba", "Pirambu", "Santo Amaro das Brotas"], 
    12: ["Lagarto"], 
    13: ["Laranjeiras", "Areia Branca", "Riachuelo"], 
    14: ["Maruim", "Carmópolis", "Divina Pastora", "General Maynard", "Rosário do Catete"], 
    15: ["Neópolis", "Brejo Grande", "Ilha das Flores", "Pacatuba", "Santana do São Francisco"], 
    16: ["Nossa Senhora das Dores", "Cumbe", "Feira Nova"], 
    17: ["Nossa Senhora da Glória", "São Miguel do Aleixo"], 
    18: ["Porto da Folha", "Monte Alegre"], 
    19: ["Propriá", "Amparo de São Francisco", "Japoatã", "São Francisco", "Telha"], 
    21: ["São Cristóvão"], 
    22: ["Simão Dias", "Poço Verde"], 
    23: ["Tobias Barreto"], 
    24: ["Campo do Brito", "Frei Paulo", "Macambira", "São Domingos"], 
    26: ["Ribeirópolis", "Malhador", "Moita Bonita", "Nossa Senhora Aparecida", "Santa Rosa de Lima"], 
    27: ["Aracaju"], 
    28: ["Canindé de São Francisco", "Poço Redondo"], 
    29: ["Carira", "Pedra Mole", "Pinhão"], 
    30: ["Cristinápolis", "Itabaianinha", "Tomar do Geru"], 
    31: ["Itaporanga d'Ajuda", "Salgado"], 
    34: ["Nossa Senhora do Socorro"], 
    35: ["Umbaúba", "Indiaroba", "Santa Luzia do Itanhy"]
}

# Função para gerar 1000 registros por município
# Criar arquivo CSV e garantir 1000 registros por município
def gerar_registros_por_municipio():
    with open('dados_eleitorais_aleatorios.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for zona, municipios in loc_municipios_fixos.items():
            for municipio in municipios:
                for _ in range(random.randint(350, 1500)):  # Garantir exatamente 1000 registros por município
                    data = gerar_uma_data_ponderada()  # Gera uma data única por registro
                    prazo = random.choices(final_prazo, weights=pesos_prazo, k=1)[0]
                    net = random.choices(titulo_net, weights=pesos_titulo_net, k=1)[0]
                    requerimento = None
                    pendencia_bio = None
                    if net == 'TituloNET':
                        requerimento = random.choice([
                                "AGUARDANDO ANÁLISE",
                                "EXCLUÍDO",
                                "EM PROCESSAMENTO",
                                "EXCLUÍDO POR DECURSO DE PRAZO LEGAL COM PENDÊNCIA",
                                "PENDENTE DE DOCUMENTOS",
                                "EM ANÁLISE",
                                "EM PROCESSAMENTO COM PENDÊNCIA",
                                "FINALIZADO COM SUCESSO",
                                "ARQUIVOS DELETADOS",
                                "FINALIZADO COM INSUCESSO (DECISÃO DA AUTORIDADE JUDICIÁRIA)",
                                "FINALIZADO COM INSUCESSO (IDENTIFICADO ERROS)",
                                "FINALIZADO COM INSUCESSO (INVIABILIZADO DE SER SUBMETIDO AO PROCESSAMENTO)",
                                "FINALIZADO COM INSUCESSO (INDEFERIDO APÓS DILIGÊNCIA)",
                                "FINALIZADO COM INSUCESSO (RECUSADO AUTOMATICAMENTE PELO SISTEMA)",
                                "FINALIZADO COM INSUCESSO (PERÍODO DE SOLICITAÇÃO INVÁLIDO)",
                                "PENDENTE DE COLETA BIOMÉTRICA"
                            ])
                        tipo_rae = random.choice(["Sem RAE","Alistamento", "Revisão", "Transferência"])
                        situacao = random.choice([
                            "AGUARDANDO RESULTADO DO BATIMENTO BIOMÉTRICO",
                            "ATUALIZADO",
                            "BATIMENTO EM ANDAMENTO",
                            "BATIMENTO OK",
                            "CANCELADO DE COINCIDÊNCIA",
                            "CANCELADO DE COINCIDÊNCIA COM MUDANÇA DE COMPETÊNCIA",
                            "CANCELADO DE COINCIDÊNCIA COM MUDANÇA DE COMPETÊNCIA-ATUALIZADO",
                            "COM ERRO",
                            "CANCELADO DE COINCIDÊNCIA COM MUDANÇA DE COMPETÊNCIA CRITICADO",
                            "COM PENDÊNCIA BIOMÉTRICA",
                            "CORRIGIDO",
                            "CRITICADO",
                            "CRITICADO APÓS BATIMENTO",
                            "DIGITADO",
                            "DILIGENCIADO",
                            "DILIGÊNCIA VIRTUAL RESPONDIDA",
                            "DUPLICIDADE/PLURALIDADE-CRITICADO",
                            "ELEITOR CANCELADO EM REVISÃO OU TRANSFERÊNCIA-CRITICADO",
                            "ELEITOR CANCELADO EM REVISÃO OU TRANSFERÊNCIA-LIDERADO",
                            "ELEITOR LIBERADO DE DUPLICIDADE/PLURALIDADE",
                            "EM DILIGÊNCIA",
                            "EM DILIGÊNCIA VIRTUAL",
                            "ENVIADO",
                            "ENVOLVIDO EM DUPLICIDADE/PLURALIDADE",
                            "EXCLUÍDO",
                            "EXCLUÍDO DO BANCO DE ERROS",
                            "EXCLUÍDO DO BANCO DE ERROS - PRAZO EXPIRADO",
                            "FECHADO",
                            "GÊMEO EM DUPLICIDADE/PLURALIDADE - CRITICADO",
                            "GÊMEO ENVOLVIDO EM DUPLICIDADE/PLURALIDADE INDEFERIDO",
                            "PAGAMENTO DE MULTA PENDENTE REJEITADO"
                        ])

                    elif net == "Atendimento presencial":
                        situacao = random.choice([    "Com Banco de Erros",
                                                    "Em Coincidência",
                                                    "Em Pendência de Biometria",
                                                    "Em Diligência",
                                                    "Diligenciado"])
                        situacao = situacao.upper()
                        tipo_rae = random.choices(tipos_rae, weights=pesos_rae_ajustados, k=1)[0]  # Usar pesos ajustados
                    pendencia_bio = None
                    if situacao == "Em Pendência de Biometria":
                
                        pendencia_bio = random.choice([
                                "Coleta",
                                "Envio",
                                "Recebimento",
                                "Processamento",
                                "Arquivo Inválido"
                        ])
                        
                        pendencia_bio = pendencia_bio.upper()
                    tipo_bio_pen = None
                    if pendencia_bio == "COLETA":
                        tipo_bio_pen = random.choice([
                            "ASSINATURA",
                            "FOTO",
                            "DIGITAL"
                        ])
                    
                    bio = random.choices(biometria, weights=pesos_biometria, k=1)[0]
                    zona_formatada = f"{zona:02d}"

                    writer.writerow([zona_formatada, zonas_municipios[zona], municipio, data.strftime("%Y-%m-%d"), tipo_rae, prazo, net, situacao, requerimento, bio,pendencia_bio, tipo_bio_pen])

# Função para gerar uma data ponderada
def gerar_uma_data_ponderada():
    data_inicial = datetime(2022, 1, 1)
    data_final = datetime.now()
    delta = data_final - data_inicial
    dias_aleatorios = random.gauss(delta.days // 2, delta.days // 6)  # Gerar uma data com tendência para o meio do ano
    return data_inicial + timedelta(days=int(abs(dias_aleatorios)))  # Converter para uma data válida

# Chamando a função para gerar os registros
gerar_registros_por_municipio()

print("Novos registros adicionados com sucesso.")
print("Novos registros adicionados com sucesso.asd")



