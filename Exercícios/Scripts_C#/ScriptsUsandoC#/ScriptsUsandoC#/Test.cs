class Test
{
    public static int testFunction()
    {
        Console.WriteLine("INFORME UM NÚMERO: ");
        int number = int.Parse(Console.ReadLine());

        return number;
        
    }
    public static void writeNumber()
    {
        int valor = Test.testFunction();
        Console.WriteLine(valor);
    }
}
