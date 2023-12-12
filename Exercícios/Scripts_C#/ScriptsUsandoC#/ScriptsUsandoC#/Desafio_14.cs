class Desafio_14
{
    public static void ConversaoDeTemperatura()
    {
        Console.Write("Informe a temperatura em Celsius: ");
        float celsius = float.Parse(Console.ReadLine().Trim().Replace(".", ","));

        float fahrenheit = (celsius * 1.8f) + 32;

        Console.WriteLine($"\nA temperatura de {celsius}°C corresponde a {fahrenheit}°F");
    }
}
