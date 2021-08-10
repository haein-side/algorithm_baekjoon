package august_algorithm_level1_01;

import java.util.Scanner;

public class August10 {

	public static void main(String[] args) {

		/* 백준 15552 */
		
		Scanner sc = new Scanner(System.in);
		
		int roop = sc.nextInt();
		int[] sum = new int[roop];
		
		for (int i = 0 ; i < roop; i++) {
			
			int num1 = sc.nextInt();
			int num2 = sc.nextInt();
			
			sum[i] += (num1 + num2);
		}
		
		
		for (int j = 0; j < roop; j++) {
			System.out.println(sum[j]);
		}
		
	}

}
