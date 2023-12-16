using System;

class Desafio_62
{
    public static void PAWhileUpgrade()
    {
        Console.Write("Escreva o primeiro termo de uma PA: ");
        int termo = int.Parse(Console.ReadLine());

        Console.Write("Escreva o valor da razão da PA: ");
        int razao = int.Parse(Console.ReadLine());

        int cont = 1;
        int termosExtra = 0;
        char escolha = 'S';

        while (cont <= 10)
        {
            Console.Write($"{termo} ");
            termo += razao;
            cont++;
        }

        do
        {
            Console.Write("\nDeseja ver mais termos da mesma PA? [S/N]\n--> ");
            escolha = char.Parse(Console.ReadLine().ToUpper().Trim());

            if (escolha == 'S')
            {
                Console.Write("Quantos termos: ");
                termosExtra = int.Parse(Console.ReadLine());

                cont = 1;

                while (cont <= termosExtra)
                {
                    Console.Write($"{termo} ");
                    termo += razao;
                    cont++;
                }
            }
            else
            {
                Console.WriteLine("FIM");
            }

        } while (escolha == 'S');
    }
}
