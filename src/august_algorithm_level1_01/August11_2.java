package august_algorithm_level1_01;

import java.util.Scanner;

public class August11_2 {

	public static void main(String[] args) {
				
				/* 백준 11022 */
				
				//Case #1: 1 + 1 = 2
				
				Scanner sc4 = new Scanner(System.in);
				
				int roop4 = sc4.nextInt();
			
				int[] sum1 = new int[roop4];
				int[] num1 = new int[roop4];
				int[] num2 = new int[roop4];
				
				for(int h = 0; h < roop4; h++) {
					
					int numFirst = sc4.nextInt();
					int numSecond = sc4.nextInt();
					
					sum1[h] += numFirst + numSecond; 
					num1[h] += numFirst;
					num2[h] += numSecond;
					
				}
				
				for(int h = 0; h < roop4 ; h++) {
					
					System.out.println("Case #"+ (h+1) + ": " + num1[h] + " + " + num2[h] + " = " + sum1[h] );
				
				}
				
	}

		
	

}
