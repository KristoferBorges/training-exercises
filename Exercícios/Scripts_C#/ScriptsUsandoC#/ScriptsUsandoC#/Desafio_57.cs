class Desafio_57
{
    public static void LendoSexo()
    {
        while (true)
        {
            Console.Write("Informe seu Sexo [M/F]: ");
            string sexo = Console.ReadLine().ToUpper();

            if (sexo == "F" || sexo == "M")
            {
                Console.Write("Você digitou corretamente!");
                break;
            }
            else  
            {
                Console.Write("Você não digitou corretamente!\nTente novamente!\n\n");
            }
        }
    }
}
