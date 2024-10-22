#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <ctime> 
#include <chrono>
using namespace std;
int main(int argc, char** argv) {
	int i;
	string nombre;
	cin>>nombre;
	ifstream archivo(nombre);
	if (!archivo.is_open()) {
        cout << "No se pudo abrir el archivo." << endl;
        return 1;
    }
	vector<int> a;
	int numero;
     while (archivo >> numero) {
        a.push_back(numero);
    }
    archivo.close();   
    int max = *max_element(a.begin(), a.end());
    int min = *min_element(a.begin(), a.end());
    int range = max - min + 1;
    int n = a.size();		
	vector<int> conteo(range,0);
	vector<int>output(a.size());
	auto start = chrono::high_resolution_clock::now();
	for(i=0;i<a.size();i++){
		conteo[a[i]-min]++;
	}
	for (int i = 1; i < conteo.size(); i++) {
        conteo[i] += conteo[i - 1];
    }
	for (int i = a.size() - 1; i >= 0; i--) {
        output[conteo[a[i] - min] - 1] = a[i];
        conteo[a[i] - min]--;
    }
    for (int i = 0; i < a.size(); i++) {
        a[i] = output[i];
    }
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    cout<<"\Ordenados son: ";
	for(i=0;i<a.size();i++){
		cout<<a[i]<<" ";}
	cout << "\nTiempo de ordenamiento: " << duration.count() << " segundos." << endl;	
	return 0;
}