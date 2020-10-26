
import openpyxl, pprint #importando os módulos openpyxl e pprint
#O pprint é uma biblioteca nativa do Python usada para imprimir valores que não são considerados objetos em Python
print('Opening Workbook')
wb = openpyxl.load_workbook('censuspopdata.xlsx') #aqui, abrimos o arquivo Excel
sheet = wb['Population by Census Tract'] #e aqui abrimos a planilha que contém os dados do censo de cada cidade
countyData = {} #essa variável criada contém as populações e o número de setores censitários calculados para cada cidade
print('Reading rows')

for row in range(2, sheet.max_row + 1): #início da iteração em cada linha
#Cada linha da planilha contém dados do setor censitário, ou seja, estado, cidade e população
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

countyData.setdefault(state, {})
countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

#Cada linha representa um setor censitário, então incrementamos em 1 (+=1)
countyData[state][county]['tracts'] += 1
#Aumentamos a população da cidade em população do setor censitário (+= int(pop))
countyData[state][county]['pop'] += int(pop)

#As duas últimas linhas apresentadas realizam o cálculo, ou seja, o incremeto do valor do setor
#e o aumento do valor da população. 
#Para ter certeza que a abreviação da cidade, usada na planilha Excel, será reconhecida pelo código, 
#usamos o método setdefault() para marcar um valor, caso algum ainda não existe para "state".

