package backjoon;
class Circle{
   private int r;
   static private int count = 0;
   public Circle(){
      r = 0;
      count++;
   }
   public Circle(int a){
      this.r = a;
      count++;
   }
   public static int getCount(){
      return count;
   }
}
public class first_test1 {
	public static void main(String[] args) {
      Circle c1 = new Circle(10);
      Circle c2 = new Circle();
      System.out.println(Circle.getCount());
}
}