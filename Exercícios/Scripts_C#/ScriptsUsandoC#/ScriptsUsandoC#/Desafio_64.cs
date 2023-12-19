public class Desafio_64
{
	public static void TratandoValores()
	{
		int numero = 0;
		bool continua = true;
		int contNumber = 0;
		int contSoma = 0;

		while (continua)
		{
			Console.Write("DIGITE UM NÚMERO [999 PARA PARAR]: ");
			numero = int.Parse(Console.ReadLine().Trim());

			if (numero == 999)
			{
				continua = false;
			}
			else
			{
				contNumber++;
				contSoma = contSoma + numero;
			}
		}
		Console.Write($"VOCÊ DIGITOU {contNumber} e a soma entre eles foi {contSoma}");
	}
}
