#include <iostream>
#include <bitset>
#include <conio.h>
#include <iomanip>

using namespace std;

void z1() {
	int x, y;
	cout << "Координата x: "; cin >> x;
	cout << "Координата y: "; cin >> y;

	if ((x > 0) && (y > 0))
		cout << "Первая четверть" << endl;
	else if ((x < 0) && (y > 0))
		cout << "Вторая четверть" << endl;
	else if ((x < 0) && (y < 0))
		cout << "Третья четверть" << endl;
	else if ((x > 0) && (y < 0))
		cout << "Четвёртая четверть" << endl;
	else cout << "Точка на оси/осях" << endl;
}

void z2() {
	//a*x^2 + b*x + c = 0
	int a, b, c; // 5 6 1
	double x1, x2;
	cout << "Значение a: "; cin >> a;
	cout << "Значение b: "; cin >> b;
	cout << "Значение c: "; cin >> c;

	if (a == 0) {
		cout << "Не квадратное";
		exit(0);
	}
	else {
		double d = pow(b, 2) - 4 * a * c;
		x1 = (-b + sqrt(d)) / (2*a);
		x2 = (-b - sqrt(d)) / (2*a);
		cout << "x1 = " << x1 << endl << "x2 = " << x2 << endl;
	}
}

void z3() {
	int N, F = 1;
	cout << "Значение N: "; cin >> N;

	for (int i = 1; i <= N; i++)
		F *= i;
	cout << "Результат: " << F << endl;

	F = 1;
	do {
		F *= N;
		--N;
	} while (N != 0);
	cout << "Результат: " << F << endl;
}

void z4() {
	int a[] = {-15, 5, 6, 30, -5, -4};
	int summ = 0, n = size(a)-1;

	while (n >= 0) {
		if (a[n] < 0)
			summ += pow(a[n], 2);
		--n;
	}
	cout << "Результат: " << summ << endl;
}

void z5() {
	int A[10], B[10];
	int count_v = 0, num = 0;
	unsigned mask = (1 << 2);
	unsigned mask2 = (1 << 4);

	for (int i = 0; i < 10; i++)
		cin >> A[i];
	for (int i = 0; i < 10;i++)
		cout << bitset<8>(A[i]) << ' ';
	cout << endl;
	
	for (int i = 0; i < 10; i++) {
		num = A[i];
		if (((num >> 4) & 1u) == 1)
			count_v++;
		A[i] ^= mask;
		B[i] = A[i];
		cout << bitset<8>(B[i]) << " ";
	}
	cout << endl << "Кол-во значений: " << count_v << endl;
}

void z6() {
	int A[5][5];
	double k = 0;
	int min = -10, max = 30;
	double sredG = 0, sredP = 0;
	srand(time(0));
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			A[i][j] = min + rand() % max;
			cout << setw(4) << A[i][j] << ' ';
			if ((i == j) && (A[i][i] > 0)) {
				k++;
				sredG += A[i][i];
			}
		}
		cout << endl;
	}
	double nk = 0;
	int i = 0;
	for (int j = 4; j >= 0; j--) {
		if (A[i][j] > 0) {
			nk++;
			sredP += A[i][j];
		}
		i++;
	}
	cout << "Среднее главной: " << sredG / k << endl << "Среднее побочной: " << sredP / nk << endl;
}

void z7() {
	int A[5][9];
	double a[5];
	int min = -10, max = 30;
	double sred = 0;

	srand(time(0));
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 9; j++) {
			A[i][j] = min + rand() % max;
			cout << setw(4) << A[i][j] << ' ';
		}
		cout << endl;
	}
	double MAX = 0.0;
	for (int i = 0; i < 9; i++) {
		sred = 0;
		if (i % 2 == 0) {
			for (int j = 0; j < 5; j++) {
				sred += A[j][i];
			}
			a[i] = sred / 5;
		if (a[i] >= MAX) {
			MAX = a[i];
		}
		cout << a[i] << ' ';
		}
	}
	cout << endl << "Максимум: " << MAX << endl;
}

void print(int Area[20][20]) {
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			cout << setw(4) << Area[i][j] << ' ';
		}
		cout << endl;
	}
}

int move() {
	cout << "Список действий: \nL/l - пойти налево\nR/r - пойти направо\nD/d - пойти вниз\nU/u - пойти вверх\n";
	char x = getchar();
	switch (x)
	{
	case 'l':
	case 'L':
		return -1;
		break;
	case 'R':
	case 'r':
		return 1;
		break;
	case 'D':
	case 'd':
		return 11;
		break;
	case 'U':
	case 'u':
		return -11;
	default:
		break;
	}
}

void z8() {
	int Area[20][20];
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			Area[i][j] = 0;
			cout << Area[i][j] << ' ';
		}
		cout << endl;
	}

	int start1 = 0, start2 = 0;
	cout << "Начальная позиция(x, x): ";
	cin >> start1 >> start2;
	Area[start1][start2] = 1;

	print(Area);

	while ((start1 >= 0) || (start1 < 20) || (start2 >= 0) || (start2 < 20)) {
		int a = move();
		switch (a) {
		case -1:
			start2++;
			Area[start1][start2] = -1;
			print(Area);
			break;
		case 1:
			start2--;
			Area[start1][start2] = 1;
			print(Area);
			break;
		case 11:
			start1++;
			Area[start1][start2] = 11;
			print(Area);
			break;
		case -11:
			start1--;
			Area[start1][start2] = -11;
			print(Area);
			break;
		}
	}
}

int main() {
	setlocale(LC_ALL, "Russian");
	//z1();
	//z2();
	//z3();
	//z4();
	//z5();
	//z6();
	z7();
	//z8();


	system("pause");
	return 0;

}