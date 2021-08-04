package august_algorithm_level1_01;

import java.util.Scanner;

public class August04_2 {

	public static void main(String[] args) {

		//System.out.println(((0 * 60 + 44) - 45) / 60);
		//System.out.println(((0 * 60 + 44) - 45) % 60);
		//System.out.println(60 + ((0 * 60 + 44) - 45) % 60 );
		
		// 시간이 0이고 분이 45 미만이면
		// 시간은 23이 나오고 분은 60에서 위의 식을 더해줘야 함
		
		Scanner sc = new Scanner(System.in);
		
		int hour = sc.nextInt();
		int minute = sc.nextInt();
		
		if (hour == 0 && minute < 45) {
			System.out.println(23);
			System.out.println(60 + ((hour * 60 + minute) - 45) % 60 );
		} else {
			System.out.println(((hour * 60 + minute) - 45) / 60);
			System.out.println(((hour * 60 + minute) - 45) % 60);
		}
		
		
	}

}
