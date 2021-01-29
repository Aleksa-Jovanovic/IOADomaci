#include<iostream>
#include<cmath>

#define NUMBER_OF_CITIES 10

int cities[NUMBER_OF_CITIES][NUMBER_OF_CITIES] = {
		{0,374,200,223,108,178,252,285,240,356},
		{374,0,255,166,433,199,135,95,136,17},
		{200,255,0,128,277,821,180,160,131,247},
		{223,166,1128,0,430,47,52,84,40,155},
		{108,433,277,430,0,453,478,344,389,423},
		{178,199,821,47,453,0,91,110,64,181},
		{252,135,180,52,478,91,0,114,83,117},
		{285,95,160,84,344,110,114,0,47,78},
		{240,136,131,40,389,64,83,47,0,118},
		{356,17,247,155,423,181,117,78,118,0}
};

int* variations_with_repetition(int n, int k, int* lastOne);
bool sequence_to_spanningTree(int* P, int len, int* T, int* minSum);

int main() {

	int minSum = INT_MAX;
	int length = NUMBER_OF_CITIES - 2;

	int* minT = new int[2 * (length + 1)];
	int* currentT = new int[2 * (length + 1)];

	int* last = nullptr;
	int* current = nullptr;
	current = new int[NUMBER_OF_CITIES - 2];

	bool minFound = false;

	for (int i = 0; i < std::pow(NUMBER_OF_CITIES, NUMBER_OF_CITIES - 2); i++)
	{
		last = variations_with_repetition(NUMBER_OF_CITIES, NUMBER_OF_CITIES - 2, last);
		for (int j = 0; j < NUMBER_OF_CITIES - 2; j++) {
			current[j] = last[j] + 1;
		}

		minFound = sequence_to_spanningTree(current, length, currentT, &minSum);

		if (minFound) 
		{
			minFound = false;
			memcpy(minT, currentT, (2 * (length + 1)) * sizeof(int));
		}
	}

	//Ispis
	std::cout << "Cena je " << minSum << std::endl;
	std::cout << "Stablo: ";
	for (int j = 0; j < 2 * (length + 1); j++)
	{
		std::cout << minT[j];
		if (j % 2 == 1 && j != 0 && j != 2 * (length + 1) - 1)
			std::cout << " => ";
		else if (j % 2 == 0)
			std::cout << " ";
	}
	std::cout << std::endl;
	system("pause");
}

int* variations_with_repetition(int n, int k, int* lastOne)
{
	int q;
	int* p;
	if (lastOne == nullptr) 
	{
		 p= new int[k];
		for (int i = 0; i < k; i++)
			p[i] = 0;
	}
	else 
	{
		p = lastOne;
	}

	q = k - 1;
	while (q >= 0)
	{
		p[q]++;
		if (p[q] == n)
		{
			p[q] = 0;
			q--;
		}
		else
		{
			break;
		}
	}

	return p;
}

bool sequence_to_spanningTree(int* P, int len, int* T, int* minSum) {

	int cityBranches[NUMBER_OF_CITIES] = { 0 };

	int sum = 0;

	int i, j, q = 0;
	int n = len + 2;
	int* V = new int[n];

	for (i = 0; i < n; i++)
		V[i] = 0;

	for (i = 0; i < len; i++)
		V[P[i] - 1] += 1;

	for (i = 0; i < len; i++) {
		for (j = 0; j < n; j++) {
			if (V[j] == 0) {
				V[j] = -1;
				T[q++] = j + 1;
				T[q++] = P[i];

				//Summing
				cityBranches[P[i] - 1]++;
				if (cityBranches[P[i] - 1] > 3)
				{
					sum = sum + cities[j][P[i] - 1] + 100 /** (cityBranches[P[i] - 1] - 3)*/;
				}
				else 
				{
					sum = sum + cities[j][P[i] - 1];
				}
				//---

				V[P[i] - 1]--;
				break;
			}
		}

	}

	j = 0;
	int first, last;
	for (i = 0; i < n; i++) {

		if (V[i] == 0 && j == 0) {
			T[q++] = i + 1;
			last = i;
			j++;
		}
		else if (V[i] == 0 && j == 1) {
			T[q++] = i + 1;
			first = i;
			break;
		}

	}

	cityBranches[first]++;
	if (cityBranches[first] > 3)
	{
		sum = sum + cities[first][last] + 100 /** (cityBranches[first] - 3)*/;
	}
	else
	{
		sum = sum + cities[first][last];
	}

	delete[] V;

	if (sum < (*minSum))
	{
		(*minSum) = sum;
		return true;
	}
	else
	{
		return false;
	}
}