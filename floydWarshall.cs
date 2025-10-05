using System;

class FloydWarshall
{
    static readonly int INF = 99999; // representa infinito

    public static void CalcularMenoresCaminhos(int[,] grafo)
    {
        int vertices = grafo.GetLength(0);
        int[,] dist = new int[vertices, vertices];

        // copia os valores dos grafos originais
        for (int i = 0; i < vertices; i++)
        {
            for (int j = 0; j < vertices; j++)
            {
                dist[i, j] = grafo[i, j];
            }
        }

        // algoritmo principal
        for (int k = 0; k < vertices; k++) // vértice intermediario
        {
            for (int i = 0; i < vertices; i++) // origem
            {
                for (int j = 0; j < vertices; j++) // destino
                {
                    if (dist[i, k] + dist[k, j] < dist[i, j])
                    {
                        dist[i, j] = dist[i, k] + dist[k, j];
                    }
                }
            }
        }

        Print(dist, vertices);
    }

    static void Print(int[,] dist, int vertices)
    {
        Console.WriteLine("Matriz de menores distâncias entre vértices:");
        for (int i = 0; i < vertices; i++)
        {
            for (int j = 0; j < vertices; j++)
            {
                if (dist[i, j] == INF)
                {
                    Console.Write("INF".PadLeft(7));
                }
                else
                {
                    Console.Write(dist[i, j].ToString().PadLeft(7));
                }
            }
            Console.WriteLine();
        }
    }

    static void Main()
    {
        int INF = FloydWarshall.INF;

        // Exemplo de grafo com 4 vértices
        int[,] grafo = {
            { 0,   5,  INF, 10 },
            { INF, 0,   3,  INF },
            { INF, INF, 0,   1 },
            { INF, INF, INF, 0 }
        };

        FloydWarshall.CalcularMenoresCaminhos(grafo);
    }
}