package august_algorithm_level1_01;

import java.util.Scanner;

public class August03 {

	public static void main(String[] args) {

		/* 백준 10869 */
		
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		//A+B, A-B, A*B, A/B(몫), A%B(나머지)
		
		System.out.println(a + b);
		System.out.println(a - b);
		System.out.println(a * b);
		System.out.println(a / b);
		System.out.println(a % b);
		
		
		/* 백준 10430 */
		
		Scanner sc2 = new Scanner(System.in);
		
		int c = sc2.nextInt();
		int d = sc2.nextInt();
		int e = sc2.nextInt();
		
		/* 첫째 줄에 (A+B)%C, 
		 * 둘째 줄에 ((A%C) + (B%C))%C, 
		 * 셋째 줄에 (A×B)%C, 
		 * 넷째 줄에 ((A%C) × (B%C))%C를 출력한다. */
		
		System.out.println((c+d)%e);
		System.out.println(((c%e) + (d%e))%e);
		System.out.println((c*d)%e);
		System.out.println(((c%e) * (d%e))%e);
		
		
		/* 백준 2588 */
		
		Scanner sc3 = new Scanner(System.in);
		
		int f = sc3.nextInt();
		int g = sc3.nextInt();
		
		System.out.println( f * ( g - (g / 100 * 100) - (( g - (g / 100 * 100)) / 10 * 10 )));
		System.out.println( f * (( g - (g / 100 * 100)) / 10 ));
		System.out.println( f * (g / 100));
		System.out.println( f * g );
		
		
	}

}
