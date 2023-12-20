class Test
{
    public static void testFunction()
    {
        List<double> numeros = new List<double>();

        while (true)
        {
            Console.Write("DIGITE UM NÚMERO PARA LISTAGEM: ");
            double numero = double.Parse(Console.ReadLine());

            if (numero == 0)
            {
                break;
            }
            numeros.Add(numero);
        }
        foreach (double number in numeros)
        {
            Console.Write($"{number} | ");
        }
    }
}
