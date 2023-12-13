class Desafio_15
{
    public static void CalculoDeCobranca()
    {
        Console.Write("INFORME A QUANTIDADE DE [DIAS] ALUGADOS: ");
        int dias = int.Parse(Console.ReadLine().Trim());
        Console.Write("INFORME A QUANTIDADE DE [KM] RODADOS: ");
        float km = float.Parse(Console.ReadLine().Trim().Replace(".", ","));

        float preco = (60f * dias) + (km * 0.15f);
        Console.Write($"\n[DIAS ALUGADOS] - {dias}\n[KM PERCORRIDOS] - {km}\n[VALOR TOTAL] - {preco.ToString("C")}");

    }
}
