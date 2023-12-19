public class Desafio_63
{
    public static void Fibonacci()
    {
        long n1 = 0;
        long n2 = 1;
        long n3 = 0;

        Console.Write("INFORME UM NÚMERO PARA VER SUA SEQUÊNCIA FIBONACCI: ");
        long termo = int.Parse(Console.ReadLine().Trim());

        long cont = 0;
        while (cont < termo)
        {
            Console.Write($"{n1} > ");
            n3 = n1 + n2;
            n1 = n2;
            n2 = n3;
            

            cont++;
        }
        Console.WriteLine(" FIM");
    }
}
