public class Desafio_61
{
	public static void PAWhile()
	{
		bool continua = true;

		Console.Write("INFORME O TERMO: ");
		int termoInput = int.Parse(Console.ReadLine().Trim());
		Console.Write("INFORME A RAZÃO: ");
		int razaoInput = int.Parse(Console.ReadLine());

		while (continua)
		{
			int cont = 0;

			for (int termo = termoInput; termo < 999; termo = termo + razaoInput)
			{
				if (cont == 10)
				{
					continua = false;
					break;
				}
				else
				{
					Console.Write($"{termo} > ");
					cont++;
				}
			}
			Console.WriteLine("ACABOU");
		}
	}
}
