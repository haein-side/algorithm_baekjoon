package august_algorithm_level1_01;

import java.util.Scanner;

public class August15 {

	public static void main(String[] args) {

		/* 백준 10952 while문 */
		
		/* 스캐너는 한 번만 생성해줘도 됨 */
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			
			int num1 = sc.nextInt();
			int num2 = sc.nextInt();
			
			int sum = num1 + num2;
			
			/* break : 무한반복 끝내줌 */
			if (num1 == 0 && num2 == 0) {
				
				/* 열린 스캐너를 닫아줌 */
				sc.close();
				
				break;
			}
			
			System.out.println(sum);
			
		}
		
		/* 백준 10951 */
		Scanner sc2 = new Scanner(System.in);
		
		// (가장 중요한 점)
		// 파일 종료 조건 없이 그냥 입력이 주어짐
		// --> 입력에서 더 이상의 읽을 수 있는 데이터가 존재하지 않을 때 반복문 종료하라는 것
		// EOF (End of File)
		while(sc2.hasNextInt()) {
			
			int num1 = sc2.nextInt();
			int num2 = sc2.nextInt();
			
			int sum = num1 + num2;
			
			System.out.println(sum);
			
			if (num1 <= 0 || num2 >= 10) {
				sc2.close();
				break;
			}
			
		}

		
	}

}
