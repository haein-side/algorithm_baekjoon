package august_algorithm_level1_01;

import java.util.Scanner;

public class August11 {

	public static void main(String[] args) {
		
		/* 백준 2741 */
		
		Scanner sc = new Scanner(System.in);
		
		int roop = sc.nextInt();
		
		for (int i = 0; i < roop; i++) {
			System.out.println(i+1);
		}
		
		/* 백준 2742 */
		
		Scanner sc2 = new Scanner(System.in);
		
		int roop2 = sc2.nextInt();
		
		for(int j = 0; j < roop2; j++) {
			System.out.println(roop2-j);
		}
		
		/* 백준 11021 */
		
		Scanner sc3 = new Scanner(System.in);
		
		int roop3 = sc3.nextInt();
	
		int[] sum = new int[roop3];
		
		for(int h = 0; h < roop3; h++) {
			
			int num1 = sc3.nextInt();
			int num2 = sc3.nextInt();
			
			sum[h] += num1 + num2; 
			
		}
		
		for(int h = 0; h < roop3; h++) {
			
			System.out.println("Case #"+ (h+1) + ": " + sum[h] );
		
		}
		
		/* 백준 11022 */
		
		//Case #1: 1 + 1 = 2
		
		Scanner sc4 = new Scanner(System.in);
		
		int roop4 = sc3.nextInt();
	
		int[] sum1 = new int[roop4];
		
		for(int h = 0; h < roop4; h++) {
			
			int num1 = sc4.nextInt();
			int num2 = sc4.nextInt();
			
			sum1[h] += num1 + num2; 
			sum1[h+1] += num1;
			sum1[h+2] += num2;
 			
		}
		
		for(int h = 0; h < roop3 + 1; h++) {
			
			System.out.println("Case #"+ (h+1) + ": " + sum1[h+1] + " + " + sum1[h+2] + " = " + sum1[h] );
		
		}
		
	}

}
