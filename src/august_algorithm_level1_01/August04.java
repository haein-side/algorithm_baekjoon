package august_algorithm_level1_01;

import java.util.Scanner;

public class August04 {

	public static void main(String[] args) {

		/* 백준 1330 */
		
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int b = sc.nextInt();
		
		if (a == b) {
			System.out.println("==");
		} else if ( a > b ) {
			System.out.println(">");
		} else {
			System.out.println("<");
		}
		
		
		/* 백준 9498 */
		
		//90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력
		
		Scanner sc2 = new Scanner(System.in);
		
		int score = sc2.nextInt();
		
		if (score >= 90 && score <= 100) {
			System.out.println("A");
		} else if (score >= 80 && score <= 89) {
			System.out.println("B");
		} else if (score >= 70 && score <= 79) {
			System.out.println("C");
		} else if (score >= 60 && score <= 69) {
			System.out.println("D");
		} else {
			System.out.println("F");
		}
		
		
		/* 백준 2753 */
		
		//윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때
		
		Scanner sc3 = new Scanner(System.in);
		
		int year = sc3.nextInt();
		
		if ( (year % 4 == 0 && year % 100 != 0) || year % 400 == 0 ) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
		
		
		/* 백준 14681 */
		
		Scanner sc4 = new Scanner(System.in);
		
		int num1 = sc4.nextInt();
		int num2 = sc4.nextInt();
		
		if (num1 > 0 && num2 > 0) {
			System.out.println(1);
		} else if (num1 < 0 && num2 > 0) {
			System.out.println(2);
		} else if (num1 < 0 && num2 < 0) {
			System.out.println(3);
		} else if (num1 > 0 && num2 < 0) {
			System.out.println(4);
		}
		
		
		
	}

}
