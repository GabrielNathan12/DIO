using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Sintaxe_e_Tipos_de_Dados_em_CSharp.Models{
    public class Pessoa{
        // ? nos atributos referece a um parametro sendo opcional
        public string? Nome { get; set; }
        public int? Idade { get; set; }
        public float? Peso {get; set; }
        public char? Sexo {get; set; }
        public bool? Casado { get; set; }
        public DateTime DataNascimento {get; set;}
        public void Apresentar(){
            Console.WriteLine($"Olá, meu nome é {Nome}, e tenho {Idade} anos");
        }
        public void ApresentacaoCompleta(){
            Console.WriteLine($"Nome: " + Nome);
            Console.WriteLine($"Idade: " + Idade);
            Console.WriteLine($"Peso: " + Peso);
            Console.WriteLine($"Sexo: " + Sexo);
            Console.WriteLine($"Casado: " + Casado);
        }
    }
}
