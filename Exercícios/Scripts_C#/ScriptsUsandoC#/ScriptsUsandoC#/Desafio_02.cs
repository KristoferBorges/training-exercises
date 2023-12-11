public class Desafio_02
{
	public static void CapturandoNascimento()
	{
		Console.Write("Dia: ");
		int dia = int.Parse(Console.ReadLine().Trim());

		Console.Write("Mês: ");
		int mes = int.Parse(Console.ReadLine().Trim());

		Console.Write("Ano: ");
		int ano = int.Parse(Console.ReadLine().Trim());

		DateTime nascimento = new DateTime(ano, mes, dia);
		DateTime hoje = DateTime.Now;

		int idade = hoje.Year - nascimento.Year;

		Console.WriteLine($"Você nasceu no ano de {nascimento.Year} do mês {nascimento.Month} no dia {nascimento.Day}");
		Console.WriteLine($"Hoje você tem {idade} anos");
	}
}
