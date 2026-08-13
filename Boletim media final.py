print("Boletim de notas")

nome = input ("\n Nome do aluno:")
curso = input ("\n Curso:")
semestre = input ("\n Semestre:")
disciplina = input ("\n Disciplina:")
nota1 = float (input ("\n Nota primeiro Bimestre:"))
nota2 = float  (input ("\n Nota segundo Bimestre:"))

media_final = (nota1 + nota2) / 2.0

if media_final >= 6.0 and media_final <= 100.0:
    print(f"\n | nome: {nome} \n | curso: {curso} \n | semestre: {semestre} \n | disciplina: {disciplina} \n | media final: {media_final} \n | resultado: APROVADO!")

elif media_final < 6.0 and media_final > 19.0:
    print(f"\n | nome: {nome} \n | curso: {curso} \n | semestre: {semestre} \n | disciplina: {disciplina} \n | media final: {media_final} \n | resultado: RECUPERAÇÃO!")

elif media_final > 100.0:
    print("VALOR INVALIDO!") 

else:
    print(f"\n | nome: {nome} \n | curso: {curso} \n | semestre: {semestre} \n | disciplina: {disciplina} \n | media final: {media_final} \n | resultado: REPROVADO!")  
