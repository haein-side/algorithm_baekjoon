package august_algorithm_level1_01;

import java.util.Scanner;

//import java.util.Scanner;

public class August17 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int numOrigin = sc.nextInt();
		int numComp = numOrigin;
		
		int num1 = 0;
		int num2 = 0;
		
		int sum = 0;
		
		int roop = 0;
		
		while(true) {
			
			num2 = numOrigin % 10;
			num1 = numOrigin / 10;
			sum = num1 + num2;
			
			int newNum = num2 * 10 + sum % 10;
			roop += 1;
			
			System.out.println("newNum : " + newNum);
			
			if(newNum == numComp) {
				break;
			}
			
			numOrigin = newNum;
			
		}
		
		System.out.println(roop);
		
	}
}
