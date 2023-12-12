public class Desafio_09
{
	public static void Tabuada()
	{
		Console.Write("Digite um número: ");
        int numero = int.Parse(Console.ReadLine().Trim());

        for (int i = 0; i <= 10; i++)
		{
			Console.WriteLine($"{numero} x {i} = {numero * i}");
		}
	}
}
