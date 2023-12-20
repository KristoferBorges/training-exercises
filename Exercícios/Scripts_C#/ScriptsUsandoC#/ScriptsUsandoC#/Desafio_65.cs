public class Desafio_65
{
	public static void ColetandoNumeros()
	{
		int numero = 0;
		char escolha = 'S';
		int qntNumeros = 0;
		double valorTotal = 0;
		double maior = 0;
		double menor = 0;

		do
		{
			Console.Write("DIGITE UM NÚMERO: ");
			numero = int.Parse(Console.ReadLine());
			qntNumeros++;

            if (qntNumeros == 1)
			{
				maior = numero;
				menor = numero;
			}
			if (numero > maior)
			{
				maior = numero;
			}
			if (numero < menor)
			{
				menor = numero;
			}

			;
			valorTotal = valorTotal + numero;

			Console.Write("Deseja continua? [S/N]");
			escolha = char.Parse(Console.ReadLine().ToUpper());

		} while (escolha == 'S');
		Console.WriteLine($"\nVocê digitou {qntNumeros} e a média é {valorTotal / qntNumeros}");
		Console.WriteLine($"O maior número foi {maior} e o menor foi {menor}");
    }
}
