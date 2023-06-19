#include <iostream>
#include <cstdlib>
#include <chrono>
#include <algorithm>

using namespace std;

void linesearch(int n, int x, int* a) {
	auto start = chrono::steady_clock::now();
	int i = 0;
	while ((i <= n) && (a[i] != x)) {
		++i;
	}
	auto end = chrono::steady_clock::now();
	auto diff = end - start;
	cout << "Кол-во сравнений " << i << endl << "Время работы: " 
	<< chrono::duration <double, milli>(diff).count() << endl << "------------" << endl;
}

void searchbarier(int n, int x, int* a) {
	auto start = chrono::steady_clock::now();
	int i = 1;
	a[n] = x;
	while (a[i] != x) {
		++i;
	}
	auto end = chrono::steady_clock::now();
	auto diff = end - start;
	cout << "Кол-во сравнений " << i << endl 
	<< chrono::duration <double, milli>(diff).count() << endl << "------------" << endl;
}

void binarysearch(int n, int x, int* a) {
	auto start = chrono::steady_clock::now();
	int L = 1;
	int R = n;
	int m = 0;
	int i = 0;
	while (L < R) {
		++i;
		m = L + (R - L) / 2;
		if (x > a[m]) {
			++i;
			L = ++m;
		}
		else {
			++i;
			R = m;
		}
	}
	auto end = chrono::steady_clock::now();
	auto diff = end - start; 
	cout << L << " " << R << endl << "Кол-во сравнений " << i << endl
	<< chrono::duration <double, milli>(diff).count() << endl << "------------" << endl;
}

int partition(int a[], int start, int end)
{
	int pivot = a[end];
	int pIndex = start;

	for (int i = start; i < end; i++) {
		if (a[i] <= pivot) {
			swap(a[i], a[pIndex]);
			pIndex++;
		}
	}
	swap(a[pIndex], a[end]);
	return pIndex;
}

void quicksort(int a[], int start, int end) {
	if (start >= end) {
		return;
	}
	int pivot = partition(a, start, end);


	quicksort(a, start, pivot - 1);
	quicksort(a, pivot + 1, end);
}


int main() {
	setlocale(LC_ALL, "Russian");
	int min_v = -30;
	int max_v = 60;
	int n;
	cout << "Кол-во элементов: ";
	cin >> n;

	int* a = new int[n];
	srand(time(0));
	for (int i = 0; i < n; i++) {
		a[i] = min_v + rand() % max_v;
		cout << a[i] << ' ';
	}
	cout << endl;

	quicksort(a, a[0], a[n - 1]);

	for (int i = 0; i < n; i++) {
		cout << a[i] << ' ';
	}
	cout << endl;

	int x;
	cout << "Ключ: ";
	cin >> x;

	int v;
	cout << "Список алгоритмов поиска:\n1. Линейный поиск\n2. Поиск с барьером\n3. Бинарный поиск" << endl;
	cin >> v;
	switch (v) 
	{
	case 1:
		linesearch(n, x, a);
		break;
	case 2:
		searchbarier(n, x, a);
		break;
	case 3:
		binarysearch(n, x, a);
		break;
	default:
		break;
	}
	
	system("pause");
	return 0;
}

