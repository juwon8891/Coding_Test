package backjoon;
import java.util.Scanner;
import java.util.ArrayList;
public class first_test {
	public static void prime_number(int N) {
		if(N<2 || N>100)
			return;
		ArrayList<Integer> arrList = new ArrayList<>();
        for (int i = 2; i <= N; i++) {
            int num = i;
            int cnt = 0;

            for (int j = 1; j <= num; j++) {
                if(num % j == 0) {
                    cnt++;
                }
            }
            if(cnt == 2) {
                arrList.add(i);
            }
        }
        if(arrList.size() > 0) {
			System.out.printf("2부터 %d까지의 정수는 총 %d개입니다.\n", N, arrList.size());
            for (int i = 0; i < arrList.size(); i++) {
                System.out.print(arrList.get(i) + " ");
            }
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        System.out.print("정수를 입력하세요: ");
		int N = sc.nextInt();
		prime_number(N);
		sc.close();
	}
}