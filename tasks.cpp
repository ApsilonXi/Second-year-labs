#include "iostream"
#include <iomanip>
#include <conio.h>
#include <bitset>


using namespace std;

int main(void) {

	setlocale(LC_ALL, "Russian");

	/*int i = 5;
	int j = 12;
	int k = 7;

	k = (--i + 2 * j - k++, j-- + i - k);
	cout << k;*/

	/*int i, j, k, l, m;

	cin >> i >> j >> k >> l; //21 6 7 8

	if (i > (j + 2 * k)) {
		m = (i >> 4) + (j << 7) - 17 + (k << 1) - (l >> 5);
	}
	else {
		m = (i >> 4) + (j << 7) - 17 + (k << 1) + (l >> 5);
	}

	cout << m;*/

	/*int x, y;
	cin >> x >> y;
	cout << hex << x << ' ' << y << endl << (x & y) << ' ' << (x | y) << endl
	<< (x >> 2) << ' ' << (x << 1) << ' ' << (y >> 2) << ' ' << (y << 1);*/

	/*unsigned int x = 0x41424344;
	unsigned int m = 0b11111111111111100000000000000000;
	printf("%c%c%c%c\n", x >> 24, (x & 0xffffff) >> 16, (x & 0xffff) >> 8, (x & 0xff));
	x ^= m;
	printf("%c%c%c%c\n", x >> 24, (x & 0xffffff) >> 16, (x & 0xffff) >> 8, (x & 0xff));
	x ^= m;
	printf("%c%c%c%c\n", x >> 24, (x & 0xffffff) >> 16, (x & 0xffff) >> 8, (x & 0xff));*/

	int i;
	cin >> i;
	cout << bitset<64>(i)<< endl;
	i = (i & ~0xffff) | (i & 0xff) << 8 | (i & 0xff00) >> 8;
	cout << bitset<64>(i)<<endl;
	cout << i;

	/*char x;
	cin >> x;
	int num = (int)x;
	cout << bitset<64>((int)x) << endl;
	int result = 0;

	do {
		if (num % 2) result++;
		num /= 2;
	} while (num);

	cout << result;*/

	int flag = 0;
	bool s;
	cout << "Битовая карта: " << bitset<8>(flag) << endl;
	cout << "1 - занять блок | 0 - не занимать" << endl;

	cout << "блок 1: ";
	cin >> s; if (s) flag += 1;
	cout << "блок 2: ";
	cin >> s; if (s) flag += 2;
	cout << "блок 3: ";
	cin >> s; if (s) flag += 4;
	cout << "блок 4: ";
	cin >> s; if (s) flag += 8;
	cout << "блок 5: ";
	cin >> s; if (s) flag += 16;
	cout << "блок 6: ";
	cin >> s; if (s) flag += 32;
	cout << "блок 7: ";
	cin >> s; if (s) flag += 64;
	cout << "блок 8: ";
	cin >> s; if (s) flag += 128;
	cout << endl << "Состояние битовой карты: " << bitset<8>(flag) << endl;

	cout << "1 - освободить блок | 0 - не освобождать" << endl;
	cout << "блок 1: ";
	cin >> s; if ((s) && (flag & 1)) flag &= ~1;
	cout << "блок 2: ";
	cin >> s; if ((s) && (flag & 2)) flag &= ~2;
	cout << "блок 3: ";
	cin >> s; if ((s) && (flag & 4)) flag &= ~4;
	cout << "блок 4: ";
	cin >> s; if ((s) && (flag & 8)) flag &= ~8;
	cout << "блок 5: ";
	cin >> s; if ((s) && (flag & 16)) flag &= ~16;
	cout << "блок 6: ";
	cin >> s; if ((s) && (flag & 32)) flag &= ~32;
	cout << "блок 7: ";
	cin >> s; if ((s) && (flag & 64)) flag &= ~64;
	cout << "блок 8: ";
	cin >> s; if ((s) && (flag & 128)) flag &= ~128;
	cout << endl << "Состояние битовой карты: " << bitset<8>(flag) << endl;

}



