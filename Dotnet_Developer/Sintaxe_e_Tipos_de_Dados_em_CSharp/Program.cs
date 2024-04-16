// See https://aka.ms/new-console-template for more information

using Sintaxe_e_Tipos_de_Dados_em_CSharp.Models;
// Nome de Classe mesmo nome do arquivo, atributos e metodos = PascalCase
// variaveis usa-se camelCase
Pessoa pessoa = new(){
    Nome = "Gabriel",
    Idade = 24
};

pessoa.Apresentar();

pessoa.Peso = 55.8F;
pessoa.Sexo = 'M';
pessoa.Casado = false;

pessoa.ApresentacaoCompleta();

pessoa.DataNascimento = DateTime.Now;

Console.WriteLine(pessoa.DataNascimento.ToString("dd/MM/yyyy"));
