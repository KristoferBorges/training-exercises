class Desafio_17
{
    public static void CalculandoHipotenusa()
    {
        Console.Write("INFORME O CATETO OPOSTO: ");
        double oposto = double.Parse(Console.ReadLine().Trim().Replace(".", ","));
        Console.Write("INFORME O CATETO ADJACENTE: ");
        double adjacente = double.Parse(Console.ReadLine().Trim().Replace(".", ","));

        double hipotenusa = Math.Sqrt(Math.Pow(oposto, 2) + Math.Pow(adjacente, 2));
        Console.Write($"\nO VALOR DA HIPOTENUSA É: {hipotenusa:F2}");
    }
}
