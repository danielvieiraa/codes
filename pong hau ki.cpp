#include <iostream>

using namespace std;

int vet[] = {1, 2, 0, 2, 1};
const int tamanho = 5;
int jogada, zero, none;
int jogador = 1;

void tab() {
    system("clear");
    // jogador 1 e1
    cout <<  vet[0] << "/0     ";
    //jogador 1 d1
    cout <<  " " << vet[4] << "/4" << endl;
    cout << " | \\    / |\n";
    cout << " |  \\  /  |\n";
    cout << " |   \\/   |\n";
    // meio livre
    cout << " |  " << vet[2] << "/2   |" << endl;
    cout << " |   /\\   |\n";
    cout << " |  /  \\  |\n";
    cout << " | /    \\ |\n";
    // jogador 2  e2 e d2;
    cout << vet[1] << "/1------" << vet[3] << "/3" << endl;
    cout << endl;
}

int encontrarZero(int array[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        if (array[i] == 0) {
            return i;
        }
    }
}

int swap(int index) {
    int temp;
    zero = encontrarZero(vet, tamanho);

    temp = vet[index];
    vet[index] = vet[zero];
    vet[zero] = temp;
}

int main() {
    while (1) {
        int z = encontrarZero(vet, tamanho);
        tab();
        if ((vet[0] == 1 && vet[1] == 1 && vet[2] == 2 && vet[3] == 2) || (vet[3] == 1 && vet[4] == 1 && vet[2] == 2 && vet[1] == 2)) {
            cout << "Jogador 2 ganhou!";
            break;
        } else if ((vet[0] == 2 && vet[1] == 2 && vet[2] == 1 && vet[3] == 1) || (vet[3] == 2 && vet[4] == 2 && vet[2] == 1 && vet[1] == 1)) {
            cout << "Jogador 1 ganhou!";
            break;
        }
        
        cout << "Jogador " << jogador << " escolha qual peça deseja mover (Os números após a barra indica a numeração da casa): ";
        cin >> jogada;
        
        if (jogada == 0 && z == 3 || jogada == 1 && z == 4 || jogada == 3 && z == 0 || jogada == 4 && z == 1){
            cout << "Movimento Inválido" << endl;
        } else {
            if (vet[jogada] != jogador){
                cout << "Movimento Inválido" << endl;
            } else {
                if (vet[jogada] == 0) {
                    cout << "Movimento Inválido" << endl;
                } else {
                    if (swap(jogada)) {
                    
                        tab();
                        jogador = (jogador == 1) ? 2 : 1;
                    } else {
                        cout << "Movimento Inválido" << endl;
                    }
                }
            }
        }
        cout << "Digite 1 para confirmar: ";
        cin >> none;
    }
}