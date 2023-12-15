public class Desafio_60
{
	public static void Fatorial()
	{
		Console.Write("INFORME UM NÚMERO PARA VER SEU FATORIAL: ");
		int number = int.Parse(Console.ReadLine().Trim());

		int cont = number - 1;
        int resultado = 0;

        while (cont > 0)
		{
			if (cont == number - 1)
			{
				resultado = number * cont;
			}
			else
			{
				resultado = resultado * cont;
			}
            cont--;
        }

        Console.Write($"{number}! = {number}");

        for (int i = number - 1; i > 0; i--) 
		{
			Console.Write($" x {i}");
		}
		Console.WriteLine($" = {resultado}");
        
	}
}