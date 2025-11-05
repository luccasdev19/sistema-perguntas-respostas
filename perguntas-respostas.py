questions = [
    {
    'question' : 'Oque é uma variável?',
    'options' : [
        '1 - uma variável é um espaço dentro da memória onde armazena um valor que pode ser alterado.', 
        '2 - uma variável é um tipo de dado que não pode ser alterado.',
        '3 - uma variável que imprime valores na tela.',
    ],
    'correct_answer' : '1',   
    },

    {
    'question' : 'Oque é uma Feature?', 
    'options' : [
        '1 - uma feature é um bug',
        '2 - Uma feature é uma funcionalidade ou caracteristica de um software.', 
        '3 - uma feature é um tipo de dado. ', 
    ],

    'correct_answer' : '2',
    },

    {
    'question' : 'oque é refaturação? ', 
    'options' : [
        '1 - refaturação é quando um software apresenta erros.',
        '2 - refaturar é pontuar o código com comentários. ',
        '3 - Refatorar é melhorar o design interno do código sem modificar sua funcionalidade.',
    ],
    'correct_answer' : '3',
    },
]

acertos = 0

for options in questions  :
    print(options['question'])

    for option in options['options']:
        print(option)

    answer = input('Digite o número da resposta correta: ')

    if not answer.isdigit():
        print("Entrada inválida! Digite apenas números (1, 2 ou 3).")
        continue
    
    if answer == options['correct_answer']:
        print('Resposta correta!\n')

    else:
        print('Resposta incorreta. A resposta correta é:', options['correct_answer'], '\n')

    if answer == options ['correct_answer']:
        acertos += 1

    else : 
        acertos += 0 


print (f' Você acertou {acertos} de {len(questions)} perguntas. ')
print('Obrigado por participar do quiz!')















