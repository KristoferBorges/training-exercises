// Crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

class Desafio_01
{
    public static void SeuNome()
    {
        Console.Write("Digite seu nome: ");
        string nome = Console.ReadLine().Trim();

        if (string.IsNullOrWhiteSpace(nome))
        {
            Console.WriteLine("Bem-vindo, Estranho!");
        }
        else
        {
            Console.WriteLine($"Bem vindo, {nome}!");
        }
    }
}
