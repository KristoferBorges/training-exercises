class Desafio_59
{
    public static void CalculadoraSimples()
    {
        bool continua = true;

        Console.Write("BEM-VINDO(A) - CALCULADORA_SIMPLES\n\n");
        Console.Write("Informe o primeiro valor: ");
        float numero1 = float.Parse(Console.ReadLine().Trim().Replace(".", ","));
        Console.Write("Informe o segundo valor: ");
        float numero2 = float.Parse(Console.ReadLine().Trim().Replace(".", ","));



        while (continua)
        {
            Console.WriteLine("[ 1 ] - SUM");
            Console.WriteLine("[ 2 ] - SUBTRACT");
            Console.WriteLine("[ 3 ] - MULTIPLICATION");
            Console.WriteLine("[ 4 ] - DIVISION");
            Console.WriteLine("[ 5 ] - NEW NUMBERS");
            Console.WriteLine("[ 6 ] - EXIT");

            Console.Write($"\n[ ? ] - QUAL SUA ESCOLHA COM OS VALORES [{numero1} | {numero2}]\n --> ");
            int escolha = int.Parse(Console.ReadLine().Trim().Replace(".", ""));
            if (escolha == 1)
            {
                Console.WriteLine($"\n[SUM]  {numero1} + {numero2} = {numero1 + numero2}");
            }
            else if (escolha == 2)
            {
                Console.WriteLine($"\n[SUBTRACT]  {numero1} - {numero2} = {numero1 - numero2}");
            }
            else if (escolha == 3)
            {
                Console.WriteLine($"\n[MULTIPLICATION]  {numero1} * {numero2} = {numero1 * numero2}");
            }
            else if (escolha == 4)
            {
                Console.WriteLine($"\n[DIVISION]  {numero1} / {numero2} = {numero1 / numero2}");
            }
            else if (escolha == 5)
            {
                Console.WriteLine($"\n[NEW NUMBERS] - INFORME OS NOVOS NÚMEROS!");

                Console.Write("Informe o primeiro valor: ");
                numero1 = float.Parse(Console.ReadLine().Trim().Replace(".", ","));
                Console.Write("Informe o segundo valor: ");
                numero2 = float.Parse(Console.ReadLine().Trim().Replace(".", ","));

            }
            else if (escolha == 6)
            {
                Console.WriteLine($"\n[EXIT] - AGRADEÇO POR UTILIZAR NOSSO SOFTWARE");
                continua = false;
            }
        }
    }
}