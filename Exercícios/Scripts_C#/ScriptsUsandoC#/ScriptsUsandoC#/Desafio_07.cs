public class Desafio_07
{
	public static void Media()
	{
		Console.Write("Digite o primeiro valor: ");
        double valor1 = double.Parse(Console.ReadLine().Trim());

        Console.Write("Digite o segundo valor: ");
        double valor2 = double.Parse(Console.ReadLine().Trim());

        Console.Write("Digite o terceiro valor: ");
        double valor3 = double.Parse(Console.ReadLine().Trim());
        double media = (valor1 + valor2 + valor3) / 3;

        Console.WriteLine($"A média dos valores é {media:F2}");
	}
}
