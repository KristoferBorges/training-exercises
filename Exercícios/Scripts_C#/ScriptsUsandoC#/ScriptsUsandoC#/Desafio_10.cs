public class Desafio_10
{
	public static void ComprandoDollar()
	{
		const double cotacao = 5.24;

		Console.Write("Digite o valor em reais: ");
        double reais = double.Parse(Console.ReadLine().Trim());

        double conversao = reais / cotacao;
		string conversaoFormatada = conversao.ToString("C");
        Console.WriteLine($"Você pode comprar {conversaoFormatada} dólares");   
	}
}
