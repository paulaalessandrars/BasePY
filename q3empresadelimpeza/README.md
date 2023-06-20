# q3empresadelimpeza

Imagina-se que você e sua equipe foram contratados por uma empresa preste serviços de limpeza para desenvolver a solução de software. Você ficou encarregado da parte de interação com o usuário.
O valor que a empresa cobra por limpeza é dado pela seguinte equação:
total=(metragem*tipo)+adional(is)
Em que cada uma das variáveis que compõe o preço total é quantizada da seguinte maneira:
Quadro 1: Metragem versus valor
Metragem (m²)	Valor (R$)
30 <= metragem < 300	60 + 0.3 *  metragem
300 <= metragem < 700	120 + 0.5 *  metragem
Outros valores	Não são aceitos
	Quadro 2: Tipo versus multiplicador
Tipo	Multiplicador
B – Básica - Indicada para sujeiras semanais ou quinzenais	1.00
C – Completa - Indicada para sujeiras antigas e/ou não rotineiras	1.30


Quadro 3: Adicionais versus valor
Adicionais	Valor (R$)
0- Não desejo mais nada (encerrar)	0,00
1- Passar 10 peças de roupas - R$ 10.00	10,00
2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00	12,00
3- Limpeza de 1 Geladeira/Freezer - R$ 20,00	20,00

Elabore um programa em Python que:
	Pergunte a metragem (em m²);
	Se o valor for 30 e 299,deve-se printar: “É necessário contratar 1 pessoa”
	Se o valor for 300 e 699, deve-se printar “É necessário contratar 2 pessoas”
	Se o valor passar 699, for menor que 30 ou for diferente de número; deve-se repetir a pergunta;
	Pergunte a tipo de limpeza. Se digitar uma opção não válida deve repetir a pergunta
	Pergunte o adicional. Deve-se perguntar ao usuário se desejada mais algum adicional até digitar ele 0
	Encerre o total a ser pago com base na equação desse enunciado.
