class Desafio_13
{
    public static void AumentoDeSalario()
    {
        while (true)
        {
            try
            {
                Console.Write("Informe seu salário: ");
                float salario = float.Parse(Console.ReadLine());
                float novoSalario = salario + (salario * 0.15f);

                if (salario == 0)
                {
                    Console.WriteLine("\nAté mais tarde");
                    break;
                }
                else
                {
                    Console.WriteLine($"\nSeu salário é {salario.ToString("C")} e com aumento de 15% fica {novoSalario.ToString("C")}");
                }
            }
            catch (Exception a)
            {
                Console.Write(a.Message);
            }
        }
    }
}
