
#include<iostream>
using namespace std;
bool SieveOfEratosthenes(int n, bool isPrime[]) {
   isPrime[0] = isPrime[1] = false;
   for (int i=2; i<=n; i++)
      isPrime[i] = true;
   for (int p=2; p*p<=n; p++) {
      if (isPrime[p] == true) {
         for (int i=p*2; i<=n; i += p)
            isPrime[i] = false;
      }
   }
   //cout << "All primes <= " << n << endl;
   //for (int i=0; i<=n; i++ )
   //    if (isPrime[i]) cout << i << " ";
   //cout << endl;
   return 0;
}
double superPrimes(int n) {
   long int sum=0;
   bool isPrime[n+1];
   SieveOfEratosthenes(n, isPrime);
   //cout << "SieveOfEratosthenes Complete!" << endl;
   int primes[3500000], j = 0;
   //int primes[n+1], j = 0;
   int lastp=0;
   for (int p=2; p<=n; p++)
      if (isPrime[p]) {
         primes[j++] = p;
         lastp=p;
         if (j%100000 == 0 ) {
            cout << j << " " << p ;
            cout << endl;
	    cout << std::flush;
         }
      }
   cout << j << " " << lastp;
   cout << endl;
   //cout << "Primes list built!" << endl;
   for (int k=0; k<j; k++)
      // Use k or k+1 here to check based on zero or one for start
      if (isPrime[k]) {
         //cout << primes[k] << " ";
         sum += primes[k];
      }
   return sum;
}
int main(int argc, char *argv[]) {
   int n = 100;
   if (argc > 1 )
       n = atoi(argv[1]);
   long int sum=0;
   sum = superPrimes(n);
   //cout << endl << "Sum of Super-Primes less than "<< n << ": " << sum << endl;
   //cout << endl;
   
   //cout << sum << " " << sum%5623 << endl;
   cout << sum << endl;
   return 0;
}

