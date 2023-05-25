#include <iostream>
#include <istream>
#include <iomanip>
#include <stdio.h>

using namespace std;

int main(void) {
	setlocale(LC_ALL, "Russian");
	/*int x;
	int y;
	int z;
	double summ;
	string s1;
	string s2;
	string s3;*/

	/*("¬ведите значение x:\n");
	scanf_s("%d", &x);
	printf_s("¬ведите значение y:\n");
	scanf_s("%d", &y);
	printf_s("¬ведите значение z:\n");
	scanf_s("%d", &z);

	summ = (double)x + (double)y + (double)z;
	printf_s("—умма равна %f", summ);

	printf_s("\ns1...............%d", x);
	printf_s("\ns2...............%d", y);
	printf_s("\ns3...............%d", z);

	int x2;
	double y2;
	printf_s("\n¬ведите значение x: ");
	scanf_s("%d", &x2);
	printf_s("\n¬ведите значение y: ");
	scanf_s("%f", &y2);

	printf_s("\n8-ричный x: %o", &x2);
	printf_s("\n16-ричный x: %x", &x2);
	printf_s("\nэкспоненциальный y: %e", &y2);

	float x3 = 1.3456;
	printf("%.1f\n%.2f\n%.3f\n%.4f\n", x3, x3, x3, x3);*/

	/*char str1[5];
	char str2[3];
	cin.getline(str1, 5);
	cin.clear();
	cin.getline(str2, 3);
	cout << endl << "str1 = " << str1;
	cout << endl << "str2 = " << str2 << endl;
	system("pause");
	return 0;*/

	/*int x0, y0, x1, y1;
	scanf_s("%*c%d%*c%d%*c %*c%d%*c%d%*c", &x0, &y0, &x1, &y1);
	printf_s("%d\n%d\n%d\n%d\n", x0, y0, x1, y1);*/

	/*char str[9];
	scanf_s("%8s", str, 8);
	printf("%sg\n", str);*/

	/*char a, b, str[10];
	a = getchar();
	b = getchar();
	scanf_s("%s", str, 10);
	printf("a = %c\n", a);
	printf("b = %c\n", b);
	(string)str = str[2, 9];
	printf("string = %s\n", str);
	return 0;*/

	/*int a1, a2, a3, a4, a5;
	printf("%s\n", "|---------------------------|");
	printf("%s", "1. 2+2 = ?	");
	scanf_s("%d", &a1);
	printf("\n%s", "2. 2 + 1 = ?	");
	scanf_s("%d", &a2);
	printf("\n%s", "3. 1+2 = ?	");
	scanf_s("%d", &a3);
	printf("\n%s", "4. 2+3 = ?	");
	scanf_s("%d", &a4);
	printf("\n%s", "5. 3+2 = ?	");
	scanf_s("%d", &a5);
	printf("\n%s", "|---------------------------|");
	system("cls");
	printf("%s\n", "|---------------------------|");
	printf("1. %d\n", a1);
	printf("2. %d\n", a2);
	printf("3. %d\n", a3);
	printf("4. %d\n", a4);
	printf("5. %d\n", a5);
	printf("%s\n", "|---------------------------|");
	return 0;*/

	/*char a = 'A';
	printf("%d %d\n", sizeof(a), sizeof((long)a));
	return 0;*/

	//________________________________________________________________

	/*int x, y, z;
	double S;
	cout << "¬ведите значение x: ";
	cin >> x;
	cout << "¬ведите значение y: ";
	cin >> y;
	cout << "¬ведите значение z: ";
	cin >> z;
	S = (double)x + (double)y + (double)z;
	cout << fixed << "—умма: " << S;*/

	/*int x, y, z;
	string st1 = "«начение x";
	string st2 = "«начение y";
	string st3 = "«начение z";
	cout << "¬ведите значение x: ";
	cin >> x;
	cout << "¬ведите значение y: ";
	cin >> y;
	cout << "¬ведите значение z: ";
	cin >> z;
	cout << st1 << setw(30) << setfill('.') << x << endl;
	cout << st2 << setw(30) << setfill('.') << y << endl;
	cout << st3 << setw(30) << setfill('.') << z << endl;*/

	/*int x;
	double y;
	cout << "¬ведите значение x: ";
	cin >> x;
	cout << "¬ведите значение y: ";
	cin >> y;
	cout << "8ричный х: " << oct << x << endl;
	cout << "16ричный х: " << hex << x << endl;
	cout << "экспоненциальный у: " << scientific << setprecision(1) << y << endl;
	cout << "экспоненциальный у: " << scientific << setprecision(2) << y << endl;
	cout << "экспоненциальный у: " << scientific << setprecision(3) << y << endl;*/

	/*double val = 1.3456;
	cout << setprecision(2) << val << endl << setprecision(3) << val << endl
	<< setprecision(4) << val << endl << setprecision(5) << val << endl;*/

	/*int x0, y0, x1, y1;
	string str1, str2, str3;
	cin >> str1 >> x0 >> str2 >> y0 >> str3;
	cin >> str1 >> x1 >> str2 >> y1 >> str3;
	cout << x0 << " " << y0 << endl;
	cout << x1 << " " << y1 << endl;*/

	/*char str[10];
	cin.getline(str, 8, 'g');
	cout << str << 'g';*/

	/*char a, b;
	string str;
	a = getchar();
	b = getchar();
	cin >> str;
	cout << a << b << endl;
	cout << str;*/

	/*int a1, a2, a3, a4, a5;
	cout << '|' << setw(25) << setfill('-') << '|' << endl
	<< "1. 2+2 = ?             ";
	cin >> a1;
	cout << "2. 2+1 = ?             ";
	cin >> a2;
	cout << "3. 1+2 = ?             ";
	cin >> a3;
	cout << "4. 1+1 = ?             ";
	cin >> a4;
	cout << "5. 0+1 = ?             ";
	cin >> a5;
	cout << "|" << setw(25) << setfill('-') << "|";
	system("cls");
	cout << '|' << setw(25) << setfill('-') << '|' << endl
	<< "1. " << a1 << endl << "2. " << a2 << endl << "3. "
	<< a3 << endl << "4. " << a4 << endl << "5. " << a5 << endl
	<< "|" << setw(25) << setfill('-') << "|";*/

	char a = 'A';
	cout << sizeof(a) << endl << sizeof((long)a);
	





	



}