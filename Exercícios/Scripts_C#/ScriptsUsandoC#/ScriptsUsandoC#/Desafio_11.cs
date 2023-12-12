class Desafio_11
{
    public static void TintaParede()
    {   while (true)
        {
            try
            {
                Console.Write("LARGURA DA PAREDE (METROS): ");
                float largura = float.Parse(Console.ReadLine().Trim());

                Console.Write("ALTURA DA PAREDE (METROS): ");
                float altura = float.Parse(Console.ReadLine().Trim());

                float area = largura * altura;
                float litros = area / 2;

                if (largura == 0 && altura == 0)
                {
                    Console.WriteLine("\nAté mais tarde");
                    break;
                }
                else
                {
                    Console.WriteLine($"\nSua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m²");
                    Console.WriteLine($"Para pintar essa parede, você precisará de {litros}l de tinta");
                }

            }
            catch (Exception e)
            {
                Console.WriteLine($"\nErro: {e.Message}");
            }
        }
    }
}
