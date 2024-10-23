#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n;
    cout << "Ingrese la cantidad de elementos: ";
    cin >> n;
    vector<int> arr(n);
    cout << "Ingrese los elementos: "<<endl;;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    cout << "Arreglo ordenado es: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}
