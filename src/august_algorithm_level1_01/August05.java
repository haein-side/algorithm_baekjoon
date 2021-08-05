package august_algorithm_level1_01;

import java.util.Scanner;

public class August05 {

	public static void main(String[] args) {

		/* 백준 2739 */
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		for (int i = 1; i <= 9; i++) {
			
			System.out.println(num + " * " + i + " = " + num*i);
			
		}
		
		
		/* 백준 10950 */
		
		Scanner sc1 = new Scanner(System.in);
		
		int roop  = sc1.nextInt();
		int[] sum = new int[roop];
		
		for(int j = 0; j < roop; j++) {
			
			Scanner sc2 = new Scanner(System.in);
			
			int num1 = sc2.nextInt();
			int num2 = sc2.nextInt();
			
			sum[j] = num1 + num2;
			
		}
		
		for(int s = 0; s < roop; s++) {
			
			System.out.println(sum[s]);
			
		}
		
		/*https://www.acmicpc.net/help/rte/NoSuchElement*/
		
		
		/* 백준 8393 */
		
		Scanner sc3 = new Scanner(System.in);
		
		int num3 = sc3.nextInt();
		int sum3 = 0;
		
		for (int i = 0; i < num3; i++) {
			sum3 += i + 1;
		}
		
		System.out.println(sum3);
	}

}
