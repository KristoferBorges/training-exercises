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
