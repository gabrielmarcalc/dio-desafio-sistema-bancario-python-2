
# SISTEMA BANCÁRIO

## OBJETIVO GERAL
Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

## DESAFIO
Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

### SEPARAÇÃO EM FUNÇÕES
Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos nesse módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas podem ser definidos por você da forma que achar melhor.

#### DEPÓSITO
A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

#### SAQUE
A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

#### EXTRATO
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo; argumentos nomeados: extrato.

### NOVAS FUNÇÕES
Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções (exemplo: listar contas).

#### CRIAR USUÁRIO (CLIENTE)
O programa deve armazenar os usuários em uma lista. Um usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço é uma string com o formato: logradouro, nº - bairro - cidade / UF. Devem ser armazenados somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

#### CRIAR CONTA CORRENTE
O programa deve armazenar contas em uma lista. Uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário. Dica: para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
