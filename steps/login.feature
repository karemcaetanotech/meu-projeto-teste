Feature: Teste de Login
  Como um usuário de sistema
  Eu quero fazer login com credenciais válidas
  Para acessar a área restrita com sucesso

  Scenario: Login com credenciais válidas
    Given eu estou na página de login
    When eu insiro "usuario_teste" e "senha123" como credenciais
    And eu clico no botão de login
    Then eu devo ver a mensagem de boas-vindas "Bem-vindo, usuario_teste"
