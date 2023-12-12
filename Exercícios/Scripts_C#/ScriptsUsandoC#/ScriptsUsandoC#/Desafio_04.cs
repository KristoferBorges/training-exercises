public class Desafio_04
{
    public static void AnalisandoString()
    {
        Console.Write("Infome uma Palavra/Frase: ");
        string text = Console.ReadLine().Trim();

        Type tipo = text.GetType();
        Console.WriteLine($"O tipo da variável é {tipo}");
    }
}