#
#   PROGRAMA PARA DAR UNFOLLOW
#   EM QUEM NÃO TE SEGUE   
#
# 
# Versão 1.0 

# Importação
from InstagramAPI import InstagramAPI
import getpass
import time

# |Login no intagram|
# getpass solicita a senha do usuario
usuario = input('Usuário: ')
senha = getpass.getpass('Senha: ')

instagram = InstagramAPI(usuario, senha)
instagram.login()

# |Lista de seguidores|
# A funcao getTotal imprime o resultado
meu_id = instagram.username_id
lista_seguidores = instagram.getTotalFollowers(meu_id)

lista_id_seguidores = []
# append = acrescentar 
for user in lista_seguidores:
    lista_id_seguidores.append(user['pk'])

# Lista de quem te segue
lista_seguindo = instagram.getTotalFollowings(meu_id)

# Unfollow em quem você segue e não te segue de volta
# Format() método retorna a string formatada.
for user in lista_seguindo:
    if not(user['pk'] in lista_id_seguidores):
        do_unf = input('Dar unfollow em: {}?\n[Y] ou [N]: '.format(user['username']))
        do_unf = do_unf.upper()
        if(do_unf == 'Y'):
            instagram.unfollow(user['pk'])
            print('Você deixou de seguir: {} com sucesso'.format(user['username']))
            time.sleep(5)
        else:
            pass


