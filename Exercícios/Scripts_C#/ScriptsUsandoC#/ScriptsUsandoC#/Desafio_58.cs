class Desafio_58
{
    public static void AdivinheMelhorado()
    {
        while (true)
        {
            Random random = new Random();
            int choiceComputer = random.Next(1, 10 + 1);

            Console.Write("\n\n[COMPUTADOR] - Adivinhe o número que estou pensando...\n --> ");
            int choicePlayer = int.Parse(Console.ReadLine());
            
            Console.WriteLine($"SUA ESCOLHA FOI O NÚMERO [{choicePlayer}]");
            Console.WriteLine($"EU PENSEI NO NÚMERO [{choiceComputer}]");

            if (choicePlayer == choiceComputer)
            {
                Console.Write("[ ! ] - VOCÊ VENCEU.");
                break;
            }
            else 
            {
                Console.Write("[ ! ] - VOCÊ PERDEU HAHA.");
                continue;
            }
        }
    }
}
