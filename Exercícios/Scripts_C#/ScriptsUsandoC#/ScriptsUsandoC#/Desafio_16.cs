class Desafio_16
{
    public static void TruncandoNumero()
    {
        Console.Write("INFORME UM NÚMERO PARA TRUNCA-LO: ");
        double numero = double.Parse(Console.ReadLine().Trim().Replace(".", ","));
        double numeroTruncado = Math.Truncate(numero);

        Console.Write($"[NORMAL] - {numero}\n[TRUNCADO] - {numeroTruncado}");
    }
}
