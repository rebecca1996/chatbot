#trablhando com pthon, instalar o python no seu pc
#instalar o chatterbot > pip install 
#se der erro na instalação atualize o setu tolls pip install --upgrade setuptools
# ou procure soluções no goole

#iniciando a codificação
#importação 

# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

#vamos entrar no nosso bot
bot = ChatBot('Teste')

#aqui ja temos nosso bot, agora precisamos de dados para treinar ele
#conv para criar conversas e vamos ccomeçar a criar nossa lista de conversas
# para esse ipo de cconversa em lista, a proxima conversa deve estar relacionada a anterior

convTeste= ['Oi','Olá','olá Bom dia', 'boma dia, Tudo bem?']
#definir qul vai ser o metodo de treinamento
bot.set_trainer(ListTrainer)

#para treinar
bot.train(conv)

#inserindo nosso loop ppara que o bot possa ser treinaado
while True:
	quest = input('Voce:  ')
	response = bot.get_response(quest)

	print('Bot:' , response)