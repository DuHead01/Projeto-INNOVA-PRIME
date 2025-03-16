<h1>Projeto INNOVA PRIME</h1>

<h3>Necessidade: Organizar os clientes que fizeram ou irão fazer certificado digital</h3>
<br>
       "Exemplo: Eduardo precisa de um certificado digital para realizar assiatura de documentos
       
    1º - Contato com o cliente
    
    2º - Agendamento do processo (aqui entra o registro do cliente na base de dados por meio do projeto)
   
         Registro: 
               * Nome e sobrenome do cliente
               * Tipo de processo (Contrato ou aditivo) 
               * Correspondente (quem indicou o cliente) 
               * Data 
               * Status do processo
         -> Output: Eduardo Soares - Contrato - Tatiana - 01/01/2025 - Em aberto
         
    3º - Transformar tabela de clientes com status de finalizado em uma tabela para fechamento do mês

<h2>Funcionalidades necessarias</h2>

    * Cadastrar clientes
    * Editar clientes
    * Excluir clientes
    * Pesquisa com filtro (nome, correspodente e range de data)
    * Pegar os dados desejados e fazer uma tabela/documento xml
    
  
    

Linguagem que será usada: Python, sqlite3 e CTkinter (Interface Grafica)-> Possivelmente fazer implantação do firebase
