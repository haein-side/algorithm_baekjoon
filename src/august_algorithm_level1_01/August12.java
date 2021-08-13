package august_algorithm_level1_01;

import java.util.Scanner;

public class August12 {

	public static void main(String[] args) {

		/* 백준 2438 */
		Scanner sc = new Scanner(System.in);
		
		int roop = sc.nextInt();
		
		// roop개의 열 생성
		for (int i = 0; i < roop; i++) {
			// i개의 별 찍기
			for (int j = 0; j <= i; j++) {
			
			System.out.print("*");
			
			}
			// 줄바꿈
			System.out.println();
		}
	
		
		/* 백준 2439 */
		
		Scanner sc2 = new Scanner(System.in);
		 
		int roop2 = sc2.nextInt();
		
		for(int i = 1; i <= roop2; i++) {
			
			for(int j = (roop2 - i); j >= 1; j--) {
				System.out.print(" ");
			}
			
			for(int h = 1; h <= i; h++) {
				System.out.print("*");
			}
			
			System.out.println();
			
		}
		
		/* 백준 10871 */
		
		Scanner sc3 = new Scanner(System.in);
		
		int num1 = sc3.nextInt();
		int num2 = sc3.nextInt();
		int array[] = new int[num1];
		
		for (int i = 0; i < num1; i++) {
			array[i] = sc3.nextInt();
		}
		
		for (int j = 0; j < num1; j++) {
			
			if (array[j] < num2) {
				System.out.print(array[j]);
				System.out.print(" ");
				System.out.print(" ");
			}
			
		}
		
		
		
	}

}
