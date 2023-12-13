class Desafio_12
{
    public static void AplicandoDesconto()
    {
        const double desconto = 0.05;

        while (true)
        {
            try
            {
                Console.Write("Digite o valor do produto: ");
                double valor = double.Parse(Console.ReadLine().Trim().Replace(".", ","));
                string valorStr = valor.ToString("C");
                if (valor == 0)
                {
                    Console.WriteLine("\nAté mais tarde");
                    break;
                }
                else
                {
                    double valorDesconto = valor * desconto;
                    double valorFinal = valor - valorDesconto;
                    string valorFinalFormatado = valorFinal.ToString("C");

                    Console.WriteLine($"\nO valor do produto é {valorStr} e com desconto de {desconto:P} fica {valorFinalFormatado}");
                }
            }
            catch (Exception e)
            {
                Console.Write(e.Message);
            }
        }
    }
}
