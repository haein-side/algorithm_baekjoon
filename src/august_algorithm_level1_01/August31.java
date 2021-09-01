package august_algorithm_level1_01;

import java.util.Scanner;

public class August31 {

	public static void main(String[] args) {
		
		/* 백준 10818 */
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		
		int[] var = new int[num];
		
		for(int i = 0; i < num; i++) {
			
			int vars = sc.nextInt();
			
			var[i] = vars; 
		}
		
		int min = 0;	
		int max = 0;
		
		
		if (var.length >= 2) {
			
			if(var[0] > var[1]) {
				min = var[1];
				max = var[0];
			} else {
				min = var[0];
				max = var[1];
			}
			
			for(int i = 2; i < num; i++) {
				
				if(min > var[i]) {
					min = var[i];
				} 
				
				if(max < var[i]) {
					max = var[i];
				}
				
			}
		} else {
			min = var[0];
			max = var[0];
		}
		
		
		System.out.println(min);
		System.out.println(max);
		
	}
	
	
}
