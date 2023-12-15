class Desafio_57
{
    public static void LendoSexo()
    {
        Console.Write("Informe seu Sexo [M/F]: ");
        string sexo = Console.ReadLine().ToUpper();

        while (sexo != "M" && sexo != "F")
        {
            Console.Write("Você não digitou corretamente!\nTente novamente!\n\n");
            Console.Write("Informe seu Sexo [M/F]: ");
            sexo = Console.ReadLine().ToUpper();
        }
        Console.Write("Você digitou corretamente");
    }   
}