public class Desafio_06
{
    public static void DobroTriploRaiz()
    {
        Console.Write("Digite um número: ");
        double numero = double.Parse(Console.ReadLine().Trim());

        double dobro = numero * 2;
        double triplo = numero * 3;
        double raiz = Math.Sqrt(numero);

        Console.WriteLine($"O dobro de {numero} é {dobro}");
        Console.WriteLine($"O triplo de {numero} é {triplo}");
        Console.WriteLine($"A raiz quadrada de {numero} é {raiz}");
    }
}