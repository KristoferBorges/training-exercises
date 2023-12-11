public class Desafio_03
{
	public static void SomaValores()
	{
		Console.Write("Digite o primeiro valor: ");
		double valor1 = double.Parse(Console.ReadLine().Trim());

		Console.Write("Digite o segundo valor: ");
		double valor2 = double.Parse(Console.ReadLine().Trim());

		double soma = valor1 + valor2;

		Console.WriteLine($"A soma dos valores é {soma}");
	}
}
