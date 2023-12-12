public class Desafio_05
{
	public static void AntecessorSucessor()
	{
		Console.Write("Digite um número: ");
		int numero = int.Parse(Console.ReadLine().Trim());

		int antecessor = numero - 1;
		int sucessor = numero + 1;

		Console.WriteLine($"O NUMERO FOI = [{numero}]\nANTECESSOR = {antecessor}\nSUCESSOR = {sucessor}");
    }
}
