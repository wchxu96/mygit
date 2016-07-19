#include <iostream>
using namespace std;

int main()
{
	char * a = null;
	char * b = null;
	cin << a;
	cin << b;
	int lena = strlen(a);
	int lenb = strlen(b);
	int D[lena][lenb];
	for ( int i = 0;i< lena;i++) D[i][0] = 0;
	for ( int j = 0;i< lenb;j++) D[0][j] = 0;
	for ( int i = 0;i< lena;i++)
		for(int j = 0;j<lenb;j++)
			{
				if(a[i] == b[j])
				{
					
				}

			}




}
