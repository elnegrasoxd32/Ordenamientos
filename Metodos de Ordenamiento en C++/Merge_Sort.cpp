#include <iostream>
#include <vector>
using namespace std;
void merge(vector<int>& a, int izq, int centro, int dere) {
    int n1 = centro - izq + 1; 
    int n2 = dere - centro;
    vector<int> izqA(n1);
    vector<int> dereA(n2);
    for (int i = 0; i < n1; i++)
        izqA[i] = a[izq + i];
    for (int j = 0; j < n2; j++)
        dereA[j] = a[centro + 1 + j];
    int i = 0, j = 0, k = izq;
    while (i < n1 && j < n2) {
        if (izqA[i] <= dereA[j]) {
            a[k] = izqA[i];
            i++;} else {
            a[k] = dereA[j];
            j++;}
        k++;}
    while (i < n1) {
        a[k] = izqA[i];
        i++;
        k++;}
    while (j < n2) {
        a[k] = dereA[j];
        j++;
        k++;}}
void mergeSort(vector<int>& a, int izq, int dere) {
    if (izq < dere) {
        int centro = izq + (dere - izq) / 2;
        mergeSort(a, izq, centro);
        mergeSort(a, centro+ 1, dere);
        merge(a, izq, centro, dere);}}
int main() {
	int n;
	cout<<"Ingrese la cantidad de elementos: "<<endl;
	cin>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++){
    	cin>>a[i];}   
    mergeSort(a, 0, n - 1);
    cout << "Arreglo ordenado es: ";
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";}
    return 0;
}
