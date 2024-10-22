#include <iostream>
#include <vector>
using namespace std;
void heapify(vector<int>&arr, int xd, int i) {
    int largest = i; 
    int left = 2 * i + 1;  
    int right = 2 * i + 2; 
    if (left < xd && arr[left] > arr[largest])
        largest = left;
    if (right < xd && arr[right] > arr[largest])
        largest = right;
    if (largest != i) {
        swap(arr[i], arr[largest]); 
        heapify(arr, xd, largest);
    }
}
void heapSort(vector<int>&arr, int xd) {
    for (int i = xd / 2 - 1; i >= 0; i--)
        heapify(arr, xd, i);
    for (int i = xd - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
int main() {
    int xd,min,max;
	cout<<"Ingrese la cantidad de elementos: ";
    cin>>xd;
    vector<int>arr(xd);
    for(int i=0;i<xd;i++){
    	cin>>arr[i];
	}
	heapSort(arr,xd);	
    cout << "Arreglo ordenado es: ";
    for (int i = 0; i < xd; i++){
     cout << arr[i] << " ";   	
	}		
    return 0;
}