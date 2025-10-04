using System;
using System.Collections.Generic;

class Aresta
{
    public int origem, destino, peso;

    public Aresta(int origem, int destino, int peso)
    {
        this.origem = origem;
        this.destino = destino;
        this.peso = peso;
    }
}

class BellmanFord
{
    public static void Percorrer(List<Aresta> arestas, int verticesCount, int origem)
    {
        // inicializa as distâncias
        int[] distancia = new int[verticesCount];
        for (int i = 0; i < verticesCount; i++)
        {
            distancia[i] = int.MaxValue;
        }

        distancia[origem] = 0;

        // relaxa todas as arestas (V - 1) vezes
        for (int i = 1; i <= verticesCount - 1; i++)
        {
            foreach (var aresta in arestas)
            {
                int u = aresta.origem;
                int v = aresta.destino;
                int peso = aresta.peso;

                if (distancia[u] != int.MaxValue && distancia[u] + peso < distancia[v])
                {
                    distancia[v] = distancia[u] + peso;
                }
            }
        }

        // verifica ciclos negativos
        foreach (var aresta in arestas)
        {
            int u = aresta.origem;
            int v = aresta.destino;
            int peso = aresta.peso;

            if (distancia[u] != int.MaxValue && distancia[u] + peso < distancia[v])
            {
                Console.WriteLine("O grafo contém um ciclo de peso negativo");
                return;
            }
        }

        Print(distancia, verticesCount);
    }

    private static void Print(int[] distancia, int verticesCount)
    {
        Console.WriteLine("Vertice\tDistância da origem");
        for (int i = 0; i < verticesCount; i++)
        {
            string d = distancia[i] == int.MaxValue ? "∞" : distancia[i].ToString();
            Console.WriteLine(i + "\t" + d);
        }
    }

    static void Main()
    {
        int verticesCount = 5;
        var arestas = new List<Aresta>
        {
            new Aresta(0, 1, -1),
            new Aresta(0, 2, 4),
            new Aresta(1, 2, 3),
            new Aresta(1, 3, 2),
            new Aresta(1, 4, 2),
            new Aresta(3, 2, 5),
            new Aresta(3, 1, 1),
            new Aresta(4, 3, -3)
        };

        BellmanFord.Percorrer(arestas, verticesCount, 0);
    }
}