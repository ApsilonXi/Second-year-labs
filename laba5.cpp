#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <iomanip>
#include <Windows.h>
#include <vector>
#include <set>
#define MAXW 1024

using namespace std;

void z1() {
	int P[] = { 0, 2, 4, 5, 6, 7, 9, 12 };
	cout << P[3] << endl << *P << endl << *(P + 4) << endl << *(P + P[2]) << endl;
}

void z2(int &x, int &y) {
	int c = x;
	x = y;
	y = c;
}

int* z3_1() {
	int n = 10;
	int* a = new int(10);
	int min = -10, max = 30;
	int sred = 0;

	srand(time(0));
	for (int i = 0; i < n; i++) {
		a[i] = min + rand() % max;
		cout << a[i] << ' ';
	}
	cout << endl;
	return a;
}

int* z3_2(int *array, int min, int max, int n) {
	srand(time(0));
	for (int i = 0; i < n; i++) {
		array[i] = min + rand() % max;
		cout << array[i] << ' ';
	}
	cout << endl;
	return array;
}

string z4(string &str, string &del) {	
	string a[10];
	string word;
	vector<string> words;
	set <char> m;
	for (char delim:del) m.insert(delim);

	for (char i : str) {
		if (m.find(i) != m.end()) {
			words.push_back(word);
			word = "";
		}
		else {
			word = word + i;
		}
	}
	reverse(words.begin(), words.end());
	string output = "";
	for (string i : words) {
		if (i != "") {
			output = output + i + " ";
		}
	}
	return output;
}
	
void z5(int** arr, int n, int m) {
	int x, sred_geom = 1;
	int N = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> x;
			arr[i][j] = x;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << arr[i][j] << ' ';
			if ((i == j) && (arr[i][i] < 0)) {
				sred_geom *= arr[i][i];
				N++;
			}
		}
		cout << endl;
	}
	cout << sred_geom<<endl;
	double p = pow(sred_geom, (1./N));
	cout << N << ' ' << p << endl;
}

double f(double x) { return x * x * x;}

void graf(double (*func)(double), double a, double b)
{
	const int n = 8;
	const double h = (b - a) / n;

	double ymin = INFINITY;
	double ymax = -INFINITY;
	for (double x = a; x <= b; x += h) {
		double y = func(x);
		if (y < ymin) {
			ymin = y;
		}
		if (y > ymax) {
			ymax = y;
		}
	}

	const int yScrMin = 1;
	const int yScrMax = 50;
	for (double x = a; x <= b; x += h) {
		double y = func(x);
		int yScr = yScrMin + (y - ymin) / (ymax - ymin) * (yScrMax - yScrMin);
		for (int i = yScrMin; i <= yScrMax; i++) {
			if (i == yScr) {
				cout << "*";
			}
			else {
				cout << " ";
			}
		}
		cout << endl;
	}
}


void z6() {
	graf(f, -5, 5);
}
	
int main() {
	setlocale(LC_ALL, "Russian");
	

	//������� 2
	/*int x, y;
	cout << "������� x: ";
	cin >> x;
	cout << "������� y: ";
	cin >> y;
	cout << "���� " << x << " " << y << endl;
	z2(x, y);
	cout << "����� " << x << " " << y;*/

	//������� 4
	/*string str = "Hello   world ! of {C++}!";
	string del = " !{}";
	cout << "���� " << str << endl;
	string func = z4(str, del);
	cout << "����� " << func;*/

	//������� 6
	/*double x;
	z6();*/



	/*int n, m;
	cout << "������� n � m: ";
	cin >> n >> m;
	int** arr = new int*[n];
	for (int i = 0; i < n; i++) {
		arr[i] = new int[m];
	}*/
	//z5(arr, n , m);

	//z6(-5.0, 0.0, 5.0, 10.0);

	/*int n1 = 10;
	int* a = new int(n);
	int min = -10, max = 30;*/

	////�������� ������� 2, �� ������� � ����������


	/*int Z;
	do
	{
		cout << "\n1. ������� 1;" << endl;
		cout << "2. ������� 2;" << endl;
		cout << "3. ������� 3.1;" << endl;
		cout << "4. ������� 3.2." << endl;
		cout << "5. ������� 4;" << endl;
		cout << "6. �����." << endl;
		cout << endl;
		cout << "�������� �����:" << endl;
		cin >> Z;
		cout << endl;

		switch (Z) {
		case 1:
			z1();
			break;
		case 2:
			int x, y;
			cin >> x >> y;
			z2(x, y);
			break;
		case 3:
			z3_1();
			break;
		case 4:
			z3_2(a, min, max, n1);
			break;
		case 5:
			//p = z4(s);
			//cout << p;
			break;
		case 6:
			exit(0);
		default:
			break;
		}
	} while (true);
	
	system("pause");
	return 0;*/
}


	
