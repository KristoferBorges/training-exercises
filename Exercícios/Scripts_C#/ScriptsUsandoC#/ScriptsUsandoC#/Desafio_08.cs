public class Desafio_08
{
	public static void Distancias()
	{
		Console.Write("Digite um valor em Metros: ");
		double metros = double.Parse(Console.ReadLine().Trim().Replace(".", ","));

		double quilometros = metros * 0.001;
		double hectometro = metros * 0.01;
		double decametros = metros * 0.1;
		double decimetros = metros * 10;
		double centimetros = metros * 100;
		double milimetros = metros * 1000;

		Console.WriteLine($"O valor em Quilômetros é {quilometros:F3}");
		Console.WriteLine($"O valor em Hectômetros é {hectometro:F2}");
		Console.WriteLine($"O valor em Decâmetros é {decametros:F2}");
		Console.WriteLine($"O valor em Decímetros é {decimetros:F2}");
		Console.WriteLine($"O valor em Centímetros é {centimetros:F2}");
		Console.WriteLine($"O valor em Milímetros é {milimetros:F2}");

    }
}
