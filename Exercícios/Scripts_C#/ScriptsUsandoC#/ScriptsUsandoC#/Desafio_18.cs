class Desafio_18
{
    public static void SenCosTan()
    {
        Console.Write("INFORME UM ÂNGULO: ");
        double angulo = double.Parse(Console.ReadLine().Trim());
        double anguloRadiano = angulo * Math.PI / 180;

        double seno = Math.Sin(anguloRadiano);
        double cosseno = Math.Cos(anguloRadiano);
        double tangente = Math.Tan(anguloRadiano);

        Console.Write($"[SENO] = {seno}\n[COSSENO] - {cosseno}\n[TANGENTE] - {tangente}");
    }
}
